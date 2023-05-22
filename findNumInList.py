x=list(input("Enter the list"))
y=int(input("Enter the number you want to findout in list"))

for i in x:
    if i==str(y):
        print("Yess")
        break
    else:
        continue
