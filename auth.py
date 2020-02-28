##################################
# made by: M2F0  Date: 02/28/20  #
##################################

import requests
import os
from cloudfoundry_client.client import CloudFoundryClient
from cloudfoundry_client.operations.push.push import PushOperation
data = {'grant_type': 'client_credentials'}
r = requests.post('https://uaa.sys.na.vwapps.io/oauth/token', data=data, auth=('ci_889652cd-b65e-43b0-b04f-2503eb0a4de3', '4zOm1Bemz7zp-m2mMdXazV6YAbvP2vkc'))
at = (r.json()['access_token'])
headers = {'Authorization': 'Bearer ' + at,}
response = requests.get('https://vws-ci-credentials-broker.sys.na.vwapps.io/credentials/eb9b0f76-1c76-40a3-a8be-d817ed03ef8e', headers=headers)
cf_api_url = response.json()['cf_api_url'] #target_endpoint="https://api.[cf-api-domain].com"
target_endpoint = cf_api_url
username = response.json()['username']
password = response.json()['password'] 
proxy = dict(http=os.environ.get('HTTP_PROXY', ''), https=os.environ.get('HTTPS_PROXY', ''))
client = CloudFoundryClient(target_endpoint, proxy=proxy, verify=False) #client = CloudFoundryClient(target_endpoint, proxy=proxy, verify=False)
operation = PushOperation(client)
client.init_with_user_credentials(username, password)
#for app in client.v2.apps:
#    print(app.summary())
operation.push (space_id='4ba624a8-7ab3-4ddb-b55b-7ac19a57a9b1', manifest_path='manifest.yml', restart=True) #operation.push(client.v2.spaces.get_first(name='demopag-dev')['metadata']['guid'], path)
print('cf_api_url= ' + cf_api_url)
print('username= ' + username)
print('password= ' + password)




