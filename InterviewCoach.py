import openai
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QWidget, QInputDialog


class collegecoach(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Interview Coach")
        self.label = QLabel("Enter which college you want an interview from:")
        self.college_input = QLineEdit()
        self.ask_button = QPushButton("Ask Questions")
        self.ask_button.clicked.connect(self.college_interview)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.college_input)
        self.layout.addWidget(self.ask_button)
        self.layout.addWidget(self.output_text)
        self.setLayout(self.layout)


    def college_interview(self):
        openai.api_key = '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'
        college = self.college_input.text()
        repeat = True
        while repeat:
            i = 0
            while i < 5:
                question = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt="Generate a college interview question as a college admissions officer from "+college+": ",
                    max_tokens=500
                )
                self.output_text.append(question["choices"][0]["text"])
                user_answer, ok = QInputDialog.getText(self, "Your answer: ", "Enter your answer:")
                if ok and user_answer:
                    feedback = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=(f"Give constructive criticism on the following response: {user_answer}"),
                        max_tokens=500
                    )
                self.output_text.append(feedback["choices"][0]["text"])
                i += 1
            again, ok = QInputDialog.getText(self, "Another round?", "Do you want 5 more questions? (Y/N)")
            if (again.lower() == "n"):
                repeat = False



class jobcoach(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Interview Coach")
        self.label = QLabel("Enter which field you want interview questions in:")
        self.job_input = QLineEdit()
        self.ask_button = QPushButton("Ask Questions")
        self.ask_button.clicked.connect(self.ask_questionsjob)
        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.job_input)
        self.layout.addWidget(self.ask_button)
        self.layout.addWidget(self.output_text)
        self.setLayout(self.layout)

    def ask_questionsjob(self):
        openai.api_key = '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'
        job = self.job_input.text()
        repeat = True
        while repeat:
            i = 0
            while i < 5:
                question = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt="Generate a" + job + " job interview question.",
                    max_tokens=500
                )
                self.output_text.append(question["choices"][0]["text"])
                user_answer, ok = QInputDialog.getText(self, "Your answer: ", "Enter your answer:")
                if ok and user_answer:
                    feedback = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=(f"Give constructive criticism on the following response: {user_answer}"),
                        max_tokens=500
                    )
                self.output_text.append(feedback["choices"][0]["text"])
                i += 1
            again, ok = QInputDialog.getText(self, "Another round?", "Do you want 5 more questions? (Y/N)")
            if (again.lower() == "n"):
                repeat = False

def ask_interview_type(self):
    interview_type, ok = QInputDialog.getText(self, "Interview Type", "Would you like a job or college interview? (J/C)")
    if (interview_type.lower() == "j"):
        self.jobcoach = jobcoach()
        self.jobcoach.show()
    elif (interview_type.lower() == "c"):
        self.collegecoach = collegecoach()
        self.collegecoach.show()



def main():
    app = QApplication(sys.argv)
    choice, ok = QInputDialog.getText(None, "Interview Coach", "Do you want a job interview or college interview? (Job/College)")
    if ok and choice.lower() == "job":
        jobcoach_widget = jobcoach()
        jobcoach_widget.show()
    elif ok and choice.lower() == "college":
        collegecoach_widget = collegecoach()
        collegecoach_widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()