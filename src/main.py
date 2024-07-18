from src.chatbot import ChatBot
from dotenv import load_dotenv

def main():
    load_dotenv()

    chatbot = ChatBot()


    chatbot.generate_answer()

if __name__ == '__main__':
    main()