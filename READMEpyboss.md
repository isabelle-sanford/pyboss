# PyBoss
This script takes a list of employee data (employee_data.csv) and converts it into a new sheet (finished_data.csv) with the following reformattings:
* `Name` is split up into `First Name` and `Last Name` columns.
* `DOB` is changed from a `YYYY-MM-DD` format into `MM/DD/YYYY`.
* The first five digits of `SSN` are replaced with `*`s.
* `State` is changed from the full name to the state abbreviation. 

The first few lines of the output csv, with the provided dataset, should look as follows:
```csv
Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA
```

(Note: state abbreviation dictionary sourced from [Python Dictionary for State Abbreviations](https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5).)
