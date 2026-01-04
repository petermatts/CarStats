# Data

## CSV

Contains parsed/formatted (hopefully) data that comes from the semi parse JSON data.

This is where the data takes on its final form for display to a user.

Included in `.gitignore` because this is a large folder.

## JSON

Contains the altered data, from webscraping in JSON format.

Data is altered into a more suitable key value pairing for the desired result in CSV format.

Example: `{MPG: city/hwy/comb} -> {MPG city: #, MPG hwy: #, MPG comb: #}`

Included in `.gitignore` because this is a large folder.

## YAML

Raw webscraped data.

Included in `.gitignore` because this is a large folder.
