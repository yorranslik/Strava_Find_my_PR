

# This section ensures that we will only need to do the manual step once 
# with data above. With this, we will automatically call the Strava API to
# get our data! Running this piece of code, will return the variable my_dataset.
# Props to Fran. P. https://github.com/franchyze923/Code_From_Tutorials/tree/master/Strava_Api
import requests
import urllib3
import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "60035",
    'client_secret': 'cd5def1ab03ad9d3598368d000201e326e47a15c',
    'refresh_token': 'deb004d4b6076372101e0e9d910cecf790c3e16f',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
print("Access Token = {}\n".format(access_token))

header = {'Authorization': 'Bearer ' + access_token}
param = {'per_page': 200, 'page': 1}
my_dataset = requests.get(activites_url, headers=header, params=param).json()

df = pd.DataFrame(my_dataset)
df.to_csv('Strava_Activities.csv')