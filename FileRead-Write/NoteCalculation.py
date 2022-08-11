def calculate_note(line):

    line = line[:-1]
    list1 = line.split(",")
    name = list[0]
    note1 = int(list1[1])
    note2 = int(list1[2])
    note3 = int(list1[3])

    avg = note1 * 0.3 + note2 * 0.3 + note3 * 0.4

    if avg >= 90:
        letter = "AA"
    elif avg >= 85:
        letter = "BA"
    elif avg >= 80:
        letter = "BB"
    elif avg >= 75:
        letter = "CB"
    elif avg >= 70:
        letter = "CC"
    elif avg >= 65:
        letter = "DC"
    elif avg >= 60:
        letter = "DD"
    elif avg >= 55:
        letter = "FD"
    else:
        letter = "FF"

    return name + "----------->" + letter + "\n"


with open("file.txt", "r", encoding="utf-8") as file:

    list2 = []

    for i in file:
        list2.append(calculate_note(i))

    with open("notes.txt", "w", encoding="utf-8") as file2:

        for i in list2:
            file2.write(i)
