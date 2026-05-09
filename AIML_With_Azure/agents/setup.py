import os

from azure.ai.agents import AgentsClient
from azure.identity import DeviceCodeCredential
from dotenv import load_dotenv


load_dotenv()

endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT") or os.getenv("AZURE_AI_ENDPOINT")
deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME") or os.getenv("AZURE_AI_DEPLOYMENT_NAME")

if not endpoint:
    raise ValueError("Set AZURE_AI_PROJECT_ENDPOINT or AZURE_AI_ENDPOINT before running the script.")

if not deployment_name:
    raise ValueError("Set MODEL_DEPLOYMENT_NAME or AZURE_AI_DEPLOYMENT_NAME before running the script.")


credential = DeviceCodeCredential()


client = AgentsClient(
    endpoint=endpoint,
    credential=credential,
)

MODEL = deployment_name