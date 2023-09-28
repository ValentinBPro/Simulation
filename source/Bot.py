import uuid

class bot:

    # CONSTRUCTEUR
    def __init__(self, generation, parametres = [] ):

        self.generation = generation  # Numero de la génération
        self.parametres = parametres  # Liste des parametres du bot

        self.unique_id = uuid.uuid4()
        self.gains = 0  # Liste des gains associés aux parametres

        #Parametres
        self._achat_delta = 0
        self._achat_deficit_p100 = 0
        self._achat_rehausse_p100 = 0
        self._vente_deficitMax = 0
        self._vente_gainMax = 0
        self._pourcent_ajustement = 0

    
    # INFORMATIONS GENERALES

    def GetGain(self):
        return self.gains
    
    def SetGain(self, value):
        self.gains = value

    def GetGeneration(self):
        return self.gains
    
    def GetID(self):
        self.unique_id

    # GESTION DES PARAMETRES

    def GetParametres(self):
        return [self._achat_delta, self._achat_deficit_p100, self._achat_rehausse_p100, self._vente_deficitMax, self._vente_gainMax, self._pourcent_ajustement]

    def SetParametres(self, param_list):
        self._achat_delta = param_list[0]
        self._achat_deficit_p100 = param_list[1]
        self._achat_rehausse_p100 = param_list[2]
        self._vente_deficitMax = param_list[3]
        self._vente_gainMax = param_list[4]
        self._pourcent_ajustement = param_list[5]
        
    def GetAchat_delta(self):
        return self._achat_delta
    
    def GetAchat_deficit_p100(self):
        return self._achat_deficit_p100
    
    def GetAchat_rehausse_p100(self):
        return self._achat_rehausse_p100
    
    def GetVente_deficitMax(self):
        return self._vente_deficitMax
    
    def GetVente_gainMax(self):
        return self._vente_gainMax
    
    def GetPourcent_ajustement(self):
        return self._pourcent_ajustement
    
    def SetAchat_delta(self, value):
        self._achat_delta = value
    
    def SetAchat_deficit_p100(self, value):
        self._achat_deficit_p100 = value
    
    def SetAchat_rehausse_p100(self, value):
        self._achat_rehausse_p100 = value
    
    def SetVente_deficitMax(self, value):
        self._vente_deficitMax = value
    
    def SetVente_gainMax(self, value):
        self._vente_gainMax = value
    
    def SetPourcent_ajustement(self, value):
        self._pourcent_ajustement = value

    def __str__(self):
        return f"bot {self.unique_id} - Parametres: {self.parametres}, Gains: {self.gains}"
