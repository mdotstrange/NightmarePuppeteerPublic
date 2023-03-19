* **How to make your own show**

* **STEPS**
* Click [here](https://docs.google.com/spreadsheets/d/1Rrt15rgAWReQ0xaWDD5kmbijzlIkEgZBz9tI-4tfU6o/copy) then click copy and fill out the google sheet, then **download it as .csv** (google account required)
*   * You should be able to add multiple shows at once, just add them as additional rows
* [Download this example show data file](https://github.com/mdotstrange/NightmarePuppeteerPublic/releases/tag/ExampleShowFiles)
*   * Replace the supplied .csv with your csv file
*   * Replace the appropriate media in the subfolders with your own
*   Edit the **"TvModeShowLineup"** text file found in StreamingAssets and add the exact **"ShowName"** that you entered in the google sheet
* Go into the Other Setting menu in Nightmare Puppeteer (accesible from start screen)
* Click the button under **"Add a new Tv Mode Show"** and select the **"MyNewShows"**(from supplied example data file) folder that contains your csv file etc
* Your show should be created and saved/loaded every time you run Nightmare Puppeteer
---------------------------------
* **NOTES**
* For heads and body names check the "AllBodies" and "AllHeads" folders in StreamingAssets
*   * You can regenerate these by running the console command "PrintAllHeadsAndBodies"
* For font names check StreamingAssets, when you run NP it will generate a text file there with your available usable fonts
* The title and light colors use html Hex colors get hex color codes [here](https://htmlcolorcodes.com/) paste them with the #
* For multiple items like Scenes, LightColors, HeadNames etc
*   * Add muliples separated by a comma with no spaces between them like this item1,item2,item3
*   If you want to use Google text to speech api voices use the console command "GoogleTextToSpeechApiKey" and paste your api key, press space bar to leave a space then paste the api key- if you don't make a space first it throws an error (hands up emoji)
