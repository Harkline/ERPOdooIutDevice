from odoo import fields, models

class ResPartner(models.Model):

    #Héritage
    _inherit = "res.partner"

    _name = "res.partner"

    employeeRef = fields.Char(string='employeeRef')
    ref = fields.Char(string='ref')

    # Permet de faire le lien BD 1...*
    deviceIds = fields.One2many('iut.it.device', 'partnerId')
