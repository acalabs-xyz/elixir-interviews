import json


def unflatten_json(d: dict):
    # TODO
    pass


if __name__ == "__main__":
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
        "llm.request.functions.0.parameters": '{"type": "object", "properties": {"location": {"type": "string", "description": "The city and state, e.g. San Francisco, CA"}}, "required": ["location"]}',
        "gen_ai.response.model": "gpt-3.5-turbo-0125",
        "llm.usage.total_tokens": 77,
        "gen_ai.usage.completion_tokens": 10,
        "gen_ai.usage.prompt_tokens": 67,
        "gen_ai.completion.0.finish_reason": "stop",
        "gen_ai.completion.0.role": "assistant",
        "gen_ai.completion.0.content": "Hello! How can I assist you today?",
    }

    unflattened_json = unflatten_json(flat_json)
    print(json.dumps(unflattened_json, indent=4))
