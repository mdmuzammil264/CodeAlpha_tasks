# 🤖 Basic Rule-Based ChatBot in Python

A simple rule-based chatbot built using Python. This chatbot responds to predefined user inputs using a dictionary and supports both exact and partial text matching.

## 🚀 Features

* Simple and beginner-friendly Python project
* Rule-based conversation system
* Exact keyword matching
* Partial sentence matching
* Interactive command-line interface
* Easy to customize and extend

## 📂 Project Structure

```bash
chatbot/
│
├── chatbot.py
└── README.md
```

## 🛠️ Technologies Used

* Python 3.x

## 📜 How It Works

The chatbot uses a dictionary containing predefined questions and responses.

Example:

```python
responses = {
    "hello": "Hi! How can I help you today?",
    "bye": "Goodbye! Have a great day!"
}
```

### Matching Process

1. Convert user input to lowercase.
2. Check for an exact match.
3. If no exact match is found, check for partial matches.
4. Return the corresponding response.
5. If nothing matches, show a default message.

## ▶️ Running the Project

### Clone the Repository

```bash
git clone https://github.com/your-username/chatbot.git
```

### Navigate to the Project Folder

```bash
cd Chatbot
```

### Run the Program

```bash
python chatbot.py
```

## 💬 Sample Conversation

```text
========================================
       BASIC CHATBOT
========================================

ChatBot: Hi! I'm ChatBot. Type 'bye' to exit.

You: hello
ChatBot: Hi! How can I help you today?

You: tell me a joke
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs! 😄

You: bye
ChatBot: Goodbye! Have a great day!
```

## 🎯 Learning Outcomes

By building this project, you will learn:

* Python Dictionaries
* Functions
* Loops
* Conditional Statements
* String Manipulation
* User Input Handling
* Basic Chatbot Logic