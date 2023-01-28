# Workflow

Order in which to run code for desired outputs.

| Step | Script | Description | Output |
| - | - | - | - |
| 1 | `Targets.py` | Webscrapes CarAndDriver homepage for all brands an their models | `AllBrandsAndModels.json` |
| 2 | `SummaryGenerator.py` | Turns data in `AllBrandsAndModels.json` into links and puts them in a new directory (gitignored) `Links/{Brand}/SUMMARY.txt` where each `SUMMARY.txt` contains the links to the specs pages for all models of its brand. | `Links/{Brand}/SUMMARY.txt` | 
| 3 | `DataScraper.py` | Under Construction | TBD |
| 4 ||||
| 5 ||||


<!-- Process:
    1) python3 Targets.py
    2) python3 SummaryGenerator.py
    3) python3 AllLinks.py (under construction)
        - design a scraper for each latest model
        - design a legacy scraper for older models
    4) script to compile all csvs into one per auto maker
        - another for all (a master list)? -->