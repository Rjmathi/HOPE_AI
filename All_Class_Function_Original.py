class subfield():
    def subfields():
        list=["Sub-field in AI are:","Machine Learning","Neutral Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for raj in list:
            print(raj)
    def oddeven():
        num1=int(input("Enter The Number:"))
        if(num1%2==0):
            print("The number is even")
            var="The number is even"
        else:
            print("The number is odd")
            var="The number is odd"
        return var
    def Elegible():
        num1=input("Your Gender:")
        num2=int(input("Your Age:"))
        if (num2=="Male") and (num2<=18):
            print("NOT ELIGIBLE")
            var="NOT ELIGIBLE"
        else:
            print("Elegible")
            var="Elegible"
        return var
    def percentage():
        subj1=int(input("subject1="))
        subj2=int(input("subject2="))
        subj3=int(input("subject3="))
        subj4=int(input("subject4="))
        subj5=int(input("subject5="))
        Total=subj1+subj2+subj3+subj4+subj5
        print("Total:",Total)
        Percentage=Total//5
        print("Percentage:",Percentage)
    def triangle():
        hei=int(input("Height:"))
        Bre=int(input("Breadth:"))
        print("Area Formula:(Height*Breadth)/2")
        Formula=(hei*Bre)/2
        print("Area of Triangle:",Formula)
        Hei1=int(input("Height1:"))
        Hei2=int(input("Height2:"))
        Bred=int(input("Breadth:"))
        print("Perimeter Formula:Height1+Height2+Breath")
        POT=Hei1+Hei2+Bred 
        print(POT)
            