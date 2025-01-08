import spacy
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import pipeline
import pandas as pd
from .youtube_recommendation import get_youtube_recommendations

# Load spaCy English NLP model
nlp = spacy.load("en_core_web_sm")

# Predefined courses and skill levels
courses = {
    "data science": ["Python for Data Science", "Machine Learning Basics", "Deep Learning"],
    "web development": ["HTML/CSS Basics", "React.js", "Node.js"],
    "AI": ["Intro to AI", "NLP Basics", "Reinforcement Learning"],
    "blockchain": ["Blockchain Fundamentals", "Smart Contracts"],
}

# User skill levels and recommendations
level_recommendations = {
    "beginner": "We recommend starting with foundational courses to build your skills.",
    "intermediate": "Consider advancing with project-based learning.",
    "advanced": "Explore cutting-edge research and tools in your field of interest.",
}

# NLP-based topic extraction using LangChain
def extract_topics(user_response):
    prompt_template = PromptTemplate(
        input_variables=["user_response"],
        template="Extract key learning topics from the following text: {user_response}"
    )
    chain = LLMChain(llm=LangChain(), prompt=prompt_template)
    topics = chain.run(user_response=user_response.lower())
    return topics.split(', ')  # Assuming the response is a comma-separated list of topics

# Proficiency prediction using Ollama
def predict_proficiency(user_answers):
    ollama_client = Ollama(api_key='your_ollama_api_key')
    query = f"Based on the following response, determine the user's proficiency level: {user_answers}"
    response = ollama_client.query(query)
    # Assuming Ollama returns a clear proficiency level as "beginner", "intermediate", or "advanced"
    return response['proficiency_level']

# Main onboarding process
def onboarding(user_goals, user_level_response):
    # Step 1: Extract topics
    topics = extract_topics(user_goals)
    
    # Step 2: Predict proficiency
    user_level = predict_proficiency(user_level_response)

    # Step 3: Match topics with courses
    recommendations = []
    for topic in topics:
        if topic in courses:
            recommendations.extend(courses[topic])
    
    # Step 4: Provide recommendations
    return {
        "level": user_level,
        "recommendations": recommendations if recommendations else ["Explore general skills to start your journey."],
        "message": level_recommendations[user_level]
    }

# Example user input
if __name__ == "__main__":
    print("Welcome! Let's customize your learning journey.")
    user_goals = input("What do you want to learn? (e.g., data science, AI, web development): ")
    user_level_response = input("What is your current skill level? (beginner, intermediate, advanced): ")
    
    results = onboarding(user_goals, user_level_response)
    print("\nYour Learning Plan:")
    print(f"Proficiency Level: {results['level']}")
    print("Recommended Courses:", ", ".join(results["recommendations"]))
    print(results["message"])

  
def onboarding(user_goals, user_level_response):
    # Existing code for extracting topics and predicting proficiency
    topics = extract_topics(user_goals)
    user_level = predict_proficiency(user_level_response)

    # Match topics with courses and get YouTube recommendations
    recommendations = []
    youtube_videos = []
    for topic in topics:
        if topic in courses:
            recommendations.extend(courses[topic])
            youtube_videos.extend(get_youtube_recommendations(f"{topic} {user_level}", max_results=3))

    return {
        "level": user_level,
        "recommendations": recommendations if recommendations else "Explore general skills to start your journey.",
        "youtube_videos": youtube_videos if youtube_videos else "No videos found for your selected topics.",
        "message": level_recommendations[user_level]
    }

