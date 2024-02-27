'''
Make an array of objects (an array that will have objects)to store the student information andaccess it as hard-coded.

Information to store: 
    Name, age, registration number, course, favorite programming languages (should be an array), Marks of 5 different subjects (should be an object).
                
The operations to perform:
    Display every single property of any student.
    Display the first and last favorite programming language of any student.
    Display the marks of any 2 subjects of any student.
'''

details=[
    {
        'Name':'Ali',
        'age':21,
        'reg_num':'22112',
        'course':'python',
        'fav_prog_lang':['HTML','CSS','Java Script','Python'],
        'marks':{
            'English':95,
            'Math':98,
            'Physics':100,
            'Pak studies':60,
            'Urdu':70
        }
    },
        {
        'Name':'Akram',
        'age':18,
        'reg_num':'22113',
        'course':'app development',
        'fav_prog_lang':['C','C++','Java','Python'],
        'marks':{
            'English':100,
            'Math':94,
            'Physics':89,
            'Pak studies':92,
            'Urdu':79
        }
    },
        {
        'Name':'Ahmed',
        'age':20,
        'reg_num':'22114',
        'course':'web development',
        'fav_prog_lang':['HTML','CSS','Java Script','php'],
        'marks':{
            'English':99,
            'Math':80,
            'Physics':60,
            'Pak studies':80,
            'Urdu':75
        }
    }
]
# accessing every single property
print(f'Name: {details[1]['Name']}')
print(f'Age: {details[1]['age']}')
print(f'Registeration Number: {details[1]['reg_num']}')
print(f'Course: {details[1]['course']}')

print(f'Favorite programming Languages: {details[1]['fav_prog_lang']}')
print(f'Marks: {details[1]['marks']}')

# Displaying first and last favorite programming language of any student.
print(f'first favorite programming language: {details[1]['fav_prog_lang'][0]}')
print(f'last favorite programming language: {details[1]['fav_prog_lang'][-1]}')

# Displaying the marks of any 2 subjects of any student.
print(f'English : {details[1]['marks']['English']}')
print(f'Math : {details[1]['marks']['Math']}')
print(f'Physics : {details[1]['marks']['Physics']}')
print(f'Urdu : {details[1]['marks']['Urdu']}')

