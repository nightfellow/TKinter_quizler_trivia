from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Arial"
FONT_STYLE = (FONT_NAME, 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # text_label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )

        # images
        check_image = PhotoImage(file="images/true.png")
        cross_image = PhotoImage(file="images/false.png")

        # Buttons
        self.check_button = Button(image=check_image, highlightthickness=0, command=self.true_pressed)
        self.cross_button = Button(image=cross_image, highlightthickness=0, command=self.false_pressed)

        # grids
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label.grid(column=1, row=0)
        self.check_button.grid(column=0, row=2)
        self.cross_button.grid(column=1, row=2)

        # Callings
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz ended")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
