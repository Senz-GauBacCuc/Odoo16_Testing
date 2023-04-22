from datetime import date

from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Patient"

    name = fields.Char('Patient Name', tracking=True)
    dobirth = fields.Date(string='Date of Brith')
    ref = fields.Char('Reference')
    age = fields.Integer('Age', compute='_compute_age', tracking=True)
    gender = fields.Selection(
        [('male', 'Male'),
         ('female', 'Female')],
        'Gender', tracking=True
    )
    active = fields.Boolean('Active', default=True)
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment ID')

    @api.depends('dobirth')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dobirth:
                rec.age = today.year - rec.dobirth.year
            else:
                rec.age = 0

