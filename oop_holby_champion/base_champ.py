#!/usr/bin/python3
import json



class BaseChamp:

    def __init__(self, name, race, gender, level, exp_level, current_exp,
                total_exp, stats, stat_points):

        self.name = name
        self.race = race 
        self.gender = gender
        self.level = level
        self.exp_level = exp_level
        self.current_exp = current_exp
        self.total_exp = total_exp
        self.stats = stats
        self.stat_points = stat_points

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):

        if type(value) is not str:
            raise ValueError('Name must be a string.')

        if len(value) > 10:
            raise ValueError('Name must be 10 characters max.')

        self.__name = value

    @property
    def race(self):
        return self.__race

    @race.setter
    def race(self, value):
        if type(value) is not str:
            raise TypeError('Race must be a string.')

        if value not in ['Human', 'Elf', 'Dwarf', 'Hobbit', 'Orc']:
            raise ValueError('Race must be one of these: Human, Elf,\
Dwarf, Hobbit, Orc')

        self.__race = value

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if type(value) is not str:
            raise TypeError('Gender must be a string.')

        if value not in ['Male', 'Female', 'Other']:
            raise ValueError('Race must be one of these: Male,\
Female or Other')

        self.__gender = value

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if type(value) is not int:
            raise TypeError('Level must be a number')

        if value > 100:
            self.__level = 100
            print('Max level 100')
        elif value < 0:
            self.__level = 0
            print('Lower level 0')
        else:
            self.__level = value

    @property
    def exp_level(self):
        return self.__exp_level

    @exp_level.setter
    def exp_level(self, value):
        if type(value) is not int:
            raise TypeError('exp_level must be a number')

        self.__exp_level = value

    @property
    def current_exp(self):
        return self.__current_exp

    @current_exp.setter
    def current_exp(self, value):
        if type(value) is not int:
            raise TypeError('current_exp must be a number')

        self.__current_exp = value

    @property
    def total_exp(self):
        return self.__total_exp

    @total_exp.setter
    def total_exp(self, value):
        if type(value) is not int:
            raise TypeError('total_exp must be a number')

        if value < 0:
            raise ValueError('total_exp must be positive')

        self.__total_exp = value


    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, value):
        if type(value) is not dict:
            raise TypeError('Stats must be a dictionary')

        for key, value in value.items():
            if value < 0:
                value[key] = 0
                print(f'{key} must have a positive value')
            elif value > 100:
                value[key] = 100
                print(f'{key} must be less than 100')
        self.__stats = value
 
    @property
    def stat_points(self):
        return self.__stat_points

    @stat_points.setter
    def stat_points(self, value):
        if type(value) is not int:
            raise TypeError('stat_points must be a number')

        if value < 0:
            raise ValueError('stat_points must be positive')

        self.__stat_points = value

    def level_up(self, next_level_exp):
        """Increases the level of the champion and modifies the attributes.

        Attribues:
            next_level_exp (int): The value to set the next exp_level.
        """

        if self.current_exp == self.level:
            self.total_exp += self.level
            self.level += 1
            self.stat_points += 3
            self.current_exp = 0
            self.exp_level = next_level_exp
        else:
            raise Exception('Not enough current_exp for next level')

    def gain_exp(self, value):
        """Increase the champion current_exp.

        Attrbiutes:
            value (int): The number of experience to gain.
        """
        if type(value) is not int:
            raise ValueError('Increase in exp must be a number')
        self.current_exp += value
        print(f"Your current_exp is: {self.current_exp}")

    def death(self):
        """Decreases the current experience of the champion by 50%"""
        self.current_exp /= 2

    def save_character(self):
        """Returns the json represention of the champion"""
        return (json.dumps(self))

    @classmethod
    def load_character(my_str):
        """Returns the python represention of the json string
        Attributes:
            my_str (str): The string containing the json to convert."""
        return (json.loads(my_str))

    def increase_stats(self, stat):

        if type(stat) is not str:
            raise TypeError('Select one of the stats Health, Attack, Defense,\
Magic, Speed')

            self.stats[stat] += self.stat_points
            self.stat_points = 0

test_champ = BaseChamp("Test", "Orc", "Other", 50, 50, 50, 50, {"Health": 50, "Attack": 50, "Defense": 50, "Magic": 50, "Speed": 50}, 3)              
test_champ.level_up(2)
print(test_champ.__dict__)
