# data Folder

### `Conversion.py`

Converts data files from YAML -> JSON -> CSV.

Reformatting data as necessary along the way. ***Note that corrections have not yet been implemented***

Commandline argument options:
- `yaml-json`: convert YAML to JSON
- `yaml2json`: convert YAML to JSON
- `json-csv`: convert JSON to CSV
- `json2csv`: convert JSON to CSV

### `ConversionHelper.py`

Helper file for `Conversion.py`

### `Duplicate.py`

Detects and removes duplicate data instances from data YAML files

### `MakeBase.py`

Generates the set of all keys in JSON data files and outputs them to `Docs/Base.txt`
