# Infinite Loop
def infiniteLoop():
    '''(None)->None
    Function prints i an infinite number of times.
    '''
    i = 1
    while i > 0:
        print(i)

# While loop using iteration variable 
def blastoff():
    '''(None)->None
    Function prints 10,9,8,7,6,5,4,3,2,1,Blastoff!
    '''
    i = 10
    while i > 0:
        print(i)
        i-=1
    print("Blastoff!")

blastoff()
print()