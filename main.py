import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Use the font directly in Matplotlib plots
# Mapping descriptive choices to corresponding numerical values
choices = {
    "ไม่เห็นด้วยอย่างยิ่ง": 1.0,
    "ไม่เห็นด้วย": 2.0,
    "เฉยๆ": 3.0,
    "เห็นด้วย": 4.0,
    "เห็นด้วยอย่างยิ่ง": 5.0
}

# Function to calculate the question scores based on selected choices
def question(subject):
    sum = 0
    for subquestion in subject:
        choice = st.selectbox(subquestion, list(choices.keys()))
        sum += choices[choice]
    return sum

# Define the questions
math_question_lst = ["คุณชอบที่จะใช้เวลาว่างในการหาวิธีแก้ปัญหาหรือเล่นเกมที่ต้องใช้การคิดวิเคราะห์",
                     "คุณรู้สึกสบายใจเมื่อต้องเผชิญกับปัญหาหรือสถานการณ์ที่ต้องใช้ตรรกะในการแก้ไข",
                     "คุณมักจะหาโอกาสพัฒนาทักษะการวิเคราะห์ข้อมูลในชีวิตประจำวัน",
                     "คุณมักจะตั้งคำถามกับข้อมูลที่ซับซ้อนเพื่อหาคำตอบที่ดีที่สุด",
                     "คุณรู้สึกตื่นเต้นเมื่อพบกับความท้าทายทางความคิดที่ต้องใช้การคำนวณเพื่อแก้ปัญหา"]

sci_question_lst = ["คุณรู้สึกสนุกเมื่อได้ทดลองหรือค้นพบสิ่งใหม่",
                    "คุณมักจะตั้งข้อสงสัยเกี่ยวกับปรากฏการณ์ธรรมชาติที่เกิดขึ้นรอบตัวคุณ",
                    "คุณสนใจที่จะรู้ว่ากระบวนการทำงานของเครื่องจักรหรือเครื่องมือทำงานอย่างไร",
                    "คุณชอบเรียนรู้ว่าธรรมชาติและสิ่งแวดล้อมรอบตัวคุณมีการเปลี่ยนแปลงอย่างไรบ้าง",
                    "คุณชอบที่จะตั้งคำถามเกี่ยวกับโลกและจักรวาลเพื่อหาคำตอบด้วยตัวเอง"]

thai_question_lst = ["คุณชอบที่จะเล่าเรื่องราวหรือถ่ายทอดความรู้สึกผ่านการเขียน",
                     "คุณรู้สึกว่าการอ่านหนังสือหรือบทความช่วยเปิดโลกทัศน์และความคิดของคุณ",
                     "คุณสนใจที่จะค้นหาความหมายลึกซึ้งของบทกลอนหรือเรื่องราวที่อ่าน",
                     "คุณรู้สึกว่าการเขียนหรือการสื่อสารช่วยให้คุณแสดงออกความคิดได้ดีขึ้น",
                     "คุณชอบที่จะฝึกทักษะการสื่อสารเพื่อให้สามารถแสดงออกได้ชัดเจนและเข้าใจง่ายขึ้น"]

society_question_lst = ["คุณมักสนใจข่าวสารเกี่ยวกับการเมืองหรือเหตุการณ์สำคัญในประเทศ",
                        "คุณมักจะตั้งคำถามเกี่ยวกับการทำงานของระบบการปกครองหรือเศรษฐกิจ",
                        "คุณสนใจที่จะเรียนรู้เกี่ยวกับวัฒนธรรมและประวัติศาสตร์ของประเทศต่าง",
                        "คุณรู้สึกว่าการเข้าใจสังคมและวัฒนธรรมช่วยให้คุณมีมุมมองที่กว้างขึ้น",
                        "คุณคิดว่าการมีความรู้เกี่ยวกับสังคมและโลกสามารถช่วยให้คุณเป็นพลเมืองที่ดียิ่งขึ้น"]

eng_question_lst = ["คุณรู้สึกตื่นเต้นเมื่อต้องสื่อสารกับคนต่างชาติหรือใช้ภาษาต่างประเทศ",
                    "คุณชอบที่จะฝึกทักษะการฟังและพูดในภาษาต่างประเทศผ่านสื่อต่าง",
                    "คุณมักจะหาหนังสือหรือสื่อในภาษาต่างประเทศเพื่อพัฒนาทักษะของคุณ",
                    "คุณเชื่อว่าการเข้าใจภาษาต่างประเทศจะเปิดโอกาสให้คุณได้เรียนรู้สิ่งใหม่",
                    "คุณรู้สึกมั่นใจเมื่อต้องใช้ภาษาต่างประเทศในการสื่อสารในชีวิตประจำวัน"]

# Sidebar for grade input
st.sidebar.title("กรุณาใส่เกรดเฉลี่ยรายวิชา")
math = st.sidebar.number_input("เกรดวิชาคณิตศาสตร์:", 0.0, 4.0, step=0.5)
thai = st.sidebar.number_input("เกรดวิชาภาษาไทย:", 0.0, 4.0, step=0.5)
society = st.sidebar.number_input("เกรดวิชาสังคมศึกษา:", 0.0, 4.0, step=0.5)
eng = st.sidebar.number_input("เกรดวิชาภาษาอังกฤษ:", 0.0, 4.0, step=0.5)
sci = st.sidebar.number_input("เกรดวิชาวิทยาศาสตร์:", 0.0, 4.0, step=0.5)

# Main app
st.title('โปรแกรมแนะแนวการศึกษาต่อในระดับชั้นมัธยมศึกษาตอนปลาย')

with st.form("grades_form"):
    # Questions
    st.write("### กรุณาตอบคำถามตามความรู้สึกท่าน")
    
    math_question = question(math_question_lst)
    thai_question = question(thai_question_lst)
    society_question = question(society_question_lst)
    eng_question = question(eng_question_lst)
    sci_question = question(sci_question_lst)

    submit_button = st.form_submit_button(label="ประมวลผล")

if submit_button:
    # Calculations
    math_grade = math * 10
    sci_grade = sci * 10
    thai_grade = thai * 10
    society_grade = society * 10
    eng_grade = eng * 10

    math_question = math_question * 60 / 25
    sci_question = sci_question * 60 / 25
    thai_question = thai_question * 60 / 25
    society_question = society_question * 60 / 25
    eng_question = eng_question * 60 / 25

    # Weighted sum: 40% from grade, 60% from question score
    math_total = (0.4 * math_grade) + (0.6 * math_question)
    sci_total = (0.4 * sci_grade) + (0.6 * sci_question)
    thai_total = (0.4 * thai_grade) + (0.6 * thai_question)
    society_total = (0.4 * society_grade) + (0.6 * society_question)
    eng_total = (0.4 * eng_grade) + (0.6 * eng_question)

    # Display the recommended field based on total scores
    totals = [math_total, sci_total, society_total, thai_total, eng_total]
    subjects = ["คณิตศาสตร์", "วิทยาศาสตร์", "สังคมศึกษา", "ภาษาไทย", "ภาษาอังกฤษ"]
    max_score = max(totals)
    recommended_subject = []
    for i in range(len(totals)):
        if (max_score == totals[i]):
            recommended_subject.append(subjects[i])
   
    
    st.success(f"สายการเรียนที่แนะนำ : {' '.join(recommended_subject)}")
    
    # Chart showing comparison between grades and question scores (100 points total)
    labels = ["คณิตศาสตร์", "วิทยาศาสตร์", "สังคมศึกษา", "ภาษาไทย", "ภาษาอังกฤษ"]

    # Split totals into grade (40%) and question (60%) components
    grades = [math_total * 0.4, sci_total * 0.4, society_total * 0.4, thai_total * 0.4, eng_total * 0.4]
    questions = [math_total * 0.6, sci_total * 0.6, society_total * 0.6, thai_total * 0.6, eng_total * 0.6]

    import matplotlib.font_manager as fm

    # Load the custom font (Prompt-Medium.ttf)
    font_path = "./Prompt/Prompt-Medium.ttf"  # Make sure the path is correct
    prompt_font = fm.FontProperties(fname=font_path)

    # Instead of using rcParams, set the font properties directly in each plot
    fig, ax = plt.subplots()

    # Plot grade components
    ax.barh(labels, grades, color='#5DADE2', label='Grade (40%)', align='center')

    # Plot question components on top of grade components
    ax.barh(labels, questions, left=grades, color='#F1948A', label='Question (60%)', align='center')

    # Set custom font properties for the axes and title
    ax.set_xlabel('คะแนนรวม (เต็ม 100)', fontproperties=prompt_font)
    ax.set_title('เปรียบเทียบคะแนนจากเกรดและคำถาม', fontproperties=prompt_font)
    ax.legend(prop=prompt_font)

    # Use the font properties in all text elements
    for label in ax.get_xticklabels():
        label.set_fontproperties(prompt_font)
    for label in ax.get_yticklabels():
        label.set_fontproperties(prompt_font)

    st.pyplot(fig)

