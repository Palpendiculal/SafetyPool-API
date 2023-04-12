import subprocess
# install automatically external modules: inquirer and texttable 
subprocess.check_call(['pip3', 'install', 'inquirer==2.10.0'])
subprocess.check_call(['pip3', 'install', 'texttable==1.6.4'])
subprocess.check_call(['pip3', 'install', 'colorama==0.4.5'])
subprocess.check_call(['pip3', 'install', 'requests'])

from cleanup import cleanupGeneratedSdl
from authentication.GenerateToken import generate_token
from colorama import Fore, Back, Style
from options import let_user_pick
from options import UserOption 
from TestSuitesList import get_testsuites_list
from GenerateSingleScenario import get_single_scenario
from GetOntology import get_ontology
from createFolders import create_folders
from GenerateTSjson import get_testsuites_json


# delete the content of the folders 'Generated SDL' 
# if you want to keep the SDL files, comment out the cleanupGeneratedSdl()
cleanupGeneratedSdl()


# create the folders : 'Generated SDL', 'Generated Ontology', 'Generated Json'
create_folders()

# let user select an option |  options coming from options.py


Token = generate_token()
if Token != False:

    print("\n"+Fore.GREEN+ "Your API Key is vaild and you have successfully logged into the Safety Pool API")
    print(Style.RESET_ALL)
    answer = let_user_pick()

    if answer == UserOption.listTestSuites.value:
        print(Back.MAGENTA+ "You have chosen : " + UserOption.listTestSuites.value)
        print(Style.RESET_ALL)
        get_testsuites_list()
    elif answer == UserOption.listTestSuitesJson.value:
        print(Back.MAGENTA+ "You have chosen : "+UserOption.listTestSuitesJson.value)
        print(Style.RESET_ALL)
        get_testsuites_json()
        
    elif answer == UserOption.singalScenario.value:
        print(Back.MAGENTA+ "You have chosen : "+UserOption.singalScenario.value)
        print(Style.RESET_ALL)
        get_single_scenario()

    elif answer == UserOption.getOntology.value:
        print(Back.MAGENTA+ "You have chosen : "+ UserOption.getOntology.value)
        print(Style.RESET_ALL)
        get_ontology()
else:
    print("Your API Key is not valid")

