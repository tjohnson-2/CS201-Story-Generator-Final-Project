# CS201-Story-Generator-Final-Project
 
Story Generator
CS-201-01 Final Project

The python application enclosed in this folder generates children’s stories. This application will first ask for basic information about the story, such as genre, character genders and names, what kind of ending the user would like, as well as an option to save the output file or even processing the finalized story through Google’s Text to Speech processors and creating an mp3.

There are prerequisite packages and libraries that need to be installed to ensure that this program runs smoothly. These are as follows:
•	gtts 
o	pip install gtts
o	webpage

Once the prerequisite libraries are installed, simply run the following command to generate a story: 

python3 Source.py

The user is free to edit the stories file should they wish. Each story is broken down into three blocks: a beginning, middle, and end. There are three variations for each beginning and middle part for each genre. There are two variations each of a happy and sad ending for each genre. These story “blocks” are marked by having an identifier before and after each block. The format is understood as follows:

[Begin/End][Genre][Beginning/Middle/End][Variation number (1-3 is default)][Happy/Sad (only for ending sections)]
*two identifiers are needed for a single block. One ‘Begin’ and one ‘End’.

The text in between each section can be of any length the user desires. The only bug is when using a variable-***protagonistName*** for example- followed by a “‘s” (or generally any form of punctuation) will render the variable useless and unchangeable. Please ensure there is at least one space (‘ ‘) immediately preceding and following each variable.

Should the user wish to add additional stories, that is also possible. Simply follow the naming scheme for marking out sections. If the user does add more than the default amount of blocks, the source code will need to be edited. This can be done by opening the Genre Class (line 184, 212, or 240), choose the correct area for beginning/middle/end of story, and change the following highlighted value accordingly for the number of blocks the generator can chose from “randomNum = generate(1,3)”. Save both the text and source file as needed and run the program. 

The list of all variables that may be used is as follows:
•	***spellSupplyVariable***
•	***locationName***
•	***princePrincess***
•	***pronounChoiceHimHer***
•	***pronounChoiceHisHer***
•	***pronounChoiceHeShe***
•	***protagonistName***
•	***antagonistName***

![image](https://github.com/tjohnson-2/CS201-Story-Generator-Final-Project/assets/85690659/4d1576a6-fc39-4d44-9e5d-72a603fd482d)
