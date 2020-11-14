import time


class Pet(object):
    def __init__(self, name, hunger=70, boredom=70):
        print('New pet!')
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    @property
    def mood(self):
        m = ''
        if 30 >= self.hunger >= 0 and 30 >= self.boredom >= 0:
            m += '{} is happy. '.format(self.name)
        elif 70 > self.hunger >= 30 or 70 > self.boredom >= 30:
            m += '{} is OK. '.format(self.name)
        elif 100 > self.hunger >= 70 or 100 > self.boredom >= 70:
            m += '{} is unhappy. '.format(self.name)
        m += 'Hunger: {0} Boredom: {1}'.format(self.hunger, self.boredom)
        return m

    def talk(self):
        print('It is {0}. {1} \n'.format(self.name, self.mood))

    def eat(self, food=20):
        print('Omnomnom')
        self.hunger -= food
        self.hunger = max(0, self.hunger)

    def play(self, fun=15):
        print('Netflix and chill.')
        self.boredom -= fun
        self.boredom = max(0, self.boredom)

    def learn(self, lesson=20):
        print('It is interesting!')
        self.boredom -= lesson
        self.boredom = max(0, self.boredom)

    def period(self, delta):
        self.hunger += round(delta / 10)
        self.boredom += round(delta / 10)


tam_name = input('What will you name your pet?\n')
tam = Pet(tam_name)
time_0 = time.time()
choice = None
while choice != '0':
    print('0 - Exit', '1 - Find out the mood', '2 - Feed', '3 - Play', '4 - Learn', sep='\n')
    print('Choose command:\n')
    choice = input()
    delta = time.time() - time_0
    Pet.period(tam, delta)
    if choice == '0':
        print('Good luck!')
        break
    elif choice == '1':
        Pet.talk(tam)
    elif choice == '2':
        Pet.eat(tam)
    elif choice == '3':
        Pet.play(tam)
    elif choice == '4':
        Pet.learn(tam)
    else:
        print('Invalid input. Choose another command.')
    time_0 = time.time()
    if tam.hunger >= 100 or tam.boredom >= 100:
        print('Your pet is dead.')
        break
