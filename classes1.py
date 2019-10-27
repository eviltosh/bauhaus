class Point:
    ''' This program shows the distance from the point of origin to the instances
    of the class .


     '''
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def distance_from_origin(self):
        return ((self.x**2)+(self.y**2))**0.5

    def __str__(self):
        return '({0},{1})'.format(self.x,self.y)

p =Point(4,3)
q =Point(6,9)
print(p,'is',p.distance_from_origin(),'from the origin',q,'is',q.distance_from_origin(),
'from the origin')
