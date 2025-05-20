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
