#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QRadioButton, QButtonGroup, QGroupBox)
from random import shuffle, randint

class Question():
    def __init__(self, question, rihgt_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.rihgt_answer = rihgt_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Государственый язык Бразилия', 'Полтругальский','Англиский','Испанский','Бразилия'))
question_list.append(Question('Какого цвета нету на флаге России?', 'Зеленый', 'Белый', 'Красный', 'Синий'))
question_list.append(Question('Национальная хижина юкутов?', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
question_list.append(Question('в каком году вышел роблокс', '2006', '2007', '2008', '2009'))
question_list.append(Question('какое имя у создателя майна?', 'Маркус', 'Бутаков', 'Платов', 'Марат'))
question_list.append(Question('формула силы тегатения', 'g*(Mm/R^2)', 'h*(Mm/R^2)', 'b*(Mm/R^2)', 'x*(Mm/R^2)')) 
question_list.append(Question('в каом году вышла терария', '2011', '2012', '2010', '2020'))

app = QApplication([])

btn_OK = QPushButton('Ответ')
lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox =  QGroupBox("Варианты ответов")

rbtn_1 = QRadioButton('1 вариант')
rbtn_2 = QRadioButton('2 вариант')
rbtn_3 = QRadioButton('3 вариант')
rbtn_4 = QRadioButton('4 вариант')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

Layout_ans1 = QHBoxLayout()
Layout_ans2 = QVBoxLayout()
Layout_ans3 = QVBoxLayout()
Layout_ans2.addWidget(rbtn_1)
Layout_ans2.addWidget(rbtn_2)
Layout_ans3.addWidget(rbtn_3)
Layout_ans3.addWidget(rbtn_4)

Layout_ans1.addLayout(Layout_ans2)
Layout_ans1.addLayout(Layout_ans3)

RadioGroupBox.setLayout(Layout_ans1)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel("прав ты или нет?")
lb_Correct = QLabel("ответ будет тут!")

Layout_res = QVBoxLayout()
Layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
Layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(Layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следущий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.rihgt_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.rihgt_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()
    
def check_answer():
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print('Рейтинг:', (window.score/window.total*100), "%")
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            


def next_question():
    window.total +=1
    print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if btn_OK.text() =='Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')

btn_OK.clicked.connect(click_ok)
window.score = 0
window.total = 0

next_question()
window.resize(400, 300)
window.show()
app.exec()




