from datetime import datetime
from person.model import Persona

if __name__ == "__main__":
    gabriel = Persona(nacimiento=datetime(1971, 07, 17))
    print gabriel
