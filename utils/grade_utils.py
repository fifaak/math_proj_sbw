import streamlit as st

def get_grades():
    math = st.sidebar.number_input("เกรดวิชาคณิตศาสตร์:", 0.0, 4.0, step=0.5)
    thai = st.sidebar.number_input("เกรดวิชาภาษาไทย:", 0.0, 4.0, step=0.5)
    society = st.sidebar.number_input("เกรดวิชาสังคมศึกษา:", 0.0, 4.0, step=0.5)
    eng = st.sidebar.number_input("เกรดวิชาภาษาอังกฤษ:", 0.0, 4.0, step=0.5)
    sci = st.sidebar.number_input("เกรดวิชาวิทยาศาสตร์:", 0.0, 4.0, step=0.5)
    return math, thai, society, eng, sci
