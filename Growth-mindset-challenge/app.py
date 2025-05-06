import streamlit as st

# Title of the app
st.title("Growth Mindset Challenge")

# Introduction
st.write("""
Welcome to the Growth Mindset Challenge! This app is designed to help you adopt a growth mindset and track your progress.
""")

# Add a section for setting goals
st.header("Set Your Learning Goals")
goal = st.text_input("What is your learning goal for today?")
if goal:
    st.write(f"Great! You're working on: **{goal}**")

# Add a section for reflecting on learning
st.header("Reflect on Your Learning")
reflection = st.text_area("What did you learn today?")
if reflection:
    st.write("Thank you for reflecting! Keep up the good work.")

# Add a section for feedback
st.header("Seek Feedback")
feedback = st.text_area("What feedback have you received recently?")
if feedback:
    st.write("Use this feedback to improve and grow!")

# Add a motivational quote
st.header("Daily Motivation")
st.write("Here's a motivational quote to keep you going:")
st.write("> *The only limit to our realization of tomorrow is our doubts of today.* – Franklin D. Roosevelt")

# Footer
st.write("---")
st.write("Built with ❤️ using Streamlit")