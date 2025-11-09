def parse_hhmm(s):
# h y m a horas a 
    h, m = s.strip().split(":")
    return int(h), int(m)

def siguiente_minuto(h, m):
#reloj
    m += 1
    if m == 60:
        m = 0
        h += 1
        if h == 24:
            h = 0
    return h, m
