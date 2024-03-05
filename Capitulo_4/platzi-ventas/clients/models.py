import uuid

class Client():

    def __init__(self, nombre, compania, email, puesto, uid=None):
        self.nombre = nombre
        self.compania = compania
        self.email = email
        self.puesto = puesto
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        return vars(self)
    
    @staticmethod
    def schema():
        return ['nombre', 'compania', 'email', 'puesto','uid']