from tokenize import Token
from GenerateScenarioFromTS import GetScenariosByID
import requests
from requests.structures import CaseInsensitiveDict
from authentication.GenerateToken import generate_token
from texttable import Texttable
from colorama import Fore, Back, Style


Token = generate_token()

def get_testsuites_list():

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "ServerTest"
    headers["Authorization"] = "Bearer "+ Token
    url = "https://live.safetypooldb.ai/api/testsuites"
    resp = requests.get(url, headers=headers)
    JsonResult= resp.json()

    # Create Table with three columns
    t = Texttable()
    t.set_cols_align(['c', 'c','c'])
    print("\nTest Suites List: \n")
    for item in JsonResult:
           
            t.add_rows([['TestSuite Id', 'TestSuite Name','Scenarios'], [item["testsuiteid"],item["name"],str(len(item["scenarios"]))+ " scenario(s)"]])
        
    print(t.draw())

    # Input TestSuitID
    valid_int = False
    while not valid_int: #loop until the user enters a valid int
        try:
            TestSuitID = int(input(Fore.BLUE+'\nInput the Test Suite ID that you want to retrieve scenario from:') ) 
            valid_int = True #if this point is reached, TestSuitID is a valid int
        except ValueError:
            print(Fore.GREEN+'\nPlease only input integer numbers')
    print(Style.RESET_ALL)


    GetScenariosByID(TestSuitID)