import os
print('Processing')
for a in range(31):
    path = os.getcwd() + '\\python\\Day ' + str(a + 1) + '\\'
    if not os.path.isdir(path):
        os.mkdir(path)
    
        for i in range(2):
            with open(path + 'exercise_'+str(i+1)+'.txt', 'x') as file:
                file.write("Here you should paste the exercise 'your puzzle input'\n")
            with open(path + 'exercise_'+str(i+1)+'.py', 'x') as file:
                file.write("# Here you can code the solution\n")
    else: 
        print('Debe borrar las carpetas existentes en "python"')
        break 
    
print('Operation Finished')