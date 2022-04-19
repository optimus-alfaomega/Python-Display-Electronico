display =[
[
'###',
'# #',
'# #',
'# #',
'###',
],
[
'  #', 
'  #',
'  #',
'  #',
'  #',  
],
[
' ###',
'   #',
' ###',
' #'  ,
' ###',
],
[ 
' ###',
'   #',
' ###',
'   #',
' ###',
],
[ 
'# # ', 
'# # ',
'### ',
'  # ', 
'  # ',
],    
[
'###',
'#  ' ,
'###',
'  #',
'###',
], 
[
'###',
'#  ',
'###',
'# #',
'###',
], 
[
'### ',
'  # ',
'  # ',
'  # ',
'  # ',
], 
[
'###',
'# #',
'###',
'# #',
'###',  
],
[
'###',
'# #',
'###',
'  #',
'###',
],
]


#print(display)


entrada=input("digite el numero para mostrar")
for i in range(5): #cantidad de renglones de los numeros
    espacio=" "
    for digito in entrada:
        digito =int(digito)
        espacio += display[digito][i]
        espacio += " "
    print(espacio)



