import os


# create the folders : 'Generated SDL', 'Generated Ontology', 'Generated Json'

def create_folders():
    SDLpath = 'Generated SDL'
    OntologyPath = 'Generated Ontology'
    JsonPath = 'Generated Json'
    # Check whether the specified path exists or not
    isSDLExist = os.path.exists(SDLpath)
    isOntologyExist = os.path.exists(OntologyPath)
    isJsonExist = os.path.exists(JsonPath)
    if not isSDLExist:
        os.makedirs(SDLpath)
        print("\nThe " + SDLpath +" folder has been created.\n")
    if not isOntologyExist:
        os.makedirs(OntologyPath)
        print("\nThe " + OntologyPath +" folder has been created.\n")
    if not isJsonExist:
        os.makedirs(JsonPath)
        print("\nThe " + JsonPath +" folder has been created.\n")

