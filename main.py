import streamlit as st
import matplotlib.font_manager as fm
from utils.question_utils import question, math_question_lst,thai_question_lst,eng_question_lst,society_question_lst,sci_question_lst
from utils.grade_utils import get_grades
from utils.chart_utils import radar_chart, plot_grade_comparison,  plot_equation

# Load the custom font
font_path = "./Prompt/Prompt-Medium.ttf"
prompt_font = fm.FontProperties(fname=font_path)

# Sidebar for grade input
math, thai, society, eng, sci = get_grades()


st.title('โปรแกรมแนะแนวการศึกษาต่อในระดับชั้นมัธยมศึกษาตอนปลาย')

with st.form("grades_form"):
    math_question = question(math_question_lst)
    thai_question = question(thai_question_lst)
    society_question = question(society_question_lst)
    eng_question = question(eng_question_lst)
    sci_question = question(sci_question_lst)
    submit_button = st.form_submit_button(label="ประมวลผล")

if submit_button:
    # Calculate totals
    math_grade = math * 10
    sci_grade = sci * 10
    thai_grade = thai * 10
    society_grade = society * 10
    eng_grade = eng * 10

    x1 = (math_question * 60 / 25) + math_grade
    x2 = (sci_question * 60 / 25) + sci_grade 
    x3 = (thai_question * 60 / 25) + thai_grade
    x4 = (society_question * 60 / 25) + society_grade
    x5 = (eng_question * 60 / 25) + eng_grade

    y1 = (0.29 * x1) + (0.29 * x2) + (0.14 * x3) + (0.14 * x4) + (0.14 * x5)  
    y2 = (0.14 * x1) + (0.14 * x2) + (0.44 * x3) + (0.14 * x4) + (0.14 * x5)  
    y3 = (0.29 * x1) + (0.14 * x2) + (0.29 * x3) + (0.14 * x4) + (0.14 * x5)  
    y4 = (0.14 * x1) + (0.14 * x2) + (0.14 * x3) + (0.29 * x4) + (0.29 * x5)  

 
    # Display the recommended subject
    totals = [y1, y2, y3, y4]
    subjects = ["วิทยาศาสตร์-คณิตศาสตร์", "ศิลป์ภาษา", "ภาษาอังกฤษ-คณิตศาสตร์", "ภาษาไทยและกฎหมาย"]
    max_score = max(totals)
    recommended_subject = [subjects[i] for i, total in enumerate(totals) if total == max_score]

    st.success(f"สายการเรียนที่แนะนำ : {' และ '.join(recommended_subject)}")

    # Plot radar chart and grade comparison
    y_labels = ["วิทย์-คณิต", "ศิลป์ภาษา", "อังกฤษ-คณิต", "ภาษาไทยและกฎหมาย"]
    y_values = [y1, y2, y3, y4]
    
    fig2 = radar_chart(y_values, y_labels, 'คะแนนรวมของสายการเรียน', prompt_font)
    st.pyplot(fig2)

    labels = ["คณิตศาสตร์", "วิทยาศาสตร์", "สังคมศึกษา", "ภาษาไทย", "ภาษาอังกฤษ"]
    grades = [math_grade, sci_grade, society_grade, thai_grade, eng_grade]
    questions = [math_question, sci_question, society_question, thai_question, eng_question]
    
    fig1 = plot_grade_comparison(grades, questions, labels, prompt_font)
    st.pyplot(fig1)
    plot_equation(x1,x2,x3,x4,x5,y1,y2,y3,y4)