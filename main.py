import streamlit as st
import matplotlib.font_manager as fm
from utils.question_utils import question
from utils.grade_utils import get_grades
from utils.chart_utils import radar_chart, plot_grade_comparison, plot_equation

# Load the custom font
font_path = "./Prompt/Prompt-Medium.ttf"
prompt_font = fm.FontProperties(fname=font_path)

# Sidebar for grade input
math, thai, society, eng, sci = get_grades()

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

st.title('โปรแกรมแนะแนวการศึกษาต่อในระดับชั้นมัธยมศึกษาตอนปลาย')

with st.form("grades_form"):
    math_question = question(math_question_lst)
    thai_question = question(thai_question_lst)
    society_question = question(society_question_lst)
    eng_question = question(eng_question_lst)
    sci_question = question(sci_question_lst)
    submit_button = st.form_submit_button(label="ประมวลผล")

if submit_button:
        # Retrieve question sums from session state and perform the calculation
    

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
        # Rounding the totals to 2 decimal places
        totals = [round(y, 2) for y in [y1, y2, y3, y4]]
        print(totals)
        subjects = ["วิทยาศาสตร์-คณิตศาสตร์", "ศิลป์ภาษา", "ภาษาอังกฤษ-คณิตศาสตร์", "ภาษาไทยและกฎหมาย"]
        max_score = max(totals)
        recommended_subject = [subjects[i] for i, total in enumerate(totals) if total == max_score]

        # Using Markdown to create bullet points for recommended subjects
        st.markdown("สายการเรียนที่แนะนำ :\n" + "\n".join([f"- {subject}" for subject in recommended_subject]))

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
        plot_equation(x1, x2, x3, x4, x5, y1, y2, y3, y4)