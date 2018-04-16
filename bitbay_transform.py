import csv
import os
import sys

# Transformuje historie operacji do CVS

def wczytaj_plik(nazwa_pliku):
    print("wczytuje plik: {}".format(nazwa_pliku))
    num_lines = 0
    plik = open(nazwa_pliku, 'r')

    #for 0:4
    ## wczytaj linie
    #usun \n
    #wyrzuc linie CSV
    plik.close()

def njoin(filename, outfn="", n=4, linesuffix=" "):
    if not outfn:
        outfn = filename + ".join"
    with open(filename) as infh, open(outfn, "w") as outfh:
        nline = 0
        for line in infh:
            if nline % n != n-1:
                line = line.rstrip() + linesuffix
            outfh.write(line)
            nline += 1


def lista_plikow(argumenty):
    if(len(argumenty)>1):
        for i in range(1,len(argumenty)):
            #wczytaj_plik(argumenty[i])
            njoin(argumenty[i], "outfile1.csv", 4, ";")
    else:
        print("Za malo argumentow! Musisz podac conajmniej 1 plik wejsciowy!")

lista_plikow(sys.argv)


