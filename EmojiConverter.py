message = input("> ")
words = message.split(' ')
emojis = {
    ":)": "U+1F642",
    ":(": "U+2639"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
    print(output)