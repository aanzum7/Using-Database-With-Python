class PartyAnimal:
    x=0
    def __init__(self):
        print("I am constructed:")
    def party (self):
      self.x =self.x +1
      print('So far:',self.x)


    def __del__(self):
        print("i am distructed:",self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
an =42
print("an contain:",an)
print('Type:',type(an))
print("Dir:",dir(an))


