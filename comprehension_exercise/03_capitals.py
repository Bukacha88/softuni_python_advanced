countries = input().split(', ')
capitals = input().split(', ')
result = list(zip(countries, capitals))
result = {print(f"{key} -> {value}") for key, value in result}
