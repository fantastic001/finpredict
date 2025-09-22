

# finpredict


## Data collection

Create ~/.config/finpredict.json file and put your tiingo token there

	{"token": "<your token>"}

Make sure you have created data and data/news directories
and then run `finpredict data_collection` to download stock data and news articles.


## Configuration 



In order to get configuration parameters you can modify, execute:

    python scripts/detect_function_calls.py  finpredict/ get_config_ --exclude get_config_location

Every configuration parameter can be changed in configuration file and overwritten by using 
environment variable. 

For instance, `token` can be specified in configuration file and can be modified using `FINPREDICT_TOKEN` environment variable. 

Configuration file is specified using `FINPREDICT_CONFIG` and default location is at `~/.config/finpredict.json`



