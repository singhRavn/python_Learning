'''
this is creational design pattern that allows an interface or a class to create an object,
but let subclasses decide ehich class or objecy to instantiate.
Here, objects are created exposing the logic to client and for creating the new type of object, the client uses
the same common interface.
'''


# Python Code for factory method 
# it comes under the creational 
# Design Pattern

class FrenchLocalizer:
    def __init__(self):        
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

class SpanishLocalizer:

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}

    def localize(self, msg):
        return self.translations.get(msg, msg)

class EnglishLocalizer:
    def localize(self, msg):
        return msg

def Factory(language ="English"):
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }

    return localizers[language]()

if __name__ == "__main__":

    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")

    message = ["car", "bike", "cycle"]

    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))
