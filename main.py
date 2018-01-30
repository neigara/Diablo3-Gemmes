stockR = int(input('Nombre de gemmes Royales en stock '))
stockISD = int(input('Nombre de gemmes Impériales Sans Defaut en stock '))
stockI = int(input('Nombre de gemmes Impériales en stock '))
stockM = int(input('Nombre de gemmes Marquises en stock '))
needRSD = int(input('\nNbre de gemmes Royales Sans Défaut voulues ? '))

equiM = (stockM + stockI*3 + stockISD *9 + stockR*27)
RSD_possible = equiM//81
needM = needRSD*81 - equiM

#print ("Il est possible de faire %d gemmes Royales Sans Défaut" % RSD_possible)
if (needM < 1):
    print ("Vous avez suffisement de gemmes Marquises pour faire %d gemmes Royales Sans Défaut" % needRSD)
else:
    print ("\nPour créer %d gemmes Royales Sans Défaut, il faut %d gemmes Marquises supplémentaires" % (needRSD, needM))
