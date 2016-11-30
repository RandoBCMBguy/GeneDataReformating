def changeOrganismInfo(lst,todel,toadd): #lst is Organism info, todel should be the position (always 3) of the first half of the organism name, to add is the organism name
    del lst[todel] #deletes first half of organism name, second half shifts to first position
    del lst[todel] #deletes second half of organism name. Note: This code is based on fasta files' predictability. 
    accNum=str(lst[0])#makes string of accession number
    accNum=accNum[1:]#changes accesion number string to exclude the starting '>' character ('>' character denotes new sequence)
    lst[0]=accNum #Replaces old accestion number value with new value lacking the '>' character
    lst.insert(0,'>'+toadd) #adds organism name at start of list plus a '>'
    string='' #initializes string of new list
    for i in range(len(lst)):
        string=string+' '+lst[i]#adds list values sequentially as a string
    if string[len(string)-2]!=']':
        string=string +'\n' #adds newline character in case line does not end with one already(newline character does not appear if final character is a bracket for some reason
    string=string[1:] #Returns same string but without starting space that was breaking alignment programs
    return string

'''
lst=['>WP_041306158.1', 'xanthine', 'dehydrogenase', '[Kyrpidia', 'tusciae]\n']
print changeOrganismInfo(lst,3,'pumpkin')
'''