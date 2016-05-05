## Realizado por : Diego Lozano , Ivan Herrera , Ximena Medina

#   En la carpeta se encuentran cuatro archivos de audio con los cuales se prueba el programa,
#  o se pueden copear y pegar a la carpeta los archivos con los cuales desea probar el mismo



#importamos las librerias y clases necesarias

from Tkinter import *
import pyaudio
import sys
import getopt
import struct
import wave

import numpy as np
from Reproducir import Reproducir
from repro import Reproo








def main():

        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100
        status = False
        print status
        root = Tk()
        root.title("Reproduciones")

      ## Campo de texto y boton reproduccion 1
        label = Label(root, fg="black")
        label.pack()
        label.grid(row=1,column=2)
        label.config(text="Nombre o ruta (Archivo 1)")
        Nombre1 = "texto"
        Archivo = Reproducir(Nombre1)

        e1 = Entry(root)
        e1.grid(row=2,column=2,)


## llamamos las funciones respetivas de la clase Reproducir para que el audio 1 suene
        def init_audio():
            Archivo.ruta = e1.get()
            Argumentos = Archivo.abrir()
            Archivo.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo.rep()

        rep1=Button(root,text='Reproducir audio 1', command=init_audio)
        rep1.grid(row=3,column=3)




## Campo de texto y boton de reproducir 2
        label2 = Label(root, fg="black")
        label2.pack()
        label2.grid(row=4,column=2)
        label2.config(text="Nombre o ruta (Archivo 2 ) ")
        Nombre2 = "texto"
        Archivo2 = Reproducir(Nombre2)

        e2 = Entry(root)
        e2.grid(row=5,column=2)

 ## llamamos las funciones respetivas de la clase Reproducir para que el audio 2 suene
        def init_audio2():
            Archivo2.ruta = e2.get()
            Argumentos = Archivo2.abrir()
            Archivo2.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo2.rep()

        rep2=Button(root,text='Reproducir audio 2', command=init_audio2)
        rep2.grid(row=6,column=3)

## Campo de texto y boton reproduccion 3
        label3 = Label(root, fg="black")
        label3.pack()
        label3.grid(row=7,column=2)
        label3.config(text="Nombre o ruta (Archivo 3)")
        Nombre3 = "texto"
        Archivo3 = Reproducir(Nombre3)

        e3 = Entry(root)
        e3.grid(row=8,column=2,)



## llamamos las funciones respetivas de la clase Reproducir para que el audio 3 suene
        def init_audio3():
            Archivo3.ruta = e3.get()
            Argumentos = Archivo3.abrir()
            Archivo3.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo3.rep()

        rep3=Button(root,text='Reproducir audio 3', command=init_audio3)
        rep3.grid(row=9,column=3)

       ## Campo de texto y boton reproduccion 1
        label4 = Label(root, fg="black")
        label4.pack()
        label4.grid(row=10,column=2)
        label4.config(text="Nombre o ruta (Archivo 4)")
        Nombre4 = "texto"
        Archivo4 = Reproducir(Nombre4)

        e4 = Entry(root)
        e4.grid(row=11,column=2,)


        # # ## llamamos las funciones respetivas de la clase Reproducir para que el audio 1 suene
        def init_audio4():
            Archivo4.ruta = e4.get()
            Argumentos = Archivo4.abrir()
            Archivo4.inicio(Argumentos[0],Argumentos[1],Argumentos[2])
            Archivo4.rep()

        rep4=Button(root,text='Reproducir audio 4', command=init_audio4)
        rep4.grid(row=15,column=3)



        def sumar(f, A, p, x):


            channels = f.getnchannels()
            sampwidth = f.getsampwidth()
            framerate = f.getframerate()
            nframes = f.getnframes()
            comptype = f.getcomptype()
            compname = f.getcompname()


            tamanof =  f.getnframes()
            tamanoA =  A.getnframes()
            tamanop =  p.getnframes()
            tamanox =  x.getnframes()
            array1 = []
            array2 = []
            array3 = []
            array4 = []

            for i in range(0, tamanoA):
                datos1 =  struct.unpack("<h", A.readframes(1))
                array1.append(int(datos1[0]))
            for i in range(0, tamanof):
                datos2 =  struct.unpack("<h", f.readframes(1))
                array2.append(int(datos2[0]))
            for i in range(0, tamanop):
                datos3 =  struct.unpack("<h", p.readframes(1))
                array3.append(int(datos3[0]))
            for i in range(0, tamanox):
                datos4 =  struct.unpack("<h", x.readframes(1))
                array4.append(int(datos4[0]))
            wavearray=[]


            if (tamanoA >= tamanof) and tamanoA>tamanop and tamanoA > tamanox:
                for i in range(0, tamanoA):
                    wavearray.append(array1[i])
                for i in range(0,tamanof):
                    wavearray[i]=wavearray[i]+array2[i]
                for i in range(0,tamanop):
                    wavearray[i]=wavearray[i]+array3[i]
                for i in range (0, tamanox):
                    wavearray[i]=wavearray[i]+array4[i]


            if (tamanof >= tamanoA)and tamanof>tamanop and tamanof>tamanox:
                for i in range(0, tamanof):
                    wavearray.append(array2[i])
                for i in range(0,tamanoA):
                    wavearray[i]=wavearray[i]+array1[i]
                for i in range(0,tamanop):
                    wavearray[i]=wavearray[i]+array3[i]
                for i in range (0, tamanox):
                    wavearray[i]=wavearray[i]+array4[i]

            if (tamanop >= tamanoA) and (tamanop > tamanof) and tamanop>tamanox:
                for i in range(0, tamanop):
                    wavearray.append(array3[i])
                for i in range(0,tamanof):
                    wavearray[i]=wavearray[i]+array2[i]
                for i in range(0,tamanoA):
                    wavearray[i]=wavearray[i]+array1[i]
                for i in range (0, tamanox):
                    wavearray[i]=wavearray[i]+array4[i]

            if (tamanox >= tamanoA) and (tamanox > tamanof) and tamanox>tamanop:
                for i in range(0, tamanop):
                    wavearray.append(array4[i])
                for i in range(0,tamanof):
                    wavearray[i]=wavearray[i]+array2[i]
                for i in range(0,tamanoA):
                    wavearray[i]=wavearray[i]+array1[i]
                for i in range (0, tamanop):
                    wavearray[i]=wavearray[i]+array3[i]
            for i in range(0,len(wavearray)):
                if wavearray[i]>32767:
                    wavearray[i]=32767
                elif wavearray[i]<-32767:
                    wavearray[i]=-32767

            f.close()
            A.close()
            p.close()
            x.close()
            data=np.asarray(wavearray)
            sum=Reproo(CHUNK)
            sum.iniciosum(data)
            sum.cerrarsum()






# Funcion en la cual obtenemos los datos de los cuatro archivos llamamos la funcion sumar
# y reproduce los cuatro audios al tiempo


        def trs():

            card = 'default'

            opts, args = getopt.getopt(sys.argv[1:], 'c:')
            for o, a in opts:
                if o == '-c':
                    card = a
            n1=e1.get()
            n2=e2.get()
            n3=e3.get()
            n4=e3.get()
            f = wave.open(n1, 'rb')
            A = wave.open(n2, 'rb')
            p = wave.open(n3, 'rb')
            x = wave.open(n4, 'rb')
            sumar(f, A, p,x)







        tr=Button(root,text='PLAY',command=trs)
        tr.grid(row=18,column=2)





        salir=Button(root,text='Salir', command = root.destroy)
        salir.grid(row=23,column=3)


        a = BooleanVar(root)
        a.set(False)

        root.mainloop()



if __name__ == '__main__':
    main()
