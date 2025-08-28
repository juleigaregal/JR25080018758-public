class Course:
    def __init__(self, name="Fundamentals of Computer Science", contact_website= "www.hyperiondev.com"):
    # Class attribute for the course name
        self.name = name

    # Class attribute for the contact website
        self.contact_website =contact_website

    # Method to display contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
    
    def location(self):
        print("Head office location is in Cape Town")

class Oopcourse(Course):
    def __init__(self, description="OOP Fundamentals", trainer="Mr Anon A. Mouse"):
        super().__init__()
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
       print(f"Course Description: {self.description}\nThe trainer is {self.trainer}")


    def show_course_id(self):
        print("The course id is #12345")

        
        
# Example usage:
# Create an instance of the Course class
course = Course()
oop = Oopcourse()

# Call the contact_details method to display contact information
course.contact_details()
oop.trainer_details()
oop.show_course_id


