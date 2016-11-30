def FindOrganismName(InfoString):
    StartIDX=InfoString.index('[') #Finds first bracket of organism info. Denotes start of organism name
    EndIDX=InfoString.index(']') #Finds first end bracket. Denotes end of organism name
    OrganismName=InfoString[StartIDX-1:EndIDX+1] #makes string of organism name, including the brackets
    lst=OrganismName.split()
    length=len(lst)
    if length==2: #Removes spaces between words in the organism name. Cont...
        OrganismName=(lst[0] + '_' + lst[1]) #Most programs only expect to read the accession number, and stop at the first space. Cont...
    elif length==3:
        OrganismName=(lst[0]+ '_' + lst[1] + '_' + lst[2]) #This allows the whole organism name to be read and displayed
    elif length==4:
        OrganismName=(lst[0]+ '_' + lst[1] + '_' + lst[2] + '_' + lst[3])
    elif length==5:
        OrganismName=(lst[0]+ '_' + lst[1] + '_' + lst[2] + '_' +lst[3] +'_' +lst[4])
    elif length==6: #It is unlikely the organism name will be split into more than six fragments
        OrganismName=(lst[0]+ '_' + lst[1] + '_' + lst[2] + '_' +lst[3] +'_' +lst[4] + '_' + lst[5])
    return OrganismName

'''
stri='>WP_071355719.1 xanthine dehydrogenase [Bacillus sp. MUM 116] >OIK14987.1 xanthine dehydrogenase [Bacillus sp. MUM 116]'
print FindOrganismName(stri)
'''