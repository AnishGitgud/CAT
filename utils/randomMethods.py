import random

class random_generator:
    def __init__(self):
        pass

    def randInt(a:int, b:int):
        return random.randint(a, b)
    
    def rand2Dig():
        return random.randint(10,99)
    
    def rand3Dig():
        return random.randint(100,999)
    
    def randArr(arrSize:int, a:int, b:int):
        arr = []
        for i in range(0, arrSize):
            arr.append(random.randint(a,b))
        return arr
    
    def rand2Arr(arrSize:int):
        arr = []
        for i in range(0, arrSize):
            arr.append(random.randint(10,99))
        return arr
    
    def rand3Arr(arrSize:int):
        arr = []
        for i in range(0, arrSize):
            arr.append(random.randint(100,999))
        return arr
    
    def randUniq2Arr(arrSize: int):
        arr = random.sample(range(10,100), arrSize)
        return arr
    
    def randUniq3Arr(arrSize: int):
        arr = random.sample(range(100,1000), arrSize)
        return arr
    
    def randDec3():
        return round(random.uniform(0.001, 0.999), 3)