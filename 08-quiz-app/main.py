import streamlit as st
import random
import time

st.title("Quiz App 🧠")

st.write("Welcome to the Python Quiz App! Test your knowledge of Python strings, methods, and ASCII values 🐍📚")

questions = [
    {
        "question": "What is the ASCII value of 'A'?",
        "options": [65, 97, 66, 98],
        "answer": 65
    },

    {
        "question": "Which method converts a string to lowercase?",
        "options": [".lower()", ".uppercase()", ".down()", ".toLower()"],
        "answer": ".lower()"
    },

    {
        "question": "How do you get the length of a string in Python?",
        "options": ["len()", "size()", "length()", "count()"],
        "answer": "len()"
    },

    {
        "question": "What is the Unicode representation of '🐍'?",
        "options": ["U+1F40D", "U+1F600", "U+2764", "U+1F431"],
        "answer": "U+1F40D"
    },

    {
        "question": "Which operator is used for string concatenation?",
        "options": ["+", "&", "||", ","],
        "answer": "+"
    },
    
    {
        "question": "What method removes whitespace from both ends?",
        "options": [".strip()", ".trim()", ".clean()", ".remove()"],
        "answer": ".strip()"
    },

    {
        "question": "How do you split a string into a list?",
        "options": [".split()", ".break()", ".divide()", ".toList()"],
        "answer": ".split()"
    },

    {
        "question": "Which format string syntax is correct?",
        "options": ["f'{value}'", "${value}", "%{value}", "@{value}"],
        "answer": "f'{value}'"
    },

    {
        "question": "What is the ASCII range for uppercase letters?",
        "options": ["65-90", "97-122", "48-57", "32-47"],
        "answer": "65-90"
    },
    {
        "question": "Which method checks if a string starts with specific characters?",
        "options": [".startswith()", ".begins()", ".start()", ".prefix()"],
        "answer": ".startswith()"
    },
    {
        "question": "What method converts first character to uppercase?",
        "options": [".capitalize()", ".upper()", ".title()", ".firstUpper()"],
        "answer": ".capitalize()"
    },
    {
        "question": "How are Unicode characters represented in Python strings?",
        "options": ["\\u", "\\x", "\\n", "\\t"],
        "answer": "\\u"
    },
    {
        "question": "Which method replaces a substring with another string?",
        "options": [".replace()", ".change()", ".swap()", ".substitute()"],
        "answer": ".replace()"
    },
    {
        "question": "What is the ASCII value of space character?",
        "options": ["32", "0", "64", "20"],
        "answer": "32"
    },
    {
        "question": "Which method joins list elements into string?",
        "options": [".join()", ".concat()", ".merge()", ".combine()"],
        "answer": ".join()"
    }
]

if 'current_question' not in st.session_state:
    st.session_state.current_question = random.choice(questions)


question = st.session_state.current_question

st.subheader(question["question"])

selected_options =st.radio("Select your option", question["options"] , key = "answer")

if st.button("Submit Answer"):

    if selected_options == question["answer"]:
        st.success("Correct Answer!✅")
    else:    
        st.error("Incorrect!❌ The correct answer is: " + str(question["answer"]))


    time.sleep(7)

    st.session_state.current_question = random.choice(questions)
    st.rerun()
