import csv
import random

def generate_csv(filename, num_records):
    """
    Generate a CSV file with random records.

    Args:
        filename (str): The name of the CSV file to be generated.
        num_records (int): The number of records to generate.

    Returns:
        None
    """
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['price', 'bedrooms', 'floor', 'neighborhood'])
        for _ in range(num_records):
            bedrooms = random.randint(1, 5)
            floor = random.randint(1, 20)
            neighborhood = random.randint(1, 50)
            price = bedrooms * 10000 + floor * 5000 + neighborhood * 10000
            price = max(20000, min(price, 1000000))
            writer.writerow([price, bedrooms, floor, neighborhood])

#generate_csv('data.csv', 10000)
