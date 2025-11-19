def est_mot_de_passe_valide(mot_de_passe):
   
    if len(mot_de_passe) < 8:
        return False

   
    contient_chiffre = any(car.isdigit() for car in mot_de_passe)


    contient_majuscule = any(car.isupper() for car in mot_de_passe)

    
    return contient_chiffre and contient_majuscule


print(est_mot_de_passe_valide("Abcdef12"))  
print(est_mot_de_passe_valide("abcdef12")) 
print(est_mot_de_passe_valide("ABCDEFGH"))  
print(est_mot_de_passe_valide("Abc12"))  