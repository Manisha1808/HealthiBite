from flask import Flask, render_template, request
import pickle
from nutrition import get_diet_suggestions  # Import the function to interact with Nutritionix

app = Flask(__name__)

# Load model and vectorizer
with open('model/intent_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Recommendation rules (sample)
recommendations = {
    "fatigue": {
        "diet": "Eat iron-rich foods like spinach and lentils.",
        "exercise": "Try light yoga or walking.",
        "sleep": "Sleep 8+ hours regularly.",
        "tip": "Stay hydrated. Check for anemia if fatigue persists."
    },
    "digestion": {
        "diet": "Avoid spicy foods. Include yogurt and fruits.",
        "exercise": "Walk after meals.",
        "sleep": "Avoid heavy meals before bed.",
        "tip": "Chew food slowly. Stay stress-free."
    },
    "headache": {
        "diet": "Stay hydrated. Avoid caffeine.",
        "exercise": "Neck stretches can help.",
        "sleep": "Maintain a consistent sleep schedule.",
        "tip": "Monitor triggers like light or noise."
    },
    "insomnia": {
        "diet": "No coffee after 4 PM. Light dinner.",
        "exercise": "Light daily exercise (not before bed).",
        "sleep": "Follow a bedtime routine.",
        "tip": "Avoid screens before sleeping."
    },
    "weight_loss": {
        "diet": "High-protein, low-carb meals.",
        "exercise": "Cardio + strength training.",
        "sleep": "Sleep well to support metabolism.",
        "tip": "Track meals & stay consistent."
    }
}

# Exercise plans based on health concern and fitness level
def get_exercise_plan(health_concern, level):
    plans = {
        'fatigue': {
            'Beginner': [
                'Walking (10-15 minutes a few times a week)',
                'Gentle stretching (especially for the back and legs)',
                'Yoga (Child\'s Pose, Cat-Cow)'
            ],
            'Intermediate': [
                'Walking (20-30 minutes daily)',
                'Bodyweight Exercises (squats, lunges, wall push-ups)',
                'Yoga (Active poses like Downward Dog, Warrior)'
            ],
            'Advanced': [
                'Yoga (Deeper stretches like Cobra, Bridge Pose)',
                'Resistance Band Training (squats, seated rows)',
                'Cardio (Light cycling or swimming for 30 minutes)'
            ]
        },
        'digestion': {
            'Beginner': [
                'Walking (10-15 minute walk after meals)',
                'Gentle Yoga (Seated Twist, Cat-Cow)',
                'Deep Breathing (abdominal breathing techniques)'
            ],
            'Intermediate': [
                'Walking (20-30 minute post-meal walks)',
                'Yoga (Forward Fold, Child\'s Pose)',
                'Deep Breathing (to reduce stress)'
            ],
            'Advanced': [
                'Yoga (Cobra, Bridge Pose)',
                'Tai Chi (Slow movements)',
                'Post-meal walking (30 minutes)'
            ]
        },
        'headaches': {
            'Beginner': [
                'Neck Stretches (Rotate head side to side, forward, and backward)',
                'Shoulder Shrugs (Lift shoulders to ears and release slowly)'
            ],
            'Intermediate': [
                'Gentle Yoga (Shoulder openers like Eagle Pose, Cow Face Pose)',
                'Tai Chi (Neck and shoulder movements)'
            ],
            'Advanced': [
                'Strengthening exercises for the upper back and shoulders',
                'Migraine-specific stretches (Scorpion stretch, thread-the-needle pose)'
            ]
        },
        'insomnia': {
            'Beginner': [
                'Light Walking (10-15 minute walks, especially during the day)',
                'Relaxation Techniques (Stretching, deep breathing before bed)'
            ],
            'Intermediate': [
                'Gentle Yoga (Forward Fold, Legs Up the Wall)',
                'Mindfulness Meditation (guided breathing before sleep)'
            ],
            'Advanced': [
                'Relaxation Yoga (Yin Yoga, Gentle Flow)',
                'Tai Chi or Qi Gong (Slow movements to calm the mind)'
            ]
        },
        'weight_loss': {
            'Beginner': [
                'Walking or Cycling (20–30 minutes, 3–4 times a week)',
                'Bodyweight Strength Training (squats, lunges, push-ups, 1-2 sets of 10–12 reps)'
            ],
            'Intermediate': [
                'Cardio (Increase to 45 minutes, 4–5 times a week, add HIIT intervals)',
                'Strength Training (Squats, lunges, planks, resistance band exercises)'
            ],
            'Advanced': [
                'HIIT (High-Intensity Interval Training, 20 minutes, 3 times a week)',
                'Full-Body Strength Training (Deadlifts, squats, overhead presses)',
                'Cardio Endurance (Running or cycling for 60 minutes, 4–5 times a week)'
            ]
        }
    }

    # Return the exercise plan based on health concern and level
    if health_concern in plans:
        return plans[health_concern].get(level, "Invalid fitness level. Please choose from: Beginner, Intermediate, Advanced.")
    else:
        return "Invalid health concern. Please choose from: fatigue, digestion, headaches, insomnia, weight_loss."

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    prompt = request.form['prompt']
    level = request.form.get('level', 'Beginner').capitalize()  # Default to 'Beginner' if not provided
    prompt_vec = vectorizer.transform([prompt])
    prediction = model.predict(prompt_vec)[0]

    rec = recommendations.get(prediction, {
        "diet": "Eat balanced meals.",
        "exercise": "Stay active daily.",
        "sleep": "Sleep 7-8 hours.",
        "tip": ""
    })

    # Fetch diet-related info from Nutritionix API
    food_query = request.form.get('food_query', '1 banana and 2 scrambled eggs')  # Example food query
    nutrition_data = get_diet_suggestions(food_query)

    # Customize diet based on health concern
    detailed_diet = rec["diet"]

    if nutrition_data and 'foods' in nutrition_data and len(nutrition_data['foods']) > 0:
        detailed_diet += f"<br><strong>Detailed Suggestions:</strong><br>"
        for idx, food in enumerate(nutrition_data['foods']):
            food_name = food['food_name']
            calories = food['nf_calories']
            proteins = food['nf_protein']
            carbs = food['nf_total_carbohydrate']
            fats = food['nf_total_fat']

            # Improved formatting for user-friendly output
            detailed_diet += f"For Meal {idx+1}, try {food_name}: {calories} kcal, {proteins}g protein, {carbs}g carbs, {fats}g fats.<br>"

        # Add some general meal suggestions
        detailed_diet += "<br> Additional Meal Suggestions: <br> Breakfast: Add fruits and oats. <br> Lunch: Include lean proteins like chicken. <br> Dinner: Include vegetables and complex carbs."
    else:
        detailed_diet += "<br><strong>Detailed Suggestions:</strong><br> Breakfast: Add fruits and oats. <br> Lunch: Include lean proteins like chicken. <br> Dinner: Include vegetables and complex carbs."

    # Get exercise suggestions
    exercise_plan = get_exercise_plan(prediction, level)

    return render_template("result.html", prompt=prompt, diet=detailed_diet,
                           exercise=exercise_plan, sleep=rec["sleep"],
                           tip=rec["tip"], nutrition_data=nutrition_data)

if __name__ == '__main__':
    app.run(debug=True)
