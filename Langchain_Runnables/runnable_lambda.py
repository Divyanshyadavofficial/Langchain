from langchain.schema.runnable import RunnableLambda

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

load_dotenv()

def word_count(text):
    return len(text.split)

prompt = PromptTemplate(
    template = 'write a joke about {topic}',
    input_variables = ['topic']
)

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task= "text-generation"
)
parser = StrOutputParser()

model = ChatHuggingFace(llm=llm)

joke_gen_chain =  RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count': RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = final_chain.invoke({'topic':'AI'})

final_result = """{}\n word count - {}""".format(result['joke'],result['word_count'])

print(final_result)