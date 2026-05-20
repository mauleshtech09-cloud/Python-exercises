sentence=input("Enter anything you want : ")

words=sentence.split()
capitalized_words=[]

for word in words:
    
    capitalized_words.append(word.capitalize())
    
result=" ".join(capitalized_words)

print(result)    