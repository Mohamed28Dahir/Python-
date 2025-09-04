## While Loops

#Tusaale While Loop
i = 1
while i < 6:
  print(i)
  i += 1    
#Output: 1 2 3 4 5
#Note: Haddii aadan kordhin qiimaha i, loop-ku wuu soconayaa weligiis.
#Note: Haddii shuruuddu noqoto been, loop-ku wuu joojinayaa.
#Note: Haddii aad rabto in aad joojiso loop-ka, isticmaal "break" keyword.
#Example Break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
#Output: 1 2 3
#Note: Haddii aad rabto in aad booddo hal wareeg oo kaliya, isticmaal "continue" keyword.
#Example Continue   
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
#Output: 1 2 4 5 6
#Note: Haddii aad rabto in aad ogaato in loop-ku dhammaaday, isticmaal "else" keyword.
#Example Else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i waa weyn yahay ama u dhiganta 6")
#Output: 1 2 3 4 5 i waa weyn yahay ama u dhiganta 6
#Note: Haddii aad rabto in aad joojiso loop-ka oo aad u gudubto xiga, isticmaal "pass" keyword.
#Example Pass
i = 1
while i < 6:
    if i == 3:
        pass
    else:
        print(i)
    i += 1
#Output: 1 2 4 5
#Note: "pass" keyword ma sameyso waxba, waa meel haye.
#Note: Waxaa loo isticmaalaa in lagu ilaaliyo loop-ka marka aan la rabin in la sameeyo wax ficil ah.
#Note: Haddii aad rabto in aad abuurto loop aan dhammaanayn, isticmaal "while True".
#Example While True
i = 1
while True:
    print(i)
    i += 1
    if i > 5:
        break
#Output: 1 2 3 4 5
#Note: "while True" loop-ku wuu soconayaa weligiis ilaa aad joojiso.
#Note: Waxaa loo isticmaalaa in lagu abuuro loop aan dhammaanayn oo leh shuruudo joojin.
#Note: Waxaa muhiim ah in aad hubiso in shuruudaha joojinta ay jiraan si aan loo helin loop aan dhammaanayn oo aan la rabin.
#Note: Waxaa muhiim ah in aad fahanto sida loo isticmaalo while loops si aad u qorto koodh nadiif ah oo waxtar leh.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo break, continue, else, iyo pass keywords si aad u maareyso while loops si hufan.
#Note: Waxaa muhiim ah in aad barato sida loo abuuro while loops aan dhammaanayn si aad u qorto koodh awood leh.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo while loops si aad u xalliso dhibaatooyinka barnaamijyada.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo while loops si aad u horumariso xirfadahaaga barnaamijyada.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo while loops si aad u noqoto barnaamij yaqaan wanaagsan.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo while loops si aad u noq
#Note: Waxaa muhiim ah in aad barato sida loo isticmaalo while loops si aad u noqoto barnaamij yaqaan wanaagsan.o barnaamij yaqaan wanaagsan.
#Note: Waxaa muhiim ah in aad barato sida loo isticmaao while loops si aad u noqoto barnaamij yaqaan wanaagsan.to barnaamij yaqaan wanaagsan.
#Note: Waxaa muhiim ah in aad barato sida loo isticma
