from reviews import *
from utilities_langchain import create_chat_model
chat = create_chat_model()
from langchain.prompts import ChatPromptTemplate
from review_templates import review_template

prompt_template = ChatPromptTemplate.from_template(review_template)
messages = prompt_template.format_messages(text=customer_review)


response = chat.invoke(messages)
print(type(response.content))
print(response.content)
