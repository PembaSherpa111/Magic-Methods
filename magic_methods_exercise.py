class Astronaut():
    """Astronaut Class"""
    def __init__(self,name,flight_hr,status):
        self._name = name
        self._flight_hr = flight_hr
        self._status = status

    def __gt__(self,other):
        print('__gt__ called - self: (%s), other: (%s)' % (self,other))
        if self._flight_hr > other._flight_hr:
            print(True)
        else:
            print(False)
    
    def __ge__(self,other):
        print('__ge__ called - self: (%s), other: (%s)' % (self,other))
        if self._flight_hr >= other._flight_hr:
            print(True)
        else:
            print(False)

    def __eq__(self,other):
        print('__eq__ called - self: (%s), other: (%s)' % (self,other))
        if self._flight_hr == other._flight_hr:
            print(True)
        else:
            print(False)
    
    def __str__(self):
        return '%s, %s' % (self._name,self._status)


import csv 
astronauts = []
with open('astronauts.csv') as csvfile:
    for line in csv.DictReader(csvfile):
        astronauts.append(line)

astronaut = [Astronaut(each_astronaut['Name'], int(each_astronaut['Space Flight (hr)']), each_astronaut['Status']) for each_astronaut in astronauts]

for each_astronaut in astronaut:
    print(each_astronaut)

print('\n============================\n')
astronaut[20] > astronaut[55]

