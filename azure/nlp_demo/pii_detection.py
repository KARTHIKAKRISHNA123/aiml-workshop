from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint =  "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = ["I am KK. my email is athvikaalm2018@gmail.com and my phone number is 123-456-7890. I live in 1234 Main St, Anytown, USA."]

response = client.recognize_pii_entities(documents=documents)

for doc in response:
    print("Redacted Text: {}".format(doc.redacted_text))
    print("PII Entities: {}".format(doc.entities) + "\n")
    print("Categories: {}".format([entity.category for entity in doc.entities]) + "\n")
    print("Subcategories: {}".format([entity.subcategory for entity in doc.entities]) + "\n")
    print("Confidence Scores: {}".format([entity.confidence_score for entity in doc.entities]) + "\n")
    print("Offset: {}".format([entity.offset for entity in doc.entities]) + "\n")