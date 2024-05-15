from flask import Flask, render_template, request, url_for, redirect, session
import mysql.connector

def base_datos():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='marcremisa10',
        database='tavit'
    )
    return connection


app = Flask(__name__)
app.config['SECRET_KEY'] = 'marcremisa10'

@app.route('/')
def pagina1_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'calendario':'CALENDARIO',
        'dondeEstamos':'DONDE ESTAMOS',
        'infoDondeEstamos' : 'La escuela se encuentra en Cardedeu, un pueblo del Valles Oriental, la calle en la cual se encuentra la escuela es la siguiente: C Ramon Llull, 12, 08440, Cardedeu (Barcelona).',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos'
    }
    
    return render_template('pagina1-esp.html',data=data)

@app.route('/logout')
def logout():
    session.pop('nombre_usuario', None)
    return redirect(url_for('pagina1_esp'))

@app.route('/correcto')
def correcto():
    data={
        'correcto':'Datos Guardados Correctamente',
        'atras':'Volver a la pagina principal'
    }
    return render_template('correcto.html', data=data)

@app.route('/registro_esp', methods=['GET', 'POST'])
def registro_esp():
    nombre_usuario = session.get('nombre_usuario')
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        domicilio = request.form['domicilio']
        telefono = request.form['telefono']
        nombre_hijo = request.form['nombreHijo']
        apellido_hijo = request.form['apellidoHijo']
        edad_hijo = request.form['edad']

        conn = base_datos()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO registro (nombre, apellido, correo_electronico, domicilio, telefono, nombre_hijo, apellido_hijo, edad_hijo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (nombre, apellido, correo, domicilio, telefono, nombre_hijo, apellido_hijo, edad_hijo))
        conn.commit()
        conn.close()

        return redirect(url_for('correcto'))
    else:
        data={
            'titulo':'TAVIT',
            'registro':'Regsitro',
            'quieneSomos':'Quienes Somos',
            'contacto':'Contacto',
            'idiomaEs':'ES',
            'idiomaCa':'CA',
            'idiomaEn':'EN',
            'nombre_usuario': nombre_usuario,
            'login':'LOGIN / REGISTER',
            'registro2' : 'REGISTRO',
            'info' : 'INFORMACION DEL TUTOR LEGAL',
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'correo' : 'Correo Electronico',
            'domicilio' : 'Domicilio',
            'telefono' : 'Telefono', 
            'info2' : 'INFORMACION DEL HIJO',
            'nombreHijo' : 'Nombre',
            'apellidoHijo' : 'Apellido',
            'edad' : 'Edad',
            'enviar' : 'ENVIAR',
            'copyright' : '© 2023',
            'privacidad' : 'Privacy — Terms',
            'sobreNosotros' : 'Sobre Nosotros',
            'dondeEstamos2' : 'Donde Estamos',
            'escuelas' : 'Escuelas',
            'tuEscuela' : 'Tu escuela',
            'informacion' : 'Informacion',
            'avisoLegal' : 'Aviso Legal',
            'politicaPrivacidad' : 'Politica de Privacidad',
            'politicaCookies' : 'Politica de Cookies',
            'proteccionDatos' : 'Proteccion de Datos',
        }
    return render_template('registro-esp.html',data=data)

@app.route('/datosCorrectos')
def datosCorrectos():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'datosCorrectos':'Datos correctos',
        'pagina1':'Ves pagina principal',
        'nombre_usuario': nombre_usuario
    }
    return render_template('datosCorrectos.html', data=data)

@app.route('/datosIncorrectos')
def datosIncorrectos():
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'login':'LOGIN / REGISTER',
        'login2' : 'LOGIN',
        'registrado' : 'No te has registrado todavia?',
        'nombre' : 'Nombre de Usuario',
        'contraseña' : 'Contraseña',
        'olvidadoContraseña' : 'He olvidado mi contraseña',
        'enviar' : 'ENVIAR',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
        'errorNombre' : 'El nombre es incorrecto',
        'errorContraseña' : 'La contraseña es incorrecta'
    }
    return render_template('datosIncorrectos.html', data=data)

@app.route('/login_esp', methods=['GET', 'POST'])
def login_esp():
    if request.method == 'POST':
        nombre_usuario = request.form['nombreUsuario']
        contraseña = request.form['contraseña']
        
        conn = base_datos()
        cursor = conn.cursor()
        
        consulta = "SELECT * FROM register WHERE NombreUsuario = %s AND Contraseña = %s"
        valores = (nombre_usuario, contraseña)
        cursor.execute(consulta, valores)
        
        usuario = cursor.fetchone()
        
        conn.close()
        
        if usuario:
            session['nombre_usuario'] = nombre_usuario
            return redirect(url_for('datosCorrectos'))
        else:
            data = {
                'error': 'Usuario o contraseña incorrectos.',
                'titulo': 'TAVIT',
                'registro': 'Registro',
                'quieneSomos': 'Quiénes Somos',
                'contacto': 'Contacto',
                'idiomaEs': 'ES',
                'idiomaCa': 'CA',
                'idiomaEn': 'EN',
                'login': 'LOGIN / REGISTER',
                'login2': 'LOGIN',
                'registrado': '¿No te has registrado todavía?',
                'nombre': 'Nombre de Usuario',
                'contraseña': 'Contraseña',
                'olvidadoContraseña': 'He olvidado mi contraseña',
                'enviar': 'ENVIAR',
                'copyright': '© 2023',
                'privacidad': 'Privacidad — Términos',
                'sobreNosotros': 'Sobre Nosotros',
                'dondeEstamos2': 'Dónde Estamos',
                'escuelas': 'Escuelas',
                'tuEscuela': 'Tu Escuela',
                'informacion': 'Información',
                'avisoLegal': 'Aviso Legal',
                'politicaPrivacidad': 'Política de Privacidad',
                'politicaCookies': 'Política de Cookies',
                'proteccionDatos': 'Protección de Datos',
            }
            return render_template('login_esp.html', data=data)
    
    data = {
        'titulo': 'TAVIT',
        'registro': 'Registro',
        'quieneSomos': 'Quiénes Somos',
        'contacto': 'Contacto',
        'idiomaEs': 'ES',
        'idiomaCa': 'CA',
        'idiomaEn': 'EN',
        'login': 'LOGIN / REGISTER',
        'login2': 'LOGIN',
        'registrado': '¿No te has registrado todavía?',
        'nombre': 'Nombre de Usuario o Correo Electrónico',
        'contraseña': 'Contraseña',
        'olvidadoContraseña': 'He olvidado mi contraseña',
        'enviar': 'ENVIAR',
        'copyright': '© 2023',
        'privacidad': 'Privacidad — Términos',
        'sobreNosotros': 'Sobre Nosotros',
        'dondeEstamos2': 'Dónde Estamos',
        'escuelas': 'Escuelas',
        'tuEscuela': 'Tu Escuela',
        'informacion': 'Información',
        'avisoLegal': 'Aviso Legal',
        'politicaPrivacidad': 'Política de Privacidad',
        'politicaCookies': 'Política de Cookies',
        'proteccionDatos': 'Protección de Datos',
    }
    return render_template('login_esp.html', data=data)


@app.route('/cuentaCreada')
def cuentaCreada():
    data={
        'cuentaCreada':'La cuenta ha sido creada',
        'registro':'Registro'
    }
    return render_template('cuentaCreada.html', data=data)

@app.route('/cambiar_contraseña', methods=['GET', 'POST'])
def cambiar_contraseña():
    if request.method == 'POST':
        usuario = request.form['usuario']
        nueva_contraseña = request.form['nueva_contraseña']
        repetir_contraseña = request.form['repetir_contraseña']

        conn = base_datos()
        cursor = conn.cursor()
        
        consulta_usuario = "SELECT * FROM register WHERE NombreUsuario = %s"
        cursor.execute(consulta_usuario, (usuario,))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            consulta_update = "UPDATE register SET Contraseña = %s, RepiteContraseña = %s WHERE NombreUsuario = %s"
            valores = (nueva_contraseña, repetir_contraseña, usuario)
            cursor.execute(consulta_update, valores)
            conn.commit()
            conn.close()
            return redirect(url_for('login_esp'))
        else:
            data = {
                'error': 'El usuario no existe en la base de datos.',
                'cambioContraseña': 'Cambio de Contraseña',
                'usuarioContraseña': 'Usuario',
                'nuevaContraseña': 'Nueva Contraseña',
                'repetirNuevaContraseña' : 'Repita la nueva contraseña',
                'cambiarContraseña': 'Cambiar Contraseña'
            }
            return render_template('cambiar_contraseña.html', data=data)
    else:
        data = {
            'cambioContraseña': 'Cambio de Contraseña',
            'usuarioContraseña': 'Usuario',
            'nuevaContraseña': 'Nueva Contraseña',
            'repetirNuevaContraseña' : 'Repita la nueva contraseña',
            'cambiarContraseña': 'Cambiar Contraseña'
        }
        return render_template('cambiar_contraseña.html', data=data)

@app.route('/register_esp' ,methods=['GET', 'POST'])
def register_esp():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        nombre_usuario = request.form['nombreUsuario']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        repite_contraseña = request.form['repiteContraseña']
        
        conn = base_datos()
        cursor = conn.cursor()
        
        consulta = "INSERT INTO register (Nombre, Apellido, NombreUsuario, CorreoElectronico, Contraseña, RepiteContraseña) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, nombre_usuario, correo, contraseña, repite_contraseña)
        cursor.execute(consulta, valores)
        
        conn.commit()
        conn.close()
        
        return redirect(url_for('cuentaCreada'))
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'login':'LOGIN / REGISTER',
        'register' : 'REGISTER',
        'cuenta' : 'Ya tienes una cuenta?',
        'nombre' : 'Nombre',
        'apellido' : 'Apellido',
        'nombreUsuario' : 'Nombre de Usuario',
        'correo' : 'Correo Electronico',
        'contraseña' : 'Contraseña',
        'repiteContraseña' : 'Repite Contraseña',
        'enviar' : 'ENVIAR',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('register_esp.html', data=data)

@app.route('/quienesSomos_esp')
def quienesSomos_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'quienesSomos2' : 'QUIENES SOMOS',
        'informacion1' : 'Somos una escuela homologada por enseñanza para niños y niñas hasta los 3 años.',
        'informacion2' : 'La escuela esta abierta de',
        'informacion3' : 'Lunes',
        'informacion4' : 'a',
        'informacion5' : 'Viernes',
        'informacion6' : 'de',
        'informacion7' : '7:30',
        'informacion8' : '18:00.',
        'informacion9' : 'Si quiere hacer que su hijo/hija pertenezca a esta escuela, pulse en',
        'informacion10' : 'Registro',
        'informacion11' : 'o',
        'informacion12' : 'pulse aquí',
        'dondeEstamos':'DONDE ESTAMOS',
        'infoDondeEstamos' : 'La escuela se encuentra en Cardedeu, un pueblo del Valles Oriental, la calle en la cual se encuentra la escuela es la siguiente: C Ramon Llull, 12, 08440, Cardedeu (Barcelona).',
        'contacto2' : 'CONTACTO',
        'facebooklink' : 'http://www.facebook.com/tavitcardedeu',
        'facebook' : 'facebook.com/tavitcardedeu',
        'gmaillink' : 'http://www.tavitcardedeu@hotmail.com',
        'gmail' : 'tavitcardedeu@hotmail.com',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('quienesSomos_esp.html', data=data)

@app.route('/avisolegal_esp')
def avisolegal_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'avisolegal2' : 'Aviso Legal',
        'texto1' : 'Esta es una página web ficticia y el contenido aquí proporcionado es solo para fines educativos e ilustrativos. No se debe considerar como asesoramiento legal.',
        'PropiedadIntelectual' : '1. Propiedad Intelectual',
        'texto2' : 'Los contenidos de esta página web, incluyendo textos, imágenes, logotipos, gráficos, sonidos, animaciones y cualquier otro elemento, están protegidos por la legislación sobre propiedad intelectual e industrial.',
        'UsoInformacion' : '2. Uso de la Información',
        'texto3' : 'La información proporcionada en esta página web es solo para fines informativos. No nos hacemos responsables de la exactitud, integridad o actualidad de la información proporcionada.',
        'EnlacesExternos' : '3. Enlaces Externos',
        'texto4' : 'Esta página web puede contener enlaces a sitios web externos sobre los cuales no tenemos control. No nos hacemos responsables del contenido o prácticas de privacidad de estos sitios.',
        'Modificaciones' : '4. Modificaciones',
        'texto5' : 'Nos reservamos el derecho de realizar cambios en esta página web, incluyendo estos términos legales, en cualquier momento y sin previo aviso. Se recomienda revisar periódicamente esta página para estar al tanto de cualquier cambio.',
        'LeyAplicable' : '5. Ley Aplicable',
        'texto6' : 'Estos términos legales se rigen por las leyes de España. Cualquier disputa relacionada con esta página web estará sujeta a la jurisdicción de los tribunales de Barcelona, España.',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('aviso_legal_esp.html', data=data)

@app.route('/politicaCookies_esp')
def politicaCookies_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'cookies' : 'Politica de Cookies',
        'texto1' : 'Esta página web utiliza cookies para mejorar la experiencia del usuario. A continuación, se explica qué son las cookies, cómo las utilizamos y cómo puede gestionarlas.',
        'queSon' : '1. ¿Qué son las Cookies?',
        'texto2' : 'Las cookies son pequeños archivos de texto que se almacenan en su dispositivo cuando visita un sitio web. Estos archivos contienen información que puede ser utilizada por el sitio web para mejorar la experiencia del usuario, recordar preferencias y realizar un seguimiento del comportamiento del usuario.',
        'tipos' : '2. Tipos de Cookies que Utilizamos',
        'texto3' : 'Utilizamos cookies de sesión y cookies persistentes en nuestro sitio web. Las cookies de sesión se eliminan automáticamente cuando cierra su navegador, mientras que las cookies persistentes permanecen en su dispositivo durante un período de tiempo determinado o hasta que las elimine manualmente.',
        'comoUtilizar' : '3. Cómo Utilizamos las Cookies',
        'texto4' : 'Utilizamos cookies para recordar sus preferencias de idioma, personalizar el contenido que ve, analizar el tráfico del sitio y mejorar nuestros servicios. También podemos compartir información sobre su uso de nuestro sitio con nuestros socios de analítica.',
        'gestion' : '4. Gestión de Cookies',
        'texto5' : 'Puede gestionar las cookies en la configuración de su navegador. La mayoría de los navegadores le permiten bloquear o eliminar cookies, así como configurar preferencias para cookies específicas de sitios web. Sin embargo, tenga en cuenta que al deshabilitar las cookies, es posible que algunas funciones de nuestro sitio web no funcionen correctamente.',
        'cambios' : '5. Cambios en la Política de Cookies',
        'texto6' : 'Nos reservamos el derecho de actualizar o cambiar nuestra Política de Cookies en cualquier momento. Le notificaremos cualquier cambio publicando la nueva Política de Cookies en esta página.',
        'contacto2' : '6. Contacto',
        'texto7' : 'Si tiene alguna pregunta sobre nuestra Política de Cookies, por favor contáctenos a tavitcardedeu@hotmail.com.',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('politica_cookies_esp.html', data=data)

@app.route('/politicaPrivacidad_esp')
def politicaPrivacidad_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'politicaPrivacidad' : 'Política de Privacidad',
        'texto1' : 'En Tavit, respetamos y protegemos la privacidad de nuestros usuarios. Esta Política de Privacidad describe cómo recopilamos, utilizamos y protegemos la información personal que usted nos proporciona a través de nuestro sitio web.',
        'recopilacionInformacion' : '1. Recopilación de Información',
        'texto2' : 'Recopilamos información personal que usted nos proporciona voluntariamente, como su nombre, dirección de correo electrónico, número de teléfono, etc., cuando se registra en nuestro sitio, se suscribe a nuestro boletín informativo, participa en encuestas o nos contacta de otras formas.',
        'usoInformacion' : '2. Uso de la Información',
        'texto3' : 'Utilizamos la información personal que recopilamos para comunicarnos con usted, proporcionarle los servicios que solicita, mejorar nuestro sitio web y nuestros servicios, y enviarle información relevante sobre nuestros productos o servicios, siempre que usted nos haya dado su consentimiento para hacerlo.',
        'compartirInformacion' : '3. Compartir Información',
        'texto4' : 'No compartiremos su información personal con terceros, excepto cuando sea necesario para proporcionarle los servicios que solicita o cuando estemos legalmente obligados a hacerlo.',
        'seguridadInformacion' : '4. Seguridad de la Información',
        'texto5' : 'Tomamos medidas razonables para proteger la información personal que recopilamos contra el acceso no autorizado, la divulgación, la alteración o la destrucción.',
        'derechos' : '5. Sus Derechos',
        'texto6' : 'Usted tiene derecho a acceder, corregir y eliminar la información personal que tenemos sobre usted. También puede optar por no recibir comunicaciones de marketing por correo electrónico en cualquier momento.',
        'cambios' : '6. Cambios a esta Política',
        'texto7' : 'Nos reservamos el derecho de actualizar o cambiar nuestra Política de Privacidad en cualquier momento. Le notificaremos cualquier cambio publicando la nueva Política de Privacidad en esta página.',
        'contacto2' : '7. Contacto',
        'texto8' : 'Si tiene alguna pregunta sobre esta Política de Privacidad, por favor contáctenos a tavitcardedeu@hotmail.com.',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('politica_privacidad_esp.html', data=data)

@app.route('/proteccionDatos_esp')
def proteccionDatos_esp():
    nombre_usuario = session.get('nombre_usuario')
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'nombre_usuario': nombre_usuario,
        'login':'LOGIN / REGISTER',
        'proteccionDatos2' : 'Política de Protección de Datos',
        'texto1' : 'En Tavit, nos tomamos muy en serio la protección de sus datos personales. Esta Política de Protección de Datos describe cómo recopilamos, utilizamos y protegemos su información personal cuando utiliza nuestros servicios.',
        'informacion2' : '1. Información que Recopilamos',
        'texto2' : 'Recopilamos información personal que usted nos proporciona voluntariamente, como su nombre, dirección de correo electrónico, número de teléfono, etc., cuando se registra en nuestros servicios, realiza una compra, se comunica con nosotros o participa en encuestas.',
        'usoInformacion' : '2. Uso de la Información',
        'texto3' : 'Utilizamos la información personal que recopilamos para proporcionarle los servicios que solicita, procesar sus transacciones, comunicarnos con usted, personalizar su experiencia y mejorar nuestros servicios.',
        'compartirInformacion' : '3. Compartir Información',
        'texto4' : 'No compartiremos su información personal con terceros, excepto cuando sea necesario para proporcionarle los servicios que solicita o cuando estemos legalmente obligados a hacerlo.',
        'seguridadDatos' : '4. Seguridad de los Datos',
        'texto5' : 'Tomamos medidas razonables para proteger la información personal que recopilamos contra el acceso no autorizado, la divulgación, la alteración o la destrucción.',
        'derechos' : '5. Sus Derechos',
        'texto6' : 'Usted tiene derecho a acceder, corregir y eliminar la información personal que tenemos sobre usted. También puede optar por no recibir comunicaciones de marketing por correo electrónico en cualquier momento.',
        'cambios' : '6. Cambios a esta Política',
        'texto7' : 'Nos reservamos el derecho de actualizar o cambiar nuestra Política de Protección de Datos en cualquier momento. Le notificaremos cualquier cambio publicando la nueva Política de Protección de Datos en esta página.',
        'contacto2' : '7. Contacto',
        'texto8' : 'Si tiene alguna pregunta sobre nuestra Política de Protección de Datos, por favor contáctenos a tavitcardedeu@hotmail.com.',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos2' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('proteccion_datos_esp.html', data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5000)