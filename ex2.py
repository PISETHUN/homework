text = input("Enter your text: ")
is_good_password = False
for i in range(len(text)):
    if text[i] == '@':
        is_good_password = True
if is_good_password:
    print("Good password")
else:
    print("Weak password")