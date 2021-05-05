# SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

# Librerías Python
from datetime import datetime

# Base de datos
import db

# Tabla de Clientes
class Clients(db.Base):

    __tablename__='Clients'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    taxNumber = Column(String(50), nullable=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name + ' ' + self.taxNumber

    # Inserta en la tabla un registro
    def save(self):
        db.session.add(self)
        db.session.commit()

# Tabla de Bancos
class Banks(db.Base):

    __tablename__='Banks'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __str__(self):
        return str(self.id) + ' ' + self.name

    # Inserta en la tabla un registro
    def save(self):
        db.session.add(self)
        db.session.commit()


# Tabla de Cuentas
class Accounts(db.Base):

    __tablename__='Accounts'
    clientId = Column(Integer, ForeignKey('Clients.id'), primary_key=True)
    bankId = Column(Integer, ForeignKey('Banks.id'), primary_key=True)
    balance = Column(Integer, nullable=False)
    created = Column(DateTime, primary_key=True)

    # Devuelve el saldo
    def __str__(self):
        return self.balance

    # Inserta en la tabla un registro
    def save(self):
        self.created=datetime.now()
        db.session.add(self)
        db.session.commit()