print("market store tiket")


print('first product')
product=input()
numero=int(input('first product price:'))
print('second product')
product=input()
numero2=int(input('second product price:'))
print('third product')
product=input()
numero3=int(input('third product price:'))
print('fourth product')
product=input()
numero4=int(input('fourth product price:'))
print('fifth product')
product=input()
numero5=int(input('fifth product price:'))


resultado=numero+numero2+numero3+numero4+numero5
print('subtotal :', resultado)

resultadoo = resultado*.16
print('iva:', resultadoo)

resultadooo= resultado + resultadoo
print ('total', resultadooo)

print("thanks for your purchasing")