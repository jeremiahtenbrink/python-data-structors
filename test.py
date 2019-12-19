class Human:
    def __init__(self, first,last,age):
        self.first = first
        self.last = last
        Human.age = age
man = Human('amir','yunas', 37)
women = Human('april', 'june', 42)
print(man.first)  #outputs 'amir'
print(man.age) #outputs '37'
print(women.first) #output 'april'
print(women.age) #outputs '42'