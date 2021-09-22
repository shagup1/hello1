class cal():
    def__init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
    def sub(self):
        returnself.a-self.b
#main program
a=double(input("enter first number:"))
b=double(input("enter second number:"))
obj=cal(a,b)
choice=input("enter an operation you want to perform:")
if choice=="+":
    print("result:",obj.add())
elif choice=="*":
    print("result:",obj.mul())
elif choice=="/":
    print("result:",obj.div())
elif choice=="-":
    print("result:",obj.sub())
else:
    print("invalid choice")

        
