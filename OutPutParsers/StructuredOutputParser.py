from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task= "text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact1",description="Fact1 about the topic"),
    ResponseSchema(name="fact2",description="Fact2 about the topic"),
    ResponseSchema(name="fact3",description="Fact3 about the topic"),

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="give 3 facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)
# final_result = parser.parse(result.content)

# print(final_result)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})
print(result)

# here the dis advantage is data validation cannot be implemented you only can specify the structure of the output but not the validation of the output
# for data validation use pydantic output parsers.