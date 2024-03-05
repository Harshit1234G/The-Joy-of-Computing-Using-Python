boy = input("Enter name of Boy: ").replace(" ", "").lower()
girl = input("Enter name of Girl: ").replace(" ", "").lower()

common_letters = set(boy).intersection(set(girl))
boy_after_remove = ''.join(i for i in boy if i not in common_letters)
girl_after_remove = ''.join(i for i in girl if i not in common_letters)
count = len(boy_after_remove + girl_after_remove)

flames = "flames"
result = {
    'f': 'Friends',
    'l': 'Love',
    'a': 'Affection',
    'm': 'Marriage',
    'e': 'Enemy',
    's': 'Siblings'
}

top = 0
while len(flames) > 1:
    top = (top + count - 1) % len(flames)
    flames = flames[:top] + flames[top+1:]

print(f"Relation between {boy} and {girl} is {result[flames]}")