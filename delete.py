# This program is used to translate English to french and vice-versa
langauage= input("What language do you want to translated To? Enter 'English' or 'French' or 'Bulgarian' : ")
langauage = langauage.upper()

French_to_English_dictionary= {
    "MONDE":"world",
    "BEAU":"handsome",
    "BELLE":"beautiful",
    "HOMME":"man",
    "FEMME":"woman",
    "AMOUR":"love",
    "PRUNE":"plum",
}
English_to_french_dictionary={
    "DOG":"chien",
    "CAT":"chat",
    "DAY":"jour",
    "PLEASE":"s'il vous plait",
    "TIME":"temps",
    "STRONG":"fort",
    "PLUM":"prune",      
}

English_to_bulgarian_dictionary={
    "NAME":"име",
    "CAR":"кола",
    "DAY":"ден",
    "PLEASE":"Моля те",
    "TIME":"време",
    "PLUM":"слива",      
}

if langauage == "ENGLISH":
    mot=input("Enter the word in FRENCH to translate to ENGLISH: ")
    mot = mot.upper()

    if  mot in French_to_English_dictionary:
        mot_traduit = French_to_English_dictionary[mot]
        print("The translation of "+ mot +" in English is: "+ mot_traduit.upper())
    else:
        print(f"{mot} is not in the Dictionary! Please try again")

elif langauage == "BULGARIAN": 
    word=input("Enter the word in ENGLISH to translate to BULGARIAN: ")
    word = word.upper()

    if word in English_to_bulgarian_dictionary:
        word_translate = English_to_bulgarian_dictionary[word]
        print("The translation of "+ word +" in bulgarian is: "+ word_translate.upper())
    else:
        print(f"{word} is not in the Dictionary! Please try again")
        
elif langauage == "FRENCH": 
    word=input("Enter the word in ENGLISH to translate to FRENCH: ")
    word = word.upper()

    if word in English_to_french_dictionary:
        word_translate = English_to_french_dictionary[word]
        print("The translation of "+ word +" in french is: "+ word_translate.upper())
    else:
        print(f"{word} is not in the Dictionary! Please try again")

else:
    print("This is not a supported language, select 'English' or 'French' or 'Bulgarian' ")