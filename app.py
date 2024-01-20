from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def pagina1_esp():
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
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
        'proteccionDatos' : 'Proteccion de Datos',
        
    }
    return render_template('pagina1-esp.html',data=data)

@app.route('/registro_esp')
def registro_esp():
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
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

@app.route('/login_esp')
def login_esp():
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
        'nombre' : 'Nombre de Usuario o Correo Electronico',
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
    }
    return render_template('login_esp.html', data=data)

@app.route('/quienesSomos')
def quienesSomos():
    data={
        'titulo':'TAVIT',
        'registro':'Regsitro',
        'quieneSomos':'Quienes Somos',
        'contacto':'Contacto',
        'idiomaEs':'ES',
        'idiomaCa':'CA',
        'idiomaEn':'EN',
        'login':'LOGIN / REGISTER',
        'quienesSomos2' : 'QUIENES SOMOS',
        'informacion1' : 'Somos una escuela homologada por enseñanza para niños y niñas hasta los 3 años',
        'informacion2' : 'La escuela esta abierta de',
        'informacion3' : 'Lunes',
        'informacion4' : 'a',
        'informacion5' : 'Viernes',
        'informacion6' : 'de',
        'informacion7' : '7:30',
        'informacion8' : '18:00',
        'informacion9' : 'Si quiere hacer que su hijo/hija pertenezca a esta escuela, pulse en',
        'informacion10' : 'Registro',
        'informacion11' : 'o',
        'informacion12' : 'pulse aquí',
        'dondeEstamos':'DONDE ESTAMOS',
        'infoDondeEstamos' : 'La escuela se encuentra en Cardedeu, un pueblo del Valles Oriental, la calle en la cual se encuentra la escuela es la siguiente: C Ramon Llull, 12, 08440, Cardedeu (Barcelona).',
        'contacto2' : 'CONTACTO',
        'facebook' : 'facebook.com/tavitcardedeu',
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

if __name__ == '__main__':
    app.run(debug=True,port=5000)