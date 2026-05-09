from setup import MODEL, client

agent = client.create_agent(
    name="hello-world-agent",
    description="An agent that says hello world",
    model=MODEL,
    tools=[],
    instructions="You are a helpful assistant that says hello world.",
)

thread = client.threads.create()

client.messages.create(thread_id=thread.id, role="user", content="Say hello world")
client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)

for message in client.messages.list(thread_id=thread.id):
    if message.role == "assistant":
        print(message.text_messages[-1].text.value)

