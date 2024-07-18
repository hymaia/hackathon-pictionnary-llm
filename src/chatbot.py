import base64
import httpx

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


PROMPT = """
Tu joues au pictionnary, dit en 1 mot ce que tu vois sur cette image
"""

image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
image_data = base64.b64encode(httpx.get(image_url).content).decode("utf-8")


class ChatBot:
    def __init__(self):
        self.model = ChatOpenAI(model="gpt-4o")

    def generate_answer(self) -> dict:
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
        chain = prompt | self.model

        response = chain.invoke({"image_data": image_data})
        print(response.content)
        return response
