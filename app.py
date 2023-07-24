# add your name to the print statement below
print("Hello, my name is " + "Ivan")

class Person:
    def __init__(self,personID,firstName,lastName,favoriteColour,age,isWorking):
        self.person_ID = personID
        self.first_Name = firstName
        self.last_Name = lastName
        self.favorite_Colour = favoriteColour
        self.age = age
        self.isWorking = isWorking
    def change_favorite_colour(self):
        self.favorite_Colour = "white"
    def get_age_in_ten_years(self):
        print(f"Customer name: {self.age+10}")

a = Person(915433,"Ivan","Hernandez","Blue",36,"Not")
