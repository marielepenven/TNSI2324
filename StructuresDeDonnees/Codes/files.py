class File_list:
    """File personalisée"""
    def __init__(self):
        self.ma_file = []
    
    def __str__(self):
        return str(self.ma_file)
        
    def file_vide(self):
        return self.ma_file == []

    def enfiler(self, x):
        self.ma_file.append(x)
        return self

    def defiler(self):
        self.ma_file.pop()
    
    def element_defile(self):
        return self.ma_file.pop()

    def taille(self):
        return len(self.ma_file)
    
    def defile_entièrement(self):
        for i in range(self.taille()):
            self.defiler()
            
    def inverse_file(self):
        rep = []
        for i in range(self.taille()):
            rep.append(self.element_defile())
            print(rep)
        for i in range((len(rep))):
            self.enfiler(rep[i])
        
    
    

    