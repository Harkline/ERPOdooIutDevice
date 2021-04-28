from odoo import api, fields, models

class IutItBrand():

    _name = "iut.it.brand"

    name = fields.Char(required=True)
    warrantyDelayMonth = fields.Integer(string="warrantyDelayMonth")
    supportPhone = fields.Integer(string="supportPhone")

    #Permet de faire le lien BD 1...*              ids
    modelId = fields.One2many('iut.it.model', 'iut_it_model.IutItModel.brandId');
