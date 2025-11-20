import csv

def calculer_moyennes(fichier_csv):

    cpu_values = []
    mem_values = []

    # Ouverture du CSV en lecture
    with open(fichier_csv, "r") as f:
        reader = csv.DictReader(f)

        for ligne in reader:
            # Conversion des valeurs 
            cpu = float(ligne["cpu_percent"])
            mem = float(ligne["mem_percent"])

            cpu_values.append(cpu)
            mem_values.append(mem)


    if not cpu_values:
        return None

    return {
        "cpu_moyen": sum(cpu_values) / len(cpu_values),
        "cpu_min": min(cpu_values),
        "cpu_max": max(cpu_values),

        "mem_moyenne": sum(mem_values) / len(mem_values),
        "mem_min": min(mem_values),
        "mem_max": max(mem_values)
    }



def detecter_pics(fichier_csv, seuil_cpu, seuil_mem):
    pics = []

    with open(fichier_csv, "r") as f:
        reader = csv.DictReader(f)

        for ligne in reader:
            cpu = float(ligne["cpu_percent"])
            mem = float(ligne["mem_percent"])

            if cpu > seuil_cpu or mem > seuil_mem:
                pics.append({
                    "timestamp": ligne["timestamp"],
                    "cpu": cpu,
                    "mem": mem
                })

    return pics
