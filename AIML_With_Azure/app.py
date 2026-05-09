from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.exceptions import HttpResponseError
from azure.core.credentials import AzureKeyCredential
from urllib.parse import urlparse

endpoint = "https://aiworkshop.cognitiveservices.azure.com/"
key = "92eF3DftuRJMqbrRSFhV6ZFXKkb7UU8dBYeJ04rwQAF2mnnad3dmJQQJ99CDACGhslBXJ3w3AAAFACOGZe3j"

client = ImageAnalysisClient(endpoint, AzureKeyCredential(key))

print("Client created successfully!")

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/PNG_transparency_demonstration_1.png/640px-PNG_transparency_demonstration_1.png"


def to_wikimedia_original(url: str) -> str | None:
	parsed = urlparse(url)
	if parsed.netloc != "upload.wikimedia.org" or "/thumb/" not in parsed.path:
		return None

	parts = parsed.path.split("/")
	try:
		thumb_idx = parts.index("thumb")
	except ValueError:
		return None

	# Thumbnail URL format:
	# /wikipedia/commons/thumb/4/47/File.png/640px-File.png
	# Original URL format:
	# /wikipedia/commons/4/47/File.png
	if len(parts) < thumb_idx + 5:
		return None

	original_parts = parts[:thumb_idx] + parts[thumb_idx + 1 : -1]
	original_path = "/".join(original_parts)
	if not original_path.startswith("/"):
		original_path = f"/{original_path}"

	return f"{parsed.scheme}://{parsed.netloc}{original_path}"


try:
	result = client.analyze_from_url(
		image_url=image_url,
		visual_features=[VisualFeatures.TAGS],
	)
except HttpResponseError as ex:
	fallback_url = to_wikimedia_original(image_url)
	if ex.status_code == 429 and fallback_url:
		print("URL was rate-limited (429). Retrying with Wikimedia original file URL...")
		print("Retry URL:", fallback_url)
		result = client.analyze_from_url(
			image_url=fallback_url,
			visual_features=[VisualFeatures.TAGS],
		)
	else:
		raise

print("Image analysis result successfully obtained!")

if result.tags:
	print("Tags:")
	for tag in result.tags.list:
		print(f"- {tag.name}: {tag.confidence:.2f}")
else:
	print("No tags found.")

