#question_utils.py
import streamlit as st

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
import streamlit as st


# Update the choices dictionary with emojis
choices = {
    "😡 ": 1.0,  # Strongly disagree
    "😕 ": 2.0,            # Disagree
    "😐 ": 3.0,                  # Neutral
    "😊 ": 4.0,               # Agree
    "😍 ": 5.0      # Strongly agree
}

def question(subject):
    sum = 0
    i =1
    for subquestion in subject:
        # Use radio buttons for each subquestion with emoji options and horizontal layout
        choice = st.radio(str(i)+".) "+subquestion, list(choices.keys()), horizontal=True)
        sum += choices[choice]
        i+=1
    return sum
