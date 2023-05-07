print("******************************************************************************")
print("**************************Departamentos de El Salvador************************")
print("******************************************************************************")

# Programa que muestra los municipios de un departamento en El Salvador
# Datos
# Se define el arreglo de departamentos
Departamentos = ["Ahuachapán", "Cabañas", "Chalatenango", "Cuscatlán", "La Libertad", "La Paz", "La Unión", "Morazán", "San Miguel", "San Salvador", "Santa Ana", "Sonsonate", "San Vicente", "Usulután"]
# Se define el arreglo de municipios para cada departamento
Municipios = {
    "Ahuachapán": ["Ahuachapán", "Atiquizaya", "Concepción de Ataco", "El Refugio", "Guaymango", "Jujutla", "San Francisco Menéndez", "San Lorenzo", "San Pedro Puxtla", "Tacuba", "Turín"],
    "Cabañas": ["Cinquera", "Dolores", "Guacotecti", "Ilobasco", "Jutiapa", "San Isidro", "Sensuntepeque", "Tejutepeque", "Victoria"],
    "Chalatenango": ["Agua Caliente", "Arcatao", "Azacualpa", "Chalatenango", "Citalá", "Comalapa", "Concepción Quezaltepeque", "Dulce Nombre de María", "El Carrizal", "El Paraíso", "La Laguna", "La Palma", "La Reina", "Las Vueltas", "Nueva Concepción", "Nueva Trinidad", "Nombre de Jesús", "Ojos de Agua", "Potonico", "San Antonio de la Cruz", "San Antonio Los Ranchos", "San Fernando", "San Francisco Lempa", "San Francisco Morazán", "San Ignacio", "San Isidro Labrador", "San José Cancasque", "San José Las Flores", "San Luis del Carmen", "San Miguel de Mercedes", "San Rafael", "Santa Rita", "Tejutla"],
    "Cuscatlán": ["Candelaria", "Cojutepeque", "El Carmen", "El Rosario", "Monte San Juan", "Oratorio de Concepción", "San Bartolomé Perulapía", "San Cristóbal", "San José Guayabal", "San Pedro Perulapán", "San Rafael Cedros", "San Ramón", "Santa Cruz Analquito", "Santa Cruz Michapa", "Suchitoto", "Tenancingo"],
    "La Libertad": ["Antiguo Cuscatlán", "Chiltiupán", "Ciudad Arce", "Colón", "Comasagua", "Huizúcar", "Jayaque", "Jicalapa", "La Libertad", "Nuevo Cuscatlán", "Quezaltepeque", "San Juan Opico", "San Matías", "Santa Tecla", "Tamanique", "Teotepeque", "Tepecoyo", "Zaragoza"],
    "La Paz": ["Cuyultitán", "El Rosario", "Jerusalén", "Mercedes La Ceiba", "Olocuilta", "Paraíso de Osorio", "San Antonio Masahuat", "San Emigdio", "San Francisco Chinameca", "San Juan Nonualco", "San Juan Talpa", "San Juan Tepezontes", "San Luis Talpa", "San Miguel Tepezontes", "San Pedro Masahuat", "San Pedro Nonualco", "San Rafael Obrajuelo", "Santa María Ostuma", "Santiago Nonualco", "Tapalhuaca", "Zacatecoluca"],
    "La Unión": ["Anamorós", "Bolívar", "Concepción de Oriente", "Conchagua", "El Carmen", "El Sauce", "Intipucá", "La Unión", "Lislique", "Meanguera del Golfo", "Nueva Esparta", "Pasaquina", "Polorós", "San Alejo", "San José", "Santa Rosa de Lima", "Yayantique", "Yucuaiquín"],
    "Morazán": ["Arambala", "Cacaopera", "Chilanga", "Corinto", "Delicias de Concepción", "El Divisadero", "El Rosario", "Gualococti", "Guatajiagua", "Joateca", "Jocoaitique", "Jocoro", "Lolotique", "Meanguera", "Osicala", "Perquín", "San Carlos", "San Fernando", "San Francisco Gotera", "San Isidro", "San Simón", "Sensembra", "Sociedad", "Torola", "Yamabal"],
    "San Miguel": ["Carolina", "Chapeltique", "Chinameca", "Chirilagua", "Ciudad Barrios", "Comacarán", "El Tránsito", "Lolotique", "Moncagua", "Nueva Guadalupe", "Nuevo Edén de San Juan", "Quelepa", "San Antonio del Mosco", "San Gerardo", "San Jorge", "San Luis de la Reina", "San Miguel", "San Rafael Oriente", "Sesori", "Uluazapa"],
    "San Salvador": ["Aguilares", "Apopa", "Ayutuxtepeque", "Cuscatancingo", "Delgado", "El Paisnal", "Guazapa", "Ilopango", "Mejicanos", "Nejapa", "Panchimalco", "Rosario de Mora", "San Marcos", "San Martín", "San Salvador", "Santiago Texacuangos", "Santo Tomás", "Soyapango", "Tonacatepeque"],
    "Santa Ana": ["Candelaria de la Frontera", "Chalchuapa", "Coatepeque", "El Congo", "El Porvenir", "Masahuat", "Metapán", "San Antonio Pajonal", "San Sebastián Salitrillo", "Santa Ana", "Santa Rosa Guachipilín", "Santiago de la Frontera", "Texistepeque"],
    "Sonsonate": ["Acajutla", "Armenia", "Caluco", "Cuisnahuat", "Izalco", "Juayúa", "Nahuizalco", "Nahulingo", "Salcoatitán", "San Antonio del Monte", "San Julián", "Santa Catarina Masahuat", "Santa Isabel Ishuatán", "Santo Domingo de Guzmán", "Sonsonate", "Sonzacate"],
    "San Vicente": ["Apastepeque", "Guadalupe", "San Cayetano Istepeque", "San Esteban Catarina", "San Ildefonso", "San Lorenzo", "San Sebastián", "San Vicente", "Santa Clara", "Santo Domingo", "Tecoluca", "Tepetitán", "Verapaz"],
    "Usulután": ["Alegría", "Berlín", "California", "Concepción Batres", "El Triunfo", "Ereguayquín", "Estanzuelas", "Jiquilisco", "Jucuapa", "Jucuarán", "Mercedes Umaña", "Nueva Granada", "Ozatlán", "Puerto El Triunfo", "San Agustín", "San Buenaventura", "San Dionisio", "San Francisco Javier", "Santa Elena", "Santa María", "Santiago de María", "Tecapán", "Usulután"]
}

def mostrar_municipios():
   
        # Se solicita al usuario el nombre de un departamento
        Departamento_elegido = input("Ingrese el nombre de un departamento: ")
        # Si el departamento elegido está en el arreglo, se muestran sus municipios
        if Departamento_elegido in Municipios:
            print(f"Los municipios de {Departamento_elegido} son:")
            # Se recorre el arreglo de municipios del departamento elegido
            for Municipio in Municipios[Departamento_elegido]:
                print(Municipio)
        else:
            print("El departamento ingresado no es válido.")
        # Se pregunta al usuario si desea consultar otro departamento

mostrar_municipios

while True:
    Consultar_otro = input("¿Desea consultar un departamento? (s/n): ")
    if Consultar_otro == 's':
        mostrar_municipios()
        # Si la respuesta es sí, se vuelve a ejecutar el programa
        break    
    else: print('Fin del programa')
    
        