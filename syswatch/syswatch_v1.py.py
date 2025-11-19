# Partie 1: Collecte basique

#importation des modules
import platform
import psutil

# Affichage simple
print("----------------------------------------")
print("Voici certaines informations de mon PC")
print("           --------------")
print("SysWatch v1.0")
print("----------------------------------------")

# Récupération des Informations Système 
def infos_systeme():
    print("--- Système ---")
    print("OS :", platform.system())
    print("Version :", platform.version())
    print("Architecture :", platform.machine())
    print("Hostname :", platform.node())
    print("Python :", platform.python_version())
    print()

# Récupération des Informations du CPU
def infos_cpu():
    print("--- CPU ---")
    print("Cœurs physiques :", psutil.cpu_count(logical=False))
    print("Cœurs logiques :", psutil.cpu_count(logical=True))
    print("Utilisation :", psutil.cpu_percent(interval=1), "%")
    print()

# Récupération des Informations de la Mémoire
def infos_memoire():
    mem = psutil.virtual_memory()
    total_go = mem.total / (1024 ** 3)
    dispo_go = mem.available / (1024 ** 3)

    print("--- Mémoire ---")
    print(f"Total : {total_go:.2f} GB")
    print(f"Disponible : {dispo_go:.2f} GB")
    print(f"Utilisation : {mem.percent}%")
    print()

# Récupération des Informations du disque
def infos_disques():
    print("--- Disques ---")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(part.mountpoint, ":", usage.percent, "% utilisé")
        except PermissionError:
            pass
    print()

# Appel des différentes fonctions à afficher 
if __name__ == "__main__":
    infos_systeme()
    infos_cpu()
    infos_memoire()
    infos_disques()

