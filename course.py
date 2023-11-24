class Course:
    def __init__(self, title, instructor, price, lectures):
        self.title = title
        self.instructor = instructor
        self.price = price
        self.lectures = lectures
        self.users = []
        self.ratings = 0
        self.avg_rating =0

    def __str__(self):
        return '{} by {}'.format(self.title, self.instructor)
        
    def new_user_enrolled(self, name):
        self.users.append(name)

    def recieved_a_rating(self, rating):
        self.avg_rating = (self.avg_rating * self.ratings + rating)/(self.ratings+1)
        self.ratings += 1

    def show_details(self):
        return '{} is taught by {}. This course costs {} dollars and has {} lectures. Users: {} Average Rating: {}'.format(self.title, self.instructor, self.price, self.lectures, self.users, self.avg_rating)

class VideoCourse(Course):
    def __init__(self, title, instructor, price, lectures, length_video):
        super().__init__(title, instructor, lectures, price)
        self.length_video = length_video

    def show_details(self):
        super().show_details()
        print(("Length of Video: {} minutes").format(self.length_video))
        
class PdfCourse(Course):
    def __init__(self, title, instructor, price, lectures, pages):
        super().__init__(title, instructor, lectures, price)
        self.pages = pages

    def show_details(self):
        super().show_details()
        print(("Number of Pages: {}").format(self.pages))

x = VideoCourse('Math', 'Mr. Bob', 14, 20, 60)
print(str(x))
x.new_user_enrolled('Steve')
x.new_user_enrolled('Alex')
x.new_user_enrolled('Jerry')
x.recieved_a_rating(7)
x.recieved_a_rating(9)
x.recieved_a_rating(5)
print(x.show_details())

#Can cook noodles
#Can cook pasta
#Can cook pasta
#Can cook pasta
#Can cook noodles
#Can cook butter chicken

#I am a Person
#I am a Student
#I am a Person
#I am a Teacher
#I am a Teaching Assistant
