#An example programm to show the MonkeyLearn API
from monkeylearn import MonkeyLearn

import requests
import json


#API from: https://app.monkeylearn.com/studio/models/explore/


def getColor(i):
    listOfColors = ['\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m',
                    '\033[35m', '\033[36m', '\033[90m']
    return listOfColors[i%len(listOfColors)]



def getAPiKey():
    with open("ApiKey.txt", 'r') as apiKeyFile:
        return apiKeyFile.read()


def OpinionUnitExtractor(str, apiKey):
    ml = MonkeyLearn(apiKey)
    data = [str]
    model_id = 'ex_N4aFcea3'
    result = ml.extractors.extract(model_id, data)
    return result.body


def SentimentAnalysis(str, apiKey):
    ml = MonkeyLearn(apiKey)
    data = [str]
    model_id = 'cl_rZ2P7hbs'
    result = ml.classifiers.classify(model_id, data)
    return result.body

def SubjectExtractor(str,apiKey):
    url = "https://api.monkeylearn.com/v3/classifiers/cl_TKb7XmdG/classify/"

    payload = json.dumps({
        "data": [str]
    })
    headers = {
        'Authorization': 'Token '+apiKey,
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)




if __name__ == '__main__':
    apiKey = getAPiKey()
    Text = " The hotel has a great location but all in all it was a horrible experience! Only stayed here because it was the pre-accommodation choice for one of our tours but it was terrible. Will never stay here again! I have to say that this hotel has the worst customer service ever. It is a shame that people in management positions (who should be more respectful of their customers) are rude and have bad attitudes. They completely ruined my Valentine's Day."

    print(Text)
    splitedText = OpinionUnitExtractor(Text, apiKey)[0]['extractions']
    for part, i in zip(splitedText, range(len(splitedText))):
        print(getColor(i),part['extracted_text'], end="")

    print(getColor(0),"\n")

    for part, i in zip(splitedText, range(len(splitedText))):
        textSentiment = SentimentAnalysis(part['extracted_text'], apiKey)[0]['classifications']
        textKeyWord = SubjectExtractor(part['extracted_text'], apiKey)[0]['classifications']
        print(getColor(i),f"{part['extracted_text']:100}", " -- Sentiment -->", textSentiment[0]['tag_name'],":",textSentiment[0]['confidence']*100,"%")
        try:
            print(getColor(i), f"{'':100}", " -- Topic -->",textKeyWord[0]['tag_name'], ":", textKeyWord[0]['confidence']*100,"%")
        except:
            print(getColor(i), f"{'':100}", " -- Topic -->","Not Classified")

        print()