def calculate_bmi(weight, height):
    """
    Calculate BMI

    Parameters:
    weight : float (kg)
    height : float (meters)

    Returns:
    bmi : float
    category : str
    """

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "Underweight"

    elif bmi < 25:
        category = "Normal Weight"

    elif bmi < 30:
        category = "Overweight"

    else:
        category = "Obese"

    return round(bmi, 2), category


# Test
if __name__ == "__main__":
    weight = 70
    height = 1.75

    bmi, category = calculate_bmi(weight, height)

    print("BMI:", bmi)
    print("Category:", category)