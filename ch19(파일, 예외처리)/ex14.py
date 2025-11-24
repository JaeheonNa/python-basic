import pickle

gameOption = {
    "Sound" : 8,
    "VideoQuality" : "HIGH",
    "Money" : 100000,
    "WeaponList" : ["gun", "missile", "knife"]
}

file = open("save.p", "wb")
pickle.dump(gameOption, file)
file.close()

file = open("save.p", "rb")
gameOption = pickle.load(file)
print(gameOption)
file.close()