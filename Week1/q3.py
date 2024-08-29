lst = []

for i in range(1,6):
    inp1 = int(input("Enter a number: "))
    lst.append(inp1)

print("Numbers divisible by 5 are: ", end = "")
for num in lst:
    if num % 5 == 0:
        print(num, end=" ")
