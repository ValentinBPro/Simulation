import Simulation
import matplotlib.pyplot as plt

# Lecture des valeurs de l'action depuis un fichier
actions = []
with open('donnees_random.txt', 'r') as file:
    for line in file:
        actions.append(float(line.strip()))  # Convertir les valeurs en float et les ajouter à la liste


vente_deficitMax = 0.1  # 10% de perte maximale
vente_gainMax = 0.01  # 15% de profit avant revente
achat_delta = 10 # Temps en Heure prise en compte
achat_diffA = 10 #% de Baisse
achat_diffB = 10 #% de Rehausse 

final_portefeuille, portefeuille_history = Simulation.simulate_trading(actions, 0, 0, vente_deficitMax, vente_gainMax)

# Afficher la courbe de l'évolution du solde
#plt.plot(range(len(actions)), actions, label='Bourse', color='blue')
plt.plot(range(len(portefeuille_history)), portefeuille_history, label='actions_detenues', color='red')
plt.xlabel('Jours')
plt.ylabel('Solde')
plt.title('Évolution du solde au fil du temps')
plt.grid(True)

# Sauvegarder la courbe dans un fichier
#plt.savefig('solde_evolution.png')

# Afficher la courbe
plt.show()