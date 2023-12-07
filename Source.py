#Random Story Generator Project

import random
from gtts import gTTS
import os
import platform 
plt = platform.system()

#storage
story=[]

#This section houses the strings of text that will present the users with a list of choices during the initialization and story generation phases
genreList = ('a. Adventure\nb. Prince/Princess\nc. Western\nd. Surprise me')
endingList = ('a. Happy\nb. Sad\nc. Surprise me')
nameGenerationChoiceList = ('a. Generate automatically\nb. Let me choose myself')
yesNoChoiceList = ('a. Yes\nb. Not now')
genderList = ('a. Male\nb. Female')
genderListGeneration = ['male','female']
maleProtagonistNameList = ['Jack','Edward','Elijah','Owen','Liam']
femaleProtagonistNameList = ['Olivia', 'Isabelle', 'Elise', 'June', 'Ava']
maleAntagonistNameList = ['Remus','Severus','Lupin','Alfor','Vilgax']
femaleAntagonistNameList = ['Maleficent','Anastasia','Haline','Jasella','Corvina']
adventureLocationName = ['Capetown','Provincetown','Cannon Beach']
fantasyLocationName = ['Verona','Isla','Shirebrooke']
westernLocationName = ['Boise','San Luis','La Tierra']
spellVariables = ['Turroca Root', 'Foot of Toad', 'Ghast Tears']

#Imports story.txt into a flattened list
def flatten(aList):
        a = []
        for element in aList:
            if type(element) is list:
                for item in element:
                    a.append(item)
            else:
                a.append(element)
        return a
def importIntoList():
    stories = open('Stories.txt','r').read().split('\n')
    return(flatten(stories))
txtAsList = importIntoList()

def unFlatten(aList):
        a = []
        b = []
        for element in aList:
            if type(element) is str:
                a.append(element.split())
            else:
                a.append(element)
        for element in a:
            if type(element) is list:
                for item in element:
                    b.append(item)
            else:
                b.append(element)
        return (b)

#The following function takes a as the beginning element and b as the ending element to cut out (essentially a+1 and b-1 will still be there)
def stripToSection(a,b,c):
    beginningIndex = c.index(a)
    endingIndex = c.index(b)
    avg = (beginningIndex+endingIndex)/2
    section = int(avg)
    newlist = c[section]
    return(newlist)

#Generating a random number as needed (0-x)
def generate(y,x):
    a = random.randrange(y,x)
    return(a)

#Concatenating the previously generated random number with the section name
def newRandomName(a,n,z):
    c = a+(str(generate(-1,n)))+z
    return(c)

#Provides input gathering functions for gender
def genderSelection(x):
    if str(x)=='a':
        protagonistGenderChoice = input('\nPlease enter the gender for your protagonist:\n'+genderList+'\n')
        antagonistGenderChoice = input('\nPlease enter the gender for your antagonist:\n'+genderList+'\n')
        if protagonistGenderChoice == 'a':
            protagonistGenderChoices = 'male'
        else:
            protagonistGenderChoices = 'female'
        if antagonistGenderChoice == 'a':
            antagonistGenderChoices = 'male'
        else:
            antagonistGenderChoices = 'female'
        genderChoices = [protagonistGenderChoices,antagonistGenderChoices]
        return(genderChoices)
    else:
            randNum1 = generate(-1,1)
            randNum2 = generate(-1,1)
            protagonistGenderChoice = genderListGeneration[randNum1]
            antagonistGenderChoice = genderListGeneration[randNum2]
            genderChoices = [protagonistGenderChoice,antagonistGenderChoice]
            return(genderChoices)

#Either collects or generates names (including gender-specific names as needed)
def nameSelection(x,genderSelection):
    randNum1 = generate(-1,1)
    randNum2 = generate(-1,1)
    if str(x)=='b':
        protagonistName = input('\nPlease enter a name for your protagonist:\n')
        antagonistName = input('\nPlease enter a name for your antagonist:\n')
        nameChoices = [protagonistName,antagonistName]
        return(nameChoices)
    if genderSelection[0] == 'male' and genderSelection[1] == 'male':
        protagonistName = maleProtagonistNameList[randNum1]
        antagonistName = maleAntagonistNameList[randNum2]
        nameChoices = [protagonistName,antagonistName]
        return(nameChoices)
    if genderSelection[0] == 'male' and genderSelection[1] == 'female':
        protagonistName = maleProtagonistNameList[randNum1]
        antagonistName = femaleAntagonistNameList[randNum2]
        nameChoices = [protagonistName,antagonistName]
        return(nameChoices)
    if genderSelection[0] == 'female' and genderSelection[1] == 'male':
        protagonistName = femaleProtagonistNameList[randNum1]
        antagonistName = maleAntagonistNameList[randNum2]
        nameChoices = [protagonistName,antagonistName]
        return(nameChoices)
    else:
        protagonistName = femaleProtagonistNameList[randNum1]
        antagonistName = femaleAntagonistNameList[randNum2]
        nameChoices = [protagonistName,antagonistName]
        return(nameChoices)

#Return story genre name given input from user
def genre(informationInput):
    str1 = ('Adventure', 'Fantasy', 'Western')
    if informationInput[0] == 'a':
        storyType = 'Adventure'
        return(storyType)
    if informationInput[0] == 'b':
        storyType = 'Fantasy'
        return(storyType)
    if informationInput[0] == 'c':
        storyType = 'Western'
        return(storyType)
    if informationInput[0] == 'd':
        storyType = str1[generate(-1,2)]
        return(storyType)

#Return story ending type given input from user
def ending(asdfgh):
    str1 = ('Happy', 'Sad')
    if asdfgh[0] == 'a':
        storyType = 'Happy'
        return(storyType)
    if asdfgh[0] == 'b':
        storyType = 'Sad'
        return(storyType)
    if asdfgh[0] == 'c':
        storyType = str1[generate(-1, 1)]
        return(storyType)

#Actually gather the information from the user and return it as a string which can be further read for story building
def getInformation():
    genreChoice = input('Hi! What kind of story would you like to hear?\n'+genreList+'\n')
    storyType = genre(genreChoice)
    endingChoice = input('\nGreat, now what kind of ending would you like?\n'+endingList+'\n')
    endingType = ending(endingChoice)
    genderChoice = input('\nWould you like to choose a gender for your protagonist and antagonist?\n'+yesNoChoiceList+'\n')
    genderChoices = genderSelection(genderChoice)
    nameGenerationChoice = input('\nAnd how would you like to choose the names for your characters?\n'+nameGenerationChoiceList+'\n')
    nameChoices = nameSelection(nameGenerationChoice,genderChoices)
    saveOutputChoice = input('\nLast, would you like to save the story you\'re about to hear so you can read it again later?\n'+yesNoChoiceList+'\n')
    audioChoice = input('\nWould you like me to read the story to you?\nNOTE: Only available in Terminal on MacOS and CMD on Windows.\n'+yesNoChoiceList+'\n')
    outputString = (storyType,endingType,genderChoices,nameChoices,saveOutputChoice,audioChoice)
    return(flatten(outputString))

#Legend:
#[genre, ending, protagonist gender, antagonist gender, protagonist name, antagonist name, save choice, story reading choice]

informationInput = getInformation()

#print(informationInput)

#Defining some classes so that I can use specific commands for each
class Adventure:
    def __init__(self, endingInput='a', genderInput='b', nameGenerationInput='b', outputInput='a'):
        self.e = endingInput
        self.g = genderInput
        self.n = nameGenerationInput
        self.o = outputInput
    def AdventureintroExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginAdventureBeginning'+ str(randomNum)
        endingName = 'EndAdventureBeginning'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def AdventureMiddleExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginAdventureMiddle'+ str(randomNum)
        endingName = 'EndAdventureMiddle'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def AdventureEndExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginAdventureEnd'+ str(randomNum) + informationInput[1]
        endingName = 'EndAdventureEnd'+ str(randomNum) + informationInput[1]
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)

class Fantasy:
    def __init__(self, endingInput='a', genderInput='b', nameGenerationInput='b', outputInput='a'):
        self.e = endingInput
        self.g = genderInput
        self.n = nameGenerationInput
        self.o = outputInput
    def FantasyintroExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginFantasyBeginning'+ str(randomNum)
        endingName = 'EndFantasyBeginning'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def FantasyMiddleExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginFantasyMiddle'+ str(randomNum)
        endingName = 'EndFantasyMiddle'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def FantasyEndExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginFantasyEnd'+ str(randomNum) + informationInput[1]
        endingName = 'EndFantasyEnd'+ str(randomNum) + informationInput[1]
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)

class Western:
    def __init__(self, endingInput='a', genderInput='b', nameGenerationInput='b', outputInput='a'):
        self.e = endingInput
        self.g = genderInput
        self.n = nameGenerationInput
        self.o = outputInput
    def WesternintroExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginWesternBeginning'+ str(randomNum)
        endingName = 'EndWesternBeginning'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def WesternMiddleExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginWesternMiddle'+ str(randomNum)
        endingName = 'EndWesternMiddle'+ str(randomNum)
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)
    def WesternEndExtro(self):
        randomNum = generate(1,3)
        beginningName = 'BeginWesternEnd'+ str(randomNum) + informationInput[1]
        endingName = 'EndWesternEnd'+ str(randomNum) + informationInput[1]
        newstring = stripToSection(beginningName,endingName,txtAsList)
        story.append(newstring)
        return(newstring)

adventure=Adventure()
fantasy=Fantasy()
western=Western()

#Changing the *** sections to the proper text variables
def changingVariables(x,y):
    g = []
    randNum02 = generate(0,2)
    randNum022 = generate(0,2)
    randNum04 = generate(0,4)
    for i in x:
        #He/She Pronoun choice
        if i == '***pronounChoiceHeShe***':
            if y[2] == 'male':
                g.append('he')
            else:
                g.append('she')
        #His/Her Pronoun choice
        elif i == '***pronounChoiceHisHer***':
            if y[2] == 'male':
                g.append('his')
            else:
                g.append('her')
        #Him/Her Pronoun choice
        elif i == '***pronounChoiceHimHer***':
            if y[2] == 'male':
                g.append('him')
            else:
                g.append('her')
        #Prince/Princess
        elif i == '***princePrincess***':
            if y[2] == 'male':
                g.append('prince')
            else:
                g.append('princess')
        #Location Name
        elif i == '***locationName***':
            if y[0] == 'Adventure':
                locationName = adventureLocationName[randNum02]
                g.append(locationName)
            elif y[0] == 'Fantasy':
                locationName = fantasyLocationName[randNum02]
                g.append(locationName)
            else:
                locationName = westernLocationName[randNum02]
                g.append(locationName)
        #Protagonist Name
        elif i == '***protagonistName***':
            if y[5] not in maleProtagonistNameList or femaleAntagonistNameList:
                g.append(y[4])
            elif y[2] == 'male':
                maleNameList = maleProtagonistNameList[randNum04]
                g.append(maleNameList)
            else:
                femaleNameList = femaleProtagonistNameList[randNum04]
                g.append(femaleNameList)
        #Antagonist Name
        elif i == '***antagonistName***':
            if y[5] not in maleProtagonistNameList or femaleAntagonistNameList:
                g.append(y[5])
            elif y[2] == 'male':
                maleNameList = maleAntagonistNameList[randNum04]
                g.append(maleNameList)
            else:
                femaleNameList = femaleAntagonistNameList[randNum04]
                g.append(femaleNameList)
        #Spell supply variable
        elif i == '***spellSupplyVariable***':
            spellVariable = spellVariables[randNum022]
            g.append(spellVariable)
        else:
            g.append(i)
    return (g)

def getStoryFromGenre(x):
    story = []
    if x[0] == 'Adventure':
        story.append(adventure.AdventureintroExtro())
        story.append(adventure.AdventureMiddleExtro())
        if x[1] == 'Happy':
            story.append(adventure.AdventureEndExtro())
        if x[1] == 'Sad':
            story.append(adventure.AdventureEndExtro())
    if x[0] == 'Fantasy':
        story.append(fantasy.FantasyintroExtro())
        story.append(fantasy.FantasyMiddleExtro())
        if x[1] == 'Happy':
            story.append(fantasy.FantasyEndExtro())
        if x[1] == 'Sad':
            story.append(fantasy.FantasyEndExtro())
    if x[0] == 'Western':
        story.append(western.WesternintroExtro())
        story.append(western.WesternMiddleExtro())
        if x[1] == 'Happy':
            story.append(western.WesternEndExtro())
        if x[1] == 'Sad':
            story.append(western.WesternEndExtro())
    return(story)

rawStory = getStoryFromGenre(informationInput)
tempStory = unFlatten(rawStory)
storyWithVariablesChanged = changingVariables(tempStory,informationInput)

finalStoryDraft = ' '.join(storyWithVariablesChanged)

def fixApostrophe(x):
    word = ' \''
    if word in x:
        replaced = x.replace(" \'","\'")
        return replaced
    else:
        return x

def fixPeriod(x):
    word = ' .'
    if word in x:
        replaced = x.replace(" .",".")
        return replaced
    else:
        return x

def fixComma(x):
    word = ' ,'
    if word in x:
        replaced = x.replace(" ,",",")
        return replaced
    else:
        return x

def fixOtherThing(x):
    word = ' ;'
    if word in x:
        replaced = x.replace(" ;",";")
        return replaced
    else:
        return x

def fixingPunctuation(x):
    z = fixApostrophe(fixComma(fixPeriod(fixOtherThing(x))))
    return z

finalStory = fixingPunctuation(str(finalStoryDraft))

if informationInput[6] == 'a':
    randName = newRandomName('StoryGeneratorOutput',9999,'.txt')
    outputFile = open(randName, "w")
    n = outputFile.write(finalStory)
    outputFile.close()

if informationInput[7] == 'a':
    print('\nPlease wait, your audiofile is being processed...\n')
    randNum350404 = str(generate(350000,375000))
    ttsFile = gTTS(text=finalStory, lang='en')
    audioFile = "storyoutput"+randNum350404+".mp3"
    ttsFile.save(audioFile)
    print('\n\n',finalStory)
    if plt == 'Darwin':
        os.system("afplay "+audioFile)
    elif plt == 'Windows':
        os.system('start '+audioFile)
    else:
        print('Unfortunately your operating ststem could not be detected. An audio file of this story has been saved in the operating folder for you to open in an application of your choice.')
else:
    print('\n\n',finalStory)