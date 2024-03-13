class SpaceShip:
    def __init__(self, speed, size, image, position, score):
        self.speed = speed
        self.size = size
        self.image = image
        self.position = position
        self.score = score
        
    def pohyb_doprava(self):
        pass
    
    def pohyb_doleva(self):
        pass
    
    def pohyb_nahoru(self):
        pass
    
    def pohyb_dolu(self):
        pass
    
    def otoceni(self):
        pass
    
    def zvyseni_skore(self):
        pass
    
    # pouzit if instance na rozpoznani s cim je kolize (asteroid nebo bonus)
    def detekuj_kolizi(self):
        pass
    
    def konec_hry(self):
        pass
    
        
class Asteroid:
    def __init__(self, speed, size, image):
        self.speed = speed
        self.size = size
        self.image = image 
        
    # cesta k obrazu, velikost, nastaveni poc. rotace, blitnuti 
    def vykresli(self):
        pass
    
    def pohyb(self):
        pass
    
    def nenaraz_do_rakety(self):
        pass
    
    
# dedicnost / vymyslet vice bonusu   
class Bonus:
    def __init__(self, position, size, hodnota, image):
        self.position = position
        self.size = size
        self.hodnota = hodnota
        self.image = image
        
        