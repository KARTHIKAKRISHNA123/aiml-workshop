from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint =  "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

documents = ["I love azure ai and It is amazing!"]
response = client.analyze_sentiment(documents=documents)
for doc in response:
    print("Document Sentiment: {}".format(doc.sentiment))
    print("Overall scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))