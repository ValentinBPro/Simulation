from tkinter import *
from tkinter import ttk
import GeneticAlgo
import matplotlib.pyplot as plt
import os


'''
1. Affichage Fenetre entrée données
Les valeurs de sorties sont :
'ChoixGeneration'       pour le nombre de générations souhaitées
'ChoixPopulation'       pour le nombre de populations souhaitées
'ChoixInvestissement'   pour le type d'investissement souhaité
'''
def FenetreInit() :
    def GetValeur():
        ChoixGeneration=ValeurGeneration.get()
        ChoixPopulation=ValeurPopulation.get()
        ChoixInvestissement=MenuInvestissement.get()
        print(ChoixGeneration)
        print(ChoixPopulation)
        print(ChoixInvestissement)   

    # Création IHM
        # Création de la fenêtre de démarrage 
    Fenetre  = Tk()
        # Personnalisation de la fenêtre de démarrage 
    Fenetre.title("Ecran de Sélection")
    Fenetre.geometry("720x300")
    Fenetre.config(background='#B3E5D9')
        # Créer Deux frame de mise en page: gauche et droite
    Frame_Gauche= Frame(Fenetre,bg='#B3E5D9')
    Frame_Gauche.grid(row=0,column=0)
    Frame_Droite= Frame(Fenetre,bg='#B3E5D9')
    Frame_Droite.grid(row=0,column=1)


    # Créer Texte Non variable Fênetre de démarrage 
        # Ajouter Texte Génération
    Generation = Label(Frame_Gauche,text="Génération :   ", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Generation.grid(row=0, column=0)
        # Ajouter Espaces1
    Espace = Label(Frame_Gauche,text="", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Espace.grid(row=1, column=0)
        # Ajouter Texte PopulationS
    Population = Label(Frame_Gauche,text="Population :   ", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Population.grid(row=2, column=0)
        # Ajouter Espaces2
    Espace1 = Label(Frame_Gauche,text="", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Espace1.grid(row=3, column=0)
        # Ajouter Type investissement
    Investissement = Label(Frame_Gauche,text="Investissement :", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Investissement.grid(row=4, column=0)



    # Créer Texte Variable
        # Créer Valeur Generation
    ValeurGeneration =Entry(Frame_Gauche,font=("Arial", 20), bg='#B3E5D9', fg='Black')
    ValeurGeneration.grid(row=0, column=1) 
        # Créer Valeur Population 
    ValeurPopulation =Entry(Frame_Gauche, font=("Arial", 20), bg='#B3E5D9', fg='Black')
    ValeurPopulation.grid(row=2, column=1) 
        # Créer Valeur Population 
    ValeurPopulation =Entry(Frame_Gauche, font=("Arial", 20), bg='#B3E5D9', fg='Black')
    ValeurPopulation.grid(row=2, column=1) 
        # Créer Menu Type D'investissement
    ListeInvestissement=["Cryptos: BTC","Cryptos: ETH","Cryptos: DOGE","Parts: Apple","Parts: Samsung","Parts: Tesla"]
    MenuInvestissement = ttk.Combobox(Frame_Gauche, values= ListeInvestissement)
    MenuInvestissement.current(0)
    MenuInvestissement.grid(row=4, column=1)

    # Recupération des valeurs entrées
        
        # Ajouter Espaces2
    Espace2 = Label(Frame_Gauche,text="", font=("Arial", 20), bg='#B3E5D9', fg='Black')
    Espace.grid(row=5, column=0)
        # Création Bouton Valider 
    BoutonGénération = Button(Frame_Gauche, height=3, width=50, text="Valider la sélection", command=GetValeur)
    BoutonGénération.grid(row=15, column=1)


    # Afficher la fenêtre de démarrage
    Fenetre.mainloop()


'''
2.Affichage Fenetre entrée données
Les valeurs de sorties sont :
'ChoixGeneration'       pour le nombre de générations souhaitées
'ChoixPopulation'       pour le nombre de populations souhaitées
'ChoixInvestissement'   pour le type d'investissement souhaité
'''

def FenetreResult():
    script_directory = os.path.dirname(__file__)
    file_path = os.path.join(script_directory, 'donnees_random.txt')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    x = []
    y1 = []  # Première courbe
    y2 = []  # Deuxième courbe

    for line in lines:
        data = line.strip().split('\t')
        if len(data) == 3:
            x.append(int(data[0]))  # Heure
            y1.append(float(data[1]))  # Première courbe
            y2.append(float(data[2]))  # Deuxième courbe

    # Trouver la valeur maximale parmi les deux ensembles de données
    max_value = max(max(y1), max(y2))

    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Heure')
    ax1.set_ylabel('Y1', color='tab:blue')
    ax1.plot(x, y1, label='Y1', color='tab:blue')

    ax2 = ax1.twinx()
    ax2.set_ylabel('Y2', color='tab:red')
    ax2.plot(x, y2, label='Y2', color='tab:red')

    # Utilisez la valeur maximale comme limite pour les deux axes y
    ax1.set_ylim(0, max_value)
    ax2.set_ylim(0, max_value)

    plt.title('Graphique avec deux courbes')
    ax1.grid(True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    plt.show()

# Appelez la fonction FenetreResult


# Appeler la fonction FenetreResult pour générer le graphique







#FenetreRes.mainloop()
    



'''
3.Déroulement des affichages 
FenetreInit     Pour la premiere fenêtre comprenant la sélection de données voullues
FenetreResult   Pour la seconde fenetre regroupant les résultats obtenus
'''
#FenetreInit()
FenetreResult()


#################################################################################################################################################
#import Simulation


# Lecture des valeurs de l'action depuis un fichier
