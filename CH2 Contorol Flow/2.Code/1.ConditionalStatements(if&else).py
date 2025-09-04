# Conditional Statements (if/elif/else)

## Example: Sharaxada If

x = 8
if x > 5:
    print("x waa ka weyn yahay 5")

## Sharaxaad:
    #1.x = 8 → Waxaan dejinay in x uu la mid yahay 8.
    #2.if x > 5: → Halkan waxaan ku hubineynaa haddii x uu ka weyn yahay 5.
    #3.Haddii shuruuddu run noqoto (True), Python wuxuu fulinayaa amarka ku jira gudaha if.
    #4.Sababtoo ah 8 > 5 waa run, barnaamijku wuxuu soo daabacayaa:
# x waa ka weyn yahay 5

#string
magac = "Ali"

if magac == "Ali":
    print("Magaca waa Ali")

#Sharaxaad:
    # 1.Waxaan abuurnay string lagu magacaabo magac oo qiimihiisu yahay "Ali".
    # 2.Waxaan isticmaalnay if si aan u hubinno haddii magac la mid yahay "Ali".
    # 3.Haddii ay run noqoto → waxay daabacaysaa "Magaca waa Ali".
#Magaca waa Ali
    

## Example: Sharaxada elIf
magac = "Ayaan"

if magac == "Ali":
    print("Magaca waa Ali")
elif magac == "Ahmed":
    print("Magaca waa Ahmed")
elif magac == "Ayaan":
    print("Magaca waa Ayaan")
else:
    print("Magaca lama garanayo")
#Sharaxaad:
    #1.Waxaan dejinay magac inuu yahay "Ayaan".     
    #2.Waxaan isticmaalnay if si aan u hubinno haddii magac la mid yahay "Ali". Tani waa been (False), markaa Python wuxuu u gudbayaa elIf-ka xiga.
    #3.Waxaan isticmaalnay elIf si aan u hubinno haddii magac la mid yahay "Ahmed". Tani waa been (False) sidoo kale, markaa Python wuxuu u gudbayaa elIf-ka xiga.
    #4.Waxaan isticmaalnay elIf si aan u hubinno haddii magac la mid yahay "Ayaan". Tani waa run (True), markaa Python wuxuu fulinayaa amarka ku jira gudaha elIf-kan.
    #5.Sababtoo ah magac waa "Ayaan", barnaamijku wuxuu soo daabacayaa:
# Magaca waa Ayaan


## Example: Sharaxada else
number = -3 
if number < 0:
    print("Number waa taban")
elif number == 0:
    print("Number waa eber")
else:
    print("Number waa togan")
#Sharaxaad:
    #1.Waxaan dejinay number inuu yahay -3.
    #2.Waxaan isticmaalnay if si aan u hubinno haddii number ka yar yahay 0. Tani waa run (True), markaa Python wuxuu fulinayaa amarka ku jira gudaha if-kan.
    #3.Sababtoo ah number waa taban, barnaamijku wuxuu soo daabacayaa:
# Number waa 10

## Sharaxaad Guud:
    #1.`if` waxaa loo isticmaalaa in lagu hubiyo xaalad gaar ah. Haddii xaaladdu run noqoto, koodhka gudaha `if` ayaa la fulinayaa.
    #2.`elif` waxaa loo adeegsadaa in lagu daro xaalado kale haddii
    #3.'else' waxaa loo isticmaalaa in lagu fuliyo koodh haddii dhammaan shuru
    #4.`if`, `elif`, iyo `else` waxay u oggolaanayaan barnaamijyada inay qaataan go'aanno ku saleysan xaaladaha kala duwan. 
    #5.Waxaad isticmaali kartaa `if`, `elif`, iyo `else` si aad u abuurto barnaamijyo ka jawaabaya xaalado kala duwan iyadoo ku xiran xogta la bixiyo.
    #6.Waxaa muhiim ah in la xasuusto in `elif` iyo `else` ay yihiin ikhtiyaari, waxaadna isticmaali kartaa `if` kaliya haddii aad rabto inaad hubiso hal xaalad oo keliya.
    #7.Haddii aad rabto inaad hubiso xaalado badan, waxaad isticmaali kartaa `elif` si aad u darto shuruudo dheeraad ah.
    #8.`else` waxaa loo isticmaalaa in lagu qabto dhammaan xaaladaha kale ee aan la daboolin by `if` iyo `elif`.
    #9.Waxaa muhiim ah in la hubiyo in shuruudaha `if` iyo `elif` ay yihiin kuwo kala duwan si looga fogaado isku dhacyada.
    #10.Waxaad isticmaali kartaa hawlaha isbarbardhigga sida `==`, `!=`, `<`, `>`, `<=`, iyo `>=` si aad u abuurto shuruudo kala duwan.
    #11.Waxaad sidoo kale isticmaali kartaa hawlaha macquulka ah sida `and`, `or`, iyo `not` si aad u abuurto shuruudo isku dhafan.
    #12.Waxaad ku dari kartaa `if`, `elif`, iyo `else` gudaha midba midka kale si aad u abuurto go'aanno adag oo ku saleysan xaalado badan.
## Tusaale Dhameystiran:
number = -3 
if number < 0:
    print("Number waa taban")
elif number == 0:
    print("Number waa eber")
else:
    print("Number waa togan")
#Sharaxaad:
    #1.Waxaan dejinay number inuu yahay -3.
    #2.Waxaan isticmaalnay if si aan u hubinno haddii number ka yar yahay 0. Tani waa run (True), markaa Python wuxuu fulinayaa amarka ku jira gudaha if-kan.
    #3.Sababtoo ah number waa taban, barnaamijku wuxuu soo daabacayaa:
# Number waa 10
