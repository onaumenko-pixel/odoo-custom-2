from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='parent_id',
        string='Contacts',
        domain="[('type', '=', 'contact')]",
        compute='_compute_contact_ids',
        readonly=False,
        store=False,
    )

    @api.depends('partner_id', 'partner_id.child_ids', 'partner_id.child_ids.type')
    def _compute_contact_ids(self):
        for lead in self:
            if lead.partner_id:
                lead.contact_ids = lead.partner_id.child_ids.filtered(
                    lambda p: p.type == 'contact'
                )
            else:
                lead.contact_ids = self.env['res.partner']
