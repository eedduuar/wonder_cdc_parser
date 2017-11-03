# wonder.cdc.gov parser


## installation :

```
$ git clone git@github.com:eedduuar/wonder_cdc_parser.git
$ cd wonder_cdc_parser
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ python live_Stories.py -h
```


## running :

```
$ python live_Stories.py -mode weekly -output /tmp/weekly.csv


$ python live_Stories.py -mode last_week -output /tmp/last_week.csv


$ python live_Stories.py -mode yearly -output /tmp/yearly.csv input_file /tmp/weekly.csv
```

