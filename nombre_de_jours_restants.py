
#saisi de la date d_aujourdhui et de la date de l_examen

date_aujourdhui = input("Entrez la date d'aujourd'hui (JJ/MM) : ")
date_oral = input("Entrez la date souhaitée (JJ/MM) : ")


#calcul nombre de jours restant avant l'oral

def nombres_de_jours_avant_oral(date_aujourdhui, date_oral):
    
    ce_jour, ce_mois = map(int, date_aujourdhui.split('/'))

    jour_oral, mois_oral = map(int, date_oral.split('/'))

    # Nombre de jours dans chaque mois
    jours_dans_le_mois = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # Vérifier si l'année bissextile (pour février)
    cette_annee = 2023 # L'année actuelle est 2023
    if cette_annee % 4 == 0 and (cette_annee % 100 != 0 or cette_annee % 400 == 0):
        jours_dans_le_mois[2] = 29

    # Calculer le nombre de jours entre les deux dates
    jours_restants = 0

    if ce_mois == mois_oral:
        jours_restants = jour_oral - ce_jour
    else:
        jours_restants += jours_dans_le_mois[ce_mois] - ce_jour

        for i in range(ce_mois+1, mois_oral):
            jours_restants += jours_dans_le_mois[i]

        jours_restants += jour_oral

    return jours_restants




jours_restants = nombres_de_jours_avant_oral(date_aujourdhui,date_oral)
#tu peux faire un print pour afficher le nombre de jours 