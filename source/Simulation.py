from Bot import bot
from collections import deque


    

# Permet de simuler le systeme dans un envirronement donné en apportant les parametres d'un bot
# Parametre 1 : Achat (Struct sur le Temps de prise en compte et le % de Baisse et remontée)
# achat.temps, achat.baisse_p100 achat_delta
# Parametre 2 : Revente (Struct sur le % de deficit et de gain)
# 
# Parametres :
# achat_delta - Temps passé prit en compte pour le calcul (en heures)
# achat_deficit_p100 - % de deficit avant remontée (entre le delta t et le point le plus bas dans le delta)
# achat_rehausse_p100 - % de gain depuis rehausse (entre point le plus bas et l'instant t)
# vente_deficit_p100 - Vente si deficit atteint % (doit t-il s'adapter? si oui, gain % n'a pas d'interet)
# vente_gain_p100 - Vente si gain atteint % 


def simulate_trading(actions, bot_choisi : bot):
    
    # On defini les parametres du bot
    achat_delta = bot_choisi.GetAchat_delta
    achat_deficit_p100 = bot_choisi.GetAchat_deficit_p100
    achat_rehausse_p100 = bot_choisi.GetAchat_rehausse_p100
    vente_deficitMax = bot_choisi.GetVente_deficitMax
    vente_gainMax = bot_choisi.GetVente_gainMax
    pourcent_ajustement = bot_choisi.GetPourcent_ajustement

    
    actions_detenues = 0
    prix_action = 1 #defaut 1€ 
    delta_actions = deque()
    portefeuille_initial = 10000  # Montant initial
    portefeuille = portefeuille_initial
    portefeuille_history = [portefeuille]       


    for prix_actuel in actions:
        
        delta_actions = maj_delta_achat(delta_actions, achat_delta, prix_actuel)
        achat_deficit_p100, achat_rehausse_p100 = analyse_achat(delta_actions)

        # Si nous n'avons pas d'actions, achetons si le prix est bas
        if actions_detenues == 0:  
            Achat_Action(portefeuille, actions_detenues, prix_actuel)
            
        # Si le prix a augmenté suffisamment, vendons
        if (prix_actuel - prix_action) / prix_action >= vente_gainMax:  
            Revente_Action_Deficit(portefeuille, actions_detenues, prix_actuel)

        # Si le prix a baissé trop, vendons pour limiter les pertes
        if (prix_action - prix_actuel) / prix_action >= vente_deficitMax:  
            Revente_Action_Gain(portefeuille, actions_detenues, prix_actuel)
        
        portefeuille_history.append(portefeuille)  # Ajouter le solde actuel à l'historique
        print({portefeuille})

    # Vendre toutes les actions restantes à la fin de la simulation
    portefeuille += actions_detenues * actions[-1]
    actions_detenues = 0
    portefeuille_history.append(portefeuille)  # Ajouter le solde final à l'historique

    # NOTE : Mettre le retour de monnaie dans le bot

    return bot_choisi


# On adapte le delta d'achat
def maj_delta_achat(delta_actions, achat_delta, prix_actuel) :
    delta_actions.append(prix_actuel)
    if len(delta_actions) == achat_delta :
        delta_actions.popleft

    return delta_actions

# On determine le taux de deficit et de gain à partir du niveau le plus bas selon le delta temps défini
def analyse_achat(delta_actions) :
    pic_bas = Get_picBas_valeur(delta_actions)
    achat_deficit_p100 = round(pic_bas/delta_actions[0],2)-1
    achat_rehausse_p100 = round(delta_actions[-1]/pic_bas,2)-1

    return achat_deficit_p100, achat_rehausse_p100

# Determine la valeur du pic le plus bas du delta temps
def Get_picBas_valeur(delta_actions) :
    pic_bas = delta_actions[0]
    for delta_action in delta_actions :
        if delta_action <= pic_bas:
            pic_bas = delta_action
    return pic_bas
    
def Achat_Action(portefeuille, actions_detenues, prix_actuel):
    prix_action = prix_actuel
    nb_actions_a_acheter = 10#int(portefeuille / prix_action)
    portefeuille -= nb_actions_a_acheter * prix_action
    actions_detenues += nb_actions_a_acheter

def Revente_Action_Deficit(portefeuille, actions_detenues, prix_actuel):
    portefeuille += actions_detenues * prix_actuel
    actions_detenues = 0

def Revente_Action_Gain(portefeuille, actions_detenues, prix_actuel):
    portefeuille += actions_detenues * prix_actuel
    actions_detenues = 0