responses = {
    "hello": "Hi! How can I help you today?",
    "hi": "Hello there! Nice to meet you!",
    "hey": "Hey! What's up?",
    "how are you": "I'm fine, thanks! How about you?",
    "i'm fine": "Great to hear that!",
    "i am fine": "Awesome! Glad you're doing well.",
    "what is your name": "I'm chatbot",
    "what can you do": "I can chat with you! Try: hello, how are you, bye.",
    "help": "Try: hello, hi, how are you, what is your name, thanks, bye.",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "See you later! Take care!",
    "thanks": "You're welcome!",
    "thank you": "Happy to help!",
    "good morning": "Good morning! Hope you have a wonderful day!",
    "good night": "Good night! Sweet dreams!",
    "what's the time": "I don't have a clock, but your device does!",
    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😄",
}

def get_response(user_input):
    lower = user_input.lower().strip()

    # Exact match
    if lower in responses:
        return responses[lower]

    # Partial match
    for key in responses:
        if key in lower:
            return responses[key]

    return "Sorry, I don't understand that yet. Type 'help' for ideas!"

def chatbot():
    print("=" * 40)
    print("       BASIC CHATBOT")
    print("=" * 40)
    print("ChatBot: Hi! I'm ChatBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        reply = get_response(user_input)
        print(f"ChatBot: {reply}\n")

        if user_input.lower() in ["bye", "goodbye"]:
            break

chatbot()