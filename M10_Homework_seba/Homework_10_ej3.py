import os



montañas = {'nombre':[  'Everest','K2','Kanchenjunga','Lhotse','Makalu',
                        'Cho Oyu','Dhaulagiri','Manaslu','Nanga Parbat','Annapurna I'],
            'orden':[1,2,3,4,5,6,7,8,9,10],
            'cordillera':['Himalaya','Karakórum','Himalaya','Himalaya','Himalaya'
                        ,'Himalaya','Himalaya','Himalaya','Karakórum','Himalaya'],
            'pais': ['Nepal','Pakistán','Nepal','Nepal','Nepal','Nepal','Nepal','Nepal',
                    'Pakistán','Nepal'],
            'altura':[8849,8611,8586,8516,8485,8188,8167,8163,8125,8091]}

archivo = open('clase09_ej3.csv', 'w')

for clave in montañas.keys():
    if (clave == 'altura'):
        archivo.write(clave+'\n')
    else:
        archivo.write(clave+',')

i = 0
while (i < 10):
    archivo.write(montañas['nombre'][i]+',')
    archivo.write(str(montañas['orden'][i])+',')
    archivo.write(montañas['cordillera'][i]+',')
    archivo.write(montañas['pais'][i]+',')
    archivo.write(str(montañas['altura'][i])+'\n')
    i += 1
    
archivo.close()

print('El archivo tiene un tamaño de', str(round(os.path.getsize('clase09_ej3.csv')/1024,2)),'MB')