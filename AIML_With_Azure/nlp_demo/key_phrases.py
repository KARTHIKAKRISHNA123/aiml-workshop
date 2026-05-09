from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint =  "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


document = ["Ai is amazing technology that is transforming the world and I am learning it. Azure natural language processing is amazing!"]

response = client.extract_key_phrases(documents=document)

for doc in response:
    print("Document Key Phrases: {}".format(doc.key_phrases) + "\n")
    
