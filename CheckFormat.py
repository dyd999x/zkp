def checkFormat(T, gamma, t1, t2):
    (m, n) = gamma.shape
    if m == len(t1) and n == len(t2):
        if T == 'PPE':
            index1 = []
            index2 = []
            for item in t1:
                if item not in ['base', 'pub', 'enc', 'com']:
                    return False
                if item == 'pub':
                    index1 += t1.index(item)
            for item in t2:
                if item not in ['base', 'pub', 'enc', 'com']:
                    return False
                if item == 'pub':
                    index2 += t1.index(item)
            if len(index1) != 0 and len(index2) != 0:
                for i in index1:
                    for j in index2:
                        if gamma[i][j] != 0:
                            return False
        if T == 'PEncG':
            for item in t1:
                if item not in ['base', 'pub', 'enc']:
                    return False
            for item in t2:
                if item not in ['base', 'com']:
                    return False
        if T == 'PConstG':
            for item in t1:
                if item not in ['base', 'pub']:
                    return False
            for item in t2:
                if item not in ['base', 'com']:
                    return False
        if T == 'PEncH':
            for item in t1:
                if item not in ['base', 'com']:
                    return False
            for item in t2:
                if item not in ['base', 'pub', 'enc']:
                    return False
        if T == 'PConstH':
            for item in t1:
                if item not in ['base', 'com']:
                    return False
            for item in t2:
                if item not in ['base', 'pub']:
                    return False
        if T == 'MEG':
            for item in t1:
                if item not in ['base', 'pub', 'enc', 'com']:
                    return False
            for item in t2:
                if item not in ['unit', 'sca']:
                    return False
        if T == 'MEncG':
            for item in t1:
                if item not in ['base', 'pub', 'enc']:
                    return False
            for item in t2:
                if item not in ['unit', 'sca']:
                    return False
        if T == 'MConstG':
            for item in t1:
                if item not in ['base', 'pub']:
                    return False
            for item in t2:
                if item not in ['unit', 'sca']:
                    return False
        if T == 'MLinG':
            for item in t1:
                if item not in ['base', 'com']:
                    return False
            for item in t2:
                if item not in ['unit']:
                    return False
        if T == 'MEH':
            for item in t1:
                if item not in ['unit', 'sca']:
                    return False
            for item in t2:
                if item not in ['base', 'pub', 'enc', 'com']:
                    return False
        if T == 'MEncH':
            for item in t1:
                if item not in ['unit', 'sca']:
                    return False
            for item in t2:
                if item not in ['base', 'pub', 'enc']:
                    return False
        if T == 'MConstH':
            for item in t1:
                if item not in ['unit', 'sca']:
                    return False
            for item in t2:
                if item not in ['base', 'pub']:
                    return False
        if T == 'MLinH':
            for item in t1:
                if item not in ['unit']:
                    return False
            for item in t2:
                if item not in ['base', 'com']:
                    return False
        if T == 'QE':
            for item in t1:
                if item not in ['unit', 'sca']:
                    return False
            for item in t2:
                if item not in ['unit', 'sca']:
                    return False
        if T == 'QConstG':
            for item in t1:
                if item not in ['unit']:
                    return False
            for item in t2:
                if item not in ['unit', 'sca']:
                    return False
        if T == 'QConstH':
            for item in t1:
                if item not in ['unit', 'sca']:
                    return False
            for item in t2:
                if item not in ['unit']:
                    return False
        return True
    else:
        return False
