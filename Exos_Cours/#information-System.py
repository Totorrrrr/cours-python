#information-System

import platform

print("==========================================")
print("==== différentes infos sur le système ====")
print("==========================================")

print("                           ")

print("======== Système d'exploitation ========")
print("Le Nom de la machine:", platform.node())
print ("La machine est sous:", platform.system(),platform.release(), "en",platform.machine())

print("                           ")

print("======== Python Version ========")
print ("Version Python:", platform.python_version())

print("                           ")

print("======== Utilisateurs ========")
print("Le User de ce PC est:", platform.release())
