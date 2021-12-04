Eingeben = input()
Eingeben = int(Eingeben)
revs_nummer = 0
if (Eingeben > 0 and Eingeben < 10000000000000000000):

       while (Eingeben > 0):

            remainder = Eingeben % 10
            revs_nummer = (revs_nummer * 10) + remainder
            Eingeben = Eingeben // 10


     

print (revs_nummer)
