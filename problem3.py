#! python3
"""
Ask the user to enter a maximum of 10 positive integers.
After each entry, add the number to a list
If the entry is -1 then stop adding numbers to the list
Sort the list and display the highest number added

inputs:
as many integers as needed

outputs:
Display the largest number:

examples:
Enter an integer:3
Enter an integer:2
Enter an integer:8
Enter an integer:92
Enter an integer:48
Enter an integer:13
Enter an integer:24
Enter an integer:-1

The largest number you entered is 92
"""
"""
s1 = int(input("Enter an integer: "))
s2 = int(input("Enter an integer: "))
s3 = int(input("Enter an integer: "))
s4 = int(input("Enter an integer: "))
s5 = int(input("Enter an integer: "))
s6 = int(input("Enter an integer: "))
s7 = int(input("Enter an integer: "))
s8 = int(input("Enter an integer: "))
s9 = int(input("Enter an integer: "))
s10 = int(input("Enter an integer: "))

sList = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
sList.sort(reverse=True)
print(f"The largest number is {sList[0]}")
"""
nlist = []
for i in range(10):
    num = int(input("Enter an integer: "))
    if num == -1:
        nlist.sort(reverse=True)
        print(f"The largest number is {nlist[0]}")
    else:
        nlist.append(num)

