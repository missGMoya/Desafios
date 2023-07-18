romanNum = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
def romanToInt():
    alga=input("insira número romano: ")
    alga=alga.upper()
    ##print(alga[0])
    resul = 0
    ##len(alga)
    if len(alga) >= 2 and romanNum[alga[0]] >= romanNum[alga[1]]:
        for i in str(alga):
            resul=resul+romanNum[i]
    elif romanNum[alga[0]] < romanNum[alga[1]]:
        for i in str(alga):
            resul = resul + romanNum[i] - romanNum[alga[0]]
    else:
        print(romanNum[alga])
    print("resultado: " + str(resul))

romanToInt()
"""
for key, value in romanNum.items():
    print(key,value)
def romaInteger():
    alga=input("insira número romano: ")
    alga=alga.upper()

    if alga 
romaInteger()
"""