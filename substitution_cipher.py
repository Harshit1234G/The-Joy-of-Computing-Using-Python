from string import ascii_letters

encryption = {
    ascii_letters[i] : ascii_letters[i-5] for i in range(len(ascii_letters))
}

with open("data.txt") as f:
    text = f.read()

encrypted_text = ""
for letter in text:
    encrypted_letter = encryption.get(letter)
    if encrypted_letter is None:
        encrypted_text += letter
    else:
        encrypted_text += encrypted_letter

print("Encripted text:", encrypted_text)