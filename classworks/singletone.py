class Singletone:

    _instance = None  # Keep instance reference

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


class A(Singletone):
    _name = None

    def __init__(self, name):
      self._name = name

    def get_name(self):
      return self._name
    
    def set_name(self, name):
      self._name = name

a1 = A('1')
a2 = A('2')

print(a1 is a2)
print(a1.get_name())
import sys
print(sys.version)