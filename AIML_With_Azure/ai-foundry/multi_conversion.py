from openai import OpenAI

endpoint = "https://ai-foundry-new-learning-by-kk1234567890.services.ai.azure.com/api/projects/proj-default/openai/v1"
key = "8XvEbONp1wYYNQyHkipmMGSbEnczTfefizABLHyFU0EmPwMJ98jxJQQJ99CDACqBBLyXJ3w3AAAAACOGV4DU"

deployment_name = "gpt-4.1-nano-1"

client = OpenAI(
    base_url=endpoint,
    api_key=key,
)


response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a helpful assistant and expert in AI."},
        {"role": "assistant", "content": "Sure! I can help you with that."},
        {"role": "user", "content": "What is Microsoft Azure AI Foundry?"}
    ],
)

print("Response from Azure AI Foundry with assistant:")
print(response.choices[0].message.content)