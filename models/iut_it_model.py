from odoo import fields, models

class IutItModel(models.Model):

    _name = "iut.it.model"

    #Rajouter la constrainte sql de clef unique sur un champ
    _python_sql_constraints_Unique_Key = [('ref_uniq', 'unique (ref)', 'ref is a unique key, violation of constraint !')]


    name = fields.Char(string='Name', required=True)
    ref = fields.Char(string='Reference')

    #Permet de faire le lien BD *...* ou *...1 ou 1..*
    typeIds = fields.Many2many('iut.model.type')
    brandId = fields.Many2one('iut.it.brand')
    deviceId = fields.One2many('iut.it.device', 'modelId')

