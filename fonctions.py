import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

import pandas as pd

class Coaching:

    def __init__(self):
        self.semaine = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        pass

    def creer_dataframe_mois(self):
        """
        Crée un DataFrame avec les jours de la semaine en colonnes et les semaines en lignes.
        """
        semaines = ['Semaine 1', 'Semaine 2', 'Semaine 3', 'Semaine 4']
        jours = self.semaine.copy()
        df = pd.DataFrame(index=semaines, columns=jours)
        return df

    
    def creer_semaine(self, liste):
        semaine = {'Lundi': [],
            'Mardi': [],
            'Mercredi': [],
            'Jeudi': [],
            'Vendredi': [],
            'Samedi': [],
            'Dimanche': []}
        for i, jour in enumerate(self.semaine):
            semaine[jour] = liste[i]
        return semaine

    def creer_mois(self, liste):
        """ 
        Permet de creer le dictionnaire mois
        """
        mois = []
        for sub in liste:
            semaine = self.creer_semaine(sub)
            mois.append(semaine)
        return mois
    

    def remplir_dataframe(self, programme):
        """
        Remplire le DataFrame avec les activités planifiées 
        pour chaque jour de chaque semaine.
        Exemple : 
        programme = [
            {'Lundi': [course.footing(30, 'facile'), self.musculation(45, 'endurance')],
            'Mardi': [course.vma(5, 400)],
            'Mercredi': [course.footing(30, 'facile')],
            'Jeudi': [course.vma(5, 400)],
            'Vendredi': [course.footing(30, 'facile')],
            'Samedi': [course.seuil()],
            'Dimanche': [course.sortie_longue()]}, 
            {},
            {},
            {}
        ]
        """
        df = self.creer_dataframe_mois()
        course = self.course_a_pied()
        semaine1 = programme[0]
        semaine2 = programme[1]
        semaine3 = programme[2]
        semaine4 = programme[3]

        SEMAINES = [semaine1, semaine2, semaine3, semaine4]

        for i, semaine in enumerate(df.index):
            SEMAINE = SEMAINES[i]
            for jour in df.columns:
                df.loc[semaine, jour] = SEMAINE[jour]
        return df



    def creer_dataframe_mois(self):
        """
        Créer un DataFrame avec les jours de la semaine en colonnes 
        et les semaines en lignes.
        """
        semaines = ['Semaine 1', 'Semaine 2', 'Semaine 3', 'Semaine 4']
        jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        df = pd.DataFrame(index=semaines, columns=jours)
        return df

    def musculation(self, qualite):
        """
        Génère une séance de musculation en fonction de la durée 
        et de la qualité visée.

        qualite : endurance ou force 
        """
        seance = ""

        if qualite == 'endurance':
            seance = (
                "Séance de musculation profil Endurance:\n"
                " - WU : 10 à 20mn de jog \n"
                " - 4 séries de 10-12 squats \n"
                " - 4 séries de 10-12 deadlift \n"
                " - 4 séries de 8-12 tractions / tirage vertical \n"
                " - 4 séries de 10-12 à la presse \n"
                " - 4 séries de 10-12 à la machine à ischios \n"
                " - opt : 4 séries de 10-12 à la machine à quadriceps (selon forme) \n"
                " - 2 minutes / 1:30 / 1:00 de planche"
            )
        elif qualite == 'force':
            seance = (
                "Séance de musculation profil Force:\n"
                " - WU : 10 à 20mn de jog \n"
                " - 4 séries squats : 12 / 8 / 6 / 4-5 \n"
                " - 4 séries de 6-10 deadlift \n"
                " - 4 séries de 8-12 tractions / tirage vertical \n"
                " - 4 séries de 8-10 à la presse \n"
                " - 4 séries de 10-12 à la machine à ischios \n"
                " - opt : 4 séries de 10-12 à la machine à quadriceps (selon forme) \n"
                " - 2 minutes / 1:30 / 1:00 de planche"
            )
        else:
            seance = "Qualité visée non reconnue. Choisissez parmi : endurance ou force."

        return seance

    def course_a_pied(self):
        """
        Contient des fonctions pour divers types d'entraînements de course à pied.
        """
        class Course:
            def __init__(self):
                pass

            def footing(self, duree, intensite):
                """
                Génère une séance de footing en fonction de la durée et de l'intensité.
                """
                seance = f"Footing de {duree} minutes à une intensité {intensite}."
                return seance

            def vma(self, liste):
                """
                Génère une séance de VMA en fonction du nombre de répétitions et des intervalles.

                liste = [nb de blocs, nb de répétitions, distance, temps, recup bloc, recup repet] 
                (! liste de liste possible)

                Ex : liste = [[2, 4, 400, 65, 45, 120], [2, 4, 300, 47, 30, 60]] correspond à : 
                2 x (4 x 400 en 65 R45) R120 + 2 x (4 x 300 en 47 R30) R60
                """
                seance = ""
                if len(np.array(liste).flatten()) != len(liste):
                    for sub in liste : 
                        [nbb, nbr, d, t, rb, rr] = sub
                else: 
                    [nbb, nbr, d, t, rb, rr] = liste
                
                seance = seance + f"{nbb} x ({nbr} x {d} en {t} R{rb}) R{rr}" 
                seance = (
                        seance
                    )
                return seance

            def seuil(self, liste):
                """Génère une séance au seuil """
                seance = ""
                for sub in liste : 
                    [nbb, nbr, d, t, rb, rr] = sub
                    seance = seance + f"{nbb} x ({nbr} x {d} en {t} R{rb}) R{rr}" 
                seance = (
                    seance
                )
                return seance

            def sortie_longue(self, duree, intensite):
                """Génère une séance de sortie longue """
                seance = f"Footing de {duree} minutes à une intensité {intensite}."
                return seance
        return Course()


