from odoo import fields, models

class IutItBrand(models.Model):

    _name = "iut.it.brand"

    _python_sql_constraints_Unique_Key = [('name_uniq', 'unique (name)', 'name is a unique key, violation of constraint !')]

    name = fields.Char(required=True)
    warrantyDelayMonth = fields.Integer(string="warrantyDelayMonth")
    supportPhone = fields.Integer(string="supportPhone")

    #Permet de faire le lien BD 1...*              ids
    modelId = fields.One2many('iut.it.model', 'brandId');
