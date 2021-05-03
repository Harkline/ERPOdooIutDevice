from odoo import fields, models

#models.Model()
class IutItDevice(models.Model):
    _name = "iut.it.device"

    name = fields.Char(string='Name', required=True)
    dateAllocation = fields.Date(string="Allocation's date")
    serialNumber = fields.Char(string="Serial's number", required=True)
    datePurchase = fields.Date(string="Purchase's date")
    dateWarrantyEnd = fields.Date(string='End Of warranty')

    # Permet de faire le lien BD *...1
    modelId = fields.Many2one('iut.it.model')
    partnerId = fields.Many2one('res.partner')