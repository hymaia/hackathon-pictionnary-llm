from typing import List

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


PROMPT = """
Tu joues au pictionnary, dit en 1 mot ce que tu vois sur cette image. Tu auras la liste des mots possibles, si tu ne reconnais pas le mot, dis je ne sais pas.
Liste des mots: [{words}]
Reponds soit un mot parmis la liste (respect bien l'orthographe du mot de la liste), ou je ne sais pas.
"""

MODEL = ChatOpenAI(model="gpt-4o")


def generate_answer(image_data, words:List[str]) -> str:

    words_str = ''
    for w in words:
        words_str = words_str + w + ', \n'

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

    response = chain.invoke({"image_data": image_data, "words": words_str})
    return response.content
