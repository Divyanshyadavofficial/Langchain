from langchain_openai import ChatOpenAI
from dotenv import load_dotenvr

load_dotenv()

model = ChatOpenAI(model="gpt-4",temperature=0,max_completion_tokens=10)
result = model.invoke("Write  a five line poem on cricket")
print(result.content)
