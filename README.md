# RoleCrawler
## Goal
Goal of this project is to get all Dota 2 heroes, their winrates and occurrences in each of the games 5 roles. This is created in order to later create a separate sortable list where one could easily determine which heroes are currently doing well in certain positions.

This crawler could be expanded to gather lot more data later on

## Steps
### What are current heroes?
First step is to fetch the current heroes and the best place to get that is api.opendota.com
### Where are they being played?
Dotabuff has information about where each of the heroes has laned, but does not necessarily determine well between positions. Therefore I've decided to mostly focus on the excelent stats provided by dota2protracker.com, which under each hero displays their played lanes and how well they have been performing on those in particular
### Where to put all this data?
I've opted to push the data to MongoDB in Azure just for it's simplicity. I don't really need to retain history information so the old info is dropped before starting a new run, allowing the collection to function as a source for which ever way of visualizing I happen to pick

## Setup
### Container
This crawler should be available later on from dockerhub and the goal is that it could be setup to run pretty much anywhere without much additional tinkering required

### MongoDB
Regular setup of mongoDB will do just fine, but you should be able to convert this to other storage solutions quite easily. The end result from the containers perspective is JSON so that should be rather easy to push anywhere

Connection string should look like this 
mongodb://**STORENAME**:**TOKEN**@**STORENAME**.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@**STORENAME**@

Running the container will put the results in:
DB: heroesDB
Collection: heroesCollection
