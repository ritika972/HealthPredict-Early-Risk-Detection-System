# src/recommendation.py

def get_recommendations(diabetes_risk, hypertension_risk):

    recommendations = []

    # Diabetes Recommendations
    if diabetes_risk == "High Risk":

        recommendations.extend([
            "Reduce sugar intake",
            "Avoid soft drinks and sweets",
            "Exercise at least 30 minutes daily",
            "Monitor blood glucose regularly",
            "Maintain a healthy weight"
        ])

    elif diabetes_risk == "Medium Risk":

        recommendations.extend([
            "Limit sugar consumption",
            "Increase physical activity",
            "Eat more fruits and vegetables"
        ])

    elif diabetes_risk == "Low Risk":

        recommendations.extend([
            "Maintain balanced diet",
            "Continue regular exercise",
            "Drink adequate water",
            "Monitor health periodically"
        ])

    # Hypertension Recommendations
    if hypertension_risk == "High Risk":

        recommendations.extend([
            "Reduce salt intake",
            "Avoid smoking and alcohol",
            "Monitor blood pressure regularly",
            "Practice stress management",
            "Follow a heart-healthy diet"
        ])

    elif hypertension_risk == "Medium Risk":

        recommendations.extend([
            "Reduce processed foods",
            "Exercise regularly",
            "Get adequate sleep"
        ])

    elif hypertension_risk == "Low Risk":

        recommendations.extend([
            "Maintain healthy body weight",
            "Continue physical activity",
            "Eat fresh fruits and vegetables",
            "Maintain healthy blood pressure habits"
        ])

    return recommendations