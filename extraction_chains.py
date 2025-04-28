from pydantic import BaseModel, Field 
from typing import TypedDict, List
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser
from typing import Optional

class Person(BaseModel):
    """Infomation about a person"""
    name: str = Field(description = "person's name")
    age: Optional[int] = Field(description = "person's age")

class Infomation(BaseModel):
    """Infomation to extract"""
    person: List[Person] = Field(description = "List of infomation about person")

infomation_function = [convert_pydantic_to_openai_function(Infomation)]

information_model = model.bind(functions = infomation_function, function_call = {"name": "Infomation"})

prompt = ChatPromptTemplate.from_messages([
    ("system", "extract the relevant details, if not explicitly provide do not guess. Extract partial info"),
    ("user", "{input}")
])

chain1 = prompt | information_model | JsonOutputFunctionsParser()

chain1.invoke({"input": "i am anand, my age is 23"})

chain1.invoke({"input": "my sister name is abi, she is 21"})

chain1.batch([{"input": "i am anand, my age is 23"}, {"input": "my sister name is abi, she is 21"}])
