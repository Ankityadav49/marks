import pandas as pd

print("Enter your marks out of 100")
a=int(input("enter your math marks"))
b=int(input("enter your english marks"))
c=int(input("enter your computer marks"))
d=int(input("enter your sciense marks"))
x=int(a+b+c+d)
average=int(x/4)
mydataset = {
    'subject': [a, b, c,d,average],
    'index': ['a', 'b', 'c', 'd', 'average']
    
}

myvar = pd.DataFrame(mydataset)

print(myvar)
#print('average':average)

if(average>=40):
    print("you are pass")
else:
    print("you are fail")



