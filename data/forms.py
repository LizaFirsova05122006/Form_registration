from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    """форма регистрации"""
    login = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm = PasswordField('Repeat password', validators=[DataRequired()])
    surname = StringField('Surname')
    name = StringField('Name')
    age = StringField('Age')
    position = StringField('Position')
    speciality = StringField('Speciality')
    address = StringField('Address')
    submit = SubmitField('Sign up')


class LoginForm(FlaskForm):
    """форма авторизации"""
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Log in')


class WorksForm(FlaskForm):
    """форма добавления работ"""
    team_leader = StringField('ID of captain', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField("Collaborators' id", validators=[DataRequired()])
    is_finished = BooleanField('Is finished?', validators=[DataRequired()])
    submit = SubmitField('Add work')


class WorksRedactionForm(FlaskForm):
    """форма редактирования работ"""
    team_leader = StringField('ID of captain', validators=[DataRequired()])
    job = StringField('Job', validators=[DataRequired()])
    work_size = StringField('Work size', validators=[DataRequired()])
    collaborators = StringField("Collaborators' id", validators=[DataRequired()])
    is_finished = BooleanField('Is finished?', validators=[DataRequired()])
    submit = SubmitField('Redact work')


class DepartmentsForm(FlaskForm):
    """форма добавления департаментов"""
    title = StringField('Title of Department', validators=[DataRequired()])
    members = StringField("Members' id", validators=[DataRequired()])
    email = EmailField('Department email', validators=[DataRequired()])
    submit = SubmitField('Add a Department')


class DepartmentsRedactionForm(FlaskForm):
    """форма редактирования департаментов"""
    title = StringField('Title of Department', validators=[DataRequired()])
    chief = StringField('Chief', validators=[DataRequired()])
    members = StringField("Members' id", validators=[DataRequired()])
    email = EmailField('Department email', validators=[DataRequired()])
    submit = SubmitField('Redact a Department')