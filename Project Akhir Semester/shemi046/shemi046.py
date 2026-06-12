def indentitas(x):
    iden = []
    
    if x > 0:
        for i in range(x):
            baris = []
            for j in range(x):
                if i == j:
                    baris.append(1)
                else:
                    baris.append(0)
            iden.append(baris)
        return iden
    
    else:
        return None
