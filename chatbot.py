print("=" * 50)
print("🤖 Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye', 'exit', or 'quit' to end the chat.")
print("=" * 50)

# Knowledge Base (Dictionary)
responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! Nice to meet you.",
    "how are you": "I'm doing great. Thanks for asking!",
    "what is your name": "I am a Rule-Based AI Chatbot.",
    "help": "I can answer basic questions and chat with you.",
    "thank you": "You're welcome!",
    "who created you": "I was created as part of an AI internship project.",
    "what can you do": "I can respond to predefined questions using rule-based logic.",
    "college": "I am designed for internship training.",
    "time": "Please check your system clock.",
    "thank you": "You're welcome!",
    "good morning": "Good morning! Have a wonderful day.",
    "good night": "Good night! Sleep well."
}

# Continuous Conversation Loop
while True:
    user_input = input("\nYou: ").lower().strip()

    # Exit Commands
    if user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day. 👋")
        break

    # Fetch Response from Dictionary
    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Please try another question."
    )

    print("Bot:", response)
