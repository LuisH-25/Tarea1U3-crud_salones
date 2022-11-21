from flask_wtf import FlaskForm
from wtforms.fields import StringField, EmailField, SubmitField, PasswordField, BooleanField

from wtforms.validators import DataRequired

class SalonesForm(FlaskForm):
    aula = StringField("Aula", validators=[DataRequired()])
    hora_entrada = StringField("Hora de Entrada", validators=[DataRequired()])
    submit = SubmitField("Enviar")


class AlumnosForm(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellido = StringField("Apellido", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired()])
    id_aula = StringField("Id Aula", validators=[DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Ingresar')
