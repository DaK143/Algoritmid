def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#Kui n on väiksem või võrdne nulliga, tagastatakse 0, sest Fibonacci jada nullindaks elemendiks on 0. Kui n võrdub 1, tagastatakse 1, kuna Fibonacci jada esimene element on 1. Kui n on suurem kui 1, kutsub funktsioon ennast rekursiivselt kaks korda: fibonacci(n - 1) ja fibonacci(n - 2). Need kaks kutsungit tagastavad vastavalt (n-1)-nda ja (n-2)-nda Fibonacci numbri. Need arvud liidetakse, et saada n-nda Fibonacci numbri väärtus.
#Rekursiivne Fibonacci funktsioon on lihtne ja intuitiivne lahendus Fibonacci arvude leidmiseks, kuid suurte n väärtuste korral võib see olla ebaefektiivne, kuna teostab palju korduvaid arvutusi.