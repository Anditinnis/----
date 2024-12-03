import random

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
