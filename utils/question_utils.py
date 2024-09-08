import streamlit as st

choices = {
    "ไม่เห็นด้วยอย่างยิ่ง": 1.0,
    "ไม่เห็นด้วย": 2.0,
    "เฉยๆ": 3.0,
    "เห็นด้วย": 4.0,
    "เห็นด้วยอย่างยิ่ง": 5.0
}

def question(subject):
    sum = 0
    for subquestion in subject:
        choice = st.selectbox(subquestion, list(choices.keys()))
        sum += choices[choice]
    return sum
