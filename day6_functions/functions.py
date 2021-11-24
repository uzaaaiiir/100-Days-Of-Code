def newFunction(inputA, inputB):
    '''(obj,obj)->obj
    Function takes two objects of the same type as input.
    Returns the objects concatenated.
    Precondition: objects are of the same type
    '''
    # Body of Fuction
    C = inputA + inputB
    return C

inputA = 5
inputB = 5
print(f"{inputA} + {inputB} = \n{newFunction (inputA, inputB)}")
print()

inputA = 'Hello'
inputB = 'World'
print(f"{inputA} + {inputB} = \n{newFunction(inputA, inputB)}")
print()

inputA = ['hello', 55, True]
inputB = ['world', 11, False, [1,2,3]]
print(f"{inputA} + {inputB} = \n{newFunction(inputA, inputB)}")
print()