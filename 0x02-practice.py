# !pip install randomuser
from randomuser import RandomUser
import pandas as pd
import requests
import json

r = RandomUser()

some_list = r.generate_users(10)
name = r.get_full_name()

for user in some_list:
    print (user.get_full_name()," ",user.get_email())
    
for user in some_list:
    print(user.get_picture())

def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)  

get_users()

df1 = pd.DataFrame(get_users()) 

data = requests.get("https://fruityvice.com/api/fruit/all")
results = json.loads(data.text)
pd.DataFrame(results)
df2 = pd.json_normalize(results)
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

banana = df2.loc[df2['name'] == 'Banana']
banana.iloc[0]['nutritions.calories']

jokes_data = requests.get('https://official-joke-api.appspot.com/jokes/ten')
jokes_data2 = json.loads(jokes_data.text)
jokes_df = pd.json_normalize(jokes_data2)
jokes_df.drop(columns=['type','id'], inplace=True)
jokes_df
