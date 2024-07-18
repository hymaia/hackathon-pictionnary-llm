PROMPT = """
Tu joues au pictionnary, dit en 1 mot ce que tu vois sur cette image
"""


class ChatBot:
    def __init__(self, llm):
        self.llm = llm
        self.rag_chain = self.llm

    def generate_answer(self, user_question: str) -> dict:
        message = self.rag_chain.invoke(user_question)
        return message
