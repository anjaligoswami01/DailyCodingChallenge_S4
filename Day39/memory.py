from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(
    k=7,
    return_messages=True
)