#Python Exercise 1
#Give users information about their specfic courses, info such as teacher, times, and name.

#Driver- Tilak Patel- UID-U32922919
#Navigator- Mario Lastra UID-U43655957

course = ('COP 2510', 'EGN 3000L', 'MAC 2281', 'MUH 3016', 'PHY 2048')
course_name = {course[0]:'Programming Concepts',course[1]:'Foundations of Engineering Lab', course[2]:'Calculus 1', course[3]:'Survey of Jazz', course[4]:'General Physics'}
course_inst = {course[0]:'S. Small', course[1]:'J. Anderson', course[2]:'A. Makaryus', course[3]:'A. Wilkins', course[4]:'G. Pradhan'}
course_time = {course[0]:'MW 12:30pm - 1:45pm', course[1]:'TR 11:00am – 12:15pm', course[2]:'MW 9:30am – 10:45am', course[3]:'online asynchronous', course[4]:'TR 5:00pm - 6:15pm'}

user_input = input('Enter a course number: ')

for x in course:
    if user_input == x:
        print('The course details are: ')
        print('Course Name:', course_name[x])
        print('Instructor:', course_inst[x])
        print('Class Times:', course_time[x])
if user_input not in course:
    print(user_input, 'is an invalid course number.')
        
