vazn = int(input())
ghad = float(input())

bmi = vazn / (ghad**2)
status = ""

if bmi < 18.5:
    status = "Underweight"
elif bmi >= 18.5 and bmi < 25:
    status = "Normal"
elif bmi >= 25 and bmi < 30:
   status = "Overweight" 
else:
    status = "Obese" 

print(f"{bmi:.2f}")
print(status)