import nltk
import random
import string  
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey|sup|yo", 
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"how are you ?|wassup|how are you doing ?",
        ["I'm doing well, thank you! How about you?", "I'm great! What about you?"]
    ],
    [
        r"who are you ?|what are you called ?",
        ["I'm a chatbot created using NLTK!", "You can call me ChatBot!"]
    ],
    [
        r"what can you do ?|what do you do ?",
        ["I can answer your questions! Try asking me something."]
    ],
    [
        r"quit|bye|goodbye", 
        ["Goodbye! Have a nice day!", "See you later!"]
    ]
]

chatbot = Chat(pairs, reflections)

def chat():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    chat()
