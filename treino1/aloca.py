def aloca(prefs):   
    renegados = []
    
    blacklist = []

    for key in sorted(prefs.keys()):
        semProj = True
        for value in prefs[key]:
            if value not in blacklist:
                blacklist.append(value)
                semProj = False
                break
        if semProj:
            renegados.append(key)

    return sorted(renegados)
