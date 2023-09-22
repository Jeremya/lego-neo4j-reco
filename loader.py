from neo4j import GraphDatabase
from dotenv import dotenv_values

import csv

config = dotenv_values('.env')
uri = config['NEO4J_URI']
user = config['NEO4J_USER']
password = config['NEO4J_PASSWORD']

AUTH = (user, password)

with GraphDatabase.driver(uri, auth=AUTH) as driver:
    driver.verify_connectivity()


with open('resources/sets.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)

    for row in reader:
        # Create a dictionary for the row using headers as keys
        row_dict = dict(zip(headers, row))


