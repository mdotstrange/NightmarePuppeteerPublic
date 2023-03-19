* **How to make your own show**

* **STEPS**
* Go [here](https://docs.google.com/spreadsheets/d/1Rrt15rgAWReQ0xaWDD5kmbijzlIkEgZBz9tI-4tfU6o/copy) click copy and fill out this google sheet, then download it as .csv (google account required)
*   * You should be able to add multiple shows at once, just add them as additional rows
* [Download this example show data file](https://github.com/mdotstrange/NightmarePuppeteerPublic/releases/tag/ExampleShowFiles)
*   * Replace the supplied .csv with yours
*   * Replace the appropriate media in the subfolders with your own
*   Edit the "TvModeShowLineup" text file found in StreamingAssets and add the exact "ShowName: you entered in the google sheet
* Go into the Other Setting menu in Nightmare Puppeteer (accesible from start screen)
* Click the button under "Add a new Tv Mode Show" and select the "MyNewShows" folder that contains your csv file etc
* Your show should be created and saved/loaded every time you run Nightmare Puppeteer
---------------------------------
* **NOTES**
* For heads and body names check the "AllBodies" and "AllHeads" folders in StreamingAssets
*   * You can regenerate these by running the console command "PrintAllHeadsAndBodies"
* For font names check StreamingAssets, when you run NP it will generate a text file there with your available usable fonts
* The title and light colors use html Hex colors get hex color codes [here](https://htmlcolorcodes.com/) paste them with the #
* For multiple items like Scenes, LightColors, HeadNames etc
*   * Add muliples separated by a comma with no spaces between them like this item1,item2,item3
