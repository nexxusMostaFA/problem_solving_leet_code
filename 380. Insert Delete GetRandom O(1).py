import random


class RandomizedSet(object):
     def __init__(self):
        self.data = []

     def insert(self, val):
          if val in self.data:
              return False
          self.data.append(val)

     def delete(self , val):
        if val in self.data:
            self.data.remove(val)
            return True
        else:
            return False


     def getRandom(self):
        return random.choice(self.data)