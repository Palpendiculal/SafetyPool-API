import requests
from requests.structures import CaseInsensitiveDict
from authentication.GenerateToken import generate_token
import json
from progressbar import *
from colorama import Fore, Back, Style
Token = generate_token()

# Get a list of testsuites in json format and saved it Generated Json
def get_testsuites_json():

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "ServerTest"
    headers["Authorization"] = "Bearer "+ Token
    GetSDLUrl = "https://live.safetypooldb.ai/api/testsuites/" 
    res = requests.get(GetSDLUrl, headers=headers)
    JsonResult = res.json()
    TestSuitesFileName = "TestSuites"
    json_string = json.dumps(JsonResult)

    # print(json_string)
    with open("Generated Json/"+TestSuitesFileName + ".json", "w") as f:
        f.write(json_string)
        print(Fore.GREEN+"The list of testsuites in josn format has been successfully created in the 'Generated Json' folder ")
        print(Style.RESET_ALL)
