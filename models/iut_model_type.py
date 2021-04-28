from odoo import fields, models

class IutItModelType(models.Model):

    _name = "iut.model.type"

    name = fields.Char(string="name", required=True)

    # Permet de faire le lien BD *...*, ici avec la classe model
    modelIds = fields.Many2many('iut.it.model')