import csv
import json
import time
import sys
from collector import collecter_tout       
from traitement import calculer_moyennes, detecter_pics  


def exporter_csv(metriques, fichier):
    """
    Ajoute les données dans un fichier CSV.
    Si le fichier n'existe pas → crée l'en-tête.
    """

    colonnes = [
        "timestamp", "hostname",
        "cpu_percent",
        "mem_total_gb", "mem_dispo_gb", "mem_percent",
        "disk_root_percent"
    ]

    # Construction de la ligne à écrire
    ligne = {
        "timestamp": metriques["timestamp"],
        "hostname": metriques["systeme"]["hostname"],

        "cpu_percent": metriques["cpu"]["utilisation"],

        "mem_total_gb": metriques["memoire"]["total"] / (1024**3),
        "mem_dispo_gb": metriques["memoire"]["disponible"] / (1024**3),
        "mem_percent": metriques["memoire"]["pourcentage"],

        # On prend la 1ère partition du disque (C:, /)
        "disk_root_percent": metriques["disques"][0]["pourcentage"],
    }

    fichier_existe = False
    try:
        open(fichier, "r").close()
        fichier_existe = True
    except FileNotFoundError:
        pass

    # On écrit en mode append
    with open(fichier, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=colonnes)

        if not fichier_existe:
            writer.writeheader()

        writer.writerow(ligne)


def exporter_json(metriques, fichier):
    """
    Sauvegarde toutes les métriques dans un fichier JSON lisible.
    """
    with open(fichier, "w") as f:
        json.dump(metriques, f, indent=2)

def collecter_en_continu(intervalle, nombre):
    """
    Collecte les données en boucle :
    - intervalle → temps entre collectes
    - nombre = 0 → boucle infinie
    """

    compteur = 0

    try:
        while nombre == 0 or compteur < nombre:
            m = collecter_tout()
            print(m)
            exporter_csv(m, "historique.csv")
            compteur += 1
            time.sleep(intervalle)

    except KeyboardInterrupt:
        print("\nArrêt manuel.")


if __name__ == "__main__":

   
    if len(sys.argv) == 1:
        m = collecter_tout()
        print(m)
        exporter_csv(m, "historique.csv")
        exporter_json(m, "dernier.json")
        sys.exit()

    args = sys.argv

    if "--continu" in args:
        # Récupère les paramètres ou met valeurs par défaut
        intervalle = 5
        nombre = 0

        if "--intervalle" in args:
            intervalle = int(args[args.index("--intervalle") + 1])

        if "--nombre" in args:
            nombre = int(args[args.index("--nombre") + 1])

        collecter_en_continu(intervalle, nombre)

    elif "--stats" in args:
        stats = calculer_moyennes("historique.csv")

        if stats is None:
            print("Aucune donnée dans le fichier CSV.")
        else:
            print("\n=== STATISTIQUES ===")
            print(stats)

    elif "--pics" in args:
        pics = detecter_pics("historique.csv", seuil_cpu=80, seuil_mem=80)
        print("\n=== PICS DÉTECTÉS ===")
        for p in pics:
            print(p)