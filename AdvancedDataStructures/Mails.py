file = open("mails.txt", "w")
file.write("""kc.o.esra@gmail.com
example@xyz.com
esra.com
esra@gmail
esra@yahoo.com
""")

with open("mails.txt", "r", encoding="utf-8") as file:

    for i in file:
        i = i[:-1]
        if i.endswith(".com") and i.find("@") != -1:
            print(i)

