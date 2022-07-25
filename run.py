import base64
import csv
import os
import sys

from functions import count_spaces, create_command_with_spaces

# inp_name = sys.argv[1]
inp_name = "test_1"
output_first = "lol.data"
has_spaces = False
spaces = 0

f = open(f"{inp_name}", 'r')
reader = csv.reader(f)
d = open(f"{output_first}", 'w')
writer = csv.writer(d)

for row in reader:
    writer.writerow([row[0], row[1].replace(" ", ";"), row[2].replace(" ", ";"), row[3].replace(" ", ";"), row[4].replace(" ", ",")])

if not has_spaces:
    bashCommand = f"/bin/bash count_uniq_time_without_spaces.sh {output_first} {inp_name}.data"
    os.system(bashCommand)
else:
    text = create_command_with_spaces(spaces, output_first)
    os.system(text)
    bashCommand = f"/bin/bash count_uniq_time_with_spaces.sh {output_first} {inp_name}.data"
    os.system(bashCommand)


bashCommand = f"sed 's/;/ /g' {inp_name}.data > {inp_name}.csv"
os.system(bashCommand)

Command_delete = f"rm -rv *.data"
os.system(Command_delete)
