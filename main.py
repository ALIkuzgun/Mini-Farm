import pygame,time,json,random #10,40   

# Water class
class Water():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/water.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Çapa class
class ÇapaUcu():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/çapa.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Tree class
class Tree():
    def __init__(self, x, y):
        super().__init__()
        self.imagies = [pygame.image.load('img/tree.png').convert_alpha(),
                        pygame.image.load('img/tree2.png').convert_alpha()]
        self.image = self.imagies[1]
        self.image = pygame.transform.scale(self.image, (72, 90)) 
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.süre = 10000
        self.type = "meyveli_ağaç"

    def büyüme(self):
        self.süre+=1 
        if self.süre >= 10000:
          self.type = "meyveli_ağaç"
          self.image = self.imagies[1]
          self.image = pygame.transform.scale(self.image, (72, 90)) 
        else:
            self.type = "normal_ağaç"

    def draw(self):
        self.büyüme()
        ekran.blit(self.image, self.rect.topleft)

# Wall Tree class
class Wall_Tree():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/wall_tree.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Wall class
class Wall():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/wall.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Toprak class
class Soil():
    def __init__(self, x, y):
        super().__init__()
        self.imagies = [pygame.image.load('img/soil.png'),
                        pygame.image.load('img/wetsoil.png'),
                        pygame.image.load('img/hoedsoil.png'),
                        pygame.image.load('img/patatosoil1.png'),
                        pygame.image.load('img/patatosoil2.png'),
                        pygame.image.load('img/patatosoil3.png'),
                        pygame.image.load('img/patatosoil4.png'),
                        pygame.image.load('img/patatosoil5.png'),
                        pygame.image.load('img/onionsoil1.png'),
                        pygame.image.load('img/onionsoil2.png'),
                        pygame.image.load('img/onionsoil3.png'),
                        pygame.image.load('img/onionsoil4.png'),
                        pygame.image.load('img/onionsoil5.png'),
                        pygame.image.load('img/carrotsoil1.png'),
                        pygame.image.load('img/carrotsoil2.png'),
                        pygame.image.load('img/carrotsoil3.png'),
                        pygame.image.load('img/carrotsoil4.png'),
                        pygame.image.load('img/carrotsoil5.png')]
        self.image = self.imagies[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.patates_büyüme_süresi = 0
        self.patates_ekildi = 0
        self.onion_büyüme_süresi = 0
        self.onion_ekildi = 0
        self.carrot_büyüme_süresi = 0
        self.carrot_ekildi = 0
        self.çapalanmış = 0
        self.sulanmış = 0
        self.type = "normal"
        self.vegetable_type = ""        
        self.ekildi_patates = False  
        self.ekildi_onion = False    
        self.ekildi_carrot = False 

    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Npc class
class Npc():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/npc.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Wall2 class
class Wall2():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/wall2.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Yatak class
class Bed():
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('img/bed.png')
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)

# Player class
class Player():
    # değişkenler
    def __init__(self,x, y):
        super().__init__()
        self.imagies = [pygame.image.load('img/playeridleright.png'),
                        pygame.image.load('img/playeridleleft.png'),
                        pygame.image.load('img/playeridleup.png'),
                        pygame.image.load('img/playeridledown.png'),
                        pygame.image.load('img/playerrightwalk1.png'),
                        pygame.image.load('img/playerrightwalk2.png'),
                        pygame.image.load('img/playerrightwalk3.png'),
                        pygame.image.load('img/playerrightwalk4.png'),
                        pygame.image.load('img/playerrightwalk5.png'),
                        pygame.image.load('img/playerrightwalk6.png'),
                        pygame.image.load('img/playerrightwalk7.png'),
                        pygame.image.load('img/playerrightwalk8.png'),
                        pygame.image.load('img/playerleftwalk1.png'),
                        pygame.image.load('img/playerleftwalk2.png'),
                        pygame.image.load('img/playerleftwalk3.png'),
                        pygame.image.load('img/playerleftwalk4.png'),
                        pygame.image.load('img/playerleftwalk5.png'),
                        pygame.image.load('img/playerleftwalk6.png'),
                        pygame.image.load('img/playerleftwalk7.png'),
                        pygame.image.load('img/playerleftwalk8.png'),
                        pygame.image.load('img/playerdownwalk1.png'),
                        pygame.image.load('img/playerdownwalk2.png'),
                        pygame.image.load('img/playerdownwalk3.png'),
                        pygame.image.load('img/playerdownwalk4.png'),
                        pygame.image.load('img/playerdownwalk5.png'),
                        pygame.image.load('img/playerdownwalk6.png'),
                        pygame.image.load('img/playerdownwalk7.png'),
                        pygame.image.load('img/playerdownwalk8.png'),
                        pygame.image.load('img/playerupwalk1.png'),
                        pygame.image.load('img/playerupwalk2.png'),
                        pygame.image.load('img/playerupwalk3.png'),
                        pygame.image.load('img/playerupwalk4.png'),
                        pygame.image.load('img/playerupwalk5.png'),
                        pygame.image.load('img/playerupwalk6.png'),
                        pygame.image.load('img/playerupwalk7.png'),
                        pygame.image.load('img/playerupwalk8.png'),
                        pygame.image.load('img/playersulama1.png'),
                        pygame.image.load('img/playersulama2.png'),
                        pygame.image.load('img/playerçapa1.png'),
                        pygame.image.load('img/playerçapa2.png'),
                        pygame.image.load('img/playerçapa3.png'),
                        pygame.image.load('img/playerçapa4.png'),
                        pygame.image.load('img/playersulamaleft1.png'),
                        pygame.image.load('img/playersulamaleft2.png')]
        self.image = self.imagies[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y
        self.direction = "right"
        self.move_type = "stay"
        self.kova = 0
        self.tuş_1 = 0
        self.tuş_2 = 0
        self.tuş_3 = 0
        self.tuş_r = 0
        self.money = 30
        self.patates_ek = 0
        self.onion_ek = 0
        self.carrot_ek = 0
        self.çapa = 0
        self.balta = 0
        self.animation_süre = 0
        self.text_imleç_x = 50
        self.text_imleç_y = 342
        self.water = 0
        self.çapaucu = 0
        self.haraket = 1
        self.number_of_patates_seed = 0
        self.number_of_carrot_seed = 0
        self.number_of_onion_seed = 0
        self.number_of_patato = 0
        self.number_of_carrot = 0
        self.number_of_onion = 0
        self.number_of_apple = 0
        self.konuşma = "soru"
        self.item_1 = ""
        self.item_2 = ""
        self.item_3 = ""
        self.item_4 = ""
        self.item_5 = ""
        self.item_6 = ""
        self.item_7 = ""
        self.number__of_item_1 = 0
        self.number__of_item_2 = 0
        self.number__of_item_3 = 0
        self.number__of_item_4 = 0
        self.number__of_item_5 = 0
        self.number__of_item_6 = 0
        self.number__of_item_7 = 0
        self.buy_p_seed_buton = pygame.Rect((56,168,150,30))
        self.buy_c_seed_buton = pygame.Rect((56,214,150,30))
        self.buy_o_seed_buton = pygame.Rect((56,256,150,30))
        self.sell_patato_buton = pygame.Rect((56,168,150,30))
        self.sell_carrot_buton = pygame.Rect((56,214,150,30))
        self.sell_onion_buton = pygame.Rect((56,256,150,30))
        self.sell_apple_buton = pygame.Rect((56,298,150,30))
    # haraket ve tuşlar
    def move(self):
        key = pygame.key.get_pressed()
        if self.haraket == 1:
            if key[pygame.K_d]:
                self.x += 3
                self.direction = "right"
                self.move_type = "right"
            elif key[pygame.K_a]:
                self.x -= 3
                self.direction = "left"
                self.move_type = "left"
            elif key[pygame.K_w]:
                self.y -= 3
                self.direction = "up"
                self.move_type = "up"
            elif key[pygame.K_s]:
                self.y += 3
                self.direction = "down"
                self.move_type = "down"
            else:
             self.move_type = "stay"

        if self.direction=="right":
            self.image = self.imagies[0]
        elif self.direction=="left":
            self.image = self.imagies[1]
        elif self.direction=="up":
            self.image = self.imagies[2]
        elif self.direction=="down":
            self.image = self.imagies[23]

        if self.move_type == "right":
           self.animation_süre += 1
           if self.animation_süre >= 8:
            self.image = self.imagies[4]
           if self.animation_süre >= 16:
            self.image = self.imagies[5]
           if self.animation_süre >= 24:
            self.image = self.imagies[6]
           if self.animation_süre >= 32:
            self.image = self.imagies[7]
           if self.animation_süre >= 40:
            self.image = self.imagies[8]
           if self.animation_süre >= 48:
            self.image = self.imagies[9]
           if self.animation_süre >= 56:
            self.image = self.imagies[10]
           if self.animation_süre >= 64:
            self.image = self.imagies[11]
           if self.animation_süre >= 72:
            self.animation_süre = 0

        if self.move_type == "left":
           self.animation_süre += 1
           if self.animation_süre >= 8:
            self.image = self.imagies[12]
           if self.animation_süre >= 16:
            self.image = self.imagies[13]
           if self.animation_süre >= 24:
            self.image = self.imagies[14]
           if self.animation_süre >= 32:
            self.image = self.imagies[15]
           if self.animation_süre >= 40:
            self.image = self.imagies[16]
           if self.animation_süre >= 48:
            self.image = self.imagies[17]
           if self.animation_süre >= 56:
            self.image = self.imagies[18]
           if self.animation_süre >= 64:
            self.image = self.imagies[19]
           if self.animation_süre >= 72:
            self.animation_süre = 0

        if self.move_type == "down":
           self.animation_süre += 1
           if self.animation_süre >= 8:
            self.image = self.imagies[20]
           if self.animation_süre >= 16:
            self.image = self.imagies[21]
           if self.animation_süre >= 24:
            self.image = self.imagies[22]
           if self.animation_süre >= 32:
            self.image = self.imagies[23]
           if self.animation_süre >= 40:
            self.image = self.imagies[24]
           if self.animation_süre >= 48:
            self.image = self.imagies[25]
           if self.animation_süre >= 56:
            self.image = self.imagies[26]
           if self.animation_süre >= 64:
            self.image = self.imagies[27]
           if self.animation_süre >= 72:
            self.animation_süre = 0

        if self.move_type == "up":
           self.animation_süre += 1
           if self.animation_süre >= 8:
            self.image = self.imagies[28]
           if self.animation_süre >= 16:
            self.image = self.imagies[29]
           if self.animation_süre >= 24:
            self.image = self.imagies[30]
           if self.animation_süre >= 32:
            self.image = self.imagies[31]
           if self.animation_süre >= 40:
            self.image = self.imagies[32]
           if self.animation_süre >= 48:
            self.image = self.imagies[33]
           if self.animation_süre >= 56:
            self.image = self.imagies[34]
           if self.animation_süre >= 64:
            self.image = self.imagies[35]
           if self.animation_süre >= 72:
            self.animation_süre = 0

        if self.move_type == "sulama":
            self.image = self.imagies[36]

        if self.x <= 0:
            self.x = 0
        if self.x >= width - 33:
            self.x = width - 33
        if self.y <= 0:
            self.y = 0
        if self.y >= height - 39:
            self.y = height - 39

        self.rect.topleft = (self.x, self.y)
        water.rect.topleft = (self.x+50, self.y+34)
        çapaucu.rect.topleft = (self.x+42, self.y+40)

        if key[pygame.K_1]:
            self.tuş_1 = 1
            self.tuş_3 = 0
            self.tuş_2 = 0
        if self.tuş_1==1:
           if key[pygame.K_SPACE]:
                self.çapa = 1
                self.çapalanmış = 1
                self.move_type = "çapa"
                if self.move_type == "çapa":
                  self.animation_süre += 1
                  self.haraket = 0
                  if self.animation_süre >= 15:
                    self.image = self.imagies[38]
                  if self.animation_süre >= 30:
                    self.image = self.imagies[39]
                  if self.animation_süre >= 45:
                    self.image = self.imagies[40]
                  if self.animation_süre >= 60:
                    self.image = self.imagies[41]
                    self.çapaucu = 1
                    çapaucu.draw()    
                  if self.animation_süre >= 75:
                    self.animation_süre = 0
                    self.çapaucu = 0
                    self.haraket = 1
           else:
               self.çapa = 0
               self.çapalanmış = 0 
               self.çapaucu = 0
               self.haraket = 1

        if key[pygame.K_2]:
            self.tuş_2 = 1
            self.tuş_1 = 0
            self.tuş_3 = 0
        if self.tuş_2==1:
           if key[pygame.K_SPACE]:
                self.kova = 1
                soil.sulanmış = 1
                self.move_type = "sulama"
                if self.move_type == "sulama":
                 self.animation_süre += 1
                 self.haraket = 0
                if self.animation_süre >= 10:
                    self.image = self.imagies[0]
                if self.animation_süre >= 30:
                    self.image = self.imagies[36]
                if self.animation_süre >= 60:
                    self.image = self.imagies[37]
                    self.water = 1
                    water.draw()
                if self.animation_süre >= 90:
                    self.animation_süre = 0
                    self.water = 0
                    self.haraket = 1
           else:
               self.kova = 0
               soil.sulanmış = 0
               self.haraket = 1
               self.water = 0
               self.move_type = ""

        if key[pygame.K_3]:
            self.tuş_3 = 1
            self.tuş_1 = 0
            self.tuş_2 = 0
        if self.tuş_3==1:
           if key[pygame.K_SPACE]:
               self.balta = 1
           else:
               self.balta = 0

        if key[pygame.K_p]:
            self.patates_ek = 1
        else:
            self.patates_ek = 0

        if key[pygame.K_o]:
            self.onion_ek = 1
        else:
            self.onion_ek = 0

        if key[pygame.K_c]:
            self.carrot_ek = 1
        else:
            self.carrot_ek = 0

        if key[pygame.K_r]:
            self.tuş_r = 1
        else:
            self.tuş_r = 0
    # duvar teması
    def wall_hit(self):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if self.direction == "right":
                    self.rect.right = wall.rect.left
                if self.direction == "left":
                    self.rect.left = wall.rect.right
                if self.direction == "up":
                    self.rect.top = wall.rect.bottom
                elif self.direction == "down":
                    self.rect.bottom = wall.rect.top

                self.x, self.y = self.rect.topleft

        for wall2 in walls2:
            if self.rect.colliderect(wall2.rect):
                if self.direction == "right":
                    self.rect.right = wall2.rect.left
                elif self.direction == "left":
                    self.rect.left = wall2.rect.right
                elif self.direction == "up":
                    self.rect.top = wall2.rect.bottom
                elif self.direction == "down":
                    self.rect.bottom = wall2.rect.top
                
                self.x, self.y = self.rect.topleft

        for wall_tree in wall_treies:
            if self.rect.colliderect(wall_tree.rect):
                if self.direction == "right":
                    self.rect.right = wall_tree.rect.left
                elif self.direction == "left":
                    self.rect.left = wall_tree.rect.right
                elif self.direction == "up":
                    self.rect.top = wall_tree.rect.bottom
                elif self.direction == "down":
                    self.rect.bottom = wall_tree.rect.top
                
                self.x, self.y = self.rect.topleft
    # yatak teması
    def bed_hit(self):
        global saniye
        if self.rect.colliderect(bed.rect):
            self.x=bed.x+4
            self.y=bed.y+4
            saniye += 80
    # patates-onion-carrot-apple envantere ekle
    def apple_envanter_ekle(self): 
      if self.item_1 == "":
          self.item_1 = "Apple"
          self.number__of_item_1 = self.number_of_apple
      elif self.item_1 == "Apple":
          self.number__of_item_1 = self.number_of_apple
      elif self.item_2 == "":
          self.item_2 = "Apple"
          self.number__of_item_2 = self.number_of_apple
      elif self.item_2 == "Apple":
          self.number__of_item_2 = self.number_of_apple
      elif self.item_3 == "":
          self.item_3 = "Apple"
          self.number__of_item_3 = self.number_of_apple
      elif self.item_3 == "Apple":
          self.number__of_item_3 = self.number_of_apple
      elif self.item_4 == "":
          self.item_4 = "Apple"
          self.number__of_item_4 = self.number_of_apple
      elif self.item_4 == "Apple":
          self.number__of_item_4 = self.number_of_apple
      elif self.item_5 == "":
          self.item_5 = "Apple"
          self.number__of_item_5 = self.number_of_apple
      elif self.item_5 == "Apple":
          self.number__of_item_5 = self.number_of_apple
      elif self.item_6 == "":
          self.item_6 = "Apple"
          self.number__of_item_6 = self.number_of_apple
      elif self.item_6 == "Apple":
          self.number__of_item_6 = self.number_of_apple
      elif self.item_7 == "":
          self.item_7 = "Apple"
          self.number__of_item_7 = self.number_of_apple
      elif self.item_7 == "Apple":
          self.number__of_item_7 = self.number_of_apple
    def patates_envanter_ekle(self): 
      if self.item_1 == "":
          self.item_1 = "Patato"
          self.number__of_item_1 = self.number_of_patato
      elif self.item_1 == "Patato":
          self.number__of_item_1 = self.number_of_patato
      elif self.item_2 == "":
          self.item_2 = "Patato"
          self.number__of_item_2 = self.number_of_patato
      elif self.item_2 == "Patato":
          self.number__of_item_2 = self.number_of_patato
      elif self.item_3 == "":
          self.item_3 = "Patato"
          self.number__of_item_3 = self.number_of_patato
      elif self.item_3 == "Patato":
          self.number__of_item_3 = self.number_of_patato
      elif self.item_4 == "":
          self.item_4 = "Patato"
          self.number__of_item_4 = self.number_of_patato
      elif self.item_4 == "Patato":
          self.number__of_item_4 = self.number_of_patato
      elif self.item_5 == "":
          self.item_5 = "Patato"
          self.number__of_item_5 = self.number_of_patato
      elif self.item_5 == "Patato":
          self.number__of_item_5 = self.number_of_patato
      elif self.item_6 == "":
          self.item_6 = "Patato"
          self.number__of_item_6 = self.number_of_patato
      elif self.item_6 == "Patato":
          self.number__of_item_6 = self.number_of_patato
      elif self.item_7 == "":
          self.item_7 = "Patato"
          self.number__of_item_7 = self.number_of_patato
      elif self.item_7 == "Patato":
          self.number__of_item_7 = self.number_of_patato
    def onion_envanter_ekle(self): 
      if self.item_1 == "":
          self.item_1 = "Onion"
          self.number__of_item_1 = self.number_of_onion
      elif self.item_1 == "Onion":
          self.number__of_item_1 = self.number_of_onion
      elif self.item_2 == "":
          self.item_2 = "Onion"
          self.number__of_item_2 = self.number_of_onion
      elif self.item_2 == "Onion":
          self.number__of_item_2 = self.number_of_onion
      elif self.item_3 == "":
          self.item_3 = "Onion"
          self.number__of_item_3 = self.number_of_onion
      elif self.item_3 == "Onion":
          self.number__of_item_3 = self.number_of_onion
      elif self.item_4 == "":
          self.item_4 = "Onion"
          self.number__of_item_4 = self.number_of_onion
      elif self.item_4 == "Onion":
          self.number__of_item_4 = self.number_of_onion
      elif self.item_5 == "":
          self.item_5 = "Onion"
          self.number__of_item_5 = self.number_of_onion
      elif self.item_5 == "Onion":
          self.number__of_item_5 = self.number_of_onion
      elif self.item_6 == "":
          self.item_6 = "Onion"
          self.number__of_item_6 = self.number_of_onion
      elif self.item_6 == "Onion":
          self.number__of_item_6 = self.number_of_onion
      elif self.item_7 == "":
          self.item_7 = "Onion"
          self.number__of_item_7 = self.number_of_onion
      elif self.item_7 == "Onion":
          self.number__of_item_7 = self.number_of_onion
    def carrot_envanter_ekle(self):
      if self.item_1 == "":
          self.item_1 = "Carrot"
          self.number__of_item_1 = self.number_of_carrot
      elif self.item_1 == "Carrot":
          self.number__of_item_1 = self.number_of_carrot
      elif self.item_2 == "":
          self.item_2 = "Carrot"
          self.number__of_item_2 = self.number_of_carrot
      elif self.item_2 == "Carrot":
          self.number__of_item_2 = self.number_of_carrot
      elif self.item_3 == "":
          self.item_3 = "Carrot"
          self.number__of_item_3 = self.number_of_carrot
      elif self.item_3 == "Carrot":
          self.number__of_item_3 = self.number_of_carrot
      elif self.item_4 == "":
          self.item_4 = "Carrot"
          self.number__of_item_4 = self.number_of_carrot
      elif self.item_4 == "Carrot":
          self.number__of_item_4 = self.number_of_carrot
      elif self.item_5 == "":
          self.item_5 = "Carrot"
          self.number__of_item_5 = self.number_of_carrot
      elif self.item_5 == "Carrot":
          self.number__of_item_5 = self.number_of_carrot
      elif self.item_6 == "":
          self.item_6 = "Carrot"
          self.number__of_item_6 = self.number_of_carrot
      elif self.item_6 == "Carrot":
          self.number__of_item_6 = self.number_of_carrot
      elif self.item_7 == "":
          self.item_7 = "Carrot"
          self.number__of_item_7 = self.number_of_carrot
      elif self.item_7 == "Carrot":
          self.number__of_item_7 = self.number_of_carrot

    # toprak teması ve bitki büyümesi
    def soil_hit(self):
      for soil in soils:
        if çapaucu.rect.colliderect(soil.rect):
            if self.çapa == 1 and not any([soil.patates_ekildi, soil.onion_ekildi, soil.carrot_ekildi]) and self.water == 0:
                if soil.sulanmış == 0 and self.çapaucu == 1:
                    soil.image = soil.imagies[2]
                    soil.çapalanmış = 1

        if water.rect.colliderect(soil.rect):
            if soil.çapalanmış == 1 and not any([soil.patates_ekildi, soil.onion_ekildi, soil.carrot_ekildi]):
                if self.kova == 1 and self.water == 1:
                    soil.sulanmış = 1
                    soil.image = soil.imagies[1]

        if self.rect.colliderect(soil.rect):
            if self.patates_ek == 1 and soil.type != "onion" and soil.type != "carrot":
                if not soil.ekildi_patates: 
                    if soil.sulanmış == 1 and self.number_of_patates_seed > 0:
                        soil.patates_ekildi = 1
                        soil.type = "patates"
                        soil.image = soil.imagies[3]
                        self.number_of_patates_seed -= 1
                        self.patates_ek = 0
                        patates_seed_envanter_ekle()
                        soil.ekildi_patates = True 

            if self.onion_ek == 1 and soil.type != "patates" and soil.type != "carrot":
                if not soil.ekildi_onion: 
                    if soil.sulanmış == 1 and self.number_of_onion_seed > 0:
                        soil.onion_ekildi = 1
                        soil.type = "onion"
                        soil.image = soil.imagies[8]
                        self.number_of_onion_seed -= 1
                        self.onion_ek = 0 
                        onion_seed_envanter_ekle()
                        soil.ekildi_onion = True  

            if self.carrot_ek == 1 and soil.type != "patates" and soil.type != "onion":
                if not soil.ekildi_carrot:  
                    if soil.sulanmış == 1 and self.number_of_carrot_seed > 0:
                        soil.carrot_ekildi = 1
                        soil.type = "carrot"
                        soil.image = soil.imagies[13]
                        self.number_of_carrot_seed -= 1
                        self.carrot_ek = 0 
                        carrot_seed_envanter_ekle()
                        soil.ekildi_carrot = True 

        if soil.patates_ekildi == 1:
            soil.patates_büyüme_süresi += 1
            if soil.patates_büyüme_süresi >= 0:
              soil.image = soil.imagies[3]
            if soil.patates_büyüme_süresi >= 100:
              soil.image = soil.imagies[4]
            if soil.patates_büyüme_süresi >= 200:
              soil.image = soil.imagies[5]
            if soil.patates_büyüme_süresi >= 300:
              soil.image = soil.imagies[6]
            if soil.patates_büyüme_süresi >= 400:
              soil.image = soil.imagies[7]
              soil.vegetable_type = "patato"
              if self.rect.colliderect(soil.rect):
                 if soil.vegetable_type == "patato":
                    if self.tuş_r == 1:
                        soil.patates_büyüme_süresi = 0
                        self.number_of_patato += 1
                        self.patates_envanter_ekle()
                        if self.item_1 == "":
                          self.item_1 = "Patato"
                        if player.item_1 == "Carrot Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Onion" or player.item_1 == "Carrot":
                            if player.item_1 != "Patato":
                              if player.item_2 == "":
                                player.item_2 = "Patato"
                        if player.item_2 == "Carrot Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Apple" or player.item_1 == "Patato Seed" or player.item_2 == "Onion" or player.item_2 == "Carrot":
                            if player.item_1 != "Patato" and player.item_2 != "Patato":
                              if player.item_3 == "":
                                player.item_3 = "Patato"
                        if player.item_3 == "Carrot Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Apple" or player.item_1 == "Patato Seed" or player.item_3 == "Onion" or player.item_3 == "Carrot":
                            if player.item_1 != "Patato" and player.item_2 != "Patato" and player.item_3 != "Patato":
                              if player.item_4 == "":
                                player.item_4 = "Patato"
                        if player.item_4 == "Carrot Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Apple" or player.item_4 == "Patato Seed" or player.item_4 == "Onion" or player.item_4 == "Carrot":
                            if player.item_1 != "Patato" and player.item_2 != "Patato" and player.item_3 != "Patato" and player.item_4 != "Patato":
                              if player.item_5 == "":
                                player.item_5 = "Patato"
                        if player.item_5 == "Carrot Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Apple" or player.item_5 == "Patato Seed" or player.item_5 == "Onion" or player.item_5 == "Carrot":
                            if player.item_1 != "Patato" and player.item_2 != "Patato" and player.item_3 != "Patato" and player.item_4 != "Patato" and player.item_5 != "Patato":
                              if player.item_6 == "":
                                player.item_6 = "Patato"
                        if player.item_6 == "Carrot Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Apple" or player.item_6 == "Patato Seed" or player.item_6 == "Onion" or player.item_6 == "Carrot":
                            if player.item_1 != "Patato" and player.item_2 != "Patato" and player.item_3 != "Patato" and player.item_4 != "Patato" and player.item_5 != "Patato" and player.item_6 != "Patato":
                              if player.item_7 == "":
                                player.item_7 = "Patato"

        if soil.onion_ekildi == 1:
            soil.onion_büyüme_süresi += 1
            if soil.patates_büyüme_süresi >= 0:
              soil.image = soil.imagies[8]
            if soil.onion_büyüme_süresi >= 100:
              soil.image = soil.imagies[9]
            if soil.onion_büyüme_süresi >= 200:
              soil.image = soil.imagies[10]
            if soil.onion_büyüme_süresi >= 300:
              soil.image = soil.imagies[11]
            if soil.onion_büyüme_süresi >= 400:
              soil.image = soil.imagies[12]
              soil.vegetable_type = "onion"
              if self.rect.colliderect(soil.rect):
                 if soil.vegetable_type == "onion":
                    if self.tuş_r == 1:
                        soil.onion_büyüme_süresi = 0
                        self.number_of_onion+=1
                        self.onion_envanter_ekle()
                        if player.item_1 == "":
                          player.item_1 = "Onion"
                        if player.item_1 == "Carrot Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_1 == "Carrot":
                            if player.item_2 == "":
                              player.item_2 = "Onion"
                        if player.item_2 == "Carrot Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_2 == "Carrot":
                            if player.item_1 != "Onion" and player.item_2 != "Onion":
                              if player.item_3 == "":
                                player.item_3 = "Onion"
                        if player.item_3 == "Carrot Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_3 == "Carrot":
                            if player.item_1 != "Onion" and player.item_2 != "Onion" and player.item_3 != "Onion":
                              if player.item_4 == "":
                                player.item_4 = "Onion"
                        if player.item_4 == "Carrot Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Apple" or player.item_4 == "Patato Seed" or player.item_1 == "Patato" or player.item_4 == "Carrot":
                            if player.item_1 != "Onion" and player.item_2 != "Onion" and player.item_3 != "Onion" and player.item_4 != "Onion":
                              if player.item_5 == "":
                                player.item_5 = "Onion"
                        if player.item_5 == "Carrot Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Apple" or player.item_5 == "Patato Seed" or player.item_5 == "Patato" or player.item_5 == "Carrot":
                            if player.item_1 != "Onion" and player.item_2 != "Onion" and player.item_3 != "Onion" and player.item_4 != "Onion" and player.item_5 != "Onion":
                              if player.item_6 == "":
                                player.item_6 = "Onion"
                        if player.item_6 == "Carrot Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Apple" or player.item_6 == "Patato Seed" or player.item_6 == "Patato" or player.item_6 == "Carrot":
                            if player.item_1 != "Onion" and player.item_2 != "Onion" and player.item_3 != "Onion" and player.item_4 != "Onion" and player.item_5 != "Onion" and player.item_6 != "Onion":
                              if player.item_7 == "":
                                player.item_7 = "Onion"

        if soil.carrot_ekildi == 1:
            soil.carrot_büyüme_süresi += 1
            if soil.patates_büyüme_süresi >= 0:
              soil.image = soil.imagies[13]
            if soil.carrot_büyüme_süresi >= 100:
              soil.image = soil.imagies[14]
            if soil.carrot_büyüme_süresi >= 200:
              soil.image = soil.imagies[15]
            if soil.carrot_büyüme_süresi >= 300:
              soil.image = soil.imagies[16]
            if soil.carrot_büyüme_süresi >= 400:
              soil.image = soil.imagies[17]
              soil.vegetable_type = "carrot"
              if self.rect.colliderect(soil.rect):
                 if soil.vegetable_type == "carrot":
                    if self.tuş_r == 1:
                        soil.carrot_büyüme_süresi = 0
                        self.number_of_carrot+=1
                        self.carrot_envanter_ekle()
                        if player.item_1 == "":
                          player.item_1 = "Carrot"
                        if player.item_1 == "Carrot Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_1 == "Onion":
                            if player.item_2 == "":
                              player.item_2 = "Carrot"
                        if player.item_2 == "Carrot Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_2 == "Onion":
                            if player.item_1 != "Carrot" and player.item_2 != "Carrot":
                              if player.item_3 == "":
                                player.item_3 = "Carrot"
                        if player.item_3 == "Carrot Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Apple" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_3 == "Onion":
                            if player.item_1 != "Carrot" and player.item_2 != "Carrot" and player.item_3 != "Carrot":
                              if player.item_4 == "":
                                player.item_4 = "Carrot"
                        if player.item_4 == "Carrot Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Apple" or player.item_4 == "Patato Seed" or player.item_1 == "Patato" or player.item_4 == "Onion":
                            if player.item_1 != "Carrot" and player.item_2 != "Carrot" and player.item_3 != "Carrot" and player.item_4 != "Carrot":
                              if player.item_5 == "":
                                player.item_5 = "Carrot"
                        if player.item_5 == "Carrot Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Apple" or player.item_5 == "Patato Seed" or player.item_5 == "Patato" or player.item_5 == "Onion":
                            if player.item_1 != "Carrot" and player.item_2 != "Carrot" and player.item_3 != "Carrot" and player.item_4 != "Carrot" and player.item_5 != "Carrot":
                              if player.item_6 == "":
                                player.item_6 = "Carrot"
                        if player.item_6 == "Carrot Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Apple" or player.item_6 == "Patato Seed" or player.item_6 == "Patato" or player.item_6 == "Onion":
                            if player.item_1 != "Carrot" and player.item_2 != "Carrot" and player.item_3 != "Carrot" and player.item_4 != "Carrot" and player.item_5 != "Carrot" and player.item_6 != "Carrot":
                              if player.item_7 == "":
                                player.item_7 = "Carrot"

    # ağaç teması ve elma toplama
    def tree_hit(self):
        for tree in treies:
          if self.rect.colliderect(tree.rect):
             if self.balta == 1 and tree.type == "meyveli_ağaç": 
                 tree.type = "normal_ağaç"
                 tree.süre = 0
                 tree.image = tree.imagies[0]
                 tree.image = pygame.transform.scale(tree.image, (72, 90)) 
                 self.number_of_apple += random.choice([1,1,1,1,2,2,3,4,2,3])
                 self.apple_envanter_ekle()
                 if player.item_1 == "":
                    player.item_1 = "Apple"
                 if player.item_1 == "Carrot Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Patato Seed" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_1 == "Carrot":
                    if player.item_2 == "":
                      player.item_2 = "Apple"
                 if player.item_2 == "Carrot Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Patato Seed" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_2 == "Carrot":
                    if player.item_1 != "Apple" and player.item_2 != "Apple":
                      if player.item_3 == "":
                         player.item_3 = "Apple"
                 if player.item_3 == "Carrot Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Patato Seed" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_3 == "Carrot":
                      if player.item_1 != "Apple" and player.item_2 != "Apple" and player.item_3 != "Apple":
                        if player.item_4 == "":
                          player.item_4 = "Apple"
                 if player.item_4 == "Carrot Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Patato" or player.item_4 == "Patato Seed" or player.item_1 == "Onion" or player.item_4 == "Carrot":
                      if player.item_1 != "Apple" and player.item_2 != "Apple" and player.item_3 != "Apple" and player.item_4 != "Apple":
                        if player.item_5 == "":
                          player.item_5 = "Apple"
                 if player.item_5 == "Carrot Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Onion" or player.item_5 == "Patato Seed" or player.item_5 == "Patato" or player.item_5 == "Carrot":
                    if player.item_1 != "Apple" and player.item_2 != "Apple" and player.item_3 != "Apple" and player.item_4 != "Apple" and player.item_5 != "Apple":
                      if player.item_6 == "":
                        player.item_6 = "Apple"
                 if player.item_6 == "Carrot Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Patato" or player.item_6 == "Patato Seed" or player.item_6 == "Onion" or player.item_6 == "Carrot":
                    if player.item_1 != "Apple" and player.item_2 != "Apple" and player.item_3 != "Apple" and player.item_4 != "Apple" and player.item_5 != "Apple" and player.item_6 != "Apple":
                      if player.item_7 == "":
                        player.item_7 = "Apple"

    # npc teması
    def npc_hit(self):
        if self.rect.colliderect(npc.rect):
            self.npc_talk()
        else:
            self.konuşma = "soru"
            self.text_imleç_y = 342
    # npc konuşmas ve alım-satım
    def npc_talk(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
          self.text_imleç_y -= 26
        if key[pygame.K_DOWN]:
          self.text_imleç_y += 24
        if key[pygame.K_RETURN]:
          if self.text_imleç_y >= 364:
              self.konuşma = "sell"
          if self.text_imleç_y == 342:
              self.konuşma = "buy"

        if self.konuşma == "sell":
            sell_box = pygame.image.load("img/npc_sell.png")   
            ekran.blit(sell_box,(30,100))

        if self.konuşma == "buy":
            sell_box = pygame.image.load("img/npc_buy.png")   
            ekran.blit(sell_box,(30,100))

        if self.konuşma == "soru":
            self.text_imleç_y = max(342, min(self.text_imleç_y, 368))
            talk_box = pygame.image.load("img/talk_box.png")   
            font = pygame.font.Font('img/SHPinscher-Regular.otf',28)
            font2 = pygame.font.Font('img/SHPinscher-Regular.otf',22)
            text = font.render('Hello farmer, what did you want?',True,(0,0,0))
            text_buy = font2.render('Buy',True,(0,0,0))
            text_sell = font2.render('Sell',True,(0,0,0))
            text_imleç_npc_talk = font2.render('>',True,(0,0,0))
            ekran.blit(talk_box,(30,305))
            ekran.blit(text,(40,310))
            ekran.blit(text_sell,(68,370))
            ekran.blit(text_buy,(68,344))
            ekran.blit(text_imleç_npc_talk,(self.text_imleç_x,self.text_imleç_y))
    # çizdirmek
    def draw(self):
        ekran.blit(self.image, self.rect.topleft)
    # metotları çalıştırma
    def update(self):
        self.wall_hit()
        self.npc_hit()
        self.draw()
        self.tree_hit()
        self.move()
        self.soil_hit()

pygame.init()

width = 960
height = 640
ekildi = False
ekildi_süre = 0
saat = 10
dakika = 0
saniye = 0
gün = 0

ekran = pygame.display.set_mode((width,height))
pygame.display.set_caption("minidew valley")
fps = pygame.time.Clock()
font = pygame.font.Font('img/SHPinscher-Regular.otf',32)

# sınıfları tanımlama
player = Player(x=100,y=100)
walls = [Wall(x=187,y=178),
         Wall(x=32,y=178),
         Wall(x=37,y=178),
         Wall(x=32,y=32),
         Wall(x=70,y=32),
         Wall(x=170,y=32),
         Wall(x=185,y=32)]

walls2 = [Wall2(x=32,y=46),
          Wall2(x=274,y=46)]

soils = [Soil(x=416,y=64),
          Soil(x=448,y=64),
          Soil(x=480,y=64),
          Soil(x=512,y=64),
          Soil(x=544,y=64),
          Soil(x=576,y=64),
          Soil(x=416,y=96),
          Soil(x=448,y=96),
          Soil(x=480,y=96),
          Soil(x=512,y=96),
          Soil(x=544,y=96),
          Soil(x=576,y=96),
          Soil(x=416,y=128),
          Soil(x=448,y=128),
          Soil(x=480,y=128),
          Soil(x=512,y=128),
          Soil(x=544,y=128),
          Soil(x=576,y=128),
          Soil(x=416,y=160),
          Soil(x=448,y=160),
          Soil(x=480,y=160),
          Soil(x=512,y=160),
          Soil(x=544,y=160),
          Soil(x=576,y=160),
          Soil(x=704,y=64),
          Soil(x=736,y=64),
          Soil(x=768,y=64),
          Soil(x=800,y=64),
          Soil(x=832,y=64),
          Soil(x=864,y=64),
          Soil(x=704,y=96),
          Soil(x=736,y=96),
          Soil(x=768,y=96),
          Soil(x=800,y=96),
          Soil(x=832,y=96),
          Soil(x=864,y=96),
          Soil(x=704,y=128),
          Soil(x=736,y=128),
          Soil(x=768,y=128),
          Soil(x=800,y=128),
          Soil(x=832,y=128),
          Soil(x=864,y=128),
          Soil(x=704,y=160),
          Soil(x=736,y=160),
          Soil(x=768,y=160),
          Soil(x=800,y=160),
          Soil(x=832,y=160),
          Soil(x=864,y=160)]

treies = [Tree(x=287,y=240),
         Tree(x=432,y=380)]

wall_treies = [Wall_Tree(x=308,y=310),
         Wall_Tree(x=452,y=450)]

water = Water(x=player.rect.x+20,y=player.rect.y+20)
çapaucu = ÇapaUcu(x=player.rect.x-40,y=player.rect.y-20)

npc = Npc(x=50,y=250)

map = pygame.image.load('img/map.png')
bg = pygame.image.load('img/bg.png')
stop_menu_bg = pygame.image.load('img/stop_menu_box.png')

bed = Bed(x=56,y=90)

# menu
text_imleç_x = 390
text_imleç_y = 230
play = 0
keys = 0
music = 0
music_ses_seviyesi = 0.2

menu_buton = pygame.Rect(450,540,100,64)
keys_menu_menu_buton = pygame.Rect(430,570,100,56)
keys_on = pygame.Rect(470,320,60,64)
keys_off = pygame.Rect(470,400,80,64)
keys_ses = 1
def menu_keys():
    ekran.blit(bg, (0, 0))
    font2 = pygame.font.Font('img/SHPinscher-Regular.otf', 42)
    font4 = pygame.font.Font('img/SHPinscher-Regular.otf', 62)
    font3 = pygame.font.Font('img/SHPinscher-Regular.otf', 170)
    text_Sound = font3.render('KEYS MENU', True, (0, 0, 0))
    ekran.blit(text_Sound, (180, 6))
    text_menu = font4.render('Menu', True, (0, 0, 0))
    ekran.blit(text_menu, (430, 560))
    text_menu = font2.render('KEYS:', True, (0, 0, 0))
    ekran.blit(text_menu, (440, 200))
    text_r = font2.render('Collect plants: r', True, (0, 0, 0))
    ekran.blit(text_r, (230, 260))
    text_bh = font2.render('Plant a plant: The initial of the plant', True, (0, 0, 0))
    ekran.blit(text_bh, (230, 320))   
    text_q = font2.render('Game pause: q', True, (0, 0, 0))
    ekran.blit(text_q, (230, 380))   
    text_e = font2.render('Open inventory: e', True, (0, 0, 0))
    ekran.blit(text_e, (230, 440))   
    text_ee = font2.render('Tools in inventory: Number next to it', True, (0, 0, 0))
    ekran.blit(text_ee, (230, 500))   

music_on = pygame.Rect(470,320,60,64)
music_off = pygame.Rect(470,400,80,64)
music_ses = 1
def menu_music():
    ekran.blit(bg, (0, 0))
    font2 = pygame.font.Font('img/SHPinscher-Regular.otf', 62)
    font3 = pygame.font.Font('img/SHPinscher-Regular.otf', 170)
    text_Sound = font3.render('MUSIC MENU', True, (0, 0, 0))
    ekran.blit(text_Sound, (130, 10))
    text_menu = font2.render('Menu', True, (0, 0, 0))
    ekran.blit(text_menu, (450, 540))
    text_menu = font2.render('Music:', True, (0, 0, 0))
    ekran.blit(text_menu, (440, 240))
    text_menu = font2.render('On', True, (0, 0, 0))
    ekran.blit(text_menu, (470, 320))
    text_menu = font2.render('Off', True, (0, 0, 0))
    ekran.blit(text_menu, (470, 400))   

def menu():
    global text_imleç_x, text_imleç_y, play, run, keys, music
    key = pygame.key.get_pressed()
    ekran.blit(bg, (0, 0))
    font2 = pygame.font.Font('img/SHPinscher-Regular.otf', 62)
    font3 = pygame.font.Font('img/SHPinscher-Regular.otf', 170)
    text_menu = font3.render('MENU', True, (0, 0, 0))
    ekran.blit(text_menu, (340, 10))

    if key[pygame.K_DOWN]:
        time.sleep(0.1)
        text_imleç_y += 100
    if key[pygame.K_UP]:
        time.sleep(0.1)
        text_imleç_y -= 100

    text_imleç_y = max(230, min(text_imleç_y, 530))

    text_imleç = font2.render('>', True, (0, 0, 0))
    ekran.blit(text_imleç, (text_imleç_x, text_imleç_y))
    text_play = font2.render('PLAY', True, (0, 0, 0))
    ekran.blit(text_play, (440, 240))
    text_keys = font2.render('KEYS', True, (0, 0, 0))
    ekran.blit(text_keys, (440, 340))
    text_music = font2.render('MUSIC', True, (0, 0, 0))
    ekran.blit(text_music, (426, 440))
    text_exit = font2.render('EXIT', True, (0, 0, 0))
    ekran.blit(text_exit, (444, 540))
    if key[pygame.K_RETURN]:
        if text_imleç_y == 230 :
           play = 1
        if text_imleç_y == 330 :
           keys = 1
        if text_imleç_y == 430 :
           music = 1
        if text_imleç_y == 530 :
           run = False
    if keys == 1:
        menu_keys()
    if music == 1:
        menu_music()

# zaman ayarlama
def saat_system():
    global saniye, dakika, saat, gün
    saniye+=2
    if saniye >= 100:
      saniye = 0
      dakika+=10
    if dakika >= 60:
        saat+=1
        dakika = 0
    if saat > 24:
        saat = 0
        gün +=1 
    if saat >= 22 or saat <= 4:
        player.bed_hit()

# envanter
def envanter():
   envanter_box = pygame.image.load('img/envanter_box.png')
   fontx = pygame.font.Font('img/SHPinscher-Regular.otf',32)
   text_1 = fontx.render("[1] Hoe", True, (0,0,0))
   text_2 = fontx.render("[2] Watering Can", True, (0,0,0))
   text_3 = fontx.render("[3] Axe", True, (0,0,0))
   text_4 = fontx.render(f"[4] {player.item_1} {player.number__of_item_1}x", True, (0,0,0))
   text_5 = fontx.render(f"[5] {player.item_2} {player.number__of_item_2}x", True, (0,0,0))
   text_6 = fontx.render(f"[6] {player.item_3} {player.number__of_item_3}x", True, (0,0,0))
   text_7 = fontx.render(f"[7] {player.item_4} {player.number__of_item_4}x", True, (0,0,0))
   text_8 = fontx.render(f"[8] {player.item_5} {player.number__of_item_5}x", True, (0,0,0))
   text_9 = fontx.render(f"[9] {player.item_6} {player.number__of_item_6}x", True, (0,0,0))
   text_10 = fontx.render(f"[10] {player.item_7} {player.number__of_item_7}x", True, (0,0,0))
   ekran.blit(envanter_box,(10,10))
   ekran.blit(text_1,(15,15))
   ekran.blit(text_2,(15,50))
   ekran.blit(text_3,(15,85))
   if player.item_1 != "":
     ekran.blit(text_4,(15,120))
   if player.item_2 != "":
     ekran.blit(text_5,(15,155))
   if player.item_3 != "":
     ekran.blit(text_6,(15,190))
   if player.item_4 != "":
     ekran.blit(text_7,(15,225))
   if player.item_5 != "":
     ekran.blit(text_8,(15,260))
   if player.item_6 != "":
     ekran.blit(text_9,(15,295))
   if player.item_7 != "":
     ekran.blit(text_10,(15,330))

# patates_sayısını_envanterde_göster
def patates_seed_envanter_ekle():
      if player.item_1 == "":
          player.item_1 = "Patato Seed"
          player.number__of_item_1 = player.number_of_patates_seed
      elif player.item_1 == "Patato Seed":
          player.number__of_item_1 = player.number_of_patates_seed
      elif player.item_2 == "":
          player.item_2 = "Patato Seed"
          player.number__of_item_2 = player.number_of_patates_seed
      elif player.item_2 == "Patato Seed":
          player.number__of_item_2 = player.number_of_patates_seed
      elif player.item_3 == "":
          player.item_3 = "Patato Seed"
          player.number__of_item_3 = player.number_of_patates_seed
      elif player.item_3 == "Patato Seed":
          player.number__of_item_3 = player.number_of_patates_seed
      elif player.item_4 == "":
          player.item_4 = "Patato Seed"
          player.number__of_item_4 = player.number_of_patates_seed
      elif player.item_4 == "Patato Seed":
          player.number__of_item_4 = player.number_of_patates_seed
      elif player.item_5 == "":
          player.item_5 = "Patato Seed"
          player.number__of_item_5 = player.number_of_patates_seed
      elif player.item_5 == "Patato Seed":
          player.number__of_item_5 = player.number_of_patates_seed
      elif player.item_6 == "":
          player.item_6 = "Patato Seed"
          player.number__of_item_6 = player.number_of_patates_seed
      elif player.item_6 == "Patato Seed":
          player.number__of_item_6 = player.number_of_patates_seed
      elif player.item_7 == "":
          player.item_7 = "Patato Seed"
          player.number__of_item_7 = player.number_of_patates_seed
      elif player.item_7 == "Patato Seed":
          player.number__of_item_7 = player.number_of_patates_seed

# onion_sayısını_envanterde_göster
def onion_seed_envanter_ekle():
      if player.item_1 == "":
          player.item_1 = "Onion Seed"
          player.number__of_item_1 = player.number_of_onion_seed
      elif player.item_1 == "Onion Seed":
          player.number__of_item_1 = player.number_of_onion_seed
      elif player.item_2 == "":
          player.item_2 = "Onion Seed"
          player.number__of_item_2 = player.number_of_onion_seed
      elif player.item_2 == "Onion Seed":
          player.number__of_item_2 = player.number_of_onion_seed
      elif player.item_3 == "":
          player.item_3 = "Onion Seed"
          player.number__of_item_3 = player.number_of_onion_seed
      elif player.item_3 == "Onion Seed":
          player.number__of_item_3 = player.number_of_onion_seed
      elif player.item_4 == "":
          player.item_4 = "Onion Seed"
          player.number__of_item_4 = player.number_of_onion_seed
      elif player.item_4 == "Onion Seed":
          player.number__of_item_4 = player.number_of_onion_seed
      elif player.item_5 == "":
          player.item_5 = "Onion Seed"
          player.number__of_item_5 = player.number_of_onion_seed
      elif player.item_5 == "Onion Seed":
          player.number__of_item_5 = player.number_of_onion_seed
      elif player.item_6 == "":
          player.item_6 = "Onion Seed"
          player.number__of_item_6 = player.number_of_onion_seed
      elif player.item_6 == "Onion Seed":
          player.number__of_item_6 = player.number_of_onion_seed
      elif player.item_7 == "":
          player.item_7 = "Onion Seed"
          player.number__of_item_7 = player.number_of_onion_seed
      elif player.item_7 == "Onion Seed":
          player.number__of_item_7 = player.number_of_onion_seed

# carrot_seed_sayısını_envanterde_göster 
def carrot_seed_envanter_ekle():
      if player.item_1 == "":
          player.item_1 = "Carrot Seed"
          player.number__of_item_1 = player.number_of_carrot_seed
      elif player.item_1 == "Carrot Seed":
          player.number__of_item_1 = player.number_of_carrot_seed
      elif player.item_2 == "":
          player.item_2 = "Carrot Seed"
          player.number__of_item_2 = player.number_of_carrot_seed
      elif player.item_2 == "Carrot Seed":
          player.number__of_item_2 = player.number_of_carrot_seed
      elif player.item_3 == "":
          player.item_3 = "Carrot Seed"
          player.number__of_item_3 = player.number_of_carrot_seed
      elif player.item_3 == "Carrot Seed":
          player.number__of_item_3 = player.number_of_carrot_seed
      elif player.item_4 == "":
          player.item_4 = "Carrot Seed"
          player.number__of_item_4 = player.number_of_carrot_seed
      elif player.item_4 == "Carrot Seed":
          player.number__of_item_4 = player.number_of_carrot_seed
      elif player.item_5 == "":
          player.item_5 = "Carrot Seed"
          player.number__of_item_5 = player.number_of_carrot_seed
      elif player.item_5 == "Carrot Seed":
          player.number__of_item_5 = player.number_of_carrot_seed
      elif player.item_6 == "":
          player.item_6 = "Carrot Seed"
          player.number__of_item_6 = player.number_of_carrot_seed
      elif player.item_6 == "Carrot Seed":
          player.number__of_item_6 = player.number_of_carrot_seed
      elif player.item_7 == "":
          player.item_7 = "Carrot Seed"
          player.number__of_item_7 = player.number_of_carrot_seed
      elif player.item_7 == "Carrot Seed":
          player.number__of_item_7 = player.number_of_carrot_seed

# kaydetme
try:
    with open('player_position.txt') as player_position_file:
        position = json.load(player_position_file)
        player.x = position['x']
        player.y = position['y']
except:
   print("olmadı")
   
try:
    with open('zaman.txt') as zaman_file:
        zaman = json.load(zaman_file)
        saat = zaman['saat']
        dakika = zaman['dakika']
        saniye = zaman['saniye']
except:
   print("olmadı")

pygame.mixer.music.load("img/arka_ses.mp3")
pygame.mixer.music.set_volume(music_ses_seviyesi)
#pygame.mixer.music.play(-1) 

fade_surface = pygame.Surface((width, height))
fade_surface.fill((0, 0, 0)) 
alpha = 0

stop_menu_menu_buton = pygame.Rect(450,310,70,32)
save_exit_button = pygame.Rect(400,190,170,32)
continue_button = pygame.Rect(420,250,130,32)
def stop_menu():
    ekran.blit(stop_menu_bg,(384,170))
    font2 = pygame.font.Font('img/SHPinscher-Regular.otf', 42)
    text_save = font2.render('Save / Exit', True, (0, 0, 0))
    ekran.blit(text_save, (400, 180))
    text_menu = font2.render('Menu', True, (0, 0, 0))
    ekran.blit(text_menu, (450, 300))
    text_continue = font2.render('Continue', True, (0, 0, 0))
    ekran.blit(text_continue, (420, 240))
save_exit = 0
stop_menu_durum = 0
player_continue = 0
tuş_q = 0

# döngü
run = True
while run:
    print(ekildi_süre)
    for event in pygame.event.get():
        key = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            run = False
        elif save_exit == 1:
            run = False
            # çıkarken veri kaydetme
            with open('player_position.txt','w') as player_position_file:
                json.dump({'x': player.x, 'y': player.y}, player_position_file)
            with open('zaman.txt','w') as zaman_file:
                json.dump({'saat': saat, 'dakika': dakika, 'saniye': saniye}, zaman_file)
        # tıklamalar
        elif event.type == pygame.MOUSEBUTTONDOWN:
          if event.button == 1:
            if keys == 1:
               if keys_menu_menu_buton.collidepoint(event.pos):
                 keys=0
                 menu()
               if keys_on.collidepoint(event.pos):
                   keys_ses = 1
               if keys_off.collidepoint(event.pos):
                   keys_ses = 0
            if music == 1:
               if menu_buton.collidepoint(event.pos):
                 music=0
                 menu()
               if music_on.collidepoint(event.pos):
                   music_ses = 1
               if music_off.collidepoint(event.pos):
                   music_ses = 0
            if player.konuşma == "buy":
               if player.buy_p_seed_buton.collidepoint(event.pos) and player.money >= 8:
                   player.number_of_patates_seed += 1
                   player.money -= 8 
                   if player.item_1 == "":
                     player.item_1 = "Patato Seed"
                   if player.item_1 == "Carrot Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Apple" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_1 == "Carrot":
                      if player.item_2 == "":
                        player.item_2 = "Patato Seed"
                   if player.item_2 == "Carrot Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Apple" or player.item_2 == "Patato" or player.item_2 == "Onion" or player.item_2 == "Carrot":
                      if player.item_1 != "Patato Seed" and player.item_2 != "Patato Seed":
                        if player.item_3 == "":
                          player.item_3 = "Patato Seed"
                   if player.item_3 == "Carrot Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Apple" or player.item_3 == "Patato" or player.item_3 == "Onion" or player.item_3 == "Carrot":
                      if player.item_1 != "Patato Seed" and player.item_2 != "Patato Seed" and player.item_3 != "Patato Seed":
                        if player.item_4 == "":
                          player.item_4 = "Patato Seed"
                   if player.item_4 == "Carrot Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Apple" or player.item_4 == "Patato" or player.item_4 == "Onion" or player.item_4 == "Carrot":
                      if player.item_1 != "Patato Seed" and player.item_2 != "Patato Seed" and player.item_3 != "Patato Seed" and player.item_4 != "Patato Seed":
                        if player.item_5 == "":
                          player.item_5 = "Patato Seed"
                   if player.item_5 == "Carrot Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Apple" or player.item_5 == "Onion" or player.item_5 == "Patato" or player.item_5 == "Carrot":
                      if player.item_1 != "Patato Seed" and player.item_2 != "Patato Seed" and player.item_3 != "Patato Seed" and player.item_4 != "Patato Seed" and player.item_5 != "Patato Seed":
                        if player.item_6 == "":
                          player.item_6 = "Patato Seed"
                   if player.item_6 == "Carrot Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Patato" or player.item_6 == "Apple" or player.item_6 == "Onion" or player.item_6 == "Carrot":
                      if player.item_1 != "Patato Seed" and player.item_2 != "Patato Seed" and player.item_3 != "Patato Seed" and player.item_4 != "Patato Seed" and player.item_5 != "Patato Seed" and player.item_6 != "Patato Seed":
                        if player.item_7 == "":
                          player.item_7 = "Patato Seed"
                   patates_seed_envanter_ekle()
                   
               if player.buy_c_seed_buton.collidepoint(event.pos) and player.money >= 5:
                   player.number_of_carrot_seed += 1
                   player.money -= 5
                   if player.item_1 == "":
                     player.item_1 = "Carrot Seed"
                   if player.item_1 == "Patato Seed" or player.item_1 == "Onion Seed" or player.item_1 == "Apple" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_1 == "Carrot":
                      if player.item_2 == "":
                        player.item_2 = "Carrot Seed"
                   if player.item_2 == "Patato Seed" or player.item_2 == "Onion Seed" or player.item_2 == "Apple" or player.item_2 == "Patato" or player.item_2 == "Onion" or player.item_2 == "Carrot":
                      if player.item_1 != "Carrot Seed" and player.item_2 != "Carrot Seed":
                        if player.item_3 == "":
                          player.item_3 = "Carrot Seed"
                   if player.item_3 == "Patato Seed" or player.item_3 == "Onion Seed" or player.item_3 == "Apple" or player.item_3 == "Patato" or player.item_3 == "Onion" or player.item_3 == "Carrot":
                      if player.item_1 != "Carrot Seed" and player.item_2 != "Carrot Seed" and player.item_3 != "Carrot Seed":
                        if player.item_4 == "":
                          player.item_4 = "Carrot Seed"
                   if player.item_4 == "Patato Seed" or player.item_4 == "Onion Seed" or player.item_4 == "Apple" or player.item_4 == "Patato" or player.item_4 == "Onion" or player.item_4 == "Carrot":
                      if player.item_1 != "Carrot Seed" and player.item_2 != "Carrot Seed" and player.item_3 != "Carrot Seed" and player.item_4 != "Carrot Seed":
                        if player.item_5 == "":
                          player.item_5 = "Carrot Seed"
                   if player.item_5 == "Patato Seed" or player.item_5 == "Onion Seed" or player.item_5 == "Apple" or player.item_5 == "Onion" or player.item_5 == "Patato" or player.item_5 == "Carrot":
                      if player.item_1 != "Carrot Seed" and player.item_2 != "Carrot Seed" and player.item_3 != "Carrot Seed" and player.item_4 != "Carrot Seed" and player.item_5 != "Carrot Seed":
                        if player.item_6 == "":
                          player.item_6 = "Carrot Seed"
                   if player.item_6 == "Patato Seed" or player.item_6 == "Onion Seed" or player.item_6 == "Patato" or player.item_6 == "Apple" or player.item_6 == "Onion" or player.item_6 == "Carrot":
                      if player.item_1 != "Carrot Seed" and player.item_2 != "Carrot Seed" and player.item_3 != "Carrot Seed" and player.item_4 != "Carrot Seed" and player.item_5 != "Carrot Seed" and player.item_6 != "Carrot Seed":
                        if player.item_7 == "":
                          player.item_7 = "Carrot Seed"
                   carrot_seed_envanter_ekle()

               if player.buy_o_seed_buton.collidepoint(event.pos) and player.money >= 10:
                   player.number_of_onion_seed += 1
                   player.money -= 10
                   if player.item_1 == "":
                     player.item_1 = "Onion Seed"
                   if player.item_1 == "Carrot Seed" or player.item_1 == "Patato Seed" or player.item_1 == "Apple" or player.item_1 == "Patato" or player.item_1 == "Onion" or player.item_1 == "Carrot":
                      if player.item_2 == "":
                        player.item_2 = "Onion Seed"
                   if player.item_2 == "Carrot Seed" or player.item_2 == "Patato Seed" or player.item_2 == "Apple" or player.item_2 == "Patato" or player.item_2 == "Onion" or player.item_2 == "Carrot":
                      if player.item_1 != "Onion Seed" and player.item_2 != "Onion Seed":
                        if player.item_3 == "":
                          player.item_3 = "Onion Seed"
                   if player.item_3 == "Patato Seed" or player.item_3 == "Carrot Seed" or player.item_3 == "Apple" or player.item_3 == "Patato" or player.item_3 == "Onion" or player.item_3 == "Carrot":
                      if player.item_1 != "Onion Seed" and player.item_2 != "Onion Seed" and player.item_3 != "Onion Seed":
                        if player.item_4 == "":
                          player.item_4 = "Onion Seed"
                   if player.item_4 == "Patato Seed" or player.item_4 == "Carrot Seed" or player.item_4 == "Apple" or player.item_4 == "Patato" or player.item_4 == "Onion" or player.item_4 == "Carrot":
                      if player.item_1 != "Onion Seed" and player.item_2 != "Onion Seed" and player.item_3 != "Onion Seed" and player.item_4 != "Onion Seed":
                        if player.item_5 == "":
                          player.item_5 = "Onion Seed"
                   if player.item_5 == "Carrot Seed" or player.item_5 == "Patato Seed" or player.item_5 == "Apple" or player.item_5 == "Onion" or player.item_5 == "Patato" or player.item_5 == "Carrot":
                      if player.item_1 != "Onion Seed" and player.item_2 != "Onion Seed" and player.item_3 != "Onion Seed" and player.item_4 != "Onion Seed" and player.item_5 != "Onion Seed":
                        if player.item_6 == "":
                          player.item_6 = "Onion Seed"
                   if player.item_6 == "Patato Seed" or player.item_6 == "Carrot Seed" or player.item_6 == "Patato" or player.item_6 == "Apple" or player.item_6 == "Onion" or player.item_6 == "Carrot":
                      if player.item_1 != "Onion Seed" and player.item_2 != "Onion Seed" and player.item_3 != "Onion Seed" and player.item_4 != "Onion Seed" and player.item_5 != "Onion Seed" and player.item_6 != "Onion Seed":
                        if player.item_7 == "":
                          player.item_7 = "Onion Seed"
                   onion_seed_envanter_ekle()

            if player.konuşma == "sell":
               if player.number_of_patato > 0:
                 if player.sell_patato_buton.collidepoint(event.pos) and player.number_of_patato >= 1:
                     player.number_of_patato -= 1
                     player.money += 10
                     player.patates_envanter_ekle() 
               if player.number_of_carrot > 0: 
                   if player.sell_carrot_buton.collidepoint(event.pos) and player.number_of_carrot >= 1:
                     player.number_of_carrot -= 1
                     player.money += 8
                     player.carrot_envanter_ekle()  
               if player.number_of_onion > 0:
                   if player.sell_onion_buton.collidepoint(event.pos):
                     player.number_of_onion -= 1
                     player.money += 12
                     player.onion_envanter_ekle()  
               if player.number_of_apple > 0:
                    if player.sell_apple_buton.collidepoint(event.pos): 
                        player.number_of_apple -= 1
                        player.money += 14
                        player.apple_envanter_ekle()  

            if stop_menu_durum == 1:
               if stop_menu_menu_buton.collidepoint(event.pos):
                 with open('player_position.txt','w') as player_position_file:
                    json.dump({'x': player.x, 'y': player.y}, player_position_file)
                 with open('zaman.txt','w') as zaman_file:
                    json.dump({'saat': saat, 'dakika': dakika, 'saniye': saniye}, zaman_file)
                 menu()
                 play = 0
               if save_exit_button.collidepoint(event.pos):
                 save_exit = 1
               if continue_button.collidepoint(event.pos):
                  player_continue = 1
                  player.haraket = 1
                  
    ekran.fill((0,0,0))
    ekran.blit(map,(0,0))    
    if music_ses == 1 and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play(-1)  
    elif music_ses == 0 and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop() 
    # oyun
    if play == 1:   
        if alpha < 255:
            if saat >= 8:
              alpha += 0.02
            if saat == 6:     
               alpha = 0
        fade_surface.set_alpha(alpha) 
        saat_system()
        if dakika <= 10:
          text_clock = font.render(f'{saat}:{dakika}0', True ,(0,0,0))
        if dakika >= 10:
          text_clock = font.render(f'{saat}:{dakika}', True ,(0,0,0))
        text = font.render('CLOCK', True ,(0,0,0))
        ekran.blit(text_clock,(896,40))
        ekran.blit(text,(890,10))
        bed.draw()
        for soil in soils:
            soil.draw()
        player.update()
        npc.draw()
        for tree in treies:
            tree.draw()
        player.npc_hit()
        if key[pygame.K_e]:
          envanter()
        text_money = font.render(f'Money:{player.money}', True, (0,0,0))
        ekran.blit(text_money, (10,600))
        ekran.blit(fade_surface, (0, 0))
        if key[pygame.K_q]:
            player_continue = 0
            if player_continue == 0:
              tuş_q = 1
              player.haraket = 0
        if tuş_q == 1:
            if player_continue == 0:
              stop_menu_durum = 1
              stop_menu()  

    if play==0 and keys==0:
      menu()
    if keys==1:
      menu_keys()
    pygame.display.flip() 
    fps.tick(90)
pygame.quit()