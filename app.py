import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Setup NLTK
ssl._create_default_https_context = ssl._create_unverified_context
nltk.data.path.append(os.path.abspath("nltk_data"))
nltk.download('punkt')

# Load intents
file_path = os.path.abspath("./intents.json")
if not os.path.exists(file_path):
    st.error("Error: 'intents.json' file not found.")
    st.stop()

with open(file_path, "r") as file:
    intents = json.load(file)

# Initialize model components
vectorizer = TfidfVectorizer(ngram_range=(1, 2))  # Simplify vectorization
clf = LogisticRegression(random_state=0, max_iter=10000)

# Prepare training data
tags, patterns = [], []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern.lower().strip())

# Train model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text.lower().strip()])
    tag = clf.predict(input_text)[0]
    for intent in intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I don't understand that."

def main():
    st.title("Chatbot with NLP")
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.write("Chat with the bot below:")
        if 'conversation' not in st.session_state:
            st.session_state.conversation = []

        user_input = st.text_input("You:")
        if user_input:
            response = chatbot(user_input)
            st.session_state.conversation.append((user_input, response))

            # Save chat history
            with open('chat_log.csv', 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                csv_writer.writerow([user_input, response, timestamp])

            # Display conversation
            for u_input, bot_response in st.session_state.conversation:
                st.write(f"You: {u_input}")
                st.write(f"Bot: {bot_response}")
                st.markdown("---")

    elif choice == "Conversation History":
        if os.path.exists('chat_log.csv'):
            st.write("Previous Conversations:")
            with open('chat_log.csv', 'r', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader, None)  # Skip header
                for row in csv_reader:
                    st.text(f"You: {row[0]} \nBot: {row[1]} \nTime: {row[2]}")
        else:
            st.warning("No conversation history found.")

    elif choice == "About":
        st.subheader("About This Chatbot")
        st.write("This chatbot uses NLP techniques and Logistic Regression for intent classification.")
        st.write("The interface is built using Streamlit, allowing user-friendly interaction.")

if __name__ == '__main__':
    main()
