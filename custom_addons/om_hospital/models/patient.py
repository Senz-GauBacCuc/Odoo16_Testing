from odoo import api, models, fields

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char('Patient Name:')
    age = fields.Integer('Age')
    gender = fields.Selection(
        [('male','Male'),
         ('female','Female')],
        'Gender'
    )