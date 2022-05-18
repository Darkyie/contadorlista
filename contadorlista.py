
a = []
for x in range (0,10):
    num = int(input())
    a.append(num)
x = input()

if x in a:
    print("NÚMERO EXISTE")
else:
    print("NÚMERO NÃO EXISTE")