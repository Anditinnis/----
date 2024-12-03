import tkinter as tk
from tkinter import filedialog, messagebox
import random
import os


def sorted_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    print("Список случайных чисел:", random_numbers)
    sorted_numbers = sorted(random_numbers)
    print("Отсортированный список:", sorted_numbers)
    print("Минимальное значение:", sorted_numbers[0])
    print("Максимальное значение:", sorted_numbers[-1])
    total_sum = 0
    for number in random_numbers:
        total_sum += number
    print("Сумма всех чисел в списке:", total_sum)
    


def create_file(filename):
    with open(filename, "w") as file:
        random_numbers = [str(random.randint(1, 100)) for _ in range(10)]
        file.write(" ".join(random_numbers))
    return random_numbers


def choose_file():
    filename = filedialog.asksaveasfilename(
        title="Выберите или создайте файл",
        defaultextension=".txt",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*")),
    )
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)


def laba2():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    sum_res = num1 + num2
    sub_res = num1 - num2
    mult_res = num1 * num2

    if num2 != 0:
        div_res = num1 / num2
        print(f"Результаты:\nСложение: {sum_res}\nВычитание: {sub_res}\nУмножение: {mult_res}\nДеление: {div_res}")
    else:
        print("Ошибка! Деление на ноль недопустимо.")


def laba1():
    name = input("Введите ваше имя: ")
    print(f"Привет, {name}! Добро пожаловать в нашу программу.")



def process_file():

    filename = file_entry.get()

    if not filename:
        messagebox.showerror("Ошибка", "Введите имя файла или выберите его.")
        return

    if not os.path.exists(filename):
        messagebox.showinfo("Информация", f"Файл {filename} не найден. Он будет создан.")
        numbers = create_file(filename)
    else:
        messagebox.showinfo("Информация", f"Файл {filename} найден.")
        with open(filename, "r") as file:
            content = file.read()
        numbers = list(map(int, content.split()))

    with open(filename, "r") as file:
        content = file.read()

    file_content_label.config(text=f"Содержимое файла:\n{content}")
    average = sum(numbers) / len(numbers)
    average_label.config(text=f"Среднее значение: {average:.2f}")


def calculate():

    try:
        expression = calc_entry.get()
        result = eval(expression)
        calc_result_label.config(text=f"Результат: {result}")
    except Exception as e:
        calc_result_label.config(text="Ошибка ввода")


def albom():
    class albom:
        def __init__(self, nameAlbom, yerAlbom, listening):
            self.nameAlbom = nameAlbom
            self.yerAlbom = yerAlbom
            self.listening = listening

        def display_info(self):
            print(f"Альбом: {self.nameAlbom} ")
            print(f"Год: {self.yerAlbom} ")
            print(f"Прослушано: {self.listening} раз")
    class song(albom):
        def __init__(self, nameAlbom, yerAlbom, listening, name):
            #унаследование
            super().__init__(nameAlbom, yerAlbom, listening)
            self.name = name
    
        def display_info(self):
            super().display_info()
            print(f"Автор: {self.name} \n")
    song1 = song("Aladdin Sane", 1973, 17453, "David Bowie")
    song2 = song("News Of The World", 1977, 19457, "Queen")

    song1.display_info()
    song2.display_info()

def newButtom():
    word = input("Напиши что-то: ")
    print(word)






root = tk.Tk()
root.title("Работа с файлами и калькулятор и лабы")




file_frame = tk.Frame(root)
file_frame.pack(pady=10)

file_label = tk.Label(file_frame, text="Имя файла:")
file_label.pack(side=tk.LEFT, padx=5)

file_entry = tk.Entry(file_frame, width=40)
file_entry.pack(side=tk.LEFT, padx=5)




choose_button = tk.Button(file_frame, text="Выбрать файл", command=choose_file)
choose_button.pack(side=tk.LEFT, padx=5)




run_button = tk.Button(root, text="Запуск", command=process_file)
run_button.pack(pady=10)



file_content_label = tk.Label(root, text="Содержимое файла:", justify=tk.LEFT)
file_content_label.pack(pady=10)



average_label = tk.Label(root, text="Среднее значение:", justify=tk.LEFT)
average_label.pack()




calc_frame = tk.Frame(root)
calc_frame.pack()

calc_label = tk.Label(calc_frame, text="Калькулятор:")
calc_label.pack()

calc_entry = tk.Entry(calc_frame, width=30)
calc_entry.pack()

calc_button = tk.Button(calc_frame, text="Вычислить", command=calculate)
calc_button.pack()

calc_result_label = tk.Label(calc_frame, text="Результат:")
calc_result_label.pack(pady=5)





albom_frame = tk.Frame(root)
albom_frame.pack()

albom_button = tk.Button(albom_frame, text="Лаба 5", command=albom)
albom_button.pack()

albom_label = tk.Label(albom_frame, text="", justify=tk.LEFT, fg="blue")
albom_label.pack()




sorted_frame = tk.Frame(root)
sorted_frame.pack()

sorted_button = tk.Button(sorted_frame, text="Лаба 3", command=sorted_numbers)
sorted_button.pack()

sorted_labels = tk.Label(sorted_frame, text="", justify=tk.LEFT, fg="blue")
sorted_labels.pack()




laba2_frame = tk.Frame(root)
laba2_frame.pack()

laba2_button = tk.Button(laba2_frame, text="Лаба 2", command=laba2)
laba2_button.pack()

laba2_labels = tk.Label(laba2_frame, text="", justify=tk.LEFT, fg="blue")
laba2_labels.pack()





laba1_frame = tk.Frame(root)
laba1_frame.pack()

laba1_button = tk.Button(laba1_frame, text="Лаба 1", command=laba1)
laba1_button.pack()

laba1_labels = tk.Label(laba1_frame, text="", justify=tk.LEFT, fg="blue")
laba1_labels.pack()


root.mainloop()