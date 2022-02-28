from LearnMonkeyAPI import OpinionUnitExtractor,getAPiKey
import datetime


listOfText = []
with open("Sentiments_clean.tsv", 'r') as rawDataFile:
    i = 0
    for line in rawDataFile.read().split('\n')[1:202]:
        text = line.replace('\n','').replace('"','').replace('&amp;','').split('\t')[1]
        print(f"-{i:5}-",text)
        listOfText.append(text)
        i += 1


print("Comfirm")
input()
#with open("Test"+str(datetime.datetime.now().date())+".tsv",'w') as output:
#    for review in listOfText:
#        output.write("\t".join([part['extracted_text'] for part in OpinionUnitExtractor(review,getAPiKey())[0]['extractions']])+"\n")

#&quot; &amp; \n ;))) . punktMitAbstandDanach  ;)  â€¢   â€¦  &#39;  HTMLTags  â‚¬