class phone:
    def call(self):
        print("you can call")
    def message(self):
        print("you can message")
        print("message please")
    def camera(self):
        print("you can take photos")
class samsung(phone):
    def call(self):
        print("You can call")

    def photo(self):
        print("You can take photos")
    def message(self):
        print("You can message")
class itel:
    def tv(self):
        print("Turn on the TV")
        print("Turn up the volume")
s = samsung()
s.message()
s.photo()
s.camera()
s.message()
print( issubclass(itel,phone))
print(issubclass(itel,phone))
print(isinstance(itel,phone))