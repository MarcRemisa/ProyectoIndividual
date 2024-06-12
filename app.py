from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

app.secret_key = 'tu_clave_secreta_aqui'

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="marcremisa10",
    database="tavit"
)

translations = {
    'ca': {
        'iniciH': 'Inici',
        'escolaH': "L'escola",
        'contacteH': 'Contacte',
        'matriculaH': 'Matrícula',
        'caH': 'CA',
        'enH': 'EN',
        'esH': 'ES',
        'calendari': 'CALENDARI',
        'frase': '"Ensenyem no només perquè els nens aprenguin, sinó perquè estimin aprendre"',
        'benvinguts': "Benvinguts a l'escola TAVIT!",
        'bentext': "És una satisfacció per a nosaltres donar-vos la benvinguda al nostre lloc web, que neix amb la voluntat d'oferir, amb claredat i transparència, informació d'interès sobre el nostre centre privat d'educació infantil, una Guarderia a Cardedeu moderna plena d'activitats durant tot el curs.",
        'info1': '☑️ Portem més de 30 anys!',
        'info2': "☑️ Obert els mesos d'estiu",
        'info3': "☑️ Centre d'educació infantil fins als 3 anys",
        'info4': "☑️ 2 plantes a l'escola",
        'info5': '☑️ Pati de 500m2',
        'escola': "L'escola TAVIT",
        'escolainfo1': "La nostra escola, amb 29 anys d'experiència, és una institució homologada per Ensenyament, dedicada a la cura i educació dels nens i nenes fins als 3 anys d'edat. El nostre principal objectiu és proporcionar un entorn segur i estimulant on els més petits puguin aprendre mitjançant el joc, gaudir del seu temps, compartir rialles i experiències, i desenvolupar-se de manera integral durant aquesta etapa tan crucial del seu creixement.",
        'opinions': 'OPINIONS',
        'quiSom': 'Qui Som',
        'infoquiSom': 'La nostra escola, amb 29 anys de experiència, és una institució homologada per Ensenyament, dedicada a la cura i educació dels nens i nenes fins als 3 anys de edat.',
        'infoquiSom2': 'El nostre principal objectiu és proporcionar un entorn segur i estimulant on els més petits puguin aprendre mitjançant el joc, gaudir del seu temps, compartir rialles i experiències, i desenvolupar-se de manera integral durant aquesta etapa tan crucial del seu creixement.',
        'infoquiSom3': 'Estem compromesos a oferir una educació de qualitat que promogui el desenvolupament físic, emocional, social i cognitiu dels nostres alumnes, sent conscients de la importància acompanyar-los en aquest viatge aprenentatge i descoberta.',
        'infoquiSom4': 'Així doncs, a la nostra escola, els nostres educadors estan plenament compromesos amb el benestar i el desenvolupament integral dels infants. Mitjançant activitats adaptades a les seves edats i necessitats, fomentem la curiositat, la creativitat i la autonomia dels nostres alumnes. A través de jocs sensorials, activitats artístiques, música, contes i moments de joc lliure, proporcionem un entorn enriquidor on poden explorar i descobrir el món que els envolta.',
        'infoquiSom5': 'A més, treballem en estreta col·laboració amb les famílies per crear una comunitat educativa cohesionada, on es fomenta la comunicació i la participació activa de tots els membres en el procés educatiu dels nens i nenes. En definitiva, la nostra escola és un espai de aprenentatge acollidor i estimulant, on cada infant és valorat i respectat com a individu únic i amb un gran potencial a explorar.',
        'horaris2': "Els nostres horaris",
        'horariEscolar': 'Horari Escolar',
        'horariEscolarinfo': 'De Dilluns a Divendres de 7:30 - 18:00',
        'HorariMenjador': 'Horari Menjador',
        'HorariMenjadorinfo': 'A partir de les 13:00',
        'HorariDiesFestius': 'Dies Festius',
        'HorariDiesFestiusinfo': 'La guarderia estara tencada els dies festius, nacionals y locals',
        'horariEstiu': 'Horari Estiu',
        'horariEstiuinfo': 'La guarderia estara oberta durant tot els mesos de Juny, Juliol, amb el mateix horari, de 7:30 - 18:00',
        'instalacio': '-INSTAL·LACIÓ-',
        'instalacioinfo': "La guarderia esta ubicada al centre de Cardedeu, te un gran pati d'uns 500 m2, amb dos plantes, on la planta principal hi esta l'entrada, el menjador, la cuina, el despaix, i un lavabo, la segona planta es on estan ubicades les sales dels nens i nenes.",
        'instalacioinfo2': "El pati, es un lloc bastant ampli i assolellat i la seva distribució ens permet que els alumnes de cada edat surtin cadascun evitant que s'ajuntin diferents edats al pati. A mes a l'estiu es fan activitats al pati, perque els nens i nenes s'ho passin be durant la calor",
        'instalacioinfo3': "Les nostres instal·lacions són modernes i compleixen estrictament totes les exigències i les normatives actuals, dissenyades amb molt de detall per aconseguir un entorn estimulant i segur que potenciï el desenvolupament saludable dels nostres alumnes.",
        'primeraPlanta': 'Primera Planta',
        'primera1': '·Entrada',
        'primera2': '·Menjador',
        'primera3': '·Cuina',
        'primera4': '·Despaix',
        'primera5': '·Lavabo',
        'segonaPlanta': 'Segona Planta',
        'segona1': '·1 sala nadons 0-1 anys',
        'segona2': '·2 sales nans 1-2 anys',
        'segona3': '·1 sala gegants 2-3 anys',
        'segona4': '·Lavabos per als nens',
        'segona5': '·Accés al pati',
        'onEstemC':'On estem',
        'detalls':'Detalls de contacte',
        'direccio':'Direcció',
        'nomDireccio':'Carrer Ramon Llull, 10, 08440 Cardedeu, Barcelona',
        'horari':'Horari',
        'horaris':'Dilluns a Divendres',
        'horarisHora':'7:30 - 18:00',
        'telefon':'Telefon',
        'telefonNum':'938 71 16 84',
        'email':'E-mail',
        'emailNom':'tavitcardedeu@hotmail.com',
        'Missatge':'Envia un missatge',
        'nom':'Nom',
        'email2':'E-mail',
        'MissatgeText':'Missatge',
        'quiEspot':'Qui es pot apuntar?',
        'quiEspotinfo':'-Els nens i nenes de 0 a 3 anys-',
        'quinEshorari':"Quin es l'horari?",
        'quinEshorariinfo':"-L'horari es de 7:30 a 18-00-",
        'formMatricula':'Matricula 2024-2025',
        'nomForm':'Nom',
        'cognomForm':'Cognom',
        'CorreuForm':'Correu Electronic',
        'DomiciliForm':'Domicili',
        'nomNadoForm':'Nom nado',
        'cognomNadoForm':'Cognom nado',
        'edatNadoForm':'Edat nado',
        'onEstem':'On estem!',
        'tempsF':'Temperatura a Cardedeu',
        'sobreF': 'Sobre Nosaltres',
        'texF': "Som una escola homologada per Ensenyament per a nens i nenes fins a 3 anys que funciona fa 29 anys. El nostre objectiu és que els infants aprenguin jugant, es diverteixin, riguin, creixin i madurin aspectes d'aquesta edat tan petita.",
        'enllaçosF': 'Enllaços Útils',
        'iniciF': 'Inici',
        'escolaF': "L'escola",
        'contacteF': 'Contacte',
        'matriculaF': 'Matrícula',
        'concate2F': 'Contacte',
        'direccioF': 'Direcció: Carrer Ramon Llull, 10, 08440 Cardedeu, Barcelona',
        'tlfF': 'Telèfon: 938 71 16 84',
        'emailF': 'Email: tavitcardedeu@hotmail.com',
        'dretsF': "Drets d'autor, 2024. Tots els drets d'autor reservats"
    },
    'en': {
        'iniciH': 'Home',
        'escolaH': 'School',
        'contacteH': 'Contact',
        'matriculaH': 'Registration',
        'caH': 'CA',
        'enH': 'EN',
        'esH': 'ES',
        'calendari': 'CALENDAR',
        'frase': '"We teach not only so that children learn, but so they love to learn"',
        'benvinguts': 'Welcome to TAVIT School!',
        'bentext': "It's a pleasure for us to welcome you to our website, which is born with the intention of offering, with clarity and transparency, interesting information about our private infant education center, a modern Nursery in Cardedeu full of activities throughout the year.",
        'info1': '☑️ Over 30 years!',
        'info2': '☑️ Open during summer months',
        'info3': '☑️ Infant education center up to 3 years',
        'info4': '☑️ 2 floors at the school',
        'info5': '☑️ 500m2 playground',
        'escola': 'TAVIT School',
        'escolainfo1': 'Our school, with 29 years of experience, is an institution approved by Education, dedicated to the care and education of children up to 3 years old. Our main goal is to provide a safe and stimulating environment where the little ones can learn through play, enjoy their time, share laughs and experiences, and develop fully during this crucial stage of their growth.',
        'opinions': 'OPINIONS',
        'quiSom': 'Who We Are',
        'infoquiSom': "Our school, with 29 years of experience, is an institution approved by Education, dedicated to the care and education of children up to 3 years old.",
        'infoquiSom2': 'Our main objective is to provide a safe and stimulating environment where the little ones can learn through play, enjoy their time, share laughs and experiences, and develop fully during this crucial stage of their growth.',
        'infoquiSom3': 'We are committed to offering quality education that promotes the physical, emotional, social, and cognitive development of our students, being aware of the importance of accompanying them on this journey of learning and discovery.',
        'infoquiSom4': 'Therefore, at our school, our educators are fully committed to the well-being and integral development of children. Through activities adapted to their ages and needs, we foster curiosity, creativity, and autonomy in our students. Through sensory games, artistic activities, music, stories, and moments of free play, we provide an enriching environment where they can explore and discover the world around them.',
        'infoquiSom5': 'Additionally, we work closely with families to create a cohesive educational community, where communication and active participation of all members in the educational process of children are encouraged. In short, our school is a welcoming and stimulating learning space, where each child is valued and respected as a unique individual with great potential to explore.',
        'horaris': "Our Schedules",
        'horariEscolar': 'School Schedule',
        'horariEscolarinfo': 'Monday to Friday from 7:30 - 18:00',
        'HorariMenjador': 'Dining Schedule',
        'HorariMenjadorinfo': 'Starting from 13:00',
        'HorariDiesFestius': 'Public Holidays',
        'HorariDiesFestiusinfo': 'The nursery will be closed on public holidays, national and local',
        'horariEstiu': 'Summer Schedule',
        'horariEstiuinfo': 'The nursery will be open during the months of June, July, with the same schedule, from 7:30 - 18:00',
        'instalacio': '-FACILITIES-',
        'instalacioinfo': "The nursery is located in the center of Cardedeu, it has a large patio of about 500 m2, with two floors, where the main floor is the entrance, the dining room, the kitchen, the office, and a bathroom, the second floor is where the classrooms of the children are located.",
        'instalacioinfo2': "The patio is a fairly large and sunny place and its distribution allows students of each age to go out avoiding different ages meeting on the patio. Also, in summer activities are held in the courtyard, so that children have fun during the heat.",
        'instalacioinfo3': "Our facilities are modern and strictly comply with all current requirements and regulations, designed in great detail to achieve a stimulating and safe environment that enhances the healthy development of our students.",
        'primeraPlanta': 'First Floor',
        'primera1': '·Entrance',
        'primera2': '·Dining room',
        'primera3': '·Kitchen',
        'primera4': '·Office',
        'primera5': '·Bathroom',
        'segonaPlanta': 'Second Floor',
        'segona1': '·1 baby room 0-1 years',
        'segona2': '·2 toddler rooms 1-2 years',
        'segona3': '·1 giant room 2-3 years',
        'segona4': '·Bathrooms for children',
        'segona5': '·Access to the patio',
        'onEstemC': 'Where we are',
        'detalls': 'Contact details',
        'direccio': 'Address',
        'nomDireccio': 'Ramon Llull Street, 10, 08440 Cardedeu, Barcelona',
        'horari': 'Opening hours',
        'horaris': 'Monday to Friday',
        'horarisHora': '7:30 - 18:00',
        'telefon': 'Phone',
        'telefonNum': '938 71 16 84',
        'email': 'Email',
        'emailNom': 'tavitcardedeu@hotmail.com',
        'Missatge': 'Send a message',
        'nom': 'Name',
        'email2': 'Email',
        'MissatgeText': 'Message',
        'quiEspot': 'Who can sign up?',
        'quiEspotinfo': '- Children from 0 to 3 years old -',
        'quinEshorari': 'What is the schedule?',
        'quinEshorariinfo': '- The schedule is from 7:30 to 18:00 -',
        'formMatricula': 'Enrollment 2024-2025',
        'nomForm': 'First Name',
        'cognomForm': 'Last Name',
        'CorreuForm': 'Email',
        'DomiciliForm': 'Address',
        'nomNadoForm': "Child's Name",
        'cognomNadoForm': "Child's Last Name",
        'edatNadoForm': "Child's Age",
        'onEstem': 'Where we are!',
        'tempsF':'Temperature at Cardedeu',
        'sobreF': 'About Us',
        'texF': "We are a school approved by Education for children up to 3 years old that has been operating for 29 years. Our goal is for children to learn through play, have fun, laugh, grow, and mature aspects of this very young age.",
        'enllaçosF': 'Useful Links',
        'iniciF': 'Home',
        'escolaF': 'School',
        'contacteF': 'Contact',
        'matriculaF': 'Registration',
        'concate2F': 'Contact',
        'direccioF': 'Address: Carrer Ramon Llull, 10, 08440 Cardedeu, Barcelona',
        'tlfF': 'Phone: 938 71 16 84',
        'emailF': 'Email: tavitcardedeu@hotmail.com',
        'dretsF': 'Copyright, 2024. All rights reserved'
    },
    'es': {
        'iniciH': 'Inicio',
        'escolaH': 'Escuela',
        'contacteH': 'Contacto',
        'matriculaH': 'Matrícula',
        'caH': 'CA',
        'enH': 'EN',
        'esH': 'ES',
        'calendari': 'CALENDARIO',
        'frase': '"Enseñamos no solo para que los niños aprendan, sino para que amen aprender"',
        'benvinguts': '¡Bienvenidos a la escuela TAVIT!',
        'bentext': "Es un placer para nosotros darles la bienvenida a nuestro sitio web, que nace con la intención de ofrecer, con claridad y transparencia, información interesante sobre nuestro centro privado de educación infantil, una Guardería en Cardedeu moderna llena de actividades durante todo el año.",
        'info1': '☑️ ¡Más de 30 años!',
        'info2': '☑️ Abierto durante los meses de verano',
        'info3': '☑️ Centro de educación infantil hasta los 3 años',
        'info4': '☑️ 2 plantas en la escuela',
        'info5': '☑️ Patio de 500m2',
        'escola': 'La escuela TAVIT',
        'escolainfo1': 'Nuestra escuela, con 29 años de experiencia, es una institución homologada por Educación, dedicada al cuidado y educación de niños y niñas hasta los 3 años de edad. Nuestro principal objetivo es proporcionar un entorno seguro y estimulante donde los más pequeños puedan aprender a través del juego, disfrutar de su tiempo, compartir risas y experiencias, y desarrollarse plenamente durante esta etapa crucial de su crecimiento.',
        'opinions': 'OPINIONES',
        'quiSom': 'Quiénes Somos',
        'infoquiSom': "Nuestra escuela, con 29 años de experiencia, es una institución aprobada por Educación, dedicada al cuidado y educación de niños de hasta 3 años.",
        'infoquiSom2': 'Nuestro principal objetivo es proporcionar un entorno seguro y estimulante donde los más pequeños puedan aprender a través del juego, disfrutar de su tiempo, compartir risas y experiencias, y desarrollarse plenamente durante esta etapa crucial de su crecimiento.',
        'infoquiSom3': 'Estamos comprometidos a ofrecer una educación de calidad que promueva el desarrollo físico, emocional, social y cognitivo de nuestros estudiantes, siendo conscientes de la importancia de acompañarlos en este viaje de aprendizaje y descubrimiento.',
        'infoquiSom4': 'Por lo tanto, en nuestra escuela, nuestros educadores están totalmente comprometidos con el bienestar y desarrollo integral de los niños. A través de actividades adaptadas a sus edades y necesidades, fomentamos la curiosidad, la creatividad y la autonomía en nuestros estudiantes. A través de juegos sensoriales, actividades artísticas, música, cuentos y momentos de juego libre, proporcionamos un entorno enriquecedor donde puedan explorar y descubrir el mundo que les rodea.',
        'infoquiSom5': 'Además, trabajamos en estrecha colaboración con las familias para crear una comunidad educativa cohesionada, donde se fomente la comunicación y la participación activa de todos los miembros en el proceso educativo de los niños. En resumen, nuestra escuela es un espacio de aprendizaje acogedor y estimulante, donde cada niño es valorado y respetado como un individuo único con un gran potencial por explorar.',
        'horaris': "Nuestros Horarios",
        'horariEscolar': 'Horario Escolar',
        'horariEscolarinfo': 'De lunes a viernes de 7:30 a 18:00',
        'HorariMenjador': 'Horario del Comedor',
        'HorariMenjadorinfo': 'A partir de las 13:00',
        'HorariDiesFestius': 'Días Festivos',
        'HorariDiesFestiusinfo': 'La guardería permanecerá cerrada en días festivos, nacionales y locales',
        'horariEstiu': 'Horario de Verano',
        'horariEstiuinfo': 'La guardería estará abierta durante los meses de junio y julio, con el mismo horario, de 7:30 a 18:00',
        'instalacio': '-INSTALACIONES-',
        'instalacioinfo': "La guardería está ubicada en el centro de Cardedeu, cuenta con un gran patio de aproximadamente 500 m2, con dos plantas, donde la planta principal es la entrada, el comedor, la cocina, la oficina y un baño, la segunda planta es donde se encuentran las aulas de los niños.",
        'instalacioinfo2': "El patio es un lugar bastante grande y soleado y su distribución permite que los estudiantes de cada edad salgan evitando que diferentes edades se encuentren en el patio. Además, en verano se realizan actividades en el patio, para que los niños se diviertan durante el calor.",
        'instalacioinfo3': "Nuestras instalaciones son modernas y cumplen estrictamente con todos los requisitos y regulaciones actuales, diseñadas con gran detalle para lograr un entorno estimulante y seguro que potencie el sano desarrollo de nuestros estudiantes.",
        'primeraPlanta': 'Primera Planta',
        'primera1': '·Entrada',
        'primera2': '·Comedor',
        'primera3': '·Cocina',
        'primera4': '·Oficina',
        'primera5': '·Baño',
        'segonaPlanta': 'Segunda Planta',
        'segona1': '·1 sala de bebés 0-1 años',
        'segona2': '·2 salas de niños pequeños 1-2 años',
        'segona3': '·1 sala gigante 2-3 años',
        'segona4': '·Baños para niños',
        'segona5': '·Acceso al patio',
        'onEstemC': 'Dónde estamos',
        'detalls': 'Detalles de contacto',
        'direccio': 'Dirección',
        'nomDireccio': 'Calle Ramon Llull, 10, 08440 Cardedeu, Barcelona',
        'horari': 'Horario',
        'horaris': 'Lunes a Viernes',
        'horarisHora': '7:30 - 18:00',
        'telefon': 'Teléfono',
        'telefonNum': '938 71 16 84',
        'email': 'Correo electrónico',
        'emailNom': 'tavitcardedeu@hotmail.com',
        'Missatge': 'Enviar un mensaje',
        'nom': 'Nombre',
        'email2': 'Correo electrónico',
        'MissatgeText': 'Mensaje',
        'quiEspot': '¿Quién puede apuntarse?',
        'quiEspotinfo': '- Niños y niñas de 0 a 3 años -',
        'quinEshorari': '¿Cuál es el horario?',
        'quinEshorariinfo': '- El horario es de 7:30 a 18:00 -',
        'formMatricula': 'Matrícula 2024-2025',
        'nomForm': 'Nombre',
        'cognomForm': 'Apellido',
        'CorreuForm': 'Correo Electrónico',
        'DomiciliForm': 'Domicilio',
        'nomNadoForm': 'Nombre del niño',
        'cognomNadoForm': 'Apellido del niño',
        'edatNadoForm': 'Edad del niño',
        'onEstem': '¡Dónde estamos!',
        'tempsF':'Temperatura en Cardedeu',
        'sobreF': 'Sobre Nosotros',
        'texF': 'Somos una escuela homologada por Educación para niños y niñas de hasta 3 años que lleva funcionando 29 años. Nuestro objetivo es que los niños aprendan jugando, se diviertan, rían, crezcan y maduren aspectos de esta temprana edad.',
        'enllaçosF': 'Enlaces Útiles',
        'iniciF': 'Inicio',
        'escolaF': 'Escuela',
        'contacteF': 'Contacto',
        'matriculaF': 'Matrícula',
        'concate2F': 'Contacto',
        'direccioF': 'Dirección: Carrer Ramon Llull, 10, 08440 Cardedeu, Barcelona',
        'tlfF': 'Teléfono: 938 71 16 84',
        'emailF': 'Email: tavitcardedeu@hotmail.com',
        'dretsF': 'Derechos de autor, 2024. Todos los derechos reservados'
        }
    }


@app.route('/')
def index():
    lang = session.get('lang', 'ca')
    data = translations.get(lang, translations['ca'])

    # Recuperar todos los datos de nombre y mensaje de la base de datos
    cursor = db.cursor()
    cursor.execute("SELECT nombre, mensaje FROM contacto ORDER BY id DESC")
    resultados = cursor.fetchall()
    cursor.close()
    
    datos_contacto = []
    for resultado in resultados:
        nombre = resultado[0]
        mensaje = resultado[1]
        datos_contacto.append({"nombre": nombre, "mensaje": mensaje})

    return render_template('paginaPrincipal.html', data=data, datos_contacto=datos_contacto)

@app.route('/escola')
def escola():
    lang = session.get('lang', 'ca')
    data = translations.get(lang, translations['ca'])
    return render_template('escola.html', data=data)

@app.route('/contacte', methods=['GET', 'POST'])
def contacte():
    lang = session.get('lang', 'ca')
    data = translations.get(lang, translations['ca'])
    nombre = ""
    mensaje = ""
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO contacto (nombre, email, mensaje) VALUES (%s, %s, %s)",
            (nombre, email, mensaje)
        )
        db.commit()
        cursor.close()
    else:
        cursor = db.cursor()
        cursor.execute("SELECT nombre, mensaje FROM contacto ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        if result:
            nombre = result[0]
            mensaje = result[1]
        cursor.close()

    return render_template('contacte.html', data=data, nombre=nombre, mensaje=mensaje)


@app.route('/matricula', methods=['GET', 'POST'])
def matricula():
    lang = session.get('lang', 'ca')
    data = translations.get(lang, translations['ca'])
    
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        domicilio = request.form['domicilio']
        nombre_hijo = request.form['nombre_hijo']
        apellido_hijo = request.form['apellido_hijo']
        edad_hijo = request.form['edad_hijo']
        
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO matricula (nombre, apellido, email, domicilio, nombre_hijo, apellido_hijo, edad_hijo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (nombre, apellido, email, domicilio, nombre_hijo, apellido_hijo, edad_hijo)
        )
        db.commit()
        cursor.close()

    return render_template('matricula.html', data=data)

@app.route('/setlang/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or '/')

if __name__ == '__main__':
    app.run(debug=True, port=(5000))
