emoji = {
    ":)": "😀",
    ":(": "😒"
}


def emoji_converter(msg):
    words = msg.split(" ")
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> :")
print(emoji_converter(message))
