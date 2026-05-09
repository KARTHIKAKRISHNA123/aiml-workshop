from setup import client, MODEL


agent  = client.create_agent(model=MODEL, name="hello", instructions="Remeber What we discuss")
thread = client.threads.create()


def chat(msg: str) -> str:
    client.messages.create(thread_id=thread.id, role="user", content=msg)
    client.runs.create_and_process(thread_id=thread.id, agent_id=agent.id)
    msgs = list(client.messages.list(thread_id=thread.id))
    return msgs[0].text_messages[-1].text.value

print(chat("My name is KK and i live in India."))
print(chat("What is my name and where do i live?"))