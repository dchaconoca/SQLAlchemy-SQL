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
