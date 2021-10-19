###############################################################
# Utilización de SQLAlchemy (ORM) y carga de datos: 
#   - Creación de base SQLite con tablas según modelos
#   - Lectura de archivos JSON y carga de datos en las tablas
# Autor: Diana Chacón Ocariz
###############################################################

import db
import loadData

def run():
    loadData.loadClients()
    loadData.loadBanks()
    loadData.loadAccounts()

if __name__ == '__main__':
    # Crea las tablas según los modelos
    db.Base.metadata.create_all(db.engine)

    # Carga los datos en las tablas de la BD
    run()
