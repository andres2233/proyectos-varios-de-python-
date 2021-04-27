import random as rd 
 
palabra = ['pollo', 'queso', 'lechuga',  'patata']
pal = rd.randint(0, len(palabra) -1) # aca me va a desri un numero que luego agregarmos para elger la palabra al azar 
pal_elegi = palabra[pal].upper()


prim_letr_pala= pal_elegi[0]
ultim_letr_palab= pal_elegi[-1]
espacios = len(pal_elegi)-2
espacio = espacios*'_'


palbra_a_adivinar = prim_letr_pala + espacio  + ultim_letr_palab 
print (palbra_a_adivinar)

