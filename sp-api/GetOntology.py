import requests
from requests.structures import CaseInsensitiveDict 
from authentication.GenerateToken import generate_token
from colorama import Fore, Back, Style
from cleanup import cleanupGeneratedOntology

Token = generate_token()

# Generate the ontology in ttl format based on the version number and save it in Generated Ontology
def get_ontology():
        
                cleanupGeneratedOntology()
                version = input(Fore.GREEN+'\nEnter the version of the ontology you want to retrieve:') 
                print(Style.RESET_ALL)

                # Retrive ontology
                headers = CaseInsensitiveDict()
                headers["User-Agent"] = "ServerTest"
                headers["Authorization"] = "Bearer "+ Token
                url = "https://live.safetypooldb.ai/api/ontologies/"+ version
                resp = requests.get(url, headers=headers)
                if resp.status_code == 200:
                  
                  ontologyResult= resp.text
                  OntologyName = "Ontology_" + version
                  f = open( "Generated Ontology/"+OntologyName + ".ttl", "w")
                  f.write(ontologyResult)
                  print("An ontology named: "+ OntologyName + ".ttl has been successfully created for you in 'Generated Ontology' folder \n")
                else:
                  print("No ontology has found for this version.")
                  

                   


               
      