import os
import sys
from authentication.GenerateToken import generate_token
import requests
from requests.structures import CaseInsensitiveDict
from progressbar import *
from colorama import Fore, Back, Style
import json
script_dir = os.path.dirname( __file__ )
mymodule_dir = os.path.join( script_dir, '..')
sys.path.append( mymodule_dir )


# Get all the scenarios based on the Testsuit ID and save them in GeneratedSDL Folder


Token = generate_token()

def GetScenariosByID(TestSuitID):
    TestSuitID = str(TestSuitID)

    headers = CaseInsensitiveDict()
    headers["User-Agent"] = "ServerTest"
    headers["Authorization"] = "Bearer "+ Token
    GetSDLUrl = "https://live.safetypooldb.ai/api/testsuites/" + TestSuitID
    res = requests.get(GetSDLUrl, headers=headers)
    SDLresult = res.json()
    if(res.status_code == 200):
        # Check if Testsuite in not empty
        if(len(SDLresult['scenarios'])==0) :
            print("\n"+Fore.RED + "No scenarios have been found in the Testsuite: "+ SDLresult['name'])
            print(Style.RESET_ALL)
       
        else:
             print(Fore.GREEN+"\bRetrieving SDL scenarios in progress....\n")
             print(Style.RESET_ALL)
             ScenarioCount = 0
             for ScenarioID in SDLresult['scenarios']:
                    
                url = "https://live.safetypooldb.ai/api/scenarios/"+ ScenarioID
                resp = requests.get(url, headers=headers)
                    # print(resp.status_code)
                
                if resp.text =='"Restricted scenarios cannot be download"':
                    print("the scenario '"+ScenarioID+ "' is restricted and cannot be downloaded.\n")
                elif resp.status_code == 200:
                    ScenarioCount += 1
                    JsonResult= resp.json()
                    for i in progressbar(range(1), "Retrieving scenario " +str(ScenarioCount) +" : "+ScenarioID+" .... ", 30):
                        # get the index of where the 'scenarioDefinition' is existed
                            types = []
                            Index_SD = 0
                            for k, v in JsonResult["openlabel"]["tags"].items():
                                types.append(v["type"])
                                for i, j in enumerate(types):
                                    if j == 'scenarioDefinition':
                                        Index_SD = i
                        
                            
                            ScenarioDefintion = JsonResult['openlabel']['tags'][str(Index_SD)]["tag_data"]["text"][0]["val"]
                            ScenarioOpenLabel = JsonResult['openlabel']

                            f = open( "Generated SDL/"+ScenarioID+".sdl", "w")
                            f.write(ScenarioDefintion)
                            f = open( "Generated OpenLabel/"+ScenarioID+"openlabel"+".sdl", "w")
                            f.write(json.dumps(ScenarioOpenLabel))

                    # end of 'for loop' (generating SDL files)
                else:
                                print("please check if the scenario id is correct")

             print ("\n"+Fore.GREEN+str(ScenarioCount) + " scenarios have been successfully retrieved and saved in the folder 'Generated SDL'")
             print(Style.RESET_ALL)
    # Check if the testsuite Id is not found         
    elif (res.status_code == 404):
        print ("\n"+Fore.RED + "Error : Testsuite with ID:" + TestSuitID + " is not found. Enter a valid ID")
        print(Style.RESET_ALL)
    