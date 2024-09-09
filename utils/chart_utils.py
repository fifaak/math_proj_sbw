import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import streamlit as st
def radar_chart(values, labels, title, font_properties):
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='#76D7C4', alpha=0.25)
    ax.plot(angles, values, color='#76D7C4', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontproperties=font_properties)
    ax.set_title(title, fontproperties=font_properties)
    ax.yaxis.set_tick_params(labelsize=10)

    return fig

def plot_grade_comparison(grades, questions, labels, font_properties):
    fig, ax = plt.subplots()
    ax.barh(labels, grades, color='#5DADE2', label='Grade (40%)', align='center')
    ax.barh(labels, questions, left=grades, color='#F1948A', label='Question (60%)', align='center')
    ax.set_xlabel('คะแนนรวม (เต็ม 100)', fontproperties=font_properties)
    ax.set_title('เปรียบเทียบคะแนนจากเกรดและคำถาม', fontproperties=font_properties)
    ax.legend(prop=font_properties)

    for label in ax.get_xticklabels():
        label.set_fontproperties(font_properties)
    for label in ax.get_yticklabels():
        label.set_fontproperties(font_properties)

    return fig


def plot_equation(x1,x2,x3,x4,x5,y1,y2,y3,y4):
    # Display linear equations for each y with values of x in Thai format and different colors
    st.header("สมการเชิงเส้นพร้อมค่า x ที่คำนวณได้")

    st.markdown(f"""**y1 ({y1:.2f})** = 
    <span style='color: #FF5733;'>0.29 \\* คณิตศาสตร์ ({x1:.2f})</span> + 
    <span style='color: #33FF57;'>0.29 \\* วิทยาศาสตร์ ({x2:.2f})</span> + 
    <span style='color: #3357FF;'>0.14 \\* ภาษาไทย ({x3:.2f})</span> + 
    <span style='color: #FF33A1;'>0.14 \\* สังคมศึกษา ({x4:.2f})</span> + 
    <span style='color: #FFD700;'>0.14 \\* ภาษาอังกฤษ ({x5:.2f})</span>""", unsafe_allow_html=True)

    st.markdown(f"""**y2 ({y2:.2f})** = 
    <span style='color: #FF5733;'>0.14 \\* คณิตศาสตร์ ({x1:.2f})</span> + 
    <span style='color: #33FF57;'>0.14 \\* วิทยาศาสตร์ ({x2:.2f})</span> + 
    <span style='color: #3357FF;'>0.14 \\* ภาษาไทย ({x3:.2f})</span> + 
    <span style='color: #FF33A1;'>0.14 \\* สังคมศึกษา ({x4:.2f})</span> + 
    <span style='color: #FFD700;'>0.44 \\* ภาษาอังกฤษ ({x5:.2f})</span>""", unsafe_allow_html=True)

    st.markdown(f"""**y3 ({y3:.2f})** = 
    <span style='color: #FF5733;'>0.29 \\* คณิตศาสตร์ ({x1:.2f})</span> + 
    <span style='color: #33FF57;'>0.14 \\* วิทยาศาสตร์ ({x2:.2f})</span> + 
    <span style='color: #3357FF;'>0.14 \\* ภาษาไทย ({x3:.2f})</span> + 
    <span style='color: #FF33A1;'>0.14 \\* สังคมศึกษา ({x4:.2f})</span> + 
    <span style='color: #FFD700;'>0.29 \\* ภาษาอังกฤษ ({x5:.2f})</span>""", unsafe_allow_html=True)

    st.markdown(f"""**y4 ({y4:.2f})** = 
    <span style='color: #FF5733;'>0.14 \\* คณิตศาสตร์ ({x1:.2f})</span> + 
    <span style='color: #33FF57;'>0.14 \\* วิทยาศาสตร์ ({x2:.2f})</span> + 
    <span style='color: #3357FF;'>0.29 \\* ภาษาไทย ({x3:.2f})</span> + 
    <span style='color: #FF33A1;'>0.29 \\* สังคมศึกษา ({x4:.2f})</span> + 
    <span style='color: #FFD700;'>0.14 \\* ภาษาอังกฤษ ({x5:.2f})</span>""", unsafe_allow_html=True)

