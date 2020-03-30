# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import pytest

import Lab22


class Test_Part1:

    def test_class_named_Car(self):
        assert 'Car' in dir(Lab22), 'Did you name your class Car?'

    def test_attributes_created(self):
        student = Lab22.Car('Toyota', 'Corolla', 2017, 'black')
        assert len(dir(student)) >= 30, 'Did you add 4 new attributes to the Car class?'

class Test_Part2:
    entries = ['Toyota', 'Corolla', 2017, 'black']

    def test_repr_method_created(self):
        student = Lab22.Car(*self.entries)
        assert '__main__' not in repr(student), 'Did you define a repr method that returns something?'

    def test_str_method_created(self):
        student = Lab22.Car(*self.entries)
        assert '__main__' not in str(student), 'Did you define a str method that returns something?'
        assert str(student) != repr(student), 'It looks like your repr and str are both returning the same thing. Either you did not define a str method, or you should make it output a more user friendly way of envisioning a vehicle like this.'

class Test_Part3:
    entries = [
            ['Toyota', 'Corolla', 2017, 'black'],
            ['Toyota', 'Camery', 2017, 'black'],
            ['Toyota', 'Corolla', 2018, 'black'],
            ['Toyota', 'Corolla', 2017, 'white'],
            ['Honda', 'Corolla', 2017, 'black'],
            ]

    def test_identical_vehicles(self):
        A = Lab22.Car(*self.entries[0])
        B = Lab22.Car(*self.entries[0])
        assert A == B, 'Two identical cars are not showing up as being the same. Are you missing some logic somewhere?'

    def test_dissimilar_vehicles(self):
        A = Lab22.Car(*self.entries[0])
        B = Lab22.Car(*self.entries[1])
        C = Lab22.Car(*self.entries[2])
        D = Lab22.Car(*self.entries[3])
        E = Lab22.Car(*self.entries[4])
        assert A != B, 'Different cars are showing up the same. Are you comparing the model?'
        assert A != C, 'Different cars are showing up the same. Are you comparing the year of manufactoring?'
        assert A != D, 'Different cars are showing up the same. Are you comparing the color?'
        assert A != E, 'Different cars are showing up the same. Are you comparing the make of the car?'


class Test_Part4:

    def test_greater_than(self):
        A = Lab22.Car('Toyota', 'Corolla', 2017, 'black')
        B = Lab22.Car('Toyota', 'Camery', 2020, 'black')
        C = Lab22.Car('Toyota', 'Tacoma', 2010, 'black')
        D = Lab22.Car('Honda', 'Ridgeline', 2015, 'white')
        greaterthan = [False, True, True]
        for car,sol in zip([B,C,D],greaterthan):
            assert (A > car) == sol

    def test_less_than(self):
        A = Lab22.Car('Toyota', 'Corolla', 2017, 'black')
        B = Lab22.Car('Toyota', 'Camery', 2020, 'black')
        C = Lab22.Car('Toyota', 'Tacoma', 2010, 'black')
        D = Lab22.Car('Honda', 'Ridgeline', 2015, 'white')
        lessthan = [True, False, False]
        for car,sol in zip([B,C,D],lessthan):
            assert (A < car) == sol
