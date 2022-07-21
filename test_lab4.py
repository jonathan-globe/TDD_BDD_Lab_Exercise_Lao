import pytest

class Calculator:
    def __init__(self, name):
        self.name=name
        
    def add(self,a,b):
        return a+b
        
    def subtract(self,a,b):
        return a-b
        
    def multiply(self,a,b):
        return a*b
        
calc= Calculator('Calc 1')

@pytest.fixture
def base_calculator():
    return Calculator('Base Caculator')
    
def test_lab4_test1(base_calculator):
    print("#1 This calculator's name is " + base_calculator.name)

    #Changing Calculator's Name
    base_calculator.name= "Changed Calculator"
    print("#1 This Calculator's name is: " + base_calculator.name)
    
    assert True

def test_lab4_test2(base_calculator):
    print("#2 This calculator's name is: " +base_calculator.name)
    
    assert True
    
def test_lab4_test3():
    assert calc.subtract(2,2) == 0
    assert calc.subtract(5.5, 3.2) == 2.3
    assert calc.subtract(0,0) == 0
    assert calc.subtract(0,-1) == 1
    assert calc.subtract(-5,-6) == 1
    
def test_lab4_test4():
    assert calc.multiply(2,2) == 4
    assert calc.multiply(5.5, 3.2) == 17.6
    assert calc.multiply(0,0) == 0
    assert calc.multiply(0,-1) == 0
    assert calc.multiply(-5,-6) == 30
    