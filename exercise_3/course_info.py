#   Course Infomation
#   Mario Lastra (U43655957)
#   This script will give the user details of the selected course.

courses = ("COP 2510", "ENG 3000L", "MAC 2281", "MUH 3016", "PHY 2048")

course_instuctors = {
    courses[0] : "S. Small",
    courses[1] : "J. Anderson",
    courses[2] : "A. Makaryus",
    courses[3] : "A. Wilkins",
    courses[4] : "G. Pradhan"
}

course_times = {
    courses[0] : "MW 12:30pm – 1:45pm",
    courses[1] : "TR 11:00am – 12:15pm",
    courses[2] : "MW 9:30am – 10:45am",
    courses[3] : "Online Asynchronous",
    courses[4] : "TR 5:00pm – 6:15pm"
}

#   Get user input
user_input = input("Enter a course number: ")

#   Check 
for x in courses:
    if user_input == x:
        print("The course details are:")
        print("Course Name: {}".format(x))
        print("Instructor: {}".format(course_instuctors[x]))
        print("Class Times: {}".format(course_times[x]))
        exit

#   Check if input is not in courses
if user_input not in courses:
    print("{} is an invalid course number.".format(user_input))