from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char('Patient Name', tracking=True)
    ref = fields.Char('Reference')
    age = fields.Integer('Age', tracking=True)
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        'Gender', tracking=True
    )
    active = fields.Boolean('Active', default=True)
