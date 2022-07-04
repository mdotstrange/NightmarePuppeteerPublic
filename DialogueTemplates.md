**If you do things wrong when editing/adding new wordlists/templates you could crash NP.
If you fuck everything up, unzip the AiWordList and/or AiConversationTemplates and allow them to overwrite**

**Editing word lists**

* The files are located in StreamingAssets/AiWordLists
* Do not leave any blank lines in the file, they must me .txt files
* Use Notepad++ for the easier workflow

**If you want to make your own dialogue text templates to be used in NP here is the syntax reference**
* **They are located in the file at StreamingAssets/AiWordLists/DialogueTemplates.txt**

* [n] **noun** - examples: airplane, sirship, airport
* [v] **verb** - examples: dive, paddle, muzzle
* [adv] **adverb** - examples: badly, awkwardly, coyly
* [adj] **adjective** - examples: aggressive, afraid, amused
* [avc] **adverb conjective** - examples: elsewhere, finally, likewise
* [avn] **adverb no LY** - examples: best, even, far
* [pn] **pronoun** - examples: he, she, they
* [feel] **feeling** - examples: love, hate, abhor
* [color] **color** - examples: green, blue, black
* [stars] **constellations** - examples: Aries, Cancer, Capricornus
* [rf] **rap filler** -  examples: ay, yeah, money
* [qs] **question starter** - examples: why, what, when
* [qg] **question glue** - examples: if, or, also
* [fish] **fish name** - examples: Salmon, trout, albacore
* [*] **curse word** - examples: shit, fuck, dildo
* [!] **random punctuation** - examples: !, ? , .
* [time] **times** - examples: forever, a minute, a long time ago
* [ship] **ship names** - examples: Adonia, Athena, Arosa star

**Create a text file where each line is a new line of dialog, Notepad++ recommended**

**Example of basic random dialogue template text line**
* [v] [n]'s [adv] [qg] [pn][!]
* [pn] [adv] [n] [pn] [n] [avn][!]
* [avn] [pn] [adj] [n] [adv] [avn]
* [n] [n]'s [adv] [v] [pn] [n][!]
* [avc], [avc], [pn] [qg] [v]ing[!]


**When writing a dialogue between 2 actors you need to use 2 separate text files**
* Look at the files in StreamingAssets/AiConversationTemplates to see how they are used
* Your files must start with with Actor1 or Actor2 
* ![](https://github.com/mdotstrange/NightmarePuppeteerPublic/raw/master/Files/dia2.png)

**When writing a dialogue to be between 2 actors and not just random lines there are some special variables to use**

* [charName1] **Actor 1's name**- this will randomly generate/retrieve a name that will be used as actor 1's name in the dialogues
* [charName2] **Actor 2's name**- this will randomly generate/retrieve a name that will be used as actor 2's name in the dialogues
* **Example** - "[charName1] waves to [charName2] and does an [adj] [v]
* These character name variables are stored and used for the entirety of the conversation

**if you add a * after any var name like this [v*] that variable will be saved and can be recalled once** 

* Looking at the above image example- the left side is Actor1's text- the right side is Actor2's text
* Looking at line 1- the [n*] that will generated in Actor1's line will be saved and used by the [n*] in actor 2's line
* As soon as Actor1 used a new [n*] like in line 4 that will create a new one to be used

* **Here are those two text files you can use as examples**
* Check the existing files to see how things are done
* You can write yours to be as many lines as you'd like
*  [Actor1 file](https://raw.githubusercontent.com/mdotstrange/NightmarePuppeteerPublic/master/Files/Actor1_Stalker.txt)
*  [Actor2 file](https://raw.githubusercontent.com/mdotstrange/NightmarePuppeteerPublic/master/Files/Actor2_Stalker.txt)
*  It's easy to create text files like that with Notepad++ 

**To share your dialogue templates please post them** [HERE](https://github.com/mdotstrange/NightmarePuppeteerPublic/discussions/419)
