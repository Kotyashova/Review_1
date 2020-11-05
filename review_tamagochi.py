class Pet(object):
    def __init__(self, name, hunger=0, boredom=0):
        print('Родился новый питомец!')
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        rep = 'Меня зовут {}. \n'.format(self.name)
        return rep

    def __pass_time(self):
       self.hunger += 1
       self.boredom += 1

    @property
    def mood(self):
        m = ''
        if 10 > self.hunger >= 7:
            m += 'Я не знаю, как можно было довести меня до такого состояния. Срочно неси еду! '
        elif 7 > self.hunger >= 4:
            m += 'Я слегка голоден. Перекусим? '
        elif 4 > self.hunger >= 0:
            m += 'Я сытый. '
        if 10 > self.boredom > 7:
            m += 'Мне смертельно скучно! Давай поиграем? '
        elif 7 > self.boredom >= 4:
            m += 'Как-то грустно. Может, посмотрим видео с котиками? '
        elif 4 > self.boredom >= 0:
            m += 'Мне очень весело '
        m += 'Голод: {0} Скука: {1}'.format(self.hunger, self.boredom)
        return m

    def talk(self):
        print('Меня зовут {0}. {1} \n'.format(self.name, self.mood))
        self.__pass_time()

    def eat(self, food=4):
        print('Спасибо!')
        self.hunger -= food
        self.hunger = max(0, self.hunger)
        self.__pass_time()

    def play(self, fun=4):
        print('Ура, смотрю тик токи')
        self.boredom -= fun
        self.boredom = max(0, self.boredom)
        self.__pass_time()

    def learn(self, lesson=4):
        print('Учиться -- это весело!')
        self.boredom -= lesson
        self.boredom = max(0, self.boredom)
        self.__pass_time()

tam_name = input('Как вы назовёте вашего питомца?\n')
tam = Pet(tam_name)

choice = None
while choice != '0':
    print('0 - Выйти\n1 - Узнать о состоянии питомца\n2 - Покормить\n3 - Поиграть\n4 - Обучить')
    print('Выберите действие:\n')
    choice = int(input())
    if choice == 0:
        print('До встречи!')
    elif choice == 1:
        Pet.talk(tam)
    elif choice == 2:
        Pet.eat(tam)
    elif choice == 3:
        Pet.play(tam)
    elif choice == 4:
        Pet.learn(tam)
    else:
        print('Некорректный ввод. Введите другую команду.')
    if tam.hunger >= 10 or tam.boredom >= 10:
        print('Ваш питомец умер.')
        break
