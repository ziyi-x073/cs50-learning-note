# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user f"{变量}"是在控制格式，让大括号中的内容以变量格式呈现，而不是“”这种文本的hard code
print(f"hello,{first}")

---

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result 【z = round(x / y, 2)】这句也有四舍五入到小数点后两位的意思
z = round(x + y)

# Print the formatted result 整数位隔三位一个逗号，比如1000会输出1,000
print(f"{z:,}")

---

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result 小数点后面省略两位，比如0.666666会输出0.67
print(f"{z:.2f}")

---
#定义了一个不含参数的函数
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

