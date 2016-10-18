from datetime import datetime

def edad(alguien):
    now = datetime.now()
    result = now.year - alguien.nacimiento.year - 1
    if now.month > alguien.nacimiento.month:
        result += 1
    return result
