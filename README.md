# `client-youngm-ifit`

Project to solve iFit exercise data problem

## Background

We recently purchased a [NordicTrack s15i](https://www.nordictrackfitness.com.au/product/commercial-studio-bikes/104/nordictrack-commercial-s15i-studio-cycle/12624/details) exercise bike which comes with the [iFit](https://www.ifit.com/apps) application. The iFit app captures and stores data about each workout which can be accessed using a touchscreen on the bike (the touchscreen is essentially an Android tablet), but also via an app or by logging into a website. Workouts can be exported from the website in two different formats.

## Problem Statement

The problem to solve is to enable an import of all the iFit workout data into my [Garmin Connect](https://connect.garmin.com) account as that is where I currently aggregate all my health data. The two export formats ([TCX](https://medium.com/decathlontechnology/gpx-tcx-fit-how-to-choose-the-best-file-extension-for-sport-activity-transfer-403487337c04) and [CSV](https://www.bigcommerce.com.au/ecommerce-answers/what-csv-file-and-what-does-it-mean-my-ecommerce-business/)) are not identical and each contain unique information, so they need to be merged into a single dataset containing the full complement of workout data. Garmin Connect accepts the TCX format, so the merged dataset needs to be exported as a TCX file.

## Possible Solution

Ideally would love an app where user can choose a workout from iFit and it imports it into Garmin Connect. Slightly less ambitious, but nevertheless really useful outcome, would be a program where user can download the workout files, pass them to a program which merges them and provides a new file to be imported into Garmin Connect.  

Whilst searching the web for a solution to the problem, user found a GitHub repo where someone had developed `R` code which does the latter. No doubt this will contain some good clues about what needs to be done. 

`markbulk/iFit_TCX_CSV_Meld`: Melding TCX & CSV files for the *NordicTrack S22i*.

## Sample Data

Note data does NOT contain PII data and (subject to size) could be stored in GitHub. 

Sample workouts exported from iFit in `data` directory.
