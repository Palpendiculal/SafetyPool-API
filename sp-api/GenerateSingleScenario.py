import requests
from requests.structures import CaseInsensitiveDict 
from authentication.GenerateToken import generate_token
from colorama import Fore, Back, Style
from progressbar import *

Token = generate_token()

# get single scenario based on the the scenario ID the user enters.

def get_single_scenario():
        valid_int = False
        while not valid_int: #loop until the user enters a valid int
                
                ScenarioID = input(Fore.BLUE+'\nEnter the scenario Id: ') 
                valid_int = True #if this point is reached, TestSuitID is a valid int
                print(Style.RESET_ALL)


                # Retrive Single Scenario
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "ServerTest"
                headers["Authorization"] = "Bearer "+ Token
                url = "https://live.safetypooldb.ai/api/scenarios/"+ ScenarioID
                resp = requests.get(url, headers=headers)    
                JsonResult= resp.json()

                # -------- Generate SDL File for single scenario  ---------


                # get the index of where the 'scenarioDefinition' is existed

                if resp.status_code == 200:
                        for i in progressbar(range(1), "Retrieving scenario '"+ScenarioID+"' in progress .... ", 30):
                                types = []
                                Index_SD = 0
                                for k, v in JsonResult["openlabel"]["tags"].items():
                                        types.append(v["type"])
                                        for i, j in enumerate(types):
                                                if j == 'scenarioDefinition':
                                                        Index_SD = i
                                        
                                
                                
                                ScenarioDefintion = JsonResult['openlabel']['tags'][str(Index_SD)]["tag_data"]["text"][0]["val"]

                                
                                f = open( "Generated SDL/"+ScenarioID + ".sdl", "w")
                                f.write(ScenarioDefintion)
                        print(Fore.GREEN+"The scenario '"+ScenarioID+"' has been successfully downloaded in the 'Generated SDL' folder ")
                elif resp.text =='"Restricted scenarios cannot be download"':
                        print("This scenario is restricted and cannot be download")
                else:
                        print("please check if the scenario id is correct")
                

                # ------ End of Generaation -------
      