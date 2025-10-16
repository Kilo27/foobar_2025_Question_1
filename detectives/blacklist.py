# this is the file that will detect anomalies in the data
# be functions that help detect anomalies in the data
# These will be imported into the main.py file

# Check blacklist for anomalies
# Take in the blacklist dataframe and transaction ID
# If an id in transaction ID is in blacklist ID, then we return the list of blacklisted IDs

# Import the blacklist dataframe
import pandas as pd
blacklist = pd.read_csv('user_materials/Blacklist.csv')
transactions = pd.read_csv('user_materials/Transactions.csv')

def check_blacklist():
    blacklisted_ids = []
    # list of blacklisted sender IDs
    blacklisted_sender_ids = blacklist['sender_id'].tolist()
    # Iterate through the sender ids in the transactions 
    for sender_id in transactions['sender_id']:
        if sender_id in blacklisted_sender_ids:
            blacklisted_ids.append(sender_id)
    return blacklisted_ids

