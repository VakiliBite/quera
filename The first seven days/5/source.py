class Foo:
    def __init__(self):
        self._x = 0
        
    @property
    def x(self):
        return int(self._x)
        
    @x.setter
    def x(self , value):
        
        if value >= 0 :
            self._x = value%100
        elif value < 0 :
            self._x = -1
