print('this program to calculate your body mass index')

weight=float(input('type your weight in kg (ex.70.5): '))
height=float(input('type your height in meters (ex.1.70): '))

bmi=weight/(height**2)
print('your bmi is: ', round(bmi,2))

if(bmi<=18.5):
    classification= "underweight"
elif(bmi>18.5 and bmi<=24.9):
    classification="normal weight"
elif(bmi>24.9 and bmi<=29.9):
    classification="overweight"
else:
    classification="obesity"

print('the classification of your bmi is: ',classification)    
    
    

    
    
    

    
