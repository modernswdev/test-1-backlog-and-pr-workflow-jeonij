# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

# Security Risk: because this is hardcoded, anyone can read/use it to triggger cheat logic. 
# Fix: just remove the secret code. 
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

# Bug: attack() doesn't reduce the boss HP. Prints damage only,  the boss HP never gets close to 0. 
# Fix: subtract 10 from boss health here 
def attack():
  global b_hp
    print("You deal 10 damage!")

# Bug: heal() has no boundary checks, without limits we can overheal/ heal at 0 hp
# Fix: when hp <= 0 then no healing and limited at the max HP
def heal():
  global p_hp
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0

# WIN CONDITION: when boss HP hits 0, the loop terminate and print victory msg. 
# currently, boss HP only reaches 0 via cheat. With proper attack() damage, add a check after actions to end the game.
if b_hp > 0:
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
