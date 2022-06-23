#Maya Carla Loleatha Anderson
#maya.anderson86@myhunter.cuny.edu
#this program prints: a pyramid from inputted message

s = input("Enter string: ") 
ls = len(s)

for i in range(ls):
    print(s[0:i])

for i in range(ls):
    print(s[i:ls])

print("Thank you for using my program!")
