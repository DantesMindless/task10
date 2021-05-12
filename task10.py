


#task1

class Person():
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):

        print ('Hey, my fullname is ' + pers.firstname, pers.lastname,   'and i am ' + pers.age + ' years old')


pers = Person('Danilo','Svirid','16')
pers.talk()

#task2

class Dog():
   def __init__(self,dogs_age):
       self.dogs_age = dogs_age
   def human_age(self):

    print('One year of a dog equals to 7 years of a human , so if the dog is 7 y. o human would be ' + str(age.dogs_age * 7))

age = Dog(7)
age.human_age()


#task3

CHANNELS = ["BBC", "Discovery", "TV1000", "UK", "USA"]

class TVremote():

    def __init__(self,channel1,channel2,channel3,channel4,channel5):
        self.channel1 = channel1
        self.channel2 = channel2
        self.channel3 = channel3
        self.channel4 = channel4
        self.channel5 = channel5

    a = 0
    channel = 0

    def first_channel(self):
        self.channel = 0
        print(CHANNELS[self.channel])
    def last_channel(self):
        self.channel = -1
        print(CHANNELS[self.channel])

    def current_channel(self):
        self.channel = self.channel
        print(CHANNELS[self.channel])

    def turn_channel(self,N):
        self.channel = N - 1
        print(CHANNELS[self.channel])

    def next_channel(self):
        self.channel += 1
        if self.channel > len(CHANNELS) - 1:
            self.first_channel()
        else:
            print(CHANNELS[self.channel])

    def previous_channel(self):

        if self.channel == 0:
            self.channel = -1
            print(CHANNELS[self.channel])
        elif self.channel == -1:
            self.channel = len(CHANNELS) - 2
            print(CHANNELS[self.channel])
        else:
            self.channel = self.channel - 1
            print(CHANNELS[self.channel])


    def is_exist(self, srch):
        if type(srch) == int:

             if srch < 0:
                 print('Number cannot be negative')
             elif srch <= len(CHANNELS):
                 print("CHANNEL EXISTS")
             else:
                 print('CHANNEL DOES NOT EXIST')
        else:
            if srch in CHANNELS:
                print('CHANNEL EXISTS')
            else:
                print('CHANNEL DOES NOT EXIST')



controller = TVremote(*CHANNELS)
user_choice = ''
controller.first_channel()
while user_choice != '1':
    user_choice = input("Turn off TV = 1\nFirst channel = 2\nLast channel = 3\nNext channel = 4\nPrevious channel = 5\nTurn channel = 6\nSearch channel = 7\n")
    if user_choice == '2':
        controller.first_channel()
    if user_choice == '3':
        controller.last_channel()
    if user_choice == '4':
        controller.next_channel()
    if user_choice == '5':
        controller.previous_channel()
    if user_choice == '6':
        turn_input = int(input('Enter number of channel you want to display'))
        controller.turn_channel(turn_input)
    if user_choice == '7':
        search_input_choice = input('Number of a channel = 1\nName of a channel = 2\n')
        if search_input_choice == '1':
            search_input_int = int(input('Type a number of a channel'))
            controller.is_exist(search_input_int)
        if search_input_choice == '2':
            search_input_str = input('Type a name of a channel')
            controller.is_exist(search_input_str)
