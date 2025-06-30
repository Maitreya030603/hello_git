# Simple Python Chatbot

def chatbot():
    print("Chatbot: Hi! I'm your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing fine!")
        elif "your name" in user_input:
            print("Chatbot: I'm just a simple chatbot without a fancy name.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
