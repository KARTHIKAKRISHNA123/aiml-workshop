from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

endpoint = "https://nlp1234.cognitiveservices.azure.com/"
key = "9piHfhdavANKavGv9TSuYx2VKeLsOz0YrVfE0SOeFk89PMPFpc4rJQQJ99CDACqBBLyXJ3w3AAAaACOG5GYT"

client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))


def print_title(title: str) -> None:
	print("\n" + "=" * 20 + f" {title} " + "=" * 20)


def run_sentiment() -> None:
	documents = ["I love azure ai and It is amazing!"]

	print_title("SENTIMENT ANALYSIS")
	print("Input:", documents)

	response = client.analyze_sentiment(documents=documents)
	print("Output:")
	for doc in response:
		if doc.is_error:
			print(f"Error: {doc.error.code} - {doc.error.message}")
			continue
		print(f"Document Sentiment: {doc.sentiment}")
		print(
			"Overall scores: positive={}; neutral={}; negative={}".format(
				doc.confidence_scores.positive,
				doc.confidence_scores.neutral,
				doc.confidence_scores.negative,
			)
		)


def run_key_phrases() -> None:
	documents = [
		"Ai is amazing technology that is transforming the world and I am learning it. Azure natural language processing is amazing!"
	]

	print_title("KEY PHRASE EXTRACTION")
	print("Input:", documents)

	response = client.extract_key_phrases(documents=documents)
	print("Output:")
	for doc in response:
		if doc.is_error:
			print(f"Error: {doc.error.code} - {doc.error.message}")
			continue
		print(f"Document Key Phrases: {doc.key_phrases}")


def run_language_detection() -> None:
	documents = [
		"I love azure ai and It is amazing!",
		"¡Me encanta Azure AI y es increible!",
		"J'adore Azure AI et c'est incroyable!",
		"Ich liebe Azure AI und es ist erstaunlich!",
		"Azure AI ga daisuki de, subarashii desu!",
		"Azure AIreul saranghago nollabseubnida!",
		"Azure AI amo e e incrivel!",
		"Azure AI lyublyu i eto udivitelno!",
	]

	print_title("LANGUAGE DETECTION")
	print("Input:", documents)

	response = client.detect_language(documents=documents)
	print("Output:")
	for doc in response:
		if doc.is_error:
			print(f"Error: {doc.error.code} - {doc.error.message}")
			continue
		print(
			"Document Language: {} | Confidence Score: {}".format(
				doc.primary_language.name,
				doc.primary_language.confidence_score,
			)
		)


def run_pii_detection() -> None:
	documents = [
		"I am KK. my email is athvikaalm2018@gmail.com and my phone number is 123-456-7890. I live in 1234 Main St, Anytown, USA."
	]

	print_title("PII DETECTION")
	print("Input:", documents)

	response = client.recognize_pii_entities(documents=documents)
	print("Output:")
	for doc in response:
		if doc.is_error:
			print(f"Error: {doc.error.code} - {doc.error.message}")
			continue
		print(f"Redacted Text: {doc.redacted_text}")
		print(f"PII Entities: {doc.entities}")
		print(f"Categories: {[entity.category for entity in doc.entities]}")
		print(f"Subcategories: {[entity.subcategory for entity in doc.entities]}")
		print(f"Confidence Scores: {[entity.confidence_score for entity in doc.entities]}")
		print(f"Offsets: {[entity.offset for entity in doc.entities]}")


if __name__ == "__main__":
	run_sentiment()
	run_key_phrases()
	run_language_detection()
	run_pii_detection()


