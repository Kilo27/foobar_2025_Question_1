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
#users = pd.read_csv('user_materials/Users.csv')

def check_blacklist():
    flagged_ids = []
    #blacklisted_user_ids = []

    # list of blacklisted sender IDs
    blacklisted_sender_ids = blacklist['ENTITY_ID'].tolist()
    # Iterate through the sender ids in the transactions 
    for sender_id in transactions['SENDER_ID']:
        # Check if the sender ID is in the blacklist
        if sender_id in blacklisted_sender_ids:
            # Check for duplicates
            if sender_id not in flagged_ids:
                flagged_ids.append(sender_id) 

    '''
    # Iterate through users dataframe and check if the user ID is in the blacklist
    for user_id in users['USER_ID']:
        if user_id in blacklisted_sender_ids:
            # Check for duplicates
            if user_id not in blacklisted_user_ids:
                blacklisted_user_ids.append(user_id) 
    '''

    return flagged_ids #blacklisted_user_ids
