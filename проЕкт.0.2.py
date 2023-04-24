import random
import tkinter as tk

class MathProblemGUI:
    def __init__(self, master):
        self.master = master
        master.title("Решение математических примеров")

        self.problem_label = tk.Label(master, text="")
        self.problem_label.pack()

        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.generate_button = tk.Button(master, text="Сгенерировать пример", command=self.generate_problem)
        self.generate_button.pack()

        self.check_button = tk.Button(master, text="Проверить ответ", command=self.check_answer)
        self.check_button.pack()

    def generate_problem(self):
        """Генерирует пример для решения"""
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        operator = random.choice(['+', '-', '*', '/'])
        self.problem = f"{num1} {operator} {num2}"
        self.problem_label.config(text=self.problem)
        self.result_label.config(text="")

    def check_answer(self):
        """Проверяет ответ пользователя"""
        try:
            user_answer = float(self.answer_entry.get())
            answer = eval(self.problem)
            if user_answer == answer:
                self.result_label.config(text="Ответ правильный!")
            else:
                self.result_label.config(text="Ответ неправильный. Попробуйте еще раз.")
        except:
            self.result_label.config(text="Сгенерируйте число.")


root = tk.Tk()
math_problem_gui = MathProblemGUI(root)
root.mainloop()