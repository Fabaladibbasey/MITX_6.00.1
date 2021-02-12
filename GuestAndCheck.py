


 ==============================================================================
 # finding the cube root root 
 cube = 18
 
 for guess in range(abs(cube)+1):
     if guess ** 3 == abs(cube):
         if cube < 0:
             guess = -guess
         print('Cube root of ' + str(cube) + ' is ' + str(guess))
         break
       
     elif guess**3 > abs(cube):
         print(cube, 'is not a perfect cube')
         break   
 ==============================================================================

print('hello world this python spyder edito is behaving some how!')