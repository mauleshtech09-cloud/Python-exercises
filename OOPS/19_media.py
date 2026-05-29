class Media:
    def __init__(self,title,price):
        self.title=title
        self.price=price
        
class Book(Media):
    def __init__(self,title,price,author):
        super().__init__(title,price)
        self.author=author
        
    def describe(self):
        print(f"Title : {self.title}  price : {self.price}   Author : {self.author}")
        
class Magazine(Media):
    
    def __init__(self,title,price,frequency):
        super().__init__(title,price)
        self.frequency=frequency
        
    def describe(self):
        print(f"Title : {self.title}  price : {self.price}   Frequency: {self.frequency}")
        
class DVD(Media):
    
    def __init__(self,title,price,duration):
        super().__init__(title,price)
        self.duration=duration
        
    def describe(self):
            print(f"Title : {self.title}  price : {self.price}  Duration: {self.duration} minutes")     
            
            
book=Book("Road not to be taken",500,"Robert frost")
magazine=Magazine("XYZ",50,300)
dvd=DVD("lion",450,120)   

book.describe()
magazine.describe()
dvd.describe()            
                   