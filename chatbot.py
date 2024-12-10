# chatbot.py
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Download nltk tokenizer
nltk.download('punkt')

# Define corpus and responses
corpus = [
    "Hello, how can I help you?",
    "What services do you offer?",
    "Tell me about your company.",
    "How can I contact support?",
    "Goodbye!"
]

responses = [
    "Hi! I'm here to assist you.",
    "We offer a range of services, including AI solutions and support.",
    "Our company specializes in AI-driven innovations.",
    "You can contact support via email at support@example.com.",
    "Goodbye! Have a great day."
]

# Preprocess the text
corpus = [sentence.lower() for sentence in corpus]

# Vectorize the corpus using a shared vectorizer
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(corpus).toarray()

# Chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Use the same vectorizer to transform the user input
    user_vec = vectorizer.transform([user_input]).toarray()
    
    # Compute cosine similarity
    similarity = cosine_similarity(user_vec, vectors).flatten()
    max_index = np.argmax(similarity)
    
    # Return response based on similarity
    if similarity[max_index] > 0.5:
        return responses[max_index]
    else:
        return "I'm sorry, I didn't understand that. Can you rephrase?"
