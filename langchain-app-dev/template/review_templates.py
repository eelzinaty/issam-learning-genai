from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser

review_template = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product \
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

Format the output as JSON with the following keys:
gift
delivery_days
price_value

text: {text}
"""

review_template_2 = """\
For the following text, extract the following information:

gift: Was the item purchased as a gift for someone else? \
Answer True if yes, False if not or unknown.

delivery_days: How many days did it take for the product\
to arrive? If this information is not found, output -1.

price_value: Extract any sentences about the value or price,\
and output them as a comma separated Python list.

text: {text}

{format_instructions}
"""

def create_response_schema():
    gift_schema = ResponseSchema(name="gift",
                                description="Was the item purchased\
                                as a gift for someone else? \
                                Answer True if yes,\
                                False if not or unknown.")
    delivery_days_schema = ResponseSchema(name="delivery_days",
                                        description="How many days\
                                        did it take for the product\
                                        to arrive? If this \
                                        information is not found,\
                                        output -1.")
    price_value_schema = ResponseSchema(name="price_value",
                                        description="Extract any\
                                        sentences about the value or \
                                        price, and output them as a \
                                        comma separated Python list.")

    response_schemas = [gift_schema, 
                        delivery_days_schema,
                        price_value_schema]

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    return output_parser

