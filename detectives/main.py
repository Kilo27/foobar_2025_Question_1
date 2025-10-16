# This is where the main logic will goes

import pandas as pd
import numpy as np

# Load all CSV files
transactions = pd.read_csv('user_materials/Transactions.csv')
users = pd.read_csv('user_materials/Users.csv')
hosts = pd.read_csv('user_materials/Hosts.csv')
blacklist = pd.read_csv('user_materials/Blacklist.csv')
notes = pd.read_csv('user_materials/Notes.csv')
devices = pd.read_csv('user_materials/Devices.csv')

# Display as dataframes/tables
print("Transactions:")
print(transactions.head())