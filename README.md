# fantasy_football_scripts

## Requirements
* make
* pip

## Howto
* `make bootstrap` - will setup `virtualenv` and install `pip` requirements
* `make run` - runs the scripts to fetch data

### Output
* espn.csv
* dw.csv

These will export corresponding .csv files to import into your favorite spreadsheet software.

### Tests
```bash
nosetests test_*
```
