# Discord Overlap
Discord Overlap is a simple tool for finding the overlap of discord
users between servers.

# Prerequisites
- python 3
- pip

# Install
```pip install -r requirements.txt```

# Usage
Put the text `creds = ["EMAIL", "PASSWORD"]` into `creds.py` replacing
`EMAIL` and `PASSWORD` with your discord account's email and password
respectively.  Run `python overlap.py` to get the data.  The output is
stored in a csv file located at `out/users.csv`.

# Output
The output is in csv format in `out/users.csv`.  Example output:
```ID,Name,Expo Planning,Future Forwards
419110059742040960,me,True,True
807839291767816193,friend,True,True
821798875263901169,someone,False,True
521370946904412915,another,True,False
```
