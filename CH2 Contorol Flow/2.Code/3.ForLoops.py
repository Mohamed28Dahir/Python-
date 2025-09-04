# **For Loops (Ku-celinta For) ee Python**

## Syntax

#Tusaale:

magacyada = ["Ali", "Ayaan", "Ahmed"]
for magac in magacyada:
    print(magac)

#Sharaxaad:
    #1.Waxaan abuurnay list lagu magacaabo magacyada oo ka kooban saddex magac.
    #2.for magac in magacyada: → wuxuu ku socda list-ka mid mid.
    #3.Variable magac wuxuu markasta qaadanayaa qiimaha hadda jira ee list-ka.
    #4.print(magac) wuxuu soo daabacayaa magaca markasta la helay.

## Iterating over a sequence
# Tusaale:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

#Sharaxaad:
#1.Waxaan abuurnay list lagu magacaabo magacyada oo ka kooban saddex magac.
#2.for magac in magacyada: → wuxuu ku socda list-ka mid mid.
#3.Variable magac wuxuu markasta qaadanayaa qiimaha hadda jira ee list-ka.
#4.print(magac) wuxuu soo daabacayaa magaca markasta la helay.

## Nested `for` loops
# Tusaale:
colors1 = ["red", "green", "blue"]
colors2 = ["yellow", "orange"]
for color1 in colors1:
    for color2 in colors2:
        print(color1, color2)
#Sharaxaad:
#1.colors1 iyo colors2 waa laba list oo midabyo ka kooban.
#2.for color1 in colors1: → loop-ka koowaad wuxuu marayaa midab kasta oo colors1 ah.
#3.for color2 in colors2: → loop-ka labaad wuxuu marayaa midab kasta oo colors2 ah mar kasta oo loop-ka koowaad socdo.
#4.print(color1, color2) → wuxuu soo bandhigayaa isku darka midab kasta oo ka imanaya colors1 iyo colors2.

## Modifying the sequence during iteration
# Tusaale:
words = ["apple", "banana", "cherry"]

for word in words:
    for letter in word:
        if letter in "aeiou":  # Haddii xarafku yahay shaqal
            word = word.replace(letter, "")  # Ka saar xarafka
    print(word)

#Sharaxaad:
#1.Waxaan abuurnay list words oo ka kooban erayo: ["apple", "banana", "cherry"].
#2.for word in words: → loop-ka koowaad wuxuu marayaa eray kasta.
#3.for letter in word: → loop-ka labaad wuxuu marayaa xaraf kasta oo erayga ku jira.
#4.if letter in "aeiou": → hubinayaa haddii xarafku yahay a, e, i, o, u (vowel).
#5.word = word.replace(letter, "") → wuxuu ka saaraya xarafka erayga.
#6.print(word) → wuxuu soo bandhigayaa erayga cusub oo aan shaqallada lahayn.