from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint =  "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


documents = ["I love azure ai and It is amazing!",
             "¡Me encanta Azure AI y es increíble!",
             "J'adore Azure AI et c'est incroyable!",
             "Ich liebe Azure AI und es ist erstaunlich!",
             "Azure AIが大好きで、素晴らしいです！",
             "Azure AI를 사랑하고 놀랍습니다!",
             "Azure AI amo e é incrível!",
             "Azure AI люблю и это удивительно!"]

response = client.detect_language(documents=documents)

for doc in response:
    print("Document Language: {}".format(doc.primary_language.name) + " confidence Score: {}".format(doc.primary_language.confidence_score) + "\n\n")
