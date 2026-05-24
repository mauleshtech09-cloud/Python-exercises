with open ("sample1.txt","r") as f:
    
    content = f.read()
    
    words_content = content.split()
    
    word_length = len(words_content)
    
    print(f"Content : {content} , has {word_length} total words") 