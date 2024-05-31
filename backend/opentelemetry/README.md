# SQL over OTel Data

Elixir stores and visualizes OpenTelemetry (specifically [OpenLLMetry](https://github.com/traceloop/openllmetry)) data for our customers.

We've preloaded some raw OTel data into a SQLite database for a single conversation (see [traces.csv](./traces.csv)).

| Column Name        | Data Type |
| ------------------ | --------- |
| Timestamp          | TEXT      |
| TraceId            | TEXT      |
| SpanId             | TEXT      |
| ParentSpanId       | REAL      |
| TraceState         | REAL      |
| SpanName           | TEXT      |
| SpanKind           | TEXT      |
| ServiceName        | TEXT      |
| ResourceAttributes | TEXT      |
| ScopeName          | TEXT      |
| ScopeVersion       | TEXT      |
| SpanAttributes     | TEXT      |
| Duration           | INTEGER   |
| StatusCode         | TEXT      |
| StatusMessage      | REAL      |
| Events.Timestamp   | TEXT      |
| Events.Name        | TEXT      |
| Events.Attributes  | TEXT      |
| Links.TraceId      | TEXT      |
| Links.SpanId       | TEXT      |
| Links.TraceState   | TEXT      |
| Links.Attributes   | TEXT      |

## Part 1: SQL Queries

### Implementation

- Write SQL queries to calculate the following metrics:
  - \# of Traces
  - Cost
  - Average Latency
  - Input Token Count
  - Completion Token Count
  - Total Token Count
- The LLM messages used in the call can be reconstructed from the `SpanAttributes` column (see `gen_ai.prompt` and `gen_ai.completion`). Implement a function to unflatten the contents into a dict.

  For example, given:

  ```
  flat_json = {
      "llm.request.type": "chat",
      "traceloop.workflow.name": "get_weather",
      "gen_ai.system": "OpenAI",
      "gen_ai.request.model": "gpt-3.5-turbo",
      "gen_ai.request.max_tokens": 20,
      "llm.headers": "None",
      "llm.is_streaming": False,
      "openai.api_base": "https://api.openai.com/v1/",
      "gen_ai.prompt.0.role": "system",
      "gen_ai.prompt.0.content": "You are my personal weather assistant",
      "gen_ai.prompt.1.role": "user",
      "gen_ai.prompt.1.content": "hi",
      "llm.request.functions.0.name": "get_current_weather",
      "llm.request.functions.0.description": "Get the current weather",
      "llm.request.functions.0.parameters": "{\"type\": \"object\", \"properties\": {\"location\": {\"type\": \"string\", \"description\": \"The city and state, e.g. San Francisco, CA\"}}, \"required\": [\"location\"]}",
      "gen_ai.response.model": "gpt-3.5-turbo-0125",
      "llm.usage.total_tokens": 77,
      "gen_ai.usage.completion_tokens": 10,
      "gen_ai.usage.prompt_tokens": 67,
      "gen_ai.completion.0.finish_reason": "stop",
      "gen_ai.completion.0.role": "assistant",
      "gen_ai.completion.0.content": "Hello! How can I assist you today?"
  }
  ```

  We want to output something like:

  ```
  {
      "llm": {
          "request": {
              "type": "chat",
              "functions": [
                  {
                      "name": "get_current_weather",
                      "description": "Get the current weather",
                      "parameters": "{\"type\": \"object\", \"properties\": {\"location\": {\"type\": \"string\", \"description\": \"The city and state, e.g. San Francisco, CA\"}}, \"required\": [\"location\"]}"
                  }
              ]
          },
          "headers": "None",
          "is_streaming": false,
          "usage": {
              "total_tokens": 77
          }
      },
      "traceloop": {
          "workflow": {
              "name": "get_weather"
          }
      },
      "gen_ai": {
          "system": "OpenAI",
          "request": {
              "model": "gpt-3.5-turbo",
              "max_tokens": 20
          },
          "prompt": [
              {
                  "role": "system",
                  "content": "You are my personal weather assistant"
              },
              {
                  "role": "user",
                  "content": "hi"
              }
          ],
          "response": {
              "model": "gpt-3.5-turbo-0125"
          },
          "usage": {
              "completion_tokens": 10,
              "prompt_tokens": 67
          },
          "completion": [
              {
                  "finish_reason": "stop",
                  "role": "assistant",
                  "content": "Hello! How can I assist you today?"
              }
          ]
      },
      "openai": {
          "api_base": "https://api.openai.com/v1/"
      }
  }
  ```

### Discussion

- Most of the important information can be found in the `SpanAttributes` column. However, because it is stored as string, it is difficult to efficiently run queries over the data. How might you redesign or extend the DB schema accordingly?
