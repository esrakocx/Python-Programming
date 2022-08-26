class File():
    def __init__(self):

        with open("text.txt", "r", encoding="utf-8") as file:

            content = file.read()
            words = content.split()
            self.simple_words = list()

            for i in words:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(",")
                i = i.strip(".")
                self.simple_words.append(i)

    def all_words(self):

        words_set = set()

        for i in self.simple_words:
            words_set.add(i)

        print("All words..........")

        for i in words_set:
            print(i)
            print("***************************")

    def word_frequency(self):

        word_dict = dict()

        for i in self.simple_words:
            if (i in word_dict):
                word_dict[i] += 1
            else:
                word_dict[i] = 1

        for word,




file = File()
