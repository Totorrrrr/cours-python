# Importation de la fonction qui collecte toutes les données
from collector import collecter_tout  


# Convertion des octets en gigaoctets
def octets_vers_go(octets):
    return f"{octets / (1024**3):.2f} GB"   # Conversion + formatage 2 décimales


print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%% INFOS SYSTEME %%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

# Affichage des informations 
def infos_systeme(data):
    print("~~~~ Système ~~~~")
    print("OS :", data["os"])
    print("Version :", data["version"])
    print("Architecture :", data["architecture"])
    print("Hostname :", data["hostname"])
    print()


# Affichage CPU
def infos_cpu(data):
    print("~~~~ CPU ~~~~")
    print("Cœurs physiques :", data["coeurs_physiques"])
    print("Cœurs logiques :", data["coeurs_logiques"])
    print(f"Utilisation : {data['utilisation']:.2f}%")
    print()


# Affichage mémoire
def infos_memoire(data):
    print("~~~~ Mémoire ~~~~")
    print("Total :", octets_vers_go(data["total"]))          # Conversion propre
    print("Disponible :", octets_vers_go(data["disponible"]))
    print(f"Utilisation : {data['pourcentage']:.2f}%")
    print()


# Affichage disques
def infos_disques(disques):
    print("~~~~ Disques ~~~~")
    for d in disques:
        print(f"{d['point_montage']} : {d['pourcentage']:.2f}% utilisé")
    print()



if __name__ == "__main__":
    data = collecter_tout()     

    # Appel des différentes informations
    infos_systeme(data["systeme"])
    infos_cpu(data["cpu"])
    infos_memoire(data["memoire"])
    infos_disques(data["disques"])