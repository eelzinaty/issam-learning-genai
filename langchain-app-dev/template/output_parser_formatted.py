from reviews import *
from utilities_langchain import create_chat_model
chat = create_chat_model()
from langchain.prompts import ChatPromptTemplate
from review_templates import create_response_schema, review_template_2

output_parser = create_response_schema()
format_instructions = output_parser.get_format_instructions()

prompt_template = ChatPromptTemplate.from_template(template=review_template_2)
messages = prompt_template.format_messages(text=customer_review, format_instructions=format_instructions)

# Invoke the chat model and get response
response = chat.invoke(messages)
print(type(response.content))
print(response.content)

# Parse the response to create an object mapped to the schema passed to the model
output_dict = output_parser.parse(response.content)
print(type(output_dict))
print(output_dict["price_value"])

