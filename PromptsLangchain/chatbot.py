from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
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

chat_history = []

while True:
    user_input = input("you: ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)
    
print(chat_history)