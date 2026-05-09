from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint =  "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))
print("Client Connected Successfully!")