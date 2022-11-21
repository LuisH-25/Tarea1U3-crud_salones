from app import db
class Alumno(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nombre = db.Column(db.String(100), primary_key=True)
    apellido = db.Column(db.String(100), primary_key=True)
    idaula = db.Column(db.Integer, db.ForeignKey('salon.id'), primary_key=True)