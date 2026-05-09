from openai import OpenAI
import json

endpoint = "https://ai-foundry-new-learning-by-kk1234567890.services.ai.azure.com/api/projects/proj-default/openai/v1"
key = "8XvEbONp1wYYNQyHkipmMGSbEnczTfefizABLHyFU0EmPwMJ98jxJQQJ99CDACqBBLyXJ3w3AAAAACOGV4DU"
deployment_name = "gpt-4.1-nano-1"


client = OpenAI(
    api_key = key,
    base_url = endpoint
)

def get_weather(location):
    # This function simulates fetching weather information for a given location.
    # In a real implementation, this could involve calling a weather API.
    return f"The current weather in {location} is sunny with a temperature of 25°C."


tools = {
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The location to get the weather for",
                },
            },
            "required": ["location"],
        },
    },
}

message = [
    {"role":"system", "content": "you are a helpful assistant who can provide weather information. Use the get_weather function to fetch weather data when needed."},
    {"role":"user", "content": "what's the weather like in New York?"}
]

response = client.chat.completions.create(
    model = deployment_name,
    messages = message,
    max_tokens = 100, 
    temperature = 0.7,
    tools = [tools],
    tool_choice = "auto"
)

assistant_message = response.choices[0].message
tool_calls = assistant_message.tool_calls or []

if tool_calls:
    tool_map = {
        "get_weather": get_weather,
    }

    message.append(assistant_message.model_dump())

    for tool_call in tool_calls:
        tool_name = tool_call.function.name
        tool_args = json.loads(tool_call.function.arguments or "{}")
        tool_func = tool_map.get(tool_name)

        if tool_func is None:
            tool_output = f"Tool '{tool_name}' is not available."
        else:
            tool_output = tool_func(**tool_args)

        message.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": tool_output,
            }
        )

    final_response = client.chat.completions.create(
        model=deployment_name,
        messages=message,
        max_tokens=100,
        temperature=0.7,
    )
    print("Ai responses")
    print(final_response.choices[0].message.content)
else:
    print("Ai responses")
    print(assistant_message.content)