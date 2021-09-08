#Matías Alejandro González Moroso
#Laboratorio N°2 de Seguridad Informática

import hashlib as hlib
from time import sleep
print("\n" *40)

#Definicion del ALfabeto a utilizar
alf = "abcdefghijklmnopqrstuvwxyz"

#Pedimos un mensaje al Usuario
mensaje = input("Ingrese el mensaje que quiera encriptar\n")
mensaje.lower()
t = open("mensajedeentrada.txt",'w')
t.write(mensaje)
t.close()
hashA = hlib.sha1(mensaje.encode())
hashB = hashA.hexdigest()
print("\n" *40)
print("El Hash del mensaje es:", hashB)
sleep(2)
#####################################################################
encriptacion = []
#ENCRIPTACIÓN
def rot_cifrado(mensaje, x):
    for i in range(len(mensaje)):
        if mensaje[i] not in alf:
            encriptacion.append(mensaje[i])
        else:
            a = alf.index(mensaje[i])
            d = a+x
            if d>=len(alf):
                d = d-26
            traduccion = alf[d]
            encriptacion.append(traduccion)
    return print("encriptando mensaje...")

#DESENCRIPTACIÓN
def rot_descifrado(mensaje, x):
    for i in range(len(mensaje)):
        if mensaje[i] not in alf:
            encriptacion.append(mensaje[i])
        else:
            a = alf.index(mensaje[i])
            d = a-x
            if d>=len(alf):
                d = d+26
            traduccion = alf[d]
            encriptacion.append(traduccion)
    return print("desencriptando mensaje...")
#####################################################################
ciclo = True
while ciclo:
    print("\n" *40)
    asd = int(input("Selecione una opcion \n(1) Codificar \n(2) Cerrar Programa\n"))
    print("\n" *40)
    if asd==1:
        #rot 5
        #Cifrando mensaje con rot 5
        rot_cifrado(mensaje, 5) 
        #vigenere
        #Cifrando mensaje con vigenere
        contraseña = "mysupersecretpassword"
        encriptacion1 = []
        contador = 0 
        for i in range(len(encriptacion)):
            if encriptacion[i] not in alf:
                encriptacion1.append(encriptacion[i])
            else:
                a = alf.index(encriptacion[i])
                b = alf.index(contraseña[contador])
                d = a+b
                if d>=len(alf):
                    d = d-26
                traduccion = alf[d] 
                encriptacion1.append(traduccion)
            contador = contador + 1
            if contador == len(contraseña):
                contador = 0
        print("encriptando mensaje...")
        #rot 18
        #Cifrando mensaje con rot 18
        mensaje = ''.join(encriptacion1)
        encriptacion = []
        rot_cifrado(mensaje, 18)
        sleep(1)
        print("\n" *40)
        print("El mensaje ya codificado es:")
        print("".join(encriptacion))
        z = open("mensajeseguro.txt",'w')
        z.write("".join(encriptacion))
        z.close()
        sleep(2)
        print("\n" *40)
        hashC = hlib.sha1("".join(encriptacion).encode())
        hashD = hashC.hexdigest()
        print("El Hash del mensaje codificado es:", hashD)
        sleep(3)
        print("\n" *40)
        asd = int(input("Selecione una opcion \n(1) Decodificar \n(2) Cerrar Programa\n"))
        if asd==1:
            print("\n" *40)
            #rot -18
            #Descifrando mensaje con rot -18
            msj = (open("mensajeseguro.txt", "r"))
            mensj = []
            for i in msj:
                mensj.append(i)
                
            mensaje = "".join(mensj)
            encriptacion = []
            rot_descifrado(mensaje, 18)
            #descifrado vigenere
            #Descifrando mensaje con vigenere
            contraseña = "mysupersecretpassword"
            encriptacion1 = []
            contador = 0 
            for i in range(len(encriptacion)):
                if encriptacion[i] not in alf:
                    encriptacion1.append(encriptacion[i])
                else:
                    a = alf.index(encriptacion[i])
                    b = alf.index(contraseña[contador])
                    d = a-b
                    if d>=len(alf):
                        d = d-26
                    traduccion = alf[d] 
                    encriptacion1.append(traduccion)
                contador = contador + 1
                if contador == len(contraseña):
                    contador = 0     
            print("desencriptando mensaje...")
            #rot -5
            #Descifrando mensaje con rot -5:")
            mensaje = ''.join(encriptacion1)
            encriptacion = []
            rot_descifrado(mensaje, 5)
            sleep(1)
            print("\n" *40)
            print("El mensaje ya decodificado es:")
            print("".join(encriptacion))
            sleep(2)
            print("\n" *40)
            hashE = hlib.sha1("".join(encriptacion).encode())
            hashF = hashE.hexdigest()
            print("El Hash del mensaje decodificado es:", hashF)
            sleep(3)
            if hashB==hashF:
                print("\n" *40)
                print("El mensaje inicial NO fue modificado")
            else:
                print("\n" *40)
                print("Vaya!, Parece que ha ocurrido un error y el mensaje ha sido modificado")
            ciclo = False
        elif asd==2:
            ciclo = False

    elif asd==2:
        ciclo = False

    else:
        ciclo
