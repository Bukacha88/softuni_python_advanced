from collections import deque
firework_effects = deque(list(map(int, input().split(', '))))

explosive_power = list(map(int, input().split(', ')))
palm_firework = 0
willow_firework = 0
crossette_firework = 0
show_is_ready = False
while firework_effects and explosive_power:

    if firework_effects[0] <= 0:
        firework_effects.popleft()
        continue
    if explosive_power[-1] <= 0:
        explosive_power.pop()
        continue
    values_sum = firework_effects[0] + explosive_power[-1]
    if values_sum % 3 == 0 and not values_sum % 5 == 0:
        palm_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif values_sum % 5 == 0 and not values_sum % 3 == 0:
        willow_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    elif values_sum % 3 == 0 and values_sum % 5 == 0:
        crossette_firework += 1
        firework_effects.popleft()
        explosive_power.pop()
    else:
        firework_effects[0] -= 1

        firework_effects.append(firework_effects.popleft())
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        show_is_ready = True
        break
if show_is_ready:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(map(str, firework_effects))}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")
print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")