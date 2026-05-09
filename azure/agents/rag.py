from setup import MODEL, client


from azure.ai.agents import FileSearchTool, WebSearchTool
agent = client.create_agent(model=MODEL, name="RAG Agent", instructions="You are a helpful assistant that uses tools to answer questions.")

thread = client.threads.create()

file = client.files.upload_and_poll(file_path="/policy.txt", purpose=FilePurpose.AGENTS)

vs = client.vector_stores.create_and_poll(file_ids=[file.id], name="policy-kb", description="vector store for policy document")

vector_store_ids = ([vs.id])