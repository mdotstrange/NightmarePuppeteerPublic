## Custom Jaw Information

* Let's say you made a custom character and you can it to have lip sync when you import it into NP
* Here's some guidelines for you
* You don't need an upper jaw, only a lower jaw.
* Name your lower jaw "customJaw" so NP can find it
* You want your jaw to rotate on the X axis when it is opening and closing
* You should test your jaw in Unity.
* Np assumes that when your jaw is closed its **X value is 20** like in this image
* ![](https://github.com/mdotstrange/NightmarePuppeteerPublic/raw/master/Files/closedJaw.png)
* Orient your jaws axis like in the these images
* NP assumes when your mouth is open its **X value is 0** like in this image
* ![](https://github.com/mdotstrange/NightmarePuppeteerPublic/raw/master/Files/OpenJaw.png)
* **Make sure the Y and Z rotation values are 0**
* If you follow these guidelines your character should be able to talk in NP.
* If you have any problems please post an issue [here](https://github.com/mdotstrange/NightmarePuppeteerPublic/issues)
