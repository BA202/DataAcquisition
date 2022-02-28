import os
import datetime

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


def getScore(currentScores):
    res = input()
    while True:
        try:
            number = int(res)
        except:
            number = None

        if number == None or number < -1 or number > 1:
            if number == None:
                print("     !\u001b[31mUnable to parse input\u001b[0m")
            else:
                print("     !\u001b[31mInt not in list\u001b[0m")
            res = input()
        else:

            return currentScores[number]

def getTags(text ,currentTags):
    listOfInputTags = []

    while True:
        inputStr = input()
        if inputStr == "":
            print("All Tags added? [y,n]?")
            print(listOfInputTags)
            inputStr = input()
            if inputStr == "y":
                return listOfInputTags
            else:
                print("Add next Tag.")
        else:
            try:
                tag = int(inputStr)

            except:
                tag = None

            if tag != None and tag in currentTags.keys():
                if currentTags[tag] in listOfInputTags:
                    print("    !\u001b[31mTag already added\u001b[0m")
                else:
                    listOfInputTags.append(currentTags[tag])
                print("[" ,end="")
                for tag in listOfInputTags:
                    print(f"\u001b[35m{tag}\u001b[0m, " ,end="")
                print("]")
                print(f"\u001b[1m{text}\u001b[0m")

            else:
                if tag == None:
                    print("     !\u001b[31mUnable to parse input\u001b[0m")
                else:
                    print("     !\u001b[31mInt not in list\u001b[0m")

def getContentType(currentContentType):
    res = input()
    while True:
        try:
            number = int(res)
        except:
            number = None

        if number == None or number not in currentContentType.keys():
            if number == None:
                print("     !\u001b[31mUnable to parse input\u001b[0m")
            else:
                print("     !\u001b[31mInt not in list\u001b[0m")
            res = input()
        else:

            return currentContentType[number]


currentScores ={
    -1: "Negative",
    0: "Neutral",
    1: "Positiv"
}

currentTags = {
    11: "PublicTransport",
    12: "Sightseeing",
    21: "Bead",
    22: "Bathroom",
    23: "Noiselevel",
    24: "Size",
    31: "Breakfast",
    32: "Snacks",
    41: "Helpfulness",
    42: "StaffAttitude",
    43: "Organisation",
    44: "Professional",
    51: "Value",
    52: "Location",
    61: "WiFi",
    62: "Parking",
    63: "Pool/Spa",
    64: "PowerOutlet",
    71: "Reception",
    72: "NightEntrance",
    73: "CheckOutTime",
    74: "HowTheHotelWasFound",
    75: "Major Issue",
    80: "Unknown"
}

currentContentType = {
    1: "Review",
    2: "TravelsAdvice",
    3: "Story"
}

path = "ClassifiedFiles_" +str(datetime.datetime.now())
os.mkdir(path)

with open("ListOfTexts_AutoSplit_Clean.tsv", 'r') as ListOfTexts:
    rawFile = ListOfTexts.read()
    currentReview = 1
    currentSentence = 1
    for line in rawFile.split('\n')[0:100]:
        with open(path+ "/RawReviews.tsv", 'a')as RawReviews:
            RawReviews.write(line.replace('\t','')+"\tTraining\tOnline\tEnglish"+"\n")
        for text in line.split('\t'):
            with open(path + "/ReviewSentences.tsv", 'a')as ReviewSentences:
                ReviewSentences.write(text + f"\t{currentReview}" + "\n")
            print(f"{currentReview:3}.{currentSentence:<4}\u001b[1m{text}\u001b[0m")
            print("\u001b[31;1mScore:\u001b[0m {", end="")
            for key in currentScores:
                print(f"\u001b[34;1m {key}\u001b[0m:{currentScores[key]},",
                      end="")
            print("}")
            score = getScore(currentScores)

            print("\u001b[31;1mTags:\u001b[0m {", end="")
            for key in currentTags:
                if ((key - 1) % 10) == 0 or key % 10 == 0:
                    print()
                print(f"\u001b[34;1m {key:3}\u001b[0m:{currentTags[key]:20},",
                      end="")
            print("}")
            tags = getTags(text, currentTags)

            print("\u001b[31;1mContentType:\u001b[0m {", end="")
            for key in currentContentType:
                if ((key - 1) % 10) == 0 or key % 10 == 0:
                    print()
                print(f"\u001b[34;1m {key:3}\u001b[0m:{currentContentType[key]:20},",
                      end="")
            print("}")
            contentType = getContentType(currentContentType)

            print("Text Classification: ",score,tags,contentType,sep=" | ")
            with open(path + "/ClassificationResult.tsv", 'a')as ClassificationResult:
                for tag in tags:
                    ClassificationResult.write(f"{score}\t1\t{tag}\t1\t{contentType}\t1\t{currentSentence}" + "\n")
            clearConsole()
            currentSentence += 1
        currentReview += 1