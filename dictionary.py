# This program is used to translate English to french and vice-versa
langauage= input("What language do you want to translated To? Enter 'English' or 'French': ")
langauage = langauage.upper()

French_to_English_dictionary= {
    "MONDE":"world",
    "BEAU":"handsome",
    "BELLE":"beautiful",
    "HOMME":"man",
    "FEMME":"woman",
    "AMOUR":"love",
}
English_to_french_dictionary={
    "DOG":"chien",
    "CAT":"chat",
    "DAY":"jour",
    "PLEASE":"s'il vous plait",
    "TIME":"temps",
    "STRONG":"fort",      
}

if langauage == "ENGLISH":
    word=input("Entrez le mot a traduire: ")
    word = word.upper()

    if  word in French_to_English_dictionary:
        word_traduit = French_to_English_dictionary[word]
        print("La traduction du mot "+word+" en Anglais est: "+word_traduit)
    else:
        print(f"{word} n'existe pas dans le dictionnaire!")
        
elif langauage == "FRENCH": 
    word=input("Enter the word to translate: ")

    if word in English_to_french_dictionary:
        print("The translation of "+ word +" in french is: "+English_to_french_dictionary[word])
    else:
        print(f"{word} is not in the Dictionary!")

else:
    print("This is not a supported language, select 'English' or 'French'")