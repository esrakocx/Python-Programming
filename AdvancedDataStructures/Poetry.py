class Poetry():

    def __init__(self):

        with open("poetry.txt", "r", encoding="utf-8") as file:
            first_letters = ""
            for row in file:
                first_letters += row[0]
        print(first_letters)


poetry = Poetry()
