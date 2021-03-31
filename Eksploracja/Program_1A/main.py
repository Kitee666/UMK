import tkinter as tk
from tkinter import messagebox
import threading
import numpy as np


class ShowData(object):
    def __init__(self, matrix, value):
        self.root = tk.Tk()
        self.matrix = matrix.astype(int)
        self.value = value
        self.e = []
        self.e.append(tk.Label(self.root, width=8, text='Real \ Prob', borderwidth=2, relief='raised'))
        self.e[-1].grid(row=0, column=0)
        self.e.append(tk.Label(self.root, width=8, text='Other', borderwidth=2, relief='raised'))
        self.e[-1].grid(row=0, column=1)
        self.e.append(tk.Label(self.root, width=8, text=str(self.value), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=0, column=2)
        self.e.append(tk.Label(self.root, width=8, text='Other', borderwidth=2, relief='raised'))
        self.e[-1].grid(row=1, column=0)
        self.e.append(tk.Label(self.root, width=8, text=str(self.matrix[0, 0]), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=1, column=1)
        self.e.append(tk.Label(self.root, width=8, text=str(self.matrix[0, 1]), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=1, column=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.value), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=2, column=0)
        self.e.append(tk.Label(self.root, width=8, text=str(self.matrix[1, 0]), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=2, column=1)
        self.e.append(tk.Label(self.root, width=8, text=str(self.matrix[1, 1]), borderwidth=2, relief='raised'))
        self.e[-1].grid(row=2, column=2)

        self.accuracy = 0
        self.tenderness = 0
        self.specificity = 0
        self.errors = 0
        self.point_false_negative = 0
        self.point_false_positive = 0
        self.proportion_true_positive = 0
        self.proportion_true_negative = 0
        self.proportion_false_positive = 0
        self.proportion_false_negative = 0

        matrix_sum = np.sum(self.matrix)
        if matrix_sum != 0:
            self.accuracy = np.round(np.sum(np.diag(self.matrix)) / matrix_sum * 100, 2)
            if np.sum(self.matrix[1]) != 0:
                self.tenderness = np.round(self.matrix[1, 1] / np.sum(self.matrix[1]) * 100, 2)
            if np.sum(self.matrix[0]) != 0:
                self.specificity = np.round(self.matrix[0, 0] / np.sum(self.matrix[0]) * 100, 2)
            self.errors = np.round(100 - self.accuracy, 1)
            self.point_false_negative = np.round(100 - self.tenderness, 2)
            self.point_false_positive = np.round(100 - self.specificity, 2)
            if np.sum(self.matrix.T[1]) != 0:
                self.proportion_true_positive = np.round(self.matrix[1, 1] / np.sum(self.matrix.T[1]) * 100, 2)
            if np.sum(self.matrix.T[0]) != 0:
                self.proportion_true_negative = np.round(self.matrix[0, 0] / np.sum(self.matrix.T[0]) * 100, 2)
            self.proportion_false_positive = np.round(100 - self.proportion_true_positive, 2)
            self.proportion_false_negative = np.round(100 - self.proportion_true_negative, 2)

        self.e.append(tk.Label(self.root, width=16, text='Trafność:'))
        self.e[-1].grid(row=3, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.accuracy) + '%'))
        self.e[-1].grid(row=3, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Całkowity wsp błędu:'))
        self.e[-1].grid(row=4, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.errors) + '%'))
        self.e[-1].grid(row=4, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Czułość:'))
        self.e[-1].grid(row=5, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.tenderness) + '%'))
        self.e[-1].grid(row=5, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Swoistość:'))
        self.e[-1].grid(row=6, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.specificity) + '%'))
        self.e[-1].grid(row=6, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Wsk fałsz neg:'))
        self.e[-1].grid(row=7, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.point_false_negative) + '%'))
        self.e[-1].grid(row=7, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Wsk fałsz poz:'))
        self.e[-1].grid(row=8, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.point_false_positive) + '%'))
        self.e[-1].grid(row=8, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Prop praw poz:'))
        self.e[-1].grid(row=9, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.proportion_true_positive) + '%'))
        self.e[-1].grid(row=9, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Prop praw neg:'))
        self.e[-1].grid(row=10, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.proportion_true_negative) + '%'))
        self.e[-1].grid(row=10, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Prop fałsz poz:'))
        self.e[-1].grid(row=11, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.proportion_false_positive) + '%'))
        self.e[-1].grid(row=11, column=2)

        self.e.append(tk.Label(self.root, width=16, text='Prop fałsz neg:'))
        self.e[-1].grid(row=12, column=0, columnspan=2)
        self.e.append(tk.Label(self.root, width=8, text=str(self.proportion_false_negative) + '%'))
        self.e[-1].grid(row=12, column=2)

        self.root.mainloop()


class Table(object):
    def __init__(self, k=2):
        self.root = tk.Tk()
        self.vcmd = self.root.register(self.callback)
        self.k = k
        self.e = []
        self.matrix = np.zeros((self.k, self.k))
        self.accuracy = tk.Label(self.root, width=8, text='0%')
        self.errors = tk.Label(self.root, width=8, text='0%')
        for i in range(self.k + 1):
            for j in range(self.k + 1):
                if i == 0:
                    if j == 0:
                        self.e.append(tk.Label(self.root, width=8, text='Real \ Prob'))
                    else:
                        self.e.append(tk.Button(self.root, width=8, text=str(j), command=lambda val=j: self.show(val)))
                elif j == 0:
                    self.e.append(tk.Button(self.root, width=8, text=str(i), command=lambda val=i: self.show(val)))
                else:
                    self.e.append(tk.Entry(self.root, width=8, validate='all',
                                           validatecommand=(self.vcmd, '%P', i, j)))
                    self.e[-1].insert(0, 0)
                self.e[-1].grid(row=i, column=j)
        self.e.append(tk.Label(self.root, width=16, text='Ogólna trafność:'))
        self.e[-1].grid(row=i + 1, column=0, columnspan=2)
        self.accuracy.grid(row=i + 1, column=2)
        self.e.append(tk.Label(self.root, width=16, text='Całkowity wsp błędu:'))
        self.e[-1].grid(row=i + 2, column=0, columnspan=2)
        self.errors.grid(row=i + 2, column=2)
        self.root.mainloop()

    def callback(self, value, i, j):
        if str.isdigit(value):
            self.matrix[int(i) - 1, int(j) - 1] = int(value)
            self.predict()
            return True
        elif value == "":
            self.matrix[int(i) - 1, int(j) - 1] = 0
            self.predict()
            return True
        else:
            return False

    def predict(self):
        matrix_sum = np.sum(self.matrix)
        if matrix_sum == 0:
            accuracy = 0
            errors = 100
        else:
            accuracy = np.round(np.sum(np.diag(self.matrix)) / matrix_sum * 100, 2)
            errors = np.round(100 - accuracy, 2)
        self.accuracy['text'] = str(accuracy) + "%"
        self.errors['text'] = str(errors) + "%"

    def show(self, value):
        calc_matrix = np.zeros((2, 2))
        calc_matrix[1, 1] = self.matrix[value - 1, value - 1]
        calc_matrix[1, 0] = np.sum(self.matrix[value - 1]) - calc_matrix[1, 1]
        calc_matrix[0, 1] = np.sum(self.matrix.T[value - 1]) - calc_matrix[1, 1]
        calc_matrix[0, 0] = np.sum(self.matrix) - np.sum(calc_matrix)
        ShowData(calc_matrix, value)


class Gui(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry(str(200) + "x" + str(50))
        self.text = tk.Label(self.root, text='Ilość zmiennych')
        self.text.grid(row=0, column=0)
        self.k = tk.StringVar()
        self.vcmd = (self.root.register(self.callback))
        self.k_entry = tk.Entry(self.root, text='2', textvariable=self.k, validate='all',
                                validatecommand=(self.vcmd, '%P'))
        self.k_entry.bind('<Return>', self.open)
        self.k_entry.grid(row=1, column=0)
        self.k_click = tk.Button(self.root, text='Zatwierdz', command=self.open)
        self.k_click.grid(row=1, column=1)
        self.root.mainloop()

    @staticmethod
    def callback(value):
        if str.isdigit(value) or value == "":
            return True
        else:
            return False

    def open(self, e=None):
        try:
            n = int(self.k.get())
            if n < 2:
                messagebox.showerror("Error", "Liczba musi być nie mniejsza niż 2")
            elif n > 20:
                messagebox.showerror("Error", "Liczba musi mniejsza niż 20")
            else:
                Table(n)
        except ValueError:
            messagebox.showerror("Error", "Coś poszło nie tak")


Gui()
