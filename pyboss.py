import csv

# open file and extract data
with open("employee_data.csv", "r") as f:
    data_iter = csv.reader(f)

    header = next(data_iter)

    data = list(data_iter)

# zip into columns
cols = list(zip(*data))

# starting columns
empid = cols[0] # no change needed
name = cols[1] # split to 1st and last
dob_init = cols[2] # change format
ssn_init = cols[3] # star first five digits
state_init = cols[4] # abbreviate

# NAME
names = [n.split(' ') for n in name] # split by space
splitnames = list(zip(*names)) # zip into first and last cols

first_name = splitnames[0]
last_name = splitnames[1]


# DOB
dob1 = [d.split('-') for d in dob_init] # initial format '1990-01-30'
dob2 = list(zip(*dob1)) # zip into y/m/d columns

year = dob2[0]
month = dob2[1]
day = dob2[2]

# reorder and reformat into 1 column
dobf = [f"{month[f]}/{day[f]}/{year[f]}" for f in range(len(dob1))]


# SSN
replace = "***-**-"
ssn_final = [(replace + s[7:11]) for s in ssn_init]

# STATE
abbrev = {'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR',
    'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE',
    'Florida': 'FL', 'Georgia': 'GA', 'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL',
    'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA',
    'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA', 'Michigan': 'MI',
    'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND',
    'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI',
    'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
    'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


state_f = [abbrev[st] for st in state_init] # look up key state for value abbrev in provided dict


# create output (header and rows)
headerf = ['Emp ID','First Name','Last Name','DOB','SSN','State']
rows = zip(*(empid, first_name, last_name, dobf, ssn_final, state_f))

# print into new csv
with open('finished_data.csv', 'w', newline="") as final:
    writer = csv.writer(final)
    writer.writerow(headerf)
    writer.writerows(rows)