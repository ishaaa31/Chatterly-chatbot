import streamlit as st
from chatterly.memory_manager import (
    add_fact, get_fact, add_episodic, get_recent_conversations, get_working_memory
)
from chatterly.search_engine import search_answer
from chatterly.semantic_memory import store_fact, query_facts
from chatterly.conversation import get_bot_reply

st.set_page_config(page_title="Chatterly", layout="wide")
st.title("Chatterly - Memory Augmented Chatbot")
st.markdown("Ask me anything or tell me about yourself!")

# Sidebar: shows memories
st.sidebar.header("Memory")

st.sidebar.subheader("Working Memory")
for k, v in get_working_memory().items():
    st.sidebar.write(f"{k}: {v}")

st.sidebar.subheader("Episodic Memory")
for msg in get_recent_conversations(5):
    st.sidebar.write(f"- {msg}")

st.sidebar.subheader("Semantic Memory (Neo4j)")
try:
    facts = query_facts()
    for h, r, t in facts:
        st.sidebar.write(f"{h} —[{r}]→ {t}")
except Exception as e:
    st.sidebar.write("Semantic memory unavailable.")
    st.sidebar.write(str(e))

# Chat input
user_input = st.text_input("You:", "")

if st.button("Send") and user_input.strip():
    text = user_input.strip().lower()
    response = ""

    # --- Memory Retrieval ---
    if "where do i live" in text:
        place = get_fact("place")
        response = f"You live in {place}." if place else "I don't know where you live yet."

    elif "what do i like" in text:
        hobby = get_fact("likes")
        response = f"You like {hobby}." if hobby else "I haven't learned your hobbies yet."

    elif "what's my name" in text or "who am i" in text:
        name = get_fact("name")
        response = f"Your name is {name}." if name else "I don't know your name yet."

    # --- Memory Storage + Neo4j ---
    elif "my name is" in text:
        name = text.split("is")[-1].strip()
        add_fact("name", name)
        store_fact("User", "has_name", name)
        response = f"Nice to meet you, {name}!"

    elif "i live in" in text:
        place = text.split("in")[-1].strip()
        add_fact("place", place)
        store_fact("User", "lives_in", place)
        response = f"Got it! You're from {place}."

    elif "i like" in text:
        hobby = text.split("like")[-1].strip()
        add_fact("likes", hobby)
        store_fact("User", "likes", hobby)
        response = f"Oh nice, I'll remember that you like {hobby}."

    elif "is a" in text:
        parts = text.split("is a")
        subject = parts[0].strip()
        obj = parts[1].strip()
        store_fact(subject, "is_a", obj)
        response = f"Got it! {subject} is a {obj}."

    # --- Factual Search ---
    elif "search" in text or "tell me about" in text:
        response = search_answer(text)

    # --- Gemini-powered reply ---
    else:
        response = get_bot_reply(user_input)

    # Update episodic memory
    add_episodic(f"User: {user_input}")
    add_episodic(f"Bot: {response}")

    st.write(f"**Chatterly**: {response}")
