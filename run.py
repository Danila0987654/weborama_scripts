import csv
import os
import sys

from functions import count_spaces, create_command_with_spaces
from pathlib import Path

inp_name = "Mediadesk_mobile_OZON"
output_first = "lol.data"
has_spaces = False
spaces = 0
path = "1045/324"
Path(f"./{path}").mkdir(parents=True, exist_ok=True)
move_code = f"cd {path}/"

f = open(f"inp_name", 'r')
reader = csv.reader(f)
d = open(f"{path}/{output_first}", 'w')
writer = csv.writer(d)


for row in reader:
    if " " in row[1]:
        has_spaces = True
        spaces = count_spaces(row[1])
    writer.writerow([row[0], row[1], row[2], row[3], row[4][:10]])

if not has_spaces:
    bashCommand = f"/bin/bash ./scripts/count_uniq_without_spaces.sh {output_first} {inp_name}.csv {path}"
    os.system(bashCommand)
else:
    text = create_command_with_spaces(spaces, output_first)
    os.system(text)
    bashCommand = f"/bin/bash ./scripts/count_uniq_with_spaces.sh {output_first} {inp_name}.csv {path}"
    os.system(bashCommand)

#bashCommand = f"/bin/bash count_uniq_time_without_spaces.sh {output_first} {inp_name}.csv"

Command_delete = f"cd {path} | rm -rv *.data"
os.system(Command_delete)