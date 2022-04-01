import preprocessor

with open("..\DataSetGerman.csv", "r") as file:
    raw_file = file.read()
    # print(raw_file)
    for line in raw_file.split("\n"):
        cleaned_text = preprocessor.splitInToParts(preprocessor.cleanUp(line))
        # print(cleaned_text)
        for text in cleaned_text:
            with open("DataSetGermanClean.csv", "a") as clean_file:
                clean_file.write(text + "\n")
