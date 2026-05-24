class Notebook:
    def __init__(self):
        self.notes=[]
        
    def add_notes(self,note):
        self.notes.append(note)
        print("New note added!")
        
    def display_notes(self):
        for i,note in enumerate(self.notes,start=1):
            print(f"{i}. {note}")
            
    def delete_notes(self):
        del_item=input("Which note you want to delete : ")
        self.notes.remove(del_item)
        print("note deleted!")          
            
note1=Notebook()
note1.add_notes("Buy groceries")
note1.add_notes("Read a book")
note1.add_notes("Call the doctor")

note1.display_notes()

note1.delete_notes()
            
note1.display_notes()
            
        
        