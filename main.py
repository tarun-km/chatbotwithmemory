from ui import ChatbotUI
from chatbot import Chatbot

def main():
    chatbot = Chatbot()
    ui = ChatbotUI(chatbot)
    ui.run()

if __name__ == "__main__":
    main()
