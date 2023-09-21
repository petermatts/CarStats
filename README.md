# CarStats

## About

This project aims to compile a list of key statistics across all common car models and brands, for ease of comparison for a user.

It does this via webscrapping the reliable [https://caranddriver.com](https://caranddriver.com).

**Note** there is no front end for this <u>yet</u>

**Note** for the time being the `Data` folder is gitignored as it is quite large

### Progress/Construction

Using python's `selenium` module this project is able to webscrape all brands and their models.

The processes of extracting the information from each cars' specs page is currently in construction.

A method to 'iteratively' scrape all models (with variants over all years that model is available) for each brand is currently on the docket to be done.

Ideally once all data is collected it should be displayed properly, most likely in a table.

## Specs

Graphic of all specs being taken into consideration **coming soon** or see `Base.txt` or `Base.csv` in the `Docs` folder. 

## Future Designs and Plans

See `Todo.txt`

## Running the project (websrcaping the data)

1. `cd src`

2. Obtain links to scrape by running `Targets.py` within the

    This writes `AllBrandsAndModels.json`

3. Next run `SummaryGenerator.py summary`

    This generates the `Links` directory, each brand has its links within a txt file here i.e. `Links/${BRAND}.txt`

4. Run `ErrLinkLogger.py check` to go through the links in the `Links` directory and  log all invalid links.

    Invalid links are logged to `Log/ErrorLinks.csv`.

5. To correct the invalid links of step 4, copy `Log/ErrorLinks.csv` to `Log/ErrorLinks-Fix.csv` appending the corrected link to the model page (main or specs, doesn't really matter) (if any) to the 3rd column. You may use the 4th column for notes. Unfortunately this is a manual process... the coded solution would not be much better
   
   For example:
   - future (car is not yet released thus no specs)
   - no specs page (car exists but does not have a specs page provided)
   - And more

    To correct these links in `Links` directory by running `ErrLinkLogger.py fix`. This overwrites the bad link with the corrected link you found that works.

6. (Optional) you may create `Docs/AllLinks.txt` by running `SummaryGenerator.py all`

7. Go up a directory into the main directory `cd ..`

8. Run the data scraper `Scraper2.py` (might get renamed)

    - Required: pass the brand you would like to scrape as first argument
    - Optional: pass specific model within brand you would like to scrape
    - Optional: pass in year or --latest to scrape a specific year or the latest year available

    This writes data to `Data/YAML/*`

9. To convert/format data, you must change directories to access the script for this: `cd src/data`

10. (Optional) run `Duplicates.py` to search for and remove duplicates from the YAML data. 

11. Run `Conversion.py yaml-json` or `Conversion.py yaml2json` to convert the YAML data into JSON data.

12. Run `Conversion.py json-csv` or `Conversion.py json2csv` to convert the JSON data into the final formatted CSV data


