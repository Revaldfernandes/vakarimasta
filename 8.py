class A:
    def __init__(self,s):


        self.s=s
    def palindrome(self):
        rev=self.s[::-1]
        if rev==self.s:
            print("The string is palindrome")
        else:
            print("Not a palindrome")

class B(A):
    '''def __init__(self,s)
            self.s=s'''
    def palindrome(self):   
        temp=self.s
        rev=0
        count=0
        while(self.s!=0):
            dig=self.s%10
            rev=rev*10+dig
            self.s=self.s//10
        if temp==rev:
            print("The Number is palindrome")
        else:
            print("Not a palindrome")
a=A(input("enter a string"))
a.palindrome()
b=B(int(input("Enter an integer")))
b.palindrome()
