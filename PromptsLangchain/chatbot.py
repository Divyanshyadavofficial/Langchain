from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
load_dotenv()


# endpoint = HuggingFaceEndpoint(
#     repo_id="HuggingFaceH4/zephyr-7b-beta",
#     task="text-generation",
#     max_new_tokens=200,
#     temperature=0.7,
# )

#model = ChatOpenAI()


# model = ChatHuggingFace(llm = endpoint)

# while True:
#     user_input = input("you: ")
#     if user_input == 'exit':
#         break
#     result = model.invoke(user_input)
#     print("AI: ",result.content)



# here the problem is the chat bot did'nt 
# know about the previous converstion or the 
# context of the topic which is going on
# so here we  need to create a history 
# so that the chatbot can be able to look
# on it to understand the previous context

# what i have to do is
    # create a chat history list
    # then each time when user types a message
    # we have to append it to chathistory
    # and send the prompt as chat history
    # then the response that came from llm we have 
    # to append it to chat history
endpoint = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=200,
)


model = ChatHuggingFace(llm = endpoint)

chat_history = [
    SystemMessage(content='you are a helpful Ai Assistant')
]

while True:
    user_input = input("you: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)
    
print(chat_history)
# now the problem is that we have messages
# stored in a  single location but the info 
# about who sends which message is not present
# so its recommended to keep track of
# who sends which message by maintaing a 
# dictionary

# we use langchain messages for this
# these are a type of static messages
# human message
# system message
# AI message