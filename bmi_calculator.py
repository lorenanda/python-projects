# Define the individuals

name1 = "Jack"
height_m1 = 1.91
weight_kg1 = 97

name2 = "Wendy"
height_m2 = 1.73
weight_kg2 = 61

name3 = "Danny"
height_m3 = 1.49
weight_kg3 = 43

# Define the function for calculating the BMI

def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print("bmi: ")
    print(bmi)
    if bmi < 25:
        return name + " is not overweight."
    else:
        return name + " is overweight."