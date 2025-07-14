# 下面这段代码如果我想喵特别特别多声我没法用下面代码实现
for i in [0, 1, 2]:
    print("meow")

# 这种情况可以用range()
for i in range(3):
    print("meow")

# 如果我不是很在意这个i，我本身不需要定义这个i，纯粹因为程序需要，这种情况就用_代替i
for _ in range(3):
    print("meow")
