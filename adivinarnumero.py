import random 

def guess(x):
    errores = 0
      #esto es para inportar numeros aleatorios
    guess = 1 #eso es popr si el programa pone un cero el while se ejecute igualmente ya que 0 es false 
    while guess :
        random_number = random.randint(1, x)
        guess = int(input(f'adivina el numero entre 1 y {x} \r\n' )) 
        if guess < random_number:
            print ('lo siento,  numero muy bajo .... ')
            errores =+ 1
        elif guess > random_number:
            
            print('lo siento , numero demasiado alto... ')
            errores += 1
        else:
        
            print(f'felicitaciones has adivinado el numero {random_number}  correctamente  ')
            print(f'tuviste {errores} errores antes en ganar .... gg ')

#ahora vamos a hacer que la computadora adivine el numero

def computer_guess(x): #la x se pone para que luego le podamos agregar unavalor numerico
    low = 1
    high = x  #deifinimos que tan bajo y tan alto va a ser la adivinanza 
    feedback = ''
    while feedback != 'c':
        if low != high: 
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'es {guess} muy alto (H), muy bajo (L), o es correcto(C)?? ')
        if feedback == 'h':
            high == guess - 1
        if feedback == 'l':
            low = guess + 1
            
    print(f'siuuu ;a computadora adivino tu numero {guess} ')




#guess(12)#aca le ponemos el valor que queremos adivinar wntre 0 y 10  
guess(100)