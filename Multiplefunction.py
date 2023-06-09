class multiplefunction():
    def oddven():
        num1=int(input("Enter the number:"))
        if(num1%2==1):
            print("Odd Number")
            var="Odd NUmber"
        else:
            print("Even number")
            var="Even Number"
        return var
    def BMI():
        BMI=int(input("Enter the Age:"))
        if (BMI<18.5):
            print("Underweight")
            massage="Underweight"
        elif(BMI<=25):
            print("Normal")
            massage="Normal"
        elif(BMI<=30):
            print("Overweight")
            massage="Overweight"
        else:
            print("very overweight")
            massage="very overweight"
        return massage