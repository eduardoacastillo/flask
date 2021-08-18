from flask import Flask
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'crypsoft1@gmail.com'
app.config['MAIL_PASSWORD'] = 'Sabbath_90210%'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
 
mail = Mail(app)

mail.init_app(app)

@app.route("/")
def index():
  msg = Message('Mensaje que quieres enviar', sender = 'crypsoft1@gmail.com', recipients = ['pysofting@gmail.com'])
  msg.body = "Buenos dias, este correo está enviado desde una aplicación Flask "
  mail.send(msg)
  return "Mensaje enviado"
 
if __name__ == '__main__':
    app.run(debug=True)