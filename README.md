# Implementation-of-chatbot-using-NLP

## Introduction

This is a chatbot project built using Natural Language Processing (NLP). The goal is to create an interactive chatbot capable of understanding user input and providing meaningful responses based on predefined patterns and intents. The chatbot uses libraries like `nltk` for NLP tasks, `scikit-learn` for machine learning, and `streamlit` to create an intuitive web interface.

---

## Features

- Recognizes various user intents, such as greetings, farewells, and expressing gratitude.
- Generates responses dynamically based on user input.
- Saves conversation history that users can review anytime.
- Developed in Python, using popular libraries for NLP and user interaction.

---

## Technology Stack

- **Programming Language**: Python
- **Libraries Used**:
  - NLTK (Natural Language Toolkit) for NLP tasks
  - Scikit-learn for implementing machine learning models
  - Streamlit for developing the web-based interface
- **Data Format**: JSON for defining intents

---

## How to Set Up

### Step 1: Clone the Repository

First, clone the repository and navigate to the project folder:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Set Up a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **Linux/Mac**:
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Step 4: Download NLTK Data

The chatbot requires NLTK resources like `punkt`. Download them using the following code:

```python
import nltk
nltk.download('punkt')
```

---

## Running the Chatbot

To start the chatbot, run the following command:

```bash
streamlit run app.py
```

This will launch a web interface where you can interact with the chatbot. Type your message in the input box and press Enter to get a response.

---

## Understanding Intents

The chatbot's responses are determined by the `intents.json` file. This file contains:

- **Tags**: Categories of user intents
- **Patterns**: Examples of user input
- **Responses**: Predefined replies for each tag

You can customize this file to add new intents or modify existing ones to suit your use case.

---

## Conversation History

All user interactions are logged in a CSV file named `chat_log.csv`. This provides a record of past conversations, which can be useful for debugging or analysis. You can view this history in the Streamlit interface by selecting the "Conversation History" option in the sidebar.

---

