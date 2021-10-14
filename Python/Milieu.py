#-------------------------------------------------------------------------------
# Name:        Calculer les cordonnées du milieu d'un parallélogramme
# Author:      Niroxy
#
# Created:     14/10/2021
# Licence:     MIT
#-------------------------------------------------------------------------------

def main():
    obj = str(input('Saisir Xa;Ya;Xb;Yb'))
    v = obj.split(';')

    XM = (float(v[0]) + float(v[2])) / 2
    YM = (float(v[1]) + float(v[3])) / 2

    return print('M(' + str(XM) +';' + str(YM) +')')
    pass

if __name__ == '__main__':
    main()
