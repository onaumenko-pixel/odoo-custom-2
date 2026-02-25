from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        related='partner_id.child_ids',
        string='Contacts',
        readonly=False,
    )
