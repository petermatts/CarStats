# Workflow

## Aquire and Format Data

Order in which to run code for desired outputs.

| Step | Script | Description | Output |
| - | - | - | - |
| 1 | `../src/Targets.py` | Webscrapes CarAndDriver homepage for all brands an their models | `AllBrandsAndModels.json` |
| 2 | `../src/SummaryGenerator.py` | Turns data in `AllBrandsAndModels.json` into links and puts them in a new directory (gitignored) `Links/{Brand}.txt` where each `{Brand}.txt` contains the links to the specs pages for all models of its brand. | `Links/{Brand}.txt` | 
| 3 | `../Scraper2.py` | Scrape data from brand passed in as a commandline arg | `Data/YAML/**` |
| 4 | `../src/data/Conversion.py` | Convert and format data YAML -> JSON -> CSV, specify conversion type at command line. | `Data/JSON/**`/`Data/CSV/**` |
| 5 | `CompCSV.py` | Compile data CSV files into master lists | `Data/CSV/**` |

<!-- ## Debugging

| Script | Description ||
| - | - | - |
| `Collection`|||| -->


<!-- Process:
    1) python3 Targets.py
    2) python3 SummaryGenerator.py
    3) python3 AllLinks.py (under construction)
        - design a scraper for each latest model
        - design a legacy scraper for older models
    4) script to compile all csvs into one per auto maker
        - another for all (a master list)? -->