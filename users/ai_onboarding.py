def evaluate_user_level(responses):
    if responses['question_2'] > 7:
        return "Advanced"
    elif responses['question_2'] > 4:
        return "Intermediate"
    return "Beginner"
