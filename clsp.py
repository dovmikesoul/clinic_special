from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)

app.secret_key = b'pbkdf2:sha256:260000$COZLeniiSCAUAHU9$fe34ef743290b5d84190c181937297065a551ce31546df20f10ff0f56d9183ee'


# Protegida. Solo pueden entrar los que han iniciado sesión


@app.route("/escritorio")
def escritorio():
    return render_template("escritorio.html")

# Formulario para iniciar sesión


@app.route("/login")
def login():
    return render_template("login.html")

# Manejar login


@app.route("/hacer_login", methods=["POST"])
def hacer_login():
    correo = request.form["correo"]
    palabra_secreta = request.form["palabra_secreta"]
    # Aquí comparamos. Lo hago así de fácil por simplicidad
    # En la vida real debería ser con una base de datos y una contraseña hasheada
    if correo == "dovmikesoul@gmail.com" and palabra_secreta == "RTX2050":
        # Si coincide, iniciamos sesión y además redireccionamos
        session["usuario"] = correo
        # Aquí puedes colocar más datos. Por ejemplo
        # session["nivel"] = "administrador"
        return redirect("/escritorio")
    else:
        # Si NO coincide, lo regresamos
        flash("Correo o contraseña incorrectos")
        return redirect("/login")


# Cerrar sesión
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


# Un "middleware" que se ejecuta antes de responder a cualquier ruta. Aquí verificamos si el usuario ha iniciado sesión
@app.before_request
def antes_de_cada_peticion():
    ruta = request.path
    # Si no ha iniciado sesión y no quiere ir a algo relacionado al login, lo redireccionamos al login
    if not 'usuario' in session and ruta != "/login" and ruta != "/hacer_login" and ruta != "/logout" and not ruta.startswith("/static"):
        flash("Inicia sesión para continuar")
        return redirect("/login")
    # Si ya ha iniciado, no hacemos nada, es decir lo dejamos pasar


# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
