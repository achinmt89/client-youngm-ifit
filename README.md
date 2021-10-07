# furry-octo-disco

Project to solve Mick Y's exercise data problem

## Description 

We recently purchased a [NordicTrack s15i](https://www.nordictrackfitness.com.au/product/commercial-studio-bikes/104/nordictrack-commercial-s15i-studio-cycle/12624/details) exercise bike which comes with the iFit application. The iFit app captures and stores data about each workout which can be accessed using a touchscreen on the bike (the touchscreen is essentially an Android tablet), but also via an app or by logging into a website. Workouts can be exported from the website in two different formats.
 
The problem to solve is to enable an import of all the iFit workout data into my Garmin Connect account as that is where I currently aggregate all my health data. The two export formats (TCX and CSV) are not identical and each contain unique information, so they need to be merged into a single dataset containing the full complement of workout data. Garmin Connect accepts the TCX format, so the merged dataset needs exported as a TCX file.
 
Ideally I would love an app where I can choose a workout from iFit and it imports it into Garmin Connect. I slightly less ambitious but nevertheless really useful outcome would be a program where I download the workout files, pass them to a program which merges them and provides a new file to be imported into Garmin Connect.  Whilst searching the web for a solution to my problem, I found a GitHub repo where someone had developed R code which does the latter . No doubt this will contain some good clues about what needs to be done. GitHub - markbulk/iFit_TCX_CSV_Meld: Melding TCX & CSV files for the NordicTrack S22i
 
Finally, I’ve attached some sample workouts exported from iFit.
