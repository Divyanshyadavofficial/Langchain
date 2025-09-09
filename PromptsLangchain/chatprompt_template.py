from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert"),
    ("human", "Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({'domain':'cricket','topic':'Dusra'})

print(prompt)
# message placeholder

# A message placeholder in langchain is a
# special placeholder used inside a chatPromopt
# template to dynamically insert chat history
# or a list of messages at runtime
