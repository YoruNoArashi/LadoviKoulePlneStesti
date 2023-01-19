import random

kolo=[100,200,300,0,400,500,600,0]
bank=0
while True:
    x = input("Chces hrat(Y/N)? ps jses kripl: ")
    if x == "Y":
        spin = random.choice(kolo)
        bank += spin
        print(spin, f"earnings: {bank}")
        if spin == 0:
            print(f"you lost fucking dumbass shit piece of human shit mrdka curak dement zmrd CUM KOLIK SI PROHRAL AHHAHAHHAHAHAHHA {bank}")
            break
    elif x =="N":
        print(f"Vyhral si {bank} nemam te rad ty kundo chlupata plesniva rasple stara")
        break