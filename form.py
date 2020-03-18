from wtforms import Form, StringField

class PlayerForm(Form):
    player = StringField()