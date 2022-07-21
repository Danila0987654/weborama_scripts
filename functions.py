import csv


def count_spaces(string):
    count = 0
    for i in string:
        if i == " ":
            count += 1
    return count


def create_command_with_spaces(spaces, output_first):
    command = "cat %s | sort | uniq -c | awk \'{" % output_first
    now = 0
    for i in range(spaces):
        now += 1
        next = now + 1
        if i == 0:
            command += f"print ${now}\",\"${next}"
        else:
            command += f"\" \"${now}\" \"${next}"
        now += 1
    command += "}\' > hello.data"

    return command

