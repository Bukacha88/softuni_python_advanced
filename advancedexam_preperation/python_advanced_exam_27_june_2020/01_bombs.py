from collections import deque
bomb_effects = list(map(int, input().split(', ')))
bomb_effects = deque(bomb_effects)
bomb_casings = list(map(int, input().split(', ')))
datura_bombs = 0
cherry_bombs = 0
smoke_bombs = 0
is_full = False

while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_bombs >= 3:
        is_full = True
        break
    if bomb_effects[0] + bomb_casings[-1] == 40:
        datura_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 60:
        cherry_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 120:
        smoke_bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
if is_full:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effects)}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casings)}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_bombs}")