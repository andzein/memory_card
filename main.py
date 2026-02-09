from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup)
from random import shuffle

total = 0
score = 0

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    grop.hide()
    grop2.show()   
    button.setText('Следующий вопрос')
def show_question():
    grop2.hide()
    grop.show()
    button.setText('Ответить')
    radiogrop.setExclusive(False)
    radiobutton1.setChecked(False)
    radiobutton2.setChecked(False)
    radiobutton3.setChecked(False)
    radiobutton4.setChecked(False)
    radiogrop.setExclusive(True)

def next_question():
    global questions
    global total
    shuffle(questions)
    if len(questions) == 0:
        questions.append(Question('вопросы кончились :(', " ", " ", " ", " "))
    else:
        total += 1
    q = questions[0]
    questions.remove(q)
    ask(q)   
#привет
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label.setText(q.question)
    label2.setText("Правильный ответ: "+q.right_answer)
    show_question()

def show_correct(res):
    label1.setText(res)
    show_result()

def check_answer():
    global score
    if answers[0].isChecked():
        show_correct("правильный ответ")
        score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correct("неправильный ответ")

def i():
    if button.text() == ("Ответить"):
        check_answer()
    else:
        next_question()


app = QApplication([])
wiget = QWidget()
wiget.setWindowTitle('Memo Card')
label = QLabel('Самый сложный вопрос в мире!')
button = QPushButton('Ответить')
button.clicked.connect(i)
grop = QGroupBox('')

radiobutton1 = QRadioButton("неверн")
radiobutton2 = QRadioButton("верн")
radiobutton3 = QRadioButton("неверн")
radiobutton4 = QRadioButton("неверн")
radiogrop = QButtonGroup()
radiogrop.addButton(radiobutton1)
radiogrop.addButton(radiobutton2)
radiogrop.addButton(radiobutton3)
radiogrop.addButton(radiobutton4)

answers = [radiobutton1, radiobutton2, radiobutton3, radiobutton4]

vlayut1 = QVBoxLayout()
hlayut1 = QHBoxLayout()
hlayut2 = QHBoxLayout()

hlayut2.addWidget(radiobutton3)
hlayut2.addWidget(radiobutton4)
hlayut1.addWidget(radiobutton1)
hlayut1.addWidget(radiobutton2)
vlayut1.addLayout(hlayut1)
vlayut1.addLayout(hlayut2)
grop.setLayout(vlayut1)

grop2 = QGroupBox('')
label1 = QLabel('прав или нет')
label2 = QLabel('')
vlayut3 = QVBoxLayout()
vlayut3.addWidget(label1)
vlayut3.addWidget(label2)
grop2.setLayout(vlayut3)

hlayut3 = QHBoxLayout()
hlayut4 = QHBoxLayout()
hlayut5 = QHBoxLayout()

hlayut3.addStretch(1)
hlayut3.addWidget(label)
hlayut3.addStretch(1)
hlayut4.addWidget(grop)
hlayut4.addWidget(grop2)
hlayut5.addWidget(button)
vlayut2 = QVBoxLayout()
vlayut2.addLayout(hlayut3)
vlayut2.addLayout(hlayut4)
vlayut2.addLayout(hlayut5)
vlayut2.setSpacing(8)
grop2.hide()
schot = -1
questions = []

questions.append(Question("В каком году была основана Москва?", "1147", "вчера", "после завтра", "1284"))
questions.append(Question("Что такое Roblox?", "Многопользовательская игра", "язык програмирования", "название кафе в Лондоне", "незнаю"))
questions.append(Question("Сколько лет игре 'Rust?", "11", "28", "не лет а 3 месяца", "так она выходит в 2027"))
questions.append(Question("Что общего между котом и выходными?", "они заставляют нас радоватся им", "оба пушистые", "Оба любят молоко", "Оба приходят неожиданно"))
next_question()
wiget.setLayout(vlayut2)



wiget.show()
app.exec()


print(score / total * 100)
