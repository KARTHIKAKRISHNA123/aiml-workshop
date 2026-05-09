from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures

endpoint = "https://aiworkshop.cognitiveservices.azure.com/"

key = "92eF3DftuRJMqbrRSFhV6ZFXKkb7UU8dBYeJ04rwQAF2mnnad3dmJQQJ99CDACGhslBXJ3w3AAAFACOGZe3j"

client = ImageAnalysisClient(endpoint, AzureKeyCredential(key))
print("Client created successfully")

image_url = "https://images.unsplash.com/photo-1776377231754-d36928e6ee4d?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

result = client.analyze_from_url(image_url, visual_features=[VisualFeatures.TAGS])
print("Image analyzed successfully")
print("Tags Found: ")
for tag in result.tags.list: 
    print(f" - {tag.name} (confidence: {tag.confidence:.2f})")