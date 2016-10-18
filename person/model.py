

class Persona(object):
    def __init__(self, nacimiento):
        self.nacimiento = nacimiento

    def __str__(self):
        return "nacido {} {} {}".format(
            self.nacimiento.year,
            self.nacimiento.month,
            self.nacimiento.day,
        )
