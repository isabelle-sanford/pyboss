import csv

with open("employee_data.csv", "r") as f:
    data_iter = csv.reader(f)

    header = next(data_iter)

    data = list(data_iter)

# Emp ID,Name,DOB,SSN,State
# 214,Sarah Simpson,1985-12-04,282-01-8166,Florida
#       TO
# Emp ID,First Name,Last Name,DOB,SSN,State
# 214,Sarah,Simpson,12/04/1985,***-**-8166,FL

cols = list(zip(*data))

empid = cols[0] # no change needed
name = cols[1] # split to 1st and last
dob_init = cols[2] # change format
ssn_init = cols[3] # star first five digits
state_init = cols[4] # abbreviate

# NAME
names = [n.split(' ') for n in name]
splitnames = list(zip(*names))

first_name = splitnames[0]
last_name = splitnames[1]

# check = [len(s) for s in names]
# print(max(check))

# DOB
dob1 = [d.split('-') for d in dob_init]
dob2 = list(zip(*dob1))
year = dob2[0]
month = dob2[1]
day = dob2[2]
dobf = [f"{month[f]}/{day[f]}/{year[f]}" for f in range(len(dob2))]

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


state_f = [abbrev[st] for st in state_init]


headerf = ['Emp ID','First Name','Last Name','DOB','SSN','State']
rows = list(zip(*(empid, first_name, last_name, dobf, ssn_final, state_f)))

print(rows)

with open('finished_data.csv', 'w', newline="") as final:
    writer = csv.writer(final)
    writer.writerow(headerf)
    writer.writerows(rows)