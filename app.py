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
        'dondeEstamos' : 'Donde Estamos',
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
        'register' : 'REGISTER',
        'nombre' : 'Nombre de Usuario o Correo Electronico',
        'contraseña' : 'Contraseña',
        'olvidadoContraseña' : 'He olvidado mi contraseña',
        'enviar' : 'ENVIAR',
        'nombre2' : 'Nombre',
        'Apellido' : 'Apellido',
        'nombreUsuario' : 'Nombre de Usuario',
        'correo' : 'Correo Electronico',
        'contraseña2' : 'Contraseña', 
        'repiteContraseña' : 'Repite Contraseña',
        'copyright' : '© 2023',
        'privacidad' : 'Privacy — Terms',
        'sobreNosotros' : 'Sobre Nosotros',
        'dondeEstamos' : 'Donde Estamos',
        'escuelas' : 'Escuelas',
        'tuEscuela' : 'Tu escuela',
        'informacion' : 'Informacion',
        'avisoLegal' : 'Aviso Legal',
        'politicaPrivacidad' : 'Politica de Privacidad',
        'politicaCookies' : 'Politica de Cookies',
        'proteccionDatos' : 'Proteccion de Datos',
    }
    return render_template('login_esp.html', data=data)

if __name__ == '__main__':
    app.run(debug=True,port=5000)