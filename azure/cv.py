from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures

endpoint = "https://aiworkshop.cognitiveservices.azure.com/"

key = "92eF3DftuRJMqbrRSFhV6ZFXKkb7UU8dBYeJ04rwQAF2mnnad3dmJQQJ99CDACGhslBXJ3w3AAAFACOGZe3j"

client = ImageAnalysisClient(endpoint, AzureKeyCredential(key))
print("Client created successfully")

image_url = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-sample-data-files/master/ComputerVision/Images/objects.jpg"

result = client.analyze_from_url(image_url, visual_features=[VisualFeatures.CAPTION])
print("Image analyzed successfully")
print(f"Caption: {result.caption.text}")