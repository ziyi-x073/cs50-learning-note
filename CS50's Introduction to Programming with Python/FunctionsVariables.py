# 笔记：https://cs50.harvard.edu/python/2022/notes/0/#def

---
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
# 定义了一个不含参数的函数
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

---
# 定义了一个有一个参数的函数
# Create our own function 我也可以直接写hello(to)，就是不定义default值（即我没有给参数的时候的输出值）
def hello(to="world"):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments 这里会输出hello, world
hello()

---
#如果我用下述方式定义一个main函数，我不用在意在主逻辑之前我有没有定义我要用的函数，因为在main这里我只是定义，最后的main()才是执行，而这时候函数都已经被定义好了
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)
    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)

main()

---
# 在下面这种情况我需要return一个值
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

# 这里用return不用print是的理由
# print是显示输出，如果我这里print(n * n)，我会在叫square函数的时候输出一个数字，但没有带着数值回去，所以会有x squared is None结果
# 上述用了return，就是函数会带着一个值回去交还给调用者，main才会显示正常结果
