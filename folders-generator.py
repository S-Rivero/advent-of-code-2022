import os
print('Processing')
for a in range(31):
    path = os.getcwd() + '\Day ' + str(a + 1)
    os.mkdir(path)
    with open(path + '\exercise_1.txt', 'x') as file:
        file.write("Here you should paste the exercise 'your puzzle input'\n")
    with open(path + '\exercise_2.txt', 'x') as file:
        file.write("Here you should paste the exercise 'your puzzle input'\n")
    
    # Default: JS is commented

    # Comment the following 4 lines if you use Javascript
    with open(path + '\exercise_1.py', 'x') as file:
        file.write("# Here you can code the solution\n")
    with open(path + '\exercise_2.py', 'x') as file:
        file.write("# Here you can code the solution\n")
    
    # Comment the following 4 lines if you use Python
    """
    with open(path + '\exercise_1.js', 'x') as file:
        file.write("// Here you can code the solution\n")
    with open(path + '\exercise_2.js', 'x') as file:
        file.write("// Here you can code the solution\n")
    """

print('Operation Finished')