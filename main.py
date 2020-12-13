################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

drink_potion()
print(player_health)

# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

# Modifying Global Scope
# Avoid modifying global scope using a function. You can use it to read if you want

enemies = 1

def increase_enemies():
    global enemies
    enemies = 2
    print(f"enemies inside functin: {enemies}")

increase_enemies()

print(f"enemies inside functin: {enemies}")

# Global Constants
# Naming convention within Python is to turn the constant name into upper case

PI = 3.14159