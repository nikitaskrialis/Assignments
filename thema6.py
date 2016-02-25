import urllib
import json
from pprint import pprint



def main():
    # h lista ayth tha periexei olous tous arithmous pou diabasame apo thn istoselida
    allnums = []
    # kathe thesi ayths ths listas exei thn syxnothta tou arithmou pou antiproswpevei h
    # thesi tou + 1 arithmoi 1 - 80 theseis 0 - 79
    numbers = [0]*80
    date = raw_input('Give a date (dd-MM-yyyy):')
    #print date
    link = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"+date+".json"
    f = urllib.urlopen(link)
    # bazoume to periexomeno tou arxeiou se string apo opou tha kanoume parsing
    myfile = f.read()
    list1 = myfile.split('results":[')
    # to prwto stoixeio ths listas den mas ediaferei
    list1.pop(0)
    # edw bgazoume olous tous arithmous pou exoun klhrwthei kai tous pername sthn
    # lista allnums se morfh arithmwn
    for i in range(len(list1)):
        temp = list1[i].split(']')
        temp.pop()
        temp = temp[0].split(',')
        for j in range(len(temp)):
            allnums.append(int(temp[j]))

    # gemizoume thn lista numbers pou kathe thesh tha exei thn syxnothta tou aritmou
    # ston opoio antistoixei h thesi + 1 px h thesi 29 periexei thn syxnothta tou
    # arithmou 30
    for num in allnums:
        numbers[num-1] += 1

    # ektypwnoume to periexomeno ths listas numbers
    for i in range(len(numbers)):
        num = i+1
        print str(num)+': '+str(numbers[i])


main()
