from langchain_ollama import ChatOllama

llm = ChatOllama(
        model="gemma3:1b",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]

ai_msg = llm.invoke(messages)
ai_msg.content
print(ai_msg.content)
# for chunk in llm.stream(messages):
#     print(chunk.text(), end="")