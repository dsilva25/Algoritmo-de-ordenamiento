#Algoritmo Insercion leyendo datos desde un archivo

def insercion(s):
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
        s[j+1] = val
 
infile = open ("numerosAleatorios.txt", "r") 
file=infile.readlines() 
lista=[]

for linea in file: 
   var=linea.strip() #depurar salto de linea
   x=var 
   lista.append(int(x)) 

infile.close()

## ----------------------- Ejecutamos InsertSort----------------------
insercion(lista)
## ---------------- Escribimos variables en otro txt-----------------
infile2=open('numOrdenados.txt','w')

for linea2 in lista:
   infile2.write(str(linea2)+'\n')

infile2.close()

print ("Archivo numOrdenados.txt generado")