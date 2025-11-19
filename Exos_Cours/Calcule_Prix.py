def calculez_prix_ttc(prix_ht, taux_tva=20):
    prix_ttc = prix_ht*(1 + taux_tva / 100)
    return round(prix_ttc, 2)

print(calculez_prix_ttc(100))       
print(calculez_prix_ttc(50, 10.5))
