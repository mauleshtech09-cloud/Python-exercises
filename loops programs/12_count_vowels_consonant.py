sentence = "Lion King"
lower_sentence = sentence.lower()
vowels = "aeiou"

v_count = 0
c_count = 0

for word in lower_sentence:
    if word.isalpha():
        if word in vowels:
            v_count += 1

        else:
            c_count += 1

print(f"Vowel Count : {v_count}")
print(f"Consonant Count : {c_count}")
