#CS100 Final Project
#Nathan Brownstein (all code by him)
#December 11, 2016

#1. Open fasta file and new file to write to
#2. For each line in the fasta file:
    #2a.Differentiate between organism information lines and data lines
        #2a.a.If line has organism information in it, switch the organism name and accession number, write new line to file
        #2a.b.If the line has sequence information, write to new file as-is

from FindOrganismName import *
from changeOrganismInfo import *

def ReformatFasta(originalFile,newFile):
    OGFile=open(originalFile,'r') #downloaded fasta/txt file
    NewFile=open(newFile,'w') #File to be written to
    
    for aline in OGFile: #Read each line in the fasta file
        if '>' in aline: #'>' denotes a line with organism info/ separates sequence data
            copyline=aline
            Organism=FindOrganismName(aline) #finds and returns the name of the organism in aline
            NewInfo=copyline.split(' ') #makes info line into a list
            NewInfo=changeOrganismInfo(NewInfo,3,Organism) #Changes info so that organism name is first, converts list to string
            NewFile.write(NewInfo) #Writes re ordered info
        else:
            NewFile.write(aline) #writes sequence data (newline characters built into fasta file)
    OGFile.close() #close files
    NewFile.close()
        
    return

'''
ReformatFasta('C:\Users\Nathan\Documents\CS project\\FastaDump.txt',
                'C:\Users\Nathan\Python\\NewFile.txt')
'''