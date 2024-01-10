import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def linear_model():
    """
    This function creates and trains a linear regression model using the given data.
    
    Returns:
    model (LinearRegression): The trained linear regression model.
    """
    # Load the data
    data = pd.read_csv('data.csv')

    # Split the data into training and test sets
    X = data[['bedrooms', 'neighborhood', 'floor']]
    y = data['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # Create a linear regression model
    model = LinearRegression()

    # Train the model with the training data
    model.fit(X_train.values, y_train.values)

    # Evaluate the model with the test data
    score = model.score(X_test, y_test)
    print(f'Score: {score}')
    return model

def inference(model, bedrooms, neighborhood, floor):
    """
    Perform inference using the given model and input features.

    Args:
        model: The trained model used for prediction.
        bedrooms: The number of bedrooms in the house.
        neighborhood: The neighborhood of the house.
        floor: The floor number of the house.

    Returns:
        The predicted value for the given input features.
    """
    # Make a prediction
    prediction = model.predict([[bedrooms, neighborhood, floor]])
    print(f'Prediction: {prediction}')
    return prediction

# model = linear_model()
# precio_predicho = inference(model, 2, 20, 20)