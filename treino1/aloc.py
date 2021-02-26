def aloc(prefs):   
    renegados = []
    blacklist = []

    for key in sorted(prefs.keys()):
        semProj = True
        for value in prefs[key]:
            if value not in blacklist:
                #prefs[key] = value                 
                blacklist.append(value)
                semProj = False
                break
        if semProj:
            #prefs[key] = None
            renegados.append(key)


    return sorted(renegados)
