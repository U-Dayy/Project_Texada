# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 00:21:43 2018

@author: udays
"""


# additional file to provide form details for 3 pages
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField,DateTimeField,FloatField
from wtforms.validators import DataRequired, Length

class input_form(FlaskForm):
    id =  IntegerField('ID', validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    datetime = DateTimeField("DateTime", validators= [DataRequired()])
    Longitude = FloatField("Langitide", validators=[DataRequired()])
    Latitude = FloatField("Latitude", validators=[DataRequired()])
    Elevation = IntegerField("Elevation", validators=[DataRequired()])
    Submit = SubmitField("Add")

class Delete_form(FlaskForm):
    Index = IntegerField("Index", validators=[DataRequired()])
    Submit = SubmitField("Delete")
    
class updqate_form(FlaskForm):
    Index = IntegerField("Index", validators=[DataRequired()])
    id =  IntegerField('ID', validators=[DataRequired()])
    description = StringField("Description", validators=[DataRequired()])
    datetime = DateTimeField("DateTime", validators= [DataRequired()])
    Longitude = FloatField("Langitide", validators=[DataRequired()])
    Latitude = FloatField("Latitude", validators=[DataRequired()])
    Elevation = IntegerField("Elevation", validators=[DataRequired()])
    Submit = SubmitField("Update")
