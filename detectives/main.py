# This is where the main logic will goes

import pandas as pd
#import numpy as np

from blacklist import check_blacklist

# Load all CSV files
transactions = pd.read_csv('detectives/Transactions.csv')
users = pd.read_csv('detectives/Users.csv')
hosts = pd.read_csv('detectives/Hosts.csv')
blacklist = pd.read_csv('detectives/Blacklist.csv')
notes = pd.read_csv('detectives/Notes.csv')
devices = pd.read_csv('detectives/Devices.csv')
def get_df():
    return 
# Display as dataframes/tables
print("Transactions:")
# print(transactions.head())


## Get blacklisted IDs
blacklisted_ids = check_blacklist()
print(blacklisted_ids)