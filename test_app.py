import csv
import unittest
from generate_csv import generate_csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from linear_regression import linear_model
import os

class GenerateCsvTestCase(unittest.TestCase):
    def test_generate_csv(self):
        # Generate a CSV file with 10 records
        generate_csv('test.csv', 10)

        # Read the generated CSV file
        with open('test.csv', 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        # Check the number of records
        self.assertEqual(len(rows), 11)  # Including the header row

        # Check the header row
        self.assertEqual(rows[0], ['price', 'bedrooms', 'floor', 'neighborhood'])

        # Check the generated records
        for row in rows[1:]:
            price, bedrooms, floor, neighborhood = map(int, row)
            self.assertGreaterEqual(price, 20000)
            self.assertLessEqual(price, 1000000)
            self.assertGreaterEqual(bedrooms, 1)
            self.assertLessEqual(bedrooms, 5)
            self.assertGreaterEqual(floor, 1)
            self.assertLessEqual(floor, 20)
            self.assertGreaterEqual(neighborhood, 1)
            self.assertLessEqual(neighborhood, 50)

        # Remove the generated CSV file
        os.remove('test.csv')


class LinearRegressionTestCase(unittest.TestCase):
    def test_linear_model(self):
        # Generate a sample data file
        data = pd.DataFrame({
            'bedrooms': [2, 3, 4, 2, 3, 4],
            'neighborhood': [10, 20, 30, 10, 20, 30],
            'floor': [1, 2, 3, 1, 2, 3],
            'price': [200000, 300000, 400000, 250000, 350000, 450000]
        })
        data.to_csv('data.csv', index=False)

        # Call the linear_model function
        model = linear_model()

        # Check if the model is an instance of LinearRegression
        self.assertIsInstance(model, LinearRegression)

        # Remove the generated data file
        os.remove('data.csv')

if __name__ == '__main__':
    unittest.main()