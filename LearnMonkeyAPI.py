

def getAPiKey():
    with open("ApiKey.txt", 'r') as apiKeyFile:
        return apiKeyFile.read()

apiKey = getAPiKey()
print(apiKey)