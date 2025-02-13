import machine
import time
import random

led_pins = [14, 15, 16]
leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

# fonction pour allumer une LED
def flash_led(index, duration=0.5):
    leds[index].value(1)
    time.sleep(duration)
    leds[index].value(0)
    time.sleep(0.3)

sequence = []
score = 0

print("Bienvenue dans le jeu du Simon !")
print("Utilisez les touches 1 [Rouge], 2 [Jaune] et 3 [Bleu] pour reproduire la séquence.")

while True:
    sequence.append(random.randint(0, 2))
    
    print("Regardez bien la séquence...")
    for i in sequence:
        flash_led(i)
    
    print("Reproduisez la séquence avec les touches 1, 2 et 3")

    for i in sequence:
        key = input("Votre réponse : ")  
        
        while key not in ['1', '2', '3']:
            print("⛔ Entrée invalide ! Réessayez en entrant **1, 2 ou 3**.")
            key = input("Votre réponse : ")

        if int(key) - 1 != i:
            print("❌ Faux ! Vous avez perdu !")
            exit()  
        flash_led(i, 0.2)  

    time.sleep(1)

    score += 1
    print(f"✅ Bien joué ! Score actuel : {score}\n")
