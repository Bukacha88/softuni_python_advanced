phone_book = {}
phone = 0
while True:
    phones = input().split('-')
    if len(phones) < 2:
        phone = int(phones[0])
        break

    name = phones[0]

    if name in phone_book:
        phone_book[name] = phones[1]
    phone_book[name] = phones[1]

for _ in range(phone):
    contact = input()
    if contact in phone_book:
        print(f"{contact} -> {phone_book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")