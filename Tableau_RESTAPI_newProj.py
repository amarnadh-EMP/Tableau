import requests
import xmltodict
import json 

url = "https://10ax.online.tableau.com/api/3.4/auth/signin"

payload="<tsRequest>\r\n  <credentials name=\"gunakala.amarnadh@outlook.com\" password=\"XXXX\" >\r\n    <site contentUrl=\"amargdev480119\" />\r\n  </credentials>\r\n</tsRequest>"
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'AWSELB=3DAB357D1283FCCC77AA83D08989B29DE92E63276AE77AD4EE133E11E6F8E8568C0C008FC5E6AFD06266F24DE724486F3BC5D03FD4D166A90BCE4BD2F4228DAE20FB62D30DF64809065F8EB34318B654D2E3D02F6F; hid=10axpd-hap02'
}

response = requests.request("POST", url, headers=headers, data=payload)

data_dict = xmltodict.parse(response.text)
json_data = json.dumps(data_dict) 
json_data=json.loads(json_data)
Token=(json_data['tsResponse']['credentials']['@token'])   


#Post Method to create a new project name called 'AmarProg' for example and its descrition  

payload="<tsRequest>\r\n  <project name=\"AmarProg\" description=\"This is my Test Proj\" />\r\n</tsRequest>"
headers = {
  'X-Tableau-Auth': Token,
  'Content-Type': 'text/plain',
  'Cookie': 'AWSELB=3DAB357D1283FCCC77AA83D08989B29DE92E63276AE77AD4EE133E11E6F8E8568C0C008FC5E6AFD06266F24DE724486F3BC5D03FD4D166A90BCE4BD2F4228DAE20FB62D30DF64809065F8EB34318B654D2E3D02F6F; hid=10axpd-hap02'
}

response = requests.request("POST", url, headers=headers, data=payload)

#Printing response output  in case its successfullly new project created.
print(response.text)
