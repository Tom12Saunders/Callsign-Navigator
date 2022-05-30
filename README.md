# Callsign-Navigator
The callsign navigator repository allows the user to easily construct a list of URLs to pull up and applications to open- all at once. The navigator also provides a script that can be set as a desktop short cut, allowing you to easily store sets of URLs and applications as a row in a csv; efficiently prompting the user for the callsign name, type, and URL before writing to a csv. This tool allows the user to automate remedial, repetitive digital navigations and is made for the purpose of expanding the techinical freedom of a person with average technological prowess, allowing everyone to create their own single-click tools; completely personalized to the individuals unique needs.

# Overview of Terminology
Callsign: A shortname, of the user's making, for a website or application that the user frequently opens in conjuction with a host of other websites/applications; for which they'd make a callsign for each site and app, then make a polysign of all constituent callsigns. The list of designated callsigns and polysigns are stored in the corresponding CSV files, and the user can quickly and easily enter their own callsigns in the builder, then build their own polysigns in the builder as well. The user is encouraged to build up a long list of callsigns so that when they start a new class/job, they can efficiently assemble a list of new URLs and applications to enter, and automate their digital navigation process down to one click from thereon after.

# Compatability Warning
* WARNING * This repository is designed for MacOSX, it also won't work for sites that require login, unless your device is already logged in. Essentially it will pull up anything that will come up after you type the URL and hit enter, nothing more/nothing less.

# Download Instructions
Download the files: 
1.  callsign.csv 
2.  polysign.csv
3.  builder.py
4.  shortcut.py

If you're having trouble with building your CSVs, here are some instructions on how to resolve those issues: 
  -To ensure no issues when reading/writing to the CSVs make sure to only open them in TextEdit and that, after using the builder to add in your    own callsigns (and/or polysigns), you open up the csv and ensure that each callsign is on it's own line; you will also need to enter     
   'Callsign' for the first callsign name you enter, 'type', for the first callsign's 'type', and 'URL', for the first callsign's URL; in order    for the program to work because I designed it to have the first line in the csv as column titles. Likewise for polysign.csv, set the polysign    name too 'Name', and only enter 1 callsign for the first polysign; 'list_of_polysigns'.
