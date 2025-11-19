import platform
import psutil
from datetime import datetime

def infos_systeme():
    return {
        "os": platform.system(),            
        "version": platform.version(),      
        "architecture": platform.machine(),
        "hostname": platform.node()         
    }

def infos_cpu():
    return {
        "coeurs_physiques": psutil.cpu_count(logical=False),  
        "coeurs_logiques": psutil.cpu_count(logical=True),    
        "utilisation": psutil.cpu_percent(interval=1)         
    }

def infos_memoire():
    mem = psutil.virtual_memory()   

    return {
        "total": mem.total,            
        "disponible": mem.available,   
        "pourcentage": mem.percent    
    }

def infos_disques():
    partitions = psutil.disk_partitions()   
    resultat = []

    for part in partitions:
        try:
            usage = psutil.disk_usage(part.mountpoint)   
            resultat.append({
                "point_montage": part.mountpoint,   
                "total": usage.total,
                "utilise": usage.used,
                "pourcentage": usage.percent
            })
        except PermissionError:
            continue

    return resultat

def collecter_tout():
    return {
        "timestamp": datetime.now().isoformat(),  

        "systeme": infos_systeme(),      
        "cpu": infos_cpu(),
        "memoire": infos_memoire(),
        "disques": infos_disques()
    }