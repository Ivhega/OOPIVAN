# add your name to the print statement below
print("Hello, my name is " + "Ivan")


class Person:
    def __init__(self, personID, firstName, lastName, favoriteColour, age, isWorking):
        self.person_ID = personID
        self.first_Name = firstName
        self.last_Name = lastName
        self.favorite_Colour = favoriteColour
        self.age = age
        self.isWorking = isWorking

    def change_favorite_colour(self, new_color):
        self.favorite_Colour = new_color

    def get_age_in_ten_years(self):
        # print(f"Age in ten year will be: {self.age+10}")
        return f"Age in ten year will be: {self.age+10}"


a = Person(915433, "Ivan", "Hernandez", "Blue", 36, "Not")

age_in_ten = a.get_age_in_ten_years()
