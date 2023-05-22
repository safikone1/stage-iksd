class cours:
    def __init__(self, titre,professeur):
        self.titre=titre
        self.professeur=professeur
        self.etudiants=[]
    def ajouter_etudiant(self, etudiants):
        self.etudiants.append(etudiant)
    def liste_etudiants(self):
        for etudiant in self.etudiants:
            print(etudiant)
class etudiant:
    def __init__(self,nom,age,niveau):
        self.nom=nom
        self.age=age
        self.niveau=niveau
    def __str__(self):
        return f"nom: {self.nom}, age: {self.age}, niveau: {self.niveau}"
    
cours_math= cours("Mathematiques","professeur")
cours_physique= cours("Physique","Professeur")

etudiant1=etudiant("Alice",20,"licence")
etudiant2=etudiant("Bob",22,"Master")
etudiant3=etudiant("Charlie",19,"licence")

cours_math.ajouter_etudiant(etudiant1)
cours_math.ajouter_etudiant(etudiant2)
cours_physique.ajouter_etudiant(etudiant2)
cours_physique.ajouter_etudiant(etudiant3)

print("etudiant inscrit en cours de math :")
cours_math.liste_etudiants()

print("etudiant inscrit en cours de physique:")
cours_physique.liste_etudiants()
    