import inquirer
import enum

# Define an enum for the list of the options that user need to choose from
class UserOption(enum.Enum):
   listTestSuites = "List all test suites"
   listTestSuitesJson = "List all test suites in json"
   singalScenario = "Retrieve single scenario"
   getOntology = "Retrieve ontologies"
   

# This is the first question when the user need to enter the API Key 
def user_api_key():
    question_3 = [
          inquirer.Text('APIKey', message="Paste your API Key here"),
    
    ]
    answer = inquirer.prompt(question_3)
    return answer['APIKey']


# if the API Key is valid, the user will pick up one of the options that listed in choices
def let_user_pick():
    question_1 = [
    inquirer.List('options',
                    message="What do you need to do?",
                    choices=[UserOption.listTestSuites.value,UserOption.listTestSuitesJson.value,UserOption.singalScenario.value, UserOption.getOntology.value],
                ),
    ]
    answer = inquirer.prompt(question_1)

    return answer['options']