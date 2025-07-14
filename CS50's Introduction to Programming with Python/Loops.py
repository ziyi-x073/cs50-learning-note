# 下面这段代码如果我想喵特别特别多声我没法用下面代码实现
for i in [0, 1, 2]:
    print("meow")

# 这种情况可以用range()
for i in range(3):
    print("meow")

# 如果我不是很在意这个i，我本身不需要定义这个i，纯粹因为程序需要，这种情况就用_代替i
for _ in range(3):
    print("meow")

# 不用for的话甚至可以写成下面这样
print("meow\n" * 3, end"")

---
# 关于dict
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
for student in students:
    print(student, students[student], sep=", ")

# 结果如下
$ python hogwarts.py
Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin

# 关于多个value，那就给key起个名字，搞一个list嵌套dict
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")

# 结果如下
Hermione, Gryffindor, Otter
Harry, Gryffindor, Stag
Ron, Gryffindor, Jack Russel terrier
Draco, Slytherin, None

---
# 输出列
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()

# 结果如下
#
#
#

# 输出行
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

# 结果如下
？？？？

# 输出矩阵
def main():
    print_square(3)

def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            #  Print brick
            print("#", end="")

        # Print blank line
        print()

main()

# 结果如下
###
###
###
