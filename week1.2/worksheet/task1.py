import sys
try:
    grade = int(input('enter your grade '))
    if grade >= 70 and grade <=100:
        print(grade,'is a distinction')
    elif grade >= 40 and grade <=69:
        print(grade,'is a pass')
    elif grade >= 0 and grade <=40:
        print(grade,'is a fail')
    else:
        sys.exit('Error: grade must be an integer between 0 and 100')
except:
    sys.exit('Error: grade must be an integer between 0 and 100')
