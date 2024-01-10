## House price predictions

This is a Python project that generates a CSV file with random records and applies a linear regression model to the data, presenting a streamlit interface to allow users

## File Structure
- ``generate_csv.py``: This Python script contains a function to generate a CSV file with random records. It's used to create a dataset for this project.

- ``linear_regression.py``: This Python script contains the implementation of a linear regression model. It's used to train a model on the generated dataset.

- ``main.py``: This is the entry point of the project. It uses the functions defined in generate_csv.py and linear_regression.py.

- ``requirements.txt``: This file lists the Python packages that the project depends on. You can install all required packages using `pip install -r requirements.txt`.

- ``test_app.py``: This is a test file, containing unit tests for the functions in generate_csv.py and linear_regression.py.

## How to Run the Project

1. First, make sure you have Python installed on your machine.
2. Clone this repository to your local machine and navigate to the project directory.
3. Set up a virtual environment and activate it:
    - Install the required packages: `pip install -r requirements.txt`
    - Run the main script: `streamlit run main.py`

## Running Tests

To run the tests, use the following command: `python -m unittest test_app.py`

## Contributing

If you want to contribute to this project, please fork the repository, make your changes, and open a pull request. All contributions are welcome.