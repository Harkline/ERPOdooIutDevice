from odoo import api, fields, models

class ResPartner():

    _employee_ref = ""
    _device_ids = ""

    employeeRef = fields.Char()
    deviceIds = fields.Integer()