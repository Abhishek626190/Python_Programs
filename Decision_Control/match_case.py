num=int(input("Enter a number")) 

num=num%2

match(num):
    
    case 0:print("Even Number")
    case 0:print("duplicate number")
    case 1.1:print("float number")
    case"string":print("String ")
    case True:print("Boolean Number")
    case _:print("Odd Number")
    
'''** points to remember:
1.duplicate case is not error in python but first match case will only work
2.case constant can be of any type 
3.match & case are soft keywords not a reserved words
4.break can not be used in match case in python
5.for default case we have to write case _
6.match case is like switch case in python
7.syntax: match expression:
        case constant1:
                  statements
        case constant2:
                  statements
        case constantn:
                  statements
        case _:
               Default Statements
8.only matched case will execute not all case  like other languages(java)
'''
    