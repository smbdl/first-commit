class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f'CPU: {self.__cpu} Memory: {self.__memory}'

    def __gt__(self, other):
        return self.memory > other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __eq__(self, other):
        return self.memory == other.memory

    def __neg__(self, other):
        return self.memory != other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = list(sim_cards_list)

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    @staticmethod
    def call(sim_card_number, call_to_number):
        return f'Идет звонок на номер {sim_card_number} с сим-карты - {call_to_number}'

    def __str__(self):
        return f'Sim-card list: {self.__sim_cards_list}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        return f'Маршрут до локации {location} построен.'

    def __str__(self):
        return super().__str__() + f' Sim-card list: {self.sim_cards_list}'


computer = Computer(15, 20)
print(computer)
smartphone = SmartPhone(15, 20, ['o!', 'megacom'])
print(smartphone)
phone = Phone(['o!', 'megacom'])
print(phone)

print(computer.make_computations())
print(smartphone.use_gps('GeekTech'))
print(phone.call('0551154054', 1))

print(computer == smartphone)
print(computer > smartphone)
print(computer < smartphone)
print(computer != smartphone)
