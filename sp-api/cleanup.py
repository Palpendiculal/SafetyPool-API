import glob
import os

# delete the content of the folders 'Generated SDL' and Generated Ontology for everyrequest
def cleanupGeneratedSdl():
    SDLpath = os.path.join('Generated SDL/*')
    tempPath = glob.glob(SDLpath)
    for t in tempPath:
        os.remove(t)
def cleanupGeneratedOntology():
    SDLpath = os.path.join('Generated Ontology/*')
    tempPath = glob.glob(SDLpath)
    for t in tempPath:
        os.remove(t)
