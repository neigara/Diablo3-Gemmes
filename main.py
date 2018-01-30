stockR = int(input('Nombre de gemmes Royales en stock : '))
stockISD = int(input('Nombre de gemmes Impériales Sans Defaut en stock : '))
stockI = int(input('Nombre de gemmes Impériales en stock : '))
stockM = int(input('Nombre de gemmes Marquises en stock : '))

needRSD = int(input('\nNbre de gemmes Royales Sans Défaut voulues ? '))

#RSD_possible = equiM//81 #nombre de gemmes Royales Sans Défaut créable avec le stock
equiM = (stockM + stockI*3 + stockISD *9 + stockR*27) #equivalent du stock en nombre de gemme Marquises
needM = needRSD*81 - equiM #gemmes Marquises manquantes

#print ("Il est possible de faire %d gemmes Royales Sans Défaut" % RSD_possible)
if (needM < 1):
    print ("\nVous avez suffisement de gemmes Marquises pour faire %d gemmes Royales Sans Défaut" % needRSD)
else:
    print ("\nIl vous manque %d gemmes Marquises pour faire %d gemmes Royales Sans Défaut" % (needM, needRSD))
