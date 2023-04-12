import requests
from requests.structures import CaseInsensitiveDict
from options import user_api_key


# This APIKey will hold the user Key 
APIKey = user_api_key()


#Generate Token
# this method will create a token based on the API Key the user entered. if the API is valid (status_code is 200)
# then it will return a 'Token' to use it for every request. Otherwise, it will return 'False' which means the API Key is not valid

def generate_token():
    
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["User-Agent"] = "ServerTest"
        URLGenerateToken= "https://live.safetypooldb.ai/api/createtoken/" + APIKey
        req = requests.post(URLGenerateToken,headers=headers)

        if req.status_code == 200:
        
            TokenResult = req.json()
            Token=TokenResult['token']
            return Token
            
    
        else:
            Token = False
            return Token





   





