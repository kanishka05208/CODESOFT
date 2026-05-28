import random
import datetime
print("===================================")
print("      WELCOME TO AI CHATBOT")
print("===================================")
print("Type 'bye' to exit\n")
jokes = [
    "Why did the computer sleep? Because it was tired!",
    "Why do programmers love Python? Because it is easy!",
    "Why was the computer cold? It forgot to close Windows!"
]
while True:
    user = input("You: ").lower()
    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")
    elif "how are you" in user:
        print("Bot: I am doing great!")
    elif "your name" in user:
        print("Bot: I am a simple AI Chatbot.")
    elif "time" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)
    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)
    elif "joke" in user:
        print("Bot:", random.choice(jokes))
    elif "add" in user:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Bot: Result =", a + b)
        except:
          print("Bot: Invalid input!")
    elif "motivate me" in user:
        print("Bot: Believe in yourself. You can achieve great things!")
    elif "help" in user:
        print("Bot: You can ask me about:")
        print("- time")
        print("- date")
        print("- jokes")
        print("- addition")
        print("- motivation")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
