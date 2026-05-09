from openai import OpenAI

endpoint = "https://ai-foundry-new-learning-by-kk1234567890.services.ai.azure.com/api/projects/proj-default/openai/v1"
key = "8XvEbONp1wYYNQyHkipmMGSbEnczTfefizABLHyFU0EmPwMJ98jxJQQJ99CDACqBBLyXJ3w3AAAAACOGV4DU"
deployment_name = "gpt-4.1-nano-1"


client = OpenAI(
    api_key = key,
    base_url = endpoint
)

message = [
    {"role":"system", "content": "you are a helpful pirate assistant Always responds in pirate language."},
    {"role":"user", "content": "how do i learn about programming?"}
]

response = client.chat.completions.create(
    model = deployment_name,
    messages = message,
    max_tokens = 100, 
    temperature = 0.7
)
print("Ai responses")
print(response.choices[0].message.content)