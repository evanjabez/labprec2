def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    
    if bmi < 18.5:
        print("BMI =" + str(bmi) + " (Underweight)")
        
    elif bmi < 25:
        print("BMI = " + str(bmi) + " (Normal weight)")

    else:
        print("BMI = " + str(bmi) + " (Overweight)")

calculate_bmi(1.73, 57)