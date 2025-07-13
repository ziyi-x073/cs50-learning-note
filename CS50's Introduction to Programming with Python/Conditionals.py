# 关于下面这个程序 重点看is_even(n)这个自创函数部分
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()

# 在python中可以改成下面这个句子，看起来很像正常说话
def is_even(n):
    return True if n % 2 == 0 else False

# 甚至我这个n % 2 == 0本身都返回一个bool值了我何必再if呢，直接返回n % 2 == 0结果不就好了
def is_even(n):
    return n % 2 == 0

---
#两种方式表达在什么条件下返回什么值
name = input("What's your name? ")

  if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")

# 用match的话
name = input("What's your name? ")

  match name: 
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")

