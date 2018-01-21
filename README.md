
<h1 align="center">
  Pokémon gen 4 and 5 overlay script
  <br>
</h1>

<h4 align="center">A script so you don't have to update your overlay by hand.</h4>



<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#download">Download</a> •
  <a href="#credits">Credits</a> •
  <a href="#related">Related</a> •
  <a href="#license">License</a>
</p>

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/Demo.gif)

## Key Features

* Autonomous 
  - Quickly see changes to your overlay with no input on your end.
* Customizable  
  - Choose what types of images you want and where they go.
* Current health
  - As plain text and as a bar graph.  
* Current level
* Artwork for each team member
  - Supports empty slots and eggs
* Nickname
  - Comming soon(tm)


## How To Use

For this script to work, you need to have the following: 
 * Python version 3.X
 * [DeSmuMe](http://desmume.org/)
 * A generation 4 or 5 Pokémon rom
 * [Open Broadcaster Software](https://obsproject.com/)



After downloading the most recent version of the script, you should have a folder like this: 
![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/Folder.PNG)

The assets folder needs to be populated with images of all pokemon and named with their national dex number:

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/Assets.PNG)
* Note: You will also need a file for an empty slot (0.png) and for an egg (egg.png)

In desmume, there is the option to add a lua script under tools -> Lua Scripting: 

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/DeSmuMe.PNG)

After the script is running in DeSmuMe, you then need to run the python script.

```
cd <path to folder>
Python Script.py
```

Then over in OBS, you need to add image sources for the the team members and their health bars making sure to point to the files located in the /out/ folder. 

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/OBSImages.PNG)

Then add the text for each team member making sure to point to the text files in the /out/ folder. 

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/OBSText.PNG)

And you're done! Unfortunately it is a lot of images/text to setup. But when you're done it should look something like this: 

![screenshot](https://raw.githubusercontent.com/The-f6X/Gen4OverlayScript/master/img/OBSSources.PNG)



## Download


You can [download]() the latest version of the script for Windows since Desmume doesn't support Lua scripting on other platforms.

## Credits

This software uses code from several open source packages.

 * [MatPlotLib](https://matplotlib.org/index.html) for the health bar code. 
 * [KazoWar](https://projectpokemon.org/home/forums/topic/30518-4th-and-5th-gen-misc-info-reading-scripts/) for the original Lua script.
 * [Shawn](https://github.com/shawnrc) for taking interest in the projct and developing the hell out of it. 
 * [Markdownify](https://github.com/amitmerchant1990/electron-markdownify) for readme formatting.

## Related



## You may also like...



## License



---

> Twitch [The_f6X](https://www.twitch.tv/the_f6x) &nbsp;&middot;&nbsp;
> GitHub [@The-f6X](https://github.com/The-f6X) &nbsp;&middot;&nbsp;
> Twitter [@The_f6X](https://twitter.com/The_f6X)
