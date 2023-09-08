# Permet de simuler le systeme dans un envirronement donné en apportant les parametres d'un bot
# Parametre 1 : Achat (Struct sur le Temps de prise en compte et le % de Baisse et remontée)
# achat.temps, achat.baisse_pourcent achat.rehausse_pourcent
# Parametre 2 : Revente (Struct sur le % de deficit et de gain)
# vente.deficit_pourcent, vente.gain_pourcent
#


def simulate_trading(actions, achat_delta, achat_diff, vente_deficitMax, vente_gainMax):
    portefeuille_initial = 10000  # Montant initial
    portefeuille = portefeuille_initial
    portefeuille_history = [portefeuille]
    actions_detenues = 0
    prix_action = 0 #defaut 1€ 
    achat_delta = 0


    for prix_actuel in actions:

        # Si nous n'avons pas d'actions, achetons si le prix est bas
        if actions_detenues == 0:  
            prix_action = prix_actuel
            nb_actions_a_acheter = 10#int(portefeuille / prix_action)
            portefeuille -= nb_actions_a_acheter * prix_action
            actions_detenues += nb_actions_a_acheter

        # Si le prix a augmenté suffisamment, vendons
        if (prix_actuel - prix_action) / prix_action >= vente_gainMax:  
            portefeuille += actions_detenues * prix_actuel
            actions_detenues = 0

        # Si le prix a baissé trop, vendons pour limiter les pertes
        if (prix_action - prix_actuel) / prix_action >= vente_deficitMax:  
            portefeuille += actions_detenues * prix_actuel
            actions_detenues = 0

        portefeuille_history.append(portefeuille)  # Ajouter le solde actuel à l'historique
        print({portefeuille})

    # Vendre toutes les actions restantes à la fin de la simulation
    portefeuille += actions_detenues * actions[-1]
    actions_detenues = 0
    portefeuille_history.append(portefeuille)  # Ajouter le solde final à l'historique

    return portefeuille, portefeuille_history
