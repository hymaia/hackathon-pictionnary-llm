from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


PROMPT = """
Tu joues au pictionnary, dit en 1 mot ce que tu vois sur cette image
"""

MODEL = ChatOpenAI(model="gpt-4o")


def generate_answer(image_data) -> dict:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", PROMPT),
            (
                "user",
                [
                    {
                        "type": "image_url",
                        "image_url": {"url": "data:image/jpeg;base64,{image_data}"},
                    }
                ],
            ),
        ]
    )
    chain = prompt | MODEL

    response = chain.invoke({"image_data": image_data})
    print(response.content)
    return response
