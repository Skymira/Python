phone = input("Phone: ")

phones = {
    "1":"one",
    "2":"two",
    "3": "three",
    "4": "four"
}
for ch in phone:
    phones.get(ch)
    print(phones[ch])



