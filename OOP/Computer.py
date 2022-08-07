import random
import time

class Computer:
    def __init__(self, pc_status="Off", pc_sound=0, programs=["Pycharm", "Whatsapp", "Spotify", "Visual Studio"], musics=["What a Wonderful Life", "Adventure of a Lifetime","Riptide", "Seni Dert Etmeler", "California Dreamin'","Fly Me to the Moon"]):

        self.pc_status = pc_status
        self.pc_sound = pc_sound
        self.programs = programs
        self.musics = musics

    def pc_on(self):
        if self.pc_status == "Off":
            self.pc_status = "On"
            print("Computer turned on!")
        else:
            print("Computer is already on!")

    def pc_off(self):
        if self.pc_status == "On":
            self.pc_status = "Off"
            print("Computer turned off!")
        else:
            print("Computer is already off!")

    def sound_settings(self):
        print("To increase: '>'\nTo decrease: '<'\nTo exit: 'q'")

        while True:
            response = input("Response: ")

            if response == ">":
                if self.pc_sound != 100:
                    self.pc_sound += 1
                    print("Sound: ", self.pc_sound)
            elif response == "<":
                if self.pc_sound != 0:
                    self.pc_sound -= 1
                    print("Sound: ", self.pc_sound)
            else:
                print("Sound: ", self.pc_sound)
                break

    def add_programs(self, program_name):

        print("Programs are downloading...")
        time.sleep(2)

        self.programs.append(program_name)

        print(program_name, "downloaded!")
        print("Valid programs: ", self.programs)

    def remove_programs(self, program_name2):

        print("Program is removing....")
        time.sleep(1)

        self.programs.remove(program_name2)

        print(program_name2, "removed!")
        print("Valid programs: ", self.programs)

    def play_songs(self):

        randomly = random.randint(0, len(self.musics)-1)
        music = self.musics[randomly]

        print("The song playing: ", music)

    def __len__(self):
        return len(self.programs)

    def __str__(self):
        return "Computer status: {}\nComputer sound: {}\nPrograms: {}\nMusics: {}".format(self.pc_status, self.pc_sound, self.programs, self.musics)


computer = Computer()

print("""

1- Turn on the computer
2- Turn off the computer
3- Sound settings
4- Download programs
5- Remove programs
6- Play a song :)
7- Computer Information
8- Find out the number of programs
9- Exit

""")

while True:
    choice = input("Choice: ")

    if choice == "1":
        computer.pc_on()
    elif choice == "2":
        computer.pc_off()
    elif choice == "3":
        computer.sound_settings()
    elif choice == "4":
        program_names = input("Enter the programs you want to download, separated by commas ',' : ")
        program_names = program_names.split(",")
        for i in program_names:
            computer.add_programs(i)
    elif choice == "5":
        program_names2 = input("Enter the program you want to remove: ")
        program_names2 = program_names2.split(",")
        for i in program_names2:
            computer.remove_programs(i)
    elif choice == "6":
        computer.play_songs()
    elif choice == "7":
        print(computer)
    elif choice == "8":
        print("Program number: ", len(computer))
    elif choice == "9":
        print("Exiting...")
        time.sleep(1)
        break
    else:
        print("Incorrect input!")

