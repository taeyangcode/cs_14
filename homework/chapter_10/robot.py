# Robot class

import random as rnd


class Robot:
    def __init__(self, good_or_evil):
        self.__good_evil = good_or_evil

        print("Greetings Master.I am here to do ", self.__good_evil, ".", sep="")

        self.__name = ""

    def set_name(self, name):  # Assign name
        self.__name = name

    def get_name(self):  # Return name of robot
        return self.__name

    def __str__(self):
        return "Battery level at " + str(rnd.randint(1, 100)) + "%"

    def wash_dishes(self):
        print(
            "I washed the dishes."
            if self.__good_evil.lower() == "good"
            else "I am an evil robot."
        )

    def save_puppy(self):
        print(
            "I saved the puppy."
            if self.__good_evil.lower() == "good"
            else "I am an evil robot."
        )

    def rob_bank(self):
        print(
            "I robbed $xx.xx."
            if self.__good_evil.lower() == "evil"
            else "I am a good robot."
        )

    def kick_puppy(self):
        print(
            "I kicked a puppy."
            if self.__good_evil.lower() == "evil"
            else "I am a good robot."
        )
