from odoo import api, fields, models

class ResPartner():

    #Héritage
    _inherit = "res.partner"

    _name = "res.partner"

    employeeRef = fields.Char()
    # Permet de faire le lien BD 1...*
    deviceIds = fields.One2many('iut.it.device', 'iut_it_device.IutItDevice.partnerId')
