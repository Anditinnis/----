def factorial(n):
    if n < 0:
        return
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
            return result


number = int(input())
result = factorial(number)
print(f"факториал {number} = {result}")


class classname:
    def __init__(self, name):
        self.name = name
        print("создан ", self.name)

    def __del__(self):
        print("удален", self.name)


def create_person():
    emma = classname("emma")

create_person()
