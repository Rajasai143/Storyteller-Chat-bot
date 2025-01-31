from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=api_key)

# Initialize Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_age_appropriate_prompt(age_group, theme):
    prompts = {
        "3-6": f"Create a very short, simple, and educational story about {theme}. Use basic vocabulary, "
               "repetitive patterns, and include moral lessons. Avoid any scary elements.",
        
        "7-12": f"Create an engaging story about {theme} with clear plot, interesting characters, and "
                "positive messages. Include some challenging vocabulary but keep the story appropriate "
                "for elementary school children.",
        
        "13-16": f"Create a more complex story about {theme} that includes themes relevant to teenagers, "
                 "character development, and meaningful life lessons. The story can have more sophisticated "
                 "plot elements while remaining age-appropriate.",
        
        "17+": f"Create a sophisticated story about {theme} that can include complex themes, detailed "
               "character development, and deeper meanings. The story can tackle more mature subjects "
               "while maintaining appropriate content."
    }
    return prompts.get(age_group, prompts["7-12"])

def get_story_response(age_group, theme, additional_preferences):
    prompt = get_age_appropriate_prompt(age_group, theme)
    if additional_preferences:
        prompt += f"\nAdditional preferences: {additional_preferences}"
    response = chat.send_message(prompt, stream=True)
    return response

# Streamlit UI
st.set_page_config(page_title="StoryTeller AI")
st.header("📚 StoryTeller AI")
st.subheader("Let me tell you a story...")

# Initialize session state for story history
if "story_history" not in st.session_state:
    st.session_state["story_history"] = []

# User inputs
age_group = st.selectbox(
    "Select age group:",
    ["3-6", "7-12", "13-16", "17+"]
)

theme = st.text_input(
    "What should the story be about? (e.g., friendship, adventure, animals)",
    placeholder="Enter a theme or topic"
)

additional_preferences = st.text_area(
    "Any additional preferences? (optional)",
    placeholder="E.g., make it funny, set it in space, include dragons..."
)

generate_button = st.button("Generate Story ✨")

if generate_button and theme:
    with st.spinner("Creating your story... 🌟"):
        response = get_story_response(age_group, theme, additional_preferences)
        
        st.subheader("Your Story:")
        story_container = st.container()
        story_text = ""
        
        # Stream the story
        for chunk in response:
            story_text += chunk.text
            story_container.write(story_text)
        
        # Save to history
        st.session_state["story_history"].append({
            "age_group": age_group,
            "theme": theme,
            "story": story_text
        })

# Display story history
if st.session_state["story_history"]:
    st.subheader("Previous Stories")
    for i, story in enumerate(reversed(st.session_state["story_history"]), 1):
        with st.expander(f"Story {i}: {story['theme']} (Age: {story['age_group']})"):
            st.write(story['story'])