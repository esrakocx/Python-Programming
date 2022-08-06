import random
import time


class Control:
    def __init__(self, tv_status="Off", tv_sound=0, channel_list=["BBC"], channel="BBC"):

        self.tv_status = tv_status
        self.tv_sound = tv_sound
        self.channel_list = channel_list
        self.channel = channel

    def tv_on(self):

        if self.tv_status == "On":
            print("TV is already on!")
        else:
            print("TV is turning on...")
            self.tv_status = "On"

    def tv_off(self):

        if self.tv_status == "Off":
            print("TV is already off!")
        else:
            print("TV is turning off...")
            self.tv_status = "Off"

    def sound_settings(self):

        print("To increase: '>'\nTo decrease: '<'\nTo exit: 'q'")

        while True:

            choice = input("Response: ")

            if choice == ">":
                if self.tv_sound != 100:
                    self.tv_sound += 1
                    print("Sound: ", self.tv_sound)

            elif choice == "<":
                if self.tv_sound != 0:
                    self.tv_sound -= 1
                    print("Sound: ", self.tv_sound)

            else:
                print("Sound updated...")
                break

    def add_channel(self, channel_name):

        print("Channel is adding...")
        time.sleep(1)

        self.channel_list.append(channel_name)

        print("Channel added!")

    def random_channel(self):

        randomly = random.randint(0, len(self.channel_list)-1)

        self.channel = self.channel_list[randomly]

        print("Current channel:", self.channel)

    def __len__(self):
        return len(self.channel_list)

    def __str__(self):
        return "TV Status: {}\nSound: {}\nChannels: {}\nCurrent Channel: {}".format(self.tv_status, self.tv_sound, self.channel_list, self.channel)


control = Control()

print("""

~Remote Control App~

Operations:

1- Turn on TV
2- Turn off TV
3- Sound settings
4- Add channel
5- Find out the number of channels
6- Go to random channel
7- TV Information
q- Exit

""")

while True:
    choice = input("Choice: ")

    if choice == "q":
        print("Program is terminated...")
        time.sleep(1)
        break
    elif choice == "1":
        control.tv_on()
    elif choice == "2":
        control.tv_off()
    elif choice == "3":
        control.sound_settings()
    elif choice == "4":
        channel_names = input("Enter the channels you want to add by separated with commas ',' :  ")

        channel_list2 = channel_names.split(",")

        for i in channel_list2:
            control.add_channel(i)
        print("Channel list updated!")
    elif choice == "5":
        print("Number of channels: ", len(control))
    elif choice == "6":
        control.random_channel()
    elif choice == "7":
        print(control)
    else:
        print("Incorrect input!")

