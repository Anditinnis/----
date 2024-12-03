from random import randint
from tkinter import filedialog


def create_file(count):
    i = 0
    filename = [
        "file1.txt",
        "file2.txt",
        "file3.txt",
    ]
    while i < count:
        list = []
        file = open(filename[i], "w")
        for c in range(10):
            num = randint(1, 100)
            list.append(num)
        for k in range(len(list)):
            file.write(str(list[k]) + "\n")
        file.close()
        i += 1


create_file(3)

filepath = filedialog.askopenfilename()
if filepath != "":
    file_read = open(filepath, "r")
    data = file_read.read()
    print("\n", data)
    data_list = data.split("\n")
    data_sum = 0
    for g in range(len(data_list) - 1):
        data_sum = data_sum + int(data_list[g])
    data_sr = data_sum / (len(data_list) - 1)
    print(data_sr)
    file_read.close()
