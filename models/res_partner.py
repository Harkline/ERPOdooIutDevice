from odoo import fields, models

class ResPartner(models.Model):

    #Héritage
    _inherit = "res.partner"

    _name = "res.partner"

    employeeRef = fields.Char(string="Employee's Reference")
    ref = fields.Char(string="Reference")

    # Permet de faire le lien BD 1...*
    deviceIds = fields.One2many('iut.it.device', 'partnerId')
