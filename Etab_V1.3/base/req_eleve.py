import mysql.connector  # Assurez-vous que ce module est installé
from base.bd import create_connection
def ajouter_eleve(curseur, date_naissance, ville, prenom, nom, telephone, classe, matricule):
    connection=create_connection()
    if connection.is_connected():
        curseur=connection.cursor()
        """Ajoute un élève à la base de données."""
        query = ("INSERT INTO personnes (date_naissance, ville, prenom, nom, telephone) "
             "VALUES (%s, %s, %s, %s, %s)")
        curseur.execute(query, (date_naissance, ville, prenom, nom, telephone))
        id_pers=curseur.lastrowid
        query = ("INSERT INTO eleves (classe, matricule, id_personne) "
             "VALUES (%s, %s, id_pers)")
        curseur.execute(query, (classe, matricule, id_pers))

def modifier_eleve(curseur, matricule, nouveau_telephone, nouvelle_classe):
    """Modifie les informations d'un élève dans la base de données."""
    query = ("UPDATE eleves SET telephone = %s, classe = %s WHERE matricule = %s")
    curseur.execute(query, (nouveau_telephone, nouvelle_classe, matricule))

def supprimer_eleve(curseur, matricule):
    """Supprime un élève de la base de données."""
    query = "DELETE FROM eleves WHERE matricule = %s"
    curseur.execute(query, (matricule,))

def lister_eleves(curseur):
    """Liste tous les élèves de la base de données."""
    query = "SELECT * FROM eleves"
    curseur.execute(query)
    return curseur.fetchall()

def recuperer_eleve(curseur, matricule):
    """Récupère un élève par son matricule."""
    query = "SELECT * FROM eleves WHERE matricule = %s"
    curseur.execute(query, (matricule,))
    return curseur.fetchone()