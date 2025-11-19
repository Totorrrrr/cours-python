def saluer_personne(nom, heure):
    if 6 <= heure < 12:
        return "Bonjour" + nom
    elif 12 <= heure < 18:
        return "Bon après-midi" + nom
    elif 18 <= heure < 24:
        return "Bonsoir" + nom
    else:
        return "Bonne nuit" + nom

print(saluer_personne("Victor", 8))  
print(saluer_personne("Tom", 15))  
print(saluer_personne("Nathan", 22))  
print(saluer_personne("Eric", 2))