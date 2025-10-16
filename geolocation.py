import pandas as pd

users = pd.read_csv('user_materials/Users.csv')
hosts = pd.read_csv('user_materials/Hosts.csv')

for i in users['USER_ID']:
    for j in users['COUNTRY']:
        
