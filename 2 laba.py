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

