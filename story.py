import time

def intro():
    print("Welcome to the Interactive Story Generator!")
    time.sleep(1)
    print("You are about to embark on an adventure.")
    time.sleep(1)
    print("Let's begin!\n")
    time.sleep(1)

def choose_path():
    print("You find yourself at a crossroads.")
    time.sleep(1)
    print("To your left, there is a dark forest.")
    time.sleep(1)
    print("To your right, there is a shimmering lake.")
    time.sleep(1)
    
    choice = input("Which path will you choose? (left/right): ").lower().strip()
    
    if choice == 'left':
        dark_forest()
    elif choice == 'right':
        shimmering_lake()
    else:
        print("Invalid choice!")
        choose_path()

def dark_forest():
    print("\nYou enter the dark forest.")
    time.sleep(1)
    print("As you walk deeper into the forest, you hear strange noises.")
    time.sleep(1)
    print("Suddenly, a group of goblins appears!")
    time.sleep(1)
    print("What will you do?")
    time.sleep(1)
    
    action = input("Fight or Run? (fight/run): ").lower().strip()
    
    if action == 'fight':
        print("\nYou bravely fight off the goblins and continue your journey.")
        time.sleep(1)
        end_story("You survived the dark forest!")
    elif action == 'run':
        print("\nYou run away from the goblins and find a safe path out of the forest.")
        time.sleep(1)
        end_story("You escaped the dark forest!")
    else:
        print("Invalid choice!")
        dark_forest()

def shimmering_lake():
    print("\nYou arrive at the shimmering lake.")
    time.sleep(1)
    print("The water looks magical, and you feel a strange pull.")
    time.sleep(1)
    print("A mermaid emerges from the lake!")
    time.sleep(1)
    print("She offers you a magical potion.")
    time.sleep(1)
    
    choice = input("Accept or Decline? (accept/decline): ").lower().strip()
    
    if choice == 'accept':
        print("\nYou drink the magical potion and feel invigorated.")
        time.sleep(1)
        end_story("You gained magical powers!")
    elif choice == 'decline':
        print("\nYou politely decline the offer and continue your journey.")
        time.sleep(1)
        end_story("You continue your adventure without magic.")
    else:
        print("Invalid choice!")
        shimmering_lake()

def end_story(message):
    print(f"\n{message}")
    time.sleep(1)
    print("Thanks for playing the Interactive Story Generator!")

def main():
    intro()
    choose_path()

if __name__ == "__main__":
    main()
