import customtkinter as ctk
from tkinter import *
import keyboard
import openpyxl
from time import gmtime, strftime
import pygame


global n_sec, Npoints,i,winner, questions, verif_arret, interface_screen, interface
global save_chrono, pointM1E1, pointM2E1, pointM3E1, pointM1E2, pointM2E2, pointM3E2, pointsM1E3, pointsM2E3, pointsM3E3, pointsE3, pointE1, pointE2, penalite1,penalite2, verif_stop, bonus_E1, bonus_E2
pointM1E1=pointM2E1=pointM3E1=pointM1E2=pointM2E2=pointM3E2=pointsM1E3=pointsM2E3=pointsM3E3=pointE1=pointE2=pointsE3=penalite1=penalite2=bonus_E1=bonus_E2=0
n_sec=save_chrono=10
Npoints=10
verif_arret = False
i=0
verif_stop=FALSE
# Ouverture du fichier Excel
fichier_excel = openpyxl.load_workbook("infos.xlsx")

# Sélection de la feuille contenant les paramètres (worksheet) par son nom
feuille = fichier_excel["data"]

# Fermer le fichier Excel
fichier_excel.close()

# Lecture du contenu d'une cellule spécifique
#cellule = feuille['A1']  # Par exemple, lecture de la cellule A1
# Afficher la valeur de la cellule
#valeur_cellule = cellule.value
#print("Contenu de la cellule A1 :", valeur_cellule)



# Affectation des noms des joueurs à leur variables correspondantes pour affichage
#Equipe1
nom_E1=feuille['B4'].value
nom_E1M1=feuille['C4'].value
nom_E1M2=feuille['D4'].value
nom_E1M3=feuille['E4'].value
#Equipe2
nom_E2=feuille['B5'].value
nom_E2M1=feuille['C5'].value
nom_E2M2=feuille['D5'].value
nom_E2M3=feuille['E5'].value
#Equipe3
nom_E3=feuille['B6'].value
nom_E3M1=feuille['C6'].value
nom_E3M2=feuille['D6'].value
nom_E3M3=feuille['E6'].value

#Sélection manuelle du thème : entrées manuelles
while True:
    saisie = input("Veuillez sélectionner un mode (0 pour défaut , 1 pour Light et 2 pour Dark) : ")
    if saisie == "0":
        var_mode = "System"
        break
    elif saisie == "1":
        var_mode = "Light"
        break
    elif saisie == "2":
        var_mode = "Dark"
        break
    else:
        print("Saisie invalide. Veuillez entrer 0 ou 1 ou 2.")
    
    interface = input("Veuillez selectionner l'interface (2 pour deux joueurs et 3 pour trois joueurs)")
    if interface == "2" or interface == "3":
        interface_screen = interface
        break
    else:
        print("La saisie est non valide")

print("Vous avez choisi le mode :", var_mode)

ctk.set_appearance_mode(var_mode)  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
pygame.init()
#Importation des questions et des réponses
questions = open('Questons.txt', 'r', encoding = 'utf-8').readlines()
reponses = open('Réponse.txt', 'r', encoding = 'utf-8').readlines()
colours = ['blue', 'red', 'yellow', 'green', 'pink']
class App3(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.bind("<Right>", self.print_question)
        self.bind("<Left>", self.previous_question)
        self.bind("<Return>", self.print_answer2)

        # configure window
        self.title("Application Génie en Herbe Club Leadership")
        self.geometry('1140x650')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1) # La largeur de la 2e colonne s'adaptera aux changements effectués sur la taille de la fenêtre
        self.grid_columnconfigure((0,2), weight=0) # quand on va redimensionner la largeyr de la fenêtre, la 1ere et la 3e colonne ne verront pas leurs largeurs etre modifiée.
        self.grid_rowconfigure((0, 1, 2), weight=1) # Les dimensions des 3 lignes s'adapteront aux changements effectués sur la taille de la fenêtre

        # create sidebar frame with widgets
        """
        #Première colonne
        self.sidebar_frame1 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame1.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame1.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.logo_label1 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E1, font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label1.grid(row=0, column=0, padx=20, pady=(20, 10))
        """
        # Trois Premières lignes frame 1 (pour les équipes)
        self.sidebar_frame1 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame1.grid(row=0, column=0, columnspan=8, rowspan=3, sticky="nsew")
        self.sidebar_frame1.grid_columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)
        self.sidebar_frame1.grid_rowconfigure((0,1,2), weight=1)
        #self.logo_label1 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E1, font=ctk.CTkFont(size=24, weight="bold"))
        #self.logo_label1.grid(row=0, column=0, padx=20, pady=(20, 10))

        # Trois Premières lignes frame 1 (pour les boutons de commandes)
        self.sidebar_frame2 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame2.grid(row=0, column=8, columnspan=2, rowspan=3, sticky="nsew")
        self.sidebar_frame2.grid_columnconfigure((0,1,2,3,4,5,6,7), weight=1)
        self.sidebar_frame2.grid_rowconfigure((0,1,2), weight=1)

        """
        #Troisième colonne
        self.sidebar_frame2 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=8, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.logo_label2 = ctk.CTkLabel(self.sidebar_frame2, text=nom_E2, font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label2.grid(row=0, column=2, padx=20, pady=(20, 10))
        """
        # Quatrième ligne (pour le question box)
        self.sidebar_frame3 = ctk.CTkFrame(self, height=350, corner_radius=10)
        self.sidebar_frame3.grid(row=3, column=0, columnspan=10, sticky="nsew")
        #self.sidebar_frame3.grid_rowconfigure((1,2), weight=1)
        self.sidebar_frame3.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        # Cinquième ligne (pour le answer box)
        self.sidebar_frame4 = ctk.CTkFrame(self, height=125, corner_radius=10)
        self.sidebar_frame4.grid(row=4, column=0, columnspan=10, sticky="nsew")
        #self.sidebar_frame3.grid_rowconfigure((1,2), weight=1)
        self.sidebar_frame4.grid_columnconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)

        """
        #seconde colonne frame 1
        self.sidebar_frame_c = ctk.CTkFrame(self, height=30, corner_radius=10)
        self.sidebar_frame_c.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.sidebar_frame_c.grid_rowconfigure((1,2), weight=1)
        self.sidebar_frame_c.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)
        """

        """
        #seconde colonne frame 2
        self.sidebar_frame_c1 = ctk.CTkFrame(self,height=30, corner_radius=10)
        self.sidebar_frame_c1.grid(row=1, column=1, rowspan=4, sticky="nsew")
        self.sidebar_frame_c1.grid_rowconfigure((0,1), weight=0)
        self.sidebar_frame_c1.grid_columnconfigure((0,1,2,3), weight=1)
        """
        

        #Options pour le mode dark ou light  
        #self.mode_label = ctk.CTkLabel(self.sidebar_frame_c, text="Mode", font=ctk.CTkFont(size=14, weight="bold"))
        #self.mode_label.grid(row=0, column=0, padx=0, pady=(15, 15))
        #self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["Dark","Light" , "System"], command=self.change_appearance_mode_event,font=ctk.CTkFont(size=14))
        #self.appearance_mode_optionemenu.grid(row=0, column=1, padx=5, pady=(15, 15))

        #Nombre de points accordés
        self.nombre_de_points_label = ctk.CTkLabel(self.sidebar_frame2, text="Points \naccordés", font=ctk.CTkFont(size=14, weight="bold"))
        self.nombre_de_points_label.grid(row=0, column=8, padx=(15,5), pady=(15, 10))
        self.nombre_de_points_menu = ctk.CTkOptionMenu(self.sidebar_frame2, values=["10","15","20","30","40","-40","-30","-20","-10"],
                                                                       command=self.nombre_de_points,font=ctk.CTkFont(size=18))
        self.nombre_de_points_menu.grid(row=0, column=9, padx=(0,0), pady=(15, 10))

        #Choix du temps du chronomètre
        self.temps_chrono_label = ctk.CTkLabel(self.sidebar_frame2, text="Temps \nChrono", font=ctk.CTkFont(size=14, weight="bold"))
        self.temps_chrono_label.grid(row=1, column=8, padx=(15,5), pady=(15, 10))
        self.temps_chrono_menu = ctk.CTkOptionMenu(self.sidebar_frame2, values=["10","15","20","25","30","60", "120"],
                                                                       command=self.temps_chrono,font=ctk.CTkFont(size=18))
        self.temps_chrono_menu.grid(row=1, column=9, padx=(3,3), pady=(15, 10))

        #Activation du chronomètre
        self.chrono_btn = ctk.CTkButton(self.sidebar_frame2, command=self.start, text="Start")
        self.chrono_btn.grid(row=3, column=8, padx=(15,10), pady=(15, 10))
        self.chrono_btn.configure(font=ctk.CTkFont(size=20, weight="bold"))
        
        
        #Boutton d'affichage du gagnant :
        self.print_winner = ctk.CTkButton(self.sidebar_frame2, command=self.winner, text="Gagnant")
        self.print_winner.grid(row=3, column=9, padx=(15,10), pady=(15, 10))
        self.print_winner.configure(font=ctk.CTkFont(size=20, weight="bold"))

        """
        #Création de l'UI de l'échelle
        self.zoom_label = ctk.CTkLabel(self.sidebar_frame_c, text="Scale", font=ctk.CTkFont(size=14, weight="bold"))
        self.zoom_label.grid(row=0, column=4, padx=(15,5), pady=(15, 15))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=0, column=5, padx=(0,0), pady=(15, 15))
        """

        #Membres des équipes
        self.logo_label1 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E1, font=ctk.CTkFont(size=16, weight="bold"))
        self.logo_label1.grid(row=0, column=0, padx=15, pady=(15, 10))
        #Membre 1 Equipe 1
        self.membre1e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre1e1, text=nom_E1M1)
        self.membre1e1btn.grid(row=0, column=2, padx=20, pady=10)
        #Score Membre 1 Equipe 1
        self.scoreM1E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM1E1_label.grid(row=0, column=3, padx=20, pady=(15, 10))

        #Membre2 Equipe 1
        self.membre2e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre2e1, text=nom_E1M2)
        self.membre2e1btn.grid(row=0, column=4, padx=20, pady=10)
        #Score Membre2 Equipe 1
        self.scoreM2E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM2E1_label.grid(row=0, column=5, padx=20, pady=(15, 10))

        #Membre3 equipe 1
        self.membre3e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre3e1, text=nom_E1M3)
        self.membre3e1btn.grid(row=0, column=6, padx=20, pady=10)
        #Score Membre3 Equipe 1
        self.scoreM3E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM3E1_label.grid(row=0, column=7, padx=20, pady=(15, 10))
        """
        #Score Equipe 1
        self.scoreE1_label = ctk.CTkLabel(self.sidebar_frame1, text="Nombre de points", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreE1_label.grid(row=0, column=1, padx=20, pady=(20, 10))
        """
        #case du score
        self.scoreE1 = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=18, weight="bold"))
        self.scoreE1.grid(row=0, column=1, padx=20, pady=(15, 10))

        #Pénalités Equipe 1
        # self.penaliteE1btn = ctk.CTkButton(self.sidebar_frame1, command=self.penaliteE2_command, text="Pénalités")
        # self.penaliteE1btn.grid(row=9, column=0, padx=20, pady=10)
        # self.penaliteE1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        # self.penaliteE1_label.grid(row=10, column=0, padx=20, pady=(20, 10))

        #Equipe 2

        self.logo_label2 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E2, font=ctk.CTkFont(size=16, weight="bold"))
        self.logo_label2.grid(row=1, column=0, padx=20, pady=(15, 10))
        #Membre 1 Equipe 2
        self.membre1e2btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre1e2, text=nom_E2M1)
        self.membre1e2btn.grid(row=1, column=2, padx=20, pady=10)
        #Score Membre 1 Equipe 2
        self.scoreM1E2_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM1E2_label.grid(row=1, column=3, padx=20, pady=(15, 10))

        #Membre2 Equipe 2
        self.membre2e2btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre2e2, text=nom_E2M2)
        self.membre2e2btn.grid(row=1, column=4, padx=20, pady=10)
        #Score Membre 2 Equipe 2
        self.scoreM2E2_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM2E2_label.grid(row=1, column=5, padx=20, pady=(15, 10))

        #Membre3 equipe 2
        self.membre3e2btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre3e2, text=nom_E2M3)
        self.membre3e2btn.grid(row=1, column=6, padx=20, pady=10)
        #Score Membre 3 Equipe 2
        self.scoreM3E2_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM3E2_label.grid(row=1, column=7, padx=20, pady=(15, 10))

        """
        #Score Equipe 2
        self.scoreE2_label = ctk.CTkLabel(self.sidebar_frame1, text="Nombre de points", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreE2_label.grid(row=7, column=2, padx=20, pady=(20, 10))
        """

        #case du score
        self.scoreE2 = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=18, weight="bold"))
        self.scoreE2.grid(row=1, column=1, padx=20, pady=(15, 10))

        #Pénalités Equipe 2
        #self.penaliteE2btn = ctk.CTkButton(self.sidebar_frame2, command=self.penaliteE2_command, text="Pénalités")
        #self.penaliteE2btn.grid(row=9, column=2, padx=20, pady=10)
        #self.penaliteE2_label = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        #self.penaliteE2_label.grid(row=10, column=2, padx=20, pady=(20, 10))

         #Equipe 3
        
        self.logo_label3 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E3, font=ctk.CTkFont(size=16, weight="bold"))
        self.logo_label3.grid(row=2, column=0, padx=20, pady=(15, 10))
        #Membre 1 Equipe 2
        self.membre1e3btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre1e3, text=nom_E3M1)
        self.membre1e3btn.grid(row=2, column=2, padx=20, pady=10)
        #Score Membre 1 Equipe 2
        self.scoreM1E3_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM1E3_label.grid(row=2, column=3, padx=20, pady=(15, 10))

        #Membre2 Equipe 2
        self.membre2e3btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre2e3, text=nom_E3M2)
        self.membre2e3btn.grid(row=2, column=4, padx=20, pady=10)
        #Score Membre 2 Equipe 2
        self.scoreM2E3_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM2E3_label.grid(row=2, column=5, padx=20, pady=(15, 10))

        #Membre3 equipe 2
        self.membre3e3btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre3e3, text=nom_E3M3)
        self.membre3e3btn.grid(row=2, column=6, padx=20, pady=10)
        #Score Membre 3 Equipe 2
        self.scoreM3E3_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM3E3_label.grid(row=2, column=7, padx=20, pady=(15, 10))

        """
        #Score Equipe 2
        self.scoreE2_label = ctk.CTkLabel(self.sidebar_frame1, text="Nombre de points", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreE2_label.grid(row=7, column=2, padx=20, pady=(20, 10))
        """

        #case du score
        self.scoreE3 = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=18, weight="bold"))
        self.scoreE3.grid(row=2, column=1, padx=20, pady=(15, 10))

        # creation de textbox questions et réponses
        #Questions
        self.Questions_textbox = ctk.CTkTextbox(self,height=350, corner_radius=20)
        self.Questions_textbox.grid(row=3, column=0, columnspan=10, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.Questions_textbox.configure(font=ctk.CTkFont(size=24, weight="bold"))

        #Réponses
        self.Reponses_textbox = ctk.CTkTextbox(self, height=125, corner_radius=20)
        self.Reponses_textbox.grid(row=4, column=0, columnspan=10, padx=(0, 0), pady=(5, 10), sticky="nsew")
        self.Reponses_textbox.configure(font=ctk.CTkFont(size=24, weight="bold"))


        #Valeurs par défaut 
        self.Questions_textbox.insert("0.0", "Questions" )
        self.Reponses_textbox.insert("0.0", "Réponses" )

    #Nombre de seconde
    n_sec=10
    def start(self):
        global n_sec, verif_stop, verif_arret
        if n_sec < 0:
            print("evoor!!!")
            self.chrono_btn.configure(text = "Start")
            if verif_stop==FALSE:
                pygame.mixer.music.load("sons/alarme.mp3")
                pygame.mixer.music.play()
            verif_stop=FALSE
            n_sec=save_chrono
        elif keyboard.is_pressed('F5'):
            # f5: pause du chronomètre
             self.chrono_btn.configure(text = strftime('%M:%S', gmtime(n_sec)))
             self.after(1, self.start)
        elif keyboard.is_pressed('F6'):
             # f6 : mettre le chronomètre à 0
              n_sec = 0
              self.after(1, self.start)
              verif_stop = TRUE
        else:
            if not verif_arret:
                self.chrono_btn.configure(text=strftime('%M:%S', gmtime(n_sec)))
                n_sec = n_sec - 1
                self.after(1000, self.start)
            else:
                verif_arret = False

    def arret_chrono(self,event):
        global n_sec, verif_arret
        n_sec = -1
        verif_arret = True
        self.start()
        self.after_cancel(self.chrono_btn.configure)

    # def sidebar_button_event(self):
    #         print("sidebar_button click")
    
    #def change_appearance_mode_event(self, new_appearance_mode: str):
    #    ctk.set_appearance_mode(new_appearance_mode)

    def nombre_de_points(self,choix : str):
        global Npoints
        Npoints=int(choix)
        print(choix)
    
    
    def temps_chrono(self,n_sec1 : str):
        global n_sec, save_chrono
        n_sec=int(n_sec1)
        save_chrono=int(n_sec1)
        print(n_sec)
    
    #Fonctions de points
    #Membre 1 Equipe 1
    def point_membre1e1(self):
         global pointM1E1
         pointM1E1+=Npoints
         self.scoreM1E1_label.configure(text = str(pointM1E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 2 Equipe 1
    def point_membre2e1(self):
         global pointM2E1
         pointM2E1+=Npoints
         self.scoreM2E1_label.configure(text = str(pointM2E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 3 Equipe 1
    def point_membre3e1(self):
         global pointM3E1
         pointM3E1+=Npoints
         self.scoreM3E1_label.configure(text = str(pointM3E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 1 Equipe 2
    def point_membre1e2(self):
         global pointM1E2
         pointM1E2+=Npoints
         self.scoreM1E2_label.configure(text = str(pointM1E2))
         self.print_answer1()
         self.point_E2()
    
    #Membre 2 Equipe 2
    def point_membre2e2(self):
         global pointM2E2
         pointM2E2+=Npoints
         self.scoreM2E2_label.configure(text = str(pointM2E2))
         self.print_answer1()
         self.point_E2()
    
    #Membre 3 Equipe 2
    def point_membre3e2(self):
         global pointM3E2
         pointM3E2+=Npoints
         self.scoreM3E2_label.configure(text = str(pointM3E2))
         self.print_answer1()
         self.point_E2()

    #Membre 1 Equipe 3
    def point_membre1e3(self):
         global pointsM1E3
         pointsM1E3+=Npoints
         self.scoreM1E3_label.configure(text = str(pointsM1E3))
         self.print_answer1()
         self.point_E3()
    
    #Membre 2 Equipe 3
    def point_membre2e3(self):
         global pointsM2E3
         pointsM2E3+=Npoints
         self.scoreM2E3_label.configure(text = str(pointsM2E3))
         self.print_answer1()
         self.point_E3()
    
    #Membre 3 Equipe 2
    def point_membre3e3(self):
         global pointsM3E3
         pointsM3E3+=Npoints
         self.scoreM3E3_label.configure(text = str(pointsM3E3))
         self.print_answer1()
         self.point_E3()
    
    #Fonction de points total
    def point_E1(self):
         global pointM1E1, pointM2E1, pointM3E1#, penalite1
         pointE1=pointM1E1+pointM2E1+ pointM3E1#+penalite1
         self.scoreE1.configure(text = str(pointE1))
    
    def point_E2(self):
         global pointM1E2, pointM2E2, pointM3E2#, penalite2
         pointE2=pointM1E2+pointM2E2+ pointM3E2#+ penalite2
         self.scoreE2.configure(text = str(pointE2))

    def point_E3(self):
         global pointsM1E3, pointsM2E3, pointsM3E3
         pointE3=pointsM1E3+pointsM2E3+ pointsM3E3
         self.scoreE3.configure(text = str(pointE3))
    
    #Fonction d'affichage des questions
    def print_question(self, event):
        global questions
        global i
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.insert("0.0", "")
        i = i+1
        self.Questions_textbox.delete("0.0", "end")  # delete all text
        self.Questions_textbox.insert("0.0", questions[i])
        self.Questions_textbox.configure(wrap="word")
        print(i)
    
    def previous_question(self, event):
        global i
        global questions
        self.Questions_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.insert("0.0", "")
        i = i-1
        self.Questions_textbox.insert("0.0", questions[i])
        self.Questions_textbox.configure(wrap="word")
    
    #Fonction d'attribution des pénalités
    #def penaliteE1_command(self):
    #     global penalite1
    #     penalite1-=Npoints
    #     self.penaliteE1_label.configure(text = str(penalite1))
    #     self.point_E1()
    
    #def penaliteE2_command(self):
    #    global penalite2
    #     penalite2-=Npoints
    #     self.penaliteE2_label.configure(text = str(penalite2))
    #     self.point_E2()
    
    #Fonction d'affichage de la réponse
    def print_answer1(self):
        global i, reponses
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.configure(wrap="word")
        self.Reponses_textbox.insert("0.0", reponses[i])
    
    def print_answer2(self,event):#event pour la gestion par le clavier
        global i, reponses
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.configure(wrap="word")
        self.Reponses_textbox.insert("0.0", reponses[i])
    
    #Fonction d'échelle d'affichage
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    
    #fonction d'affichage du gagnant
    
    def winner(self : str):  
        global pointM1E1, pointM2E1,  pointM3E1, pointM1E2, pointM2E2,  pointM3E2, pointsM1E3, pointsM2E3, pointsM3E3
        pointE1=pointM1E1+pointM2E1+ pointM3E1
        pointE2=pointM1E2+pointM2E2+ pointM3E2
        pointE3 = pointsM1E3+pointsM2E3+pointsM3E3
        
        #winner = nom_E1 if pointE1 > pointE2 else nom_E2

        if pointE1 > pointE2 and pointE1 > pointE3:
            winner = nom_E1
        elif pointE2 > pointE1 and pointE2 > pointE3:
            winner = nom_E2
        elif pointE3 > pointE1 and pointE3 > pointE2:
            winner = nom_E3
        else:
            winner = "Pas Prévu"

        window = Toplevel()
        window.geometry("1195x700")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 700,
            width = 1195,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background.png")
        background = canvas.create_image(
            608.5, 367.5,
            image=background_img)

        canvas.create_text(
            609.0, 299.0,
            text = winner,
            fill = "#ffff8e",
            font = ("Italianno-Regular", int(100.0)))

        window.resizable(False, False)
        window.mainloop()

class App2(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.bind("<Right>", self.print_question)
        self.bind("<Left>", self.previous_question)
        self.bind("<Return>", self.print_answer2)

        # configure window
        self.title("Application Génie en Herbe Club Leadership")
        self.geometry('1140x650')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        #Première colonne
        self.sidebar_frame1 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame1.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.sidebar_frame1.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.logo_label1 = ctk.CTkLabel(self.sidebar_frame1, text=nom_E1, font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label1.grid(row=0, column=0, padx=20, pady=(20, 10))
        #Troisième colonne
        self.sidebar_frame2 = ctk.CTkFrame(self, width=250, corner_radius=10)
        self.sidebar_frame2.grid(row=0, column=2, rowspan=8, sticky="nsew")
        self.sidebar_frame2.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.logo_label2 = ctk.CTkLabel(self.sidebar_frame2, text=nom_E2, font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label2.grid(row=0, column=2, padx=20, pady=(20, 10))

        #seconde colonne frame 1
        self.sidebar_frame_c = ctk.CTkFrame(self, height=30, corner_radius=10)
        self.sidebar_frame_c.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.sidebar_frame_c.grid_rowconfigure((1,2), weight=1)
        self.sidebar_frame_c.grid_columnconfigure((0,1,2,3,4,5,6), weight=1)

        #seconde colonne frame 2
        self.sidebar_frame_c1 = ctk.CTkFrame(self,height=30, corner_radius=10)
        self.sidebar_frame_c1.grid(row=1, column=1, rowspan=4, sticky="nsew")
        self.sidebar_frame_c1.grid_rowconfigure((0,1), weight=0)
        self.sidebar_frame_c1.grid_columnconfigure((0,1,2,3), weight=1)

        #Options pour le mode dark ou light  
        #self.mode_label = ctk.CTkLabel(self.sidebar_frame_c, text="Mode", font=ctk.CTkFont(size=14, weight="bold"))
        #self.mode_label.grid(row=0, column=0, padx=0, pady=(15, 15))
        #self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["Dark","Light" , "System"], command=self.change_appearance_mode_event,font=ctk.CTkFont(size=14))
        #self.appearance_mode_optionemenu.grid(row=0, column=1, padx=5, pady=(15, 15))

        #Nombre de points accordés
        self.nombre_de_points_label = ctk.CTkLabel(self.sidebar_frame_c, text="Points \naccordés", font=ctk.CTkFont(size=14, weight="bold"))
        self.nombre_de_points_label.grid(row=0, column=0, padx=(15,5), pady=(15, 15))
        self.nombre_de_points_menu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["10","15","20","30","40","-40","-30","-20","-10"],
                                                                       command=self.nombre_de_points,font=ctk.CTkFont(size=18))
        self.nombre_de_points_menu.grid(row=0, column=1, padx=(0,0), pady=(15, 15))

        #Choix du temps du chronomètre
        self.temps_chrono_label = ctk.CTkLabel(self.sidebar_frame_c, text="Temps \nChrono", font=ctk.CTkFont(size=14, weight="bold"))
        self.temps_chrono_label.grid(row=0, column=2, padx=(15,5), pady=(15, 15))
        self.temps_chrono_menu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["10","15","20","25","30","60", "120"],
                                                                       command=self.temps_chrono,font=ctk.CTkFont(size=18))
        self.temps_chrono_menu.grid(row=0, column=3, padx=(0,0), pady=(15, 15))

        #Activation du chronomètre
        self.chrono_btn = ctk.CTkButton(self.sidebar_frame_c1, command=self.start, text="Start")
        self.chrono_btn.grid(row=0, column=2, padx=(80,80), pady=(5, 5))
        self.chrono_btn.configure(font=ctk.CTkFont(size=24, weight="bold"))
        
        
        #Boutton d'affichage du gagnant :
        self.print_winner = ctk.CTkButton(self.sidebar_frame_c1, command=self.winner, text="Gagnant")
        self.print_winner.grid(row=0, column=3, padx=(80,80), pady=(7, 5))
        self.print_winner.configure(font=ctk.CTkFont(size=24, weight="bold"))

        # Points recus grace au public
        self.bonus_public_label = ctk.CTkLabel(self.sidebar_frame_c1, text="Bonus \nPublic", font=ctk.CTkFont(size=18, weight="bold"))
        self.bonus_public_label.grid(row=0, column=0, padx=(10,10), pady=(5, 5))
        self.point_public_menu = ctk.CTkOptionMenu(self.sidebar_frame_c1, values=[nom_E1,nom_E2],command=self.Bonus_public,font=ctk.CTkFont(size=18))
        self.point_public_menu.grid(row=0, column=1, padx=(10,10), pady=(5,5))
        #Création de l'UI de l'échelle
        self.zoom_label = ctk.CTkLabel(self.sidebar_frame_c, text="Scale", font=ctk.CTkFont(size=14, weight="bold"))
        self.zoom_label.grid(row=0, column=4, padx=(15,5), pady=(15, 15))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame_c, values=["100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=0, column=5, padx=(0,0), pady=(15, 15))

        #Membres des équipes
        #Membre 1 Equipe 1
        self.membre1e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre1e1, text=nom_E1M1)
        self.membre1e1btn.grid(row=1, column=0, padx=20, pady=10)
        #Score Membre 1 Equipe 1
        self.scoreM1E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM1E1_label.grid(row=2, column=0, padx=20, pady=(20, 10))

        #Membre2 Equipe 1
        self.membre2e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre2e1, text=nom_E1M2)
        self.membre2e1btn.grid(row=3, column=0, padx=20, pady=10)
        #Score Membre2 Equipe 1
        self.scoreM2E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM2E1_label.grid(row=4, column=0, padx=20, pady=(20, 10))

        #Membre3 equipe 1
        self.membre3e1btn = ctk.CTkButton(self.sidebar_frame1, command=self.point_membre3e1, text=nom_E1M3)
        self.membre3e1btn.grid(row=5, column=0, padx=20, pady=10)
        #Score Membre2 Equipe 1
        self.scoreM3E1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM3E1_label.grid(row=6, column=0, padx=20, pady=(20, 10))

        #Score Equipe 1
        self.scoreE1_label = ctk.CTkLabel(self.sidebar_frame1, text="Nombre de points", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreE1_label.grid(row=7, column=0, padx=20, pady=(20, 10))
        #case du score
        self.scoreE1 = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=18, weight="bold"))
        self.scoreE1.grid(row=8, column=0, padx=20, pady=(20, 10))

        #Pénalités Equipe 1
        # self.penaliteE1btn = ctk.CTkButton(self.sidebar_frame1, command=self.penaliteE2_command, text="Pénalités")
        # self.penaliteE1btn.grid(row=9, column=0, padx=20, pady=10)
        # self.penaliteE1_label = ctk.CTkLabel(self.sidebar_frame1, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        # self.penaliteE1_label.grid(row=10, column=0, padx=20, pady=(20, 10))

        #Membre 1 Equipe 2
        self.membre1e2btn = ctk.CTkButton(self.sidebar_frame2, command=self.point_membre1e2, text=nom_E2M1)
        self.membre1e2btn.grid(row=1, column=2, padx=20, pady=10)
        #Score Membre 1 Equipe 2
        self.scoreM1E2_label = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM1E2_label.grid(row=2, column=2, padx=20, pady=(20, 10))

        #Membre2 Equipe 2
        self.membre2e2btn = ctk.CTkButton(self.sidebar_frame2, command=self.point_membre2e2, text=nom_E2M2)
        self.membre2e2btn.grid(row=3, column=2, padx=20, pady=10)
        #Score Membre 2 Equipe 2
        self.scoreM2E2_label = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM2E2_label.grid(row=4, column=2, padx=20, pady=(20, 10))

        #Membre3 equipe 2
        self.membre3e2btn = ctk.CTkButton(self.sidebar_frame2, command=self.point_membre3e2, text=nom_E2M3)
        self.membre3e2btn.grid(row=5, column=2, padx=20, pady=10)
        #Score Membre 3 Equipe 2
        self.scoreM3E2_label = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreM3E2_label.grid(row=6, column=2, padx=20, pady=(20, 10))

        #Score Equipe 2
        self.scoreE2_label = ctk.CTkLabel(self.sidebar_frame2, text="Nombre de points", font=ctk.CTkFont(size=16, weight="bold"))
        self.scoreE2_label.grid(row=7, column=2, padx=20, pady=(20, 10))
        #case du score
        self.scoreE2 = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=18, weight="bold"))
        self.scoreE2.grid(row=8, column=2, padx=20, pady=(20, 10))

        #Pénalités Equipe 2
        #self.penaliteE2btn = ctk.CTkButton(self.sidebar_frame2, command=self.penaliteE2_command, text="Pénalités")
        #self.penaliteE2btn.grid(row=9, column=2, padx=20, pady=10)
        #self.penaliteE2_label = ctk.CTkLabel(self.sidebar_frame2, text="0", font=ctk.CTkFont(size=16, weight="bold"))
        #self.penaliteE2_label.grid(row=10, column=2, padx=20, pady=(20, 10))

        # creation de textbox questions et réponses
        #Questions
        self.Questions_textbox = ctk.CTkTextbox(self,height=275, corner_radius=20)
        self.Questions_textbox.grid(row=2, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        self.Questions_textbox.configure(font=ctk.CTkFont(size=24, weight="bold"))

        #Réponses
        self.Reponses_textbox = ctk.CTkTextbox(self, height=125, corner_radius=20)
        self.Reponses_textbox.grid(row=3, column=1, padx=(0, 0), pady=(20, 10), sticky="nsew")
        self.Reponses_textbox.configure(font=ctk.CTkFont(size=24, weight="bold"))


        #Valeurs par défaut 
        self.Questions_textbox.insert("0.0", "Questions" )
        self.Reponses_textbox.insert("0.0", "Réponses" )

    #Nombre de seconde
    n_sec=10
    def start(self):
        global n_sec, verif_stop, verif_arret
        if n_sec < 0:
            print("evoor!!!")
            self.chrono_btn.configure(text = "Start")
            if verif_stop==FALSE:
                pygame.mixer.music.load("sons/alarme.mp3")
                pygame.mixer.music.play()
            verif_stop=FALSE
            n_sec=save_chrono
        elif keyboard.is_pressed('F5'):
            # f5: pause du chronomètre
             self.chrono_btn.configure(text = strftime('%M:%S', gmtime(n_sec)))
             self.after(1, self.start)
        elif keyboard.is_pressed('F6'):
             # f6 : mettre le chronomètre à 0
              n_sec = 0
              self.after(1, self.start)
              verif_stop = TRUE
        else:
            if not verif_arret:
                self.chrono_btn.configure(text=strftime('%M:%S', gmtime(n_sec)))
                n_sec = n_sec - 1
                self.after(1000, self.start)
            else:
                verif_arret = False
    
    def arret_chrono(self,event):
        global n_sec, verif_arret
        n_sec = -1
        verif_arret = True
        self.start()
        self.after_cancel(self.chrono_btn.configure)
        
        

    # def sidebar_button_event(self):
    #         print("sidebar_button click")
    
    #def change_appearance_mode_event(self, new_appearance_mode: str):
    #    ctk.set_appearance_mode(new_appearance_mode)

    def nombre_de_points(self,choix : str):
        global Npoints
        Npoints=int(choix)
        print(choix)
    
    
    def temps_chrono(self,n_sec1 : str):
        global n_sec, save_chrono
        n_sec=int(n_sec1)
        save_chrono=int(n_sec1)
        print(n_sec)
    
    #Fonctions de points
    #Membre 1 Equipe 1
    def point_membre1e1(self):
         global pointM1E1
         pointM1E1+=Npoints
         self.scoreM1E1_label.configure(text = str(pointM1E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 2 Equipe 1
    def point_membre2e1(self):
         global pointM2E1
         pointM2E1+=Npoints
         self.scoreM2E1_label.configure(text = str(pointM2E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 3 Equipe 1
    def point_membre3e1(self):
         global pointM3E1
         pointM3E1+=Npoints
         self.scoreM3E1_label.configure(text = str(pointM3E1))
         self.print_answer1()
         self.point_E1()
    
    #Membre 1 Equipe 2
    def point_membre1e2(self):
         global pointM1E2
         pointM1E2+=Npoints
         self.scoreM1E2_label.configure(text = str(pointM1E2))
         self.print_answer1()
         self.point_E2()
    
    #Membre 2 Equipe 2
    def point_membre2e2(self):
         global pointM2E2
         pointM2E2+=Npoints
         self.scoreM2E2_label.configure(text = str(pointM2E2))
         self.print_answer1()
         self.point_E2()
    
    #Membre 3 Equipe 2
    def point_membre3e2(self):
         global pointM3E2
         pointM3E2+=Npoints
         self.scoreM3E2_label.configure(text = str(pointM3E2))
         self.print_answer1()
         self.point_E2()
    
    #Fonction de points total
    def point_E1(self):
         global pointM1E1, pointM2E1, pointM3E1, bonus_E1#, penalite1
         pointE1=bonus_E1+pointM1E1+pointM2E1+ pointM3E1#+penalite1
         self.scoreE1.configure(text = str(pointE1))
    
    def point_E2(self):
         global pointM1E2, pointM2E2, pointM3E2, bonus_E2#, penalite2
         pointE2=bonus_E2+pointM1E2+pointM2E2+ pointM3E2#+ penalite2
         self.scoreE2.configure(text = str(pointE2))

    def Bonus_public(self, equipe: str):
        global pointM1E1, pointM2E1, pointM3E1, pointM1E2, pointM2E2, pointM3E2, Npoints, nom_E1, nom_E2, pointE2, pointE1, bonus_E1, bonus_E2
        
        
        if equipe == nom_E1:
           bonus_E1+=Npoints
           pointE1=bonus_E1+pointM1E1+pointM2E1+ pointM3E1
           self.scoreE1.configure(text = str(pointE1))
        else:
            bonus_E2+=Npoints
            pointE2=bonus_E2+pointM1E2+pointM2E2+ pointM3E2 
            self.scoreE2.configure(text = str(pointE2))


    
    #Fonction d'affichage des questions
    def print_question(self, event):
        global questions
        global i
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.insert("0.0", "")
        i = i+1
        self.Questions_textbox.delete("0.0", "end")  # delete all text
        self.Questions_textbox.insert("0.0", questions[i])
        self.Questions_textbox.configure(wrap="word")
        print(i)
    
    def previous_question(self, event):
        global i
        global questions
        self.Questions_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.insert("0.0", "")
        i = i-1
        self.Questions_textbox.insert("0.0", questions[i])
        self.Questions_textbox.configure(wrap="word")
    
    #Fonction d'attribution des pénalités
    #def penaliteE1_command(self):
    #     global penalite1
    #     penalite1-=Npoints
    #     self.penaliteE1_label.configure(text = str(penalite1))
    #     self.point_E1()
    
    #def penaliteE2_command(self):
    #    global penalite2
    #     penalite2-=Npoints
    #     self.penaliteE2_label.configure(text = str(penalite2))
    #     self.point_E2()
    
    #Fonction d'affichage de la réponse
    def print_answer1(self):
        global i, reponses
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.configure(wrap="word")
        self.Reponses_textbox.insert("0.0", reponses[i])
    
    def print_answer2(self,event):#event pour la gestion par le clavier
        global i, reponses
        self.Reponses_textbox.delete("0.0", "end")  # delete all text
        self.Reponses_textbox.configure(wrap="word")
        self.Reponses_textbox.insert("0.0", reponses[i])
    
    #Fonction d'échelle d'affichage
    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    
    #fonction d'affichage du gagnant
    
    def winner(self : str):  
        global pointM1E1, pointM2E1,  pointM3E1, pointM1E2, pointM2E2,  pointM3E2, bonus_E1, bonus_E2
        pointE1=pointM1E1+pointM2E1+ pointM3E1+ bonus_E1
        pointE2=pointM1E2+pointM2E2+ pointM3E2+ bonus_E2
        
        winner = nom_E1 if pointE1 > pointE2 else nom_E2
        
        window = Toplevel()
        window.geometry("1195x700")
        window.configure(bg = "#ffffff")
        canvas = Canvas(
            window,
            bg = "#ffffff",
            height = 700,
            width = 1195,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file = f"background.png")
        background = canvas.create_image(
            608.5, 367.5,
            image=background_img)

        canvas.create_text(
            609.0, 299.0,
            text = winner,
            fill = "#ffff8e",
            font = ("Italianno-Regular", int(100.0)))

        window.resizable(False, False)
        window.mainloop()
        
if __name__ == "__main__":
    while True:
        interface = input("Veuillez selectionner l'interface (2 pour deux joueurs et 3 pour trois joueurs):   ")
        if interface == "2" or interface == "3":
            interface_screen = interface
            break
        else:
            print("La saisie est non valide")
    if interface_screen == "2":
        app = App2()
        app.bind("<F6>", app.arret_chrono)
        app.mainloop()
    else:
        app = App3()
        app.bind("<F6>", app.arret_chrono)
        app.mainloop()
