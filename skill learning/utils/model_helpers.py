# skill_learning/utils/model_helpers.py

import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def save_model(model, filename):
    """
    Saves the trained model to a file using pickle.

    Args:
        model: Trained model to be saved.
        filename (str): Path where the model will be saved.
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)
    print(f"Model saved to {filename}")

def load_model(filename):
    """
    Loads a trained model from a file using pickle.

    Args:
        filename (str): Path to the model file.

    Returns:
        The loaded model.
    """
    with open(filename, 'rb') as file:
        model = pickle.load(file)
    print(f"Model loaded from {filename}")
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model using test data and returns evaluation metrics.

    Args:
        model: Trained model to be evaluated.
        X_test: Features of the test dataset.
        y_test: True labels of the test dataset.

    Returns:
        dict: A dictionary containing accuracy, precision, recall, and F1 score.
    """
    y_pred = model.predict(X_test)
    return {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred, average='weighted'),
        'recall': recall_score(y_test, y_pred, average='weighted'),
        'f1_score': f1_score(y_test, y_pred, average='weighted')
    }

def predict_with_model(model, input_data):
    """
    Makes predictions with the given model.

    Args:
        model: Trained model to use for predictions.
        input_data: Input data for prediction.

    Returns:
        The model's predictions.
    """
    predictions = model.predict(input_data)
    return predictions
