from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about langchain")
]
result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)

# these messages are a type of static messages
# which are passed as a list of messages 

# to use dynamic messages as a list of messages
# we need to use chatprompt class
