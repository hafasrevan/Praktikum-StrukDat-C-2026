class Resonator:
    Role = ""
    def __init__(self,name,weapon,attribute):
        self.name = name
        self.weapon = weapon
        self.attribute = attribute

    def introduction(self):
        print(f"Hello my fav resonator is {self.name}, the weapon he/she use is {self.weapon}, his/her attribute is {self.attribute}, what about yours?" )

    def changeAttribute(self,new_attribute):
        old = self.attribute
        self.attribute = new_attribute
        print (f"old attribute: {old}")
        print (f"new attribute: {new_attribute}")


char1 = Resonator("rover","sword","havoc")
char2 = Resonator("carlotta","pistol","ice")
char3 = Resonator("Zani","gautlet","spectro")
Resonator.Role = "Main Damage Dealer"

char1.changeAttribute("spectro")

print()
char1.introduction()
print()
print(char1.name)
print(char1.weapon)
print(char1.attribute)
print(char1.Role)
print()
print(char2.name)
print(char2.weapon)
print(char2.attribute)
print(char2.Role)
print()
print(char3.name)
print(char3.weapon)
print(char3.attribute)
print(char3.Role)
print()
