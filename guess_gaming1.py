import random

def guess_game_with_lives():
    user_name = input("Apana name btaiye:")
    secret_number = random.randint(1, 100)
    lives = 5  # User ke paas kul 5 mauke hain


    print(f"\n--- Namaste{user_name}!Number Guessing Game mein swagat hai---")
    print("--- Number Guessing Game (Hard Mode) ---")
    print("Maine 1 se 100 ke beech ek number socha hai.")
    print(f"Aapke paas sirf {lives} lives hain. Soch samajh kar guess karein!\n")

    while lives > 0:
        print(f"Bachi hui lives: {lives}")
        
        try:
            #user se input lena 
            user_guess = int(input(f"{user_name},Apna guess batayein: "))
        except ValueError:
            print("Plese ek valid number enter karein!")
            continue

        if user_guess == secret_number:
            print(f"Shabaash{user_name}! Aapne sahi guess kiya. Number {secret_number} hi tha!")
            break
        elif user_guess < secret_number:
            print("Thoda bada number sochein! (Too Low)")
        else:
            print("Thoda chota number sochein! (Too High)")
        
        lives -= 1  # Har galat guess par ek life kam hogi
        print("-" * 20)

    # Agar saari lives khatam ho jayein
    if lives == 0:
        print(f"Game Over{user_name}! Aapki saari lives khatam ho gayi hain.")
        print(f"Sahi number {secret_number} tha. Agli baar koshish karein!")

# Game shuru karein
guess_game_with_lives()