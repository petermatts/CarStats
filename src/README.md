# src Folder

Important: data must be scraped into the `Data` folder for many of these scripts to work. `Data` folder is not included in git repo, it is too large.

### `Collection.py`

Script to return a set (no duplicates) of all possible datapoints in a specified column of each brand data csv file. If no brand is specified, it will default to all brands.

This will be helpful for debugging and implementing `Corrections.py` and the correction scripts in the `Corrections` folder.

**TODO** add sys args to this script.

WARNING: be sure to run CompCSV.py before running this script.

### `CompCSV.py`

Compiles all brands in the `Data` folder into a CSV file for each brand, in `{brand}/{brand}.csv`, as well as a master datafile `AllData.csv` in the root of the `Data` folder.

### `Corrections.py`

**TODO** add sys args to this script.

### `Counter.py`

Script to count number of models in each brand. Outputs as print statements to console/terminal.

### `ErrLinkLogger.py`

Verifies that all model links for all brands are correct (response code is 200), otherwise the link gets logged for correction. Outputs these links to `../Log/ErrorLinks.csv`.

Outputs `../Log/IncompleteLinks.txt` for links in base format. (no 6 digit code at the end of the link, just a generic specs link). This most likely happens when a car model is brand new.

**TODO** add sys args to this script.

### `FileNameVerify.py`

Some output data CSV files incorrectly include a `'-\d\d\d\d'` at the end of the name. This script finds these files and renames them correctly.

### `SummaryGenerator.py`

From the file `AllBrandsAndModels.json`, this script generates link summary link files.
If `AllBrandsAndModels.json` does not exist, run `Targets.py` first.

It will also optionally generate `AllLinks.txt`.

All output files are in the `Links` folder.

This script does not require the `Data` folder to run. It is necessary to run to, scrape data for the data folder.

**TODO** add sys args to this script.

### `Targets.py`

Webscrapes the [www.caranddriver.com](www.caranddriver.com) for brand and model names. Writes them to `AllBrandsAndModels.json`.

This script does not require the `Data` folder to run. It is necessary to run to, scrape data for the data folder.
