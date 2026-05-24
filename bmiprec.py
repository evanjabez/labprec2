def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    
    bmi = weight / (height * height)
    
    if bmi < 18.5:
        print(f"BMI ={bmi} (Underweight)")
        
    elif bmi < 25:
        print(f"BMI = {bmi} (Normal weight)")

    else:
        print(f"BMI = {bmi} (Overweight)")

calculate_bmi(1.73, 57)