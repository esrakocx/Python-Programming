class Find():

    def letter_frequency(self):

        sentence = "ProgrammingAssignmentAdvancedDataStructuresandObjectspynb"
        letter_dict = dict()

        for i in sentence:
            if i in letter_dict:
                letter_dict[i] += 1
            else:
                letter_dict[i] = 1

        for letter, number in letter_dict.items():
            print("The word of '{}' there are {} time(s)!".format(letter, number))
            print("-------------------------------------------------")


find = Find()
find.letter_frequency()
