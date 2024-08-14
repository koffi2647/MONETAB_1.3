from models.personne import Personne
from Eleve.ICrudEleve import ICRUDEleve

class Eleve(Personne, ICRUDEleve):
    """
        Classe représentant un élève, héritant de la classe Personne et de la classe ICRUDEleve.
    """
    __eleves = []

    # Initialise un nouvel élève avec ses informations personnelles
    def __init__(self, dateNaissance, ville, prenom, nom, telephone, classe, matricule):
        super().__init__(dateNaissance, ville, prenom, nom, telephone)
        self.__classe = classe
        self.__matricule = matricule

    # Retourne une représentation sous forme de chaîne de l'élève
    def __str__(self):
        return f"Eleve n° {self.get_id} : {self.get_nom} {self.get_prenom}, née le {self.get_date_naissance} à {self.ville}, classe: {self.__classe}, matricule: {self.__matricule}, téléphone: {self.telephone}"

    # Retourne le matricule de l'élève.
    @property 
    def get_matricule(self):
        return self.__matricule
    
    @property 
    def get_classe(self):
        return self.__classe

    def set_classe(self, classe):
        self.__classe = classe            

    def set_matricule(self, matricule):
        self.__matricule = matricule

    # Implémentation des méthodes CRUD
    # Ajouter un élève
    def ajouter(eleve):
        Eleve.__eleves.append(eleve)

    # modifier un élève
    def modifier(eleve):
        for index, eleve_existe in enumerate(Eleve.__eleves):
            if eleve_existe.id == eleve.id:
                Eleve.__eleves[index] = eleve
                return True
        return False

    # supprimer un élève 
    def supprimer(identifiant):
        for index, eleve in enumerate(Eleve.__eleves):
            if eleve.matricule == identifiant:
                del Eleve.__eleves[index]
                return True
        return False

    # Obtenir les élèves
    def obtenirEleve():
        return [str(eleve) for eleve in Eleve.__eleves]


    # Obtenir un élève par son id
    def obtenir(identifiant):
        for eleve in Eleve.__eleves:
            if eleve.matricule == identifiant:
                return eleve
        return None