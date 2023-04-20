from odoo import api, models, fields


class HospitalPatient(models.Model):
    _name = "hospital.appointment"
    _inherit = ["mail.thread", 'mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id = fields.Many2one(comodel_name='hospital.patient',string="Patient")
    appointment_time = fields.Datetime(string="Appointment Time")
    booking_date = fields.Date(string="Booking Date")