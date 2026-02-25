from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    contact_ids = fields.One2many(
        comodel_name='res.partner',
        compute='_compute_contact_ids',
        inverse='_inverse_contact_ids',
        string='Contacts',
    )

    @api.depends('partner_id', 'partner_id.child_ids',
                 'partner_id.child_ids.type', 'partner_id.child_ids.company_type')
    def _compute_contact_ids(self):
        for lead in self:
            if lead.partner_id:
                lead.contact_ids = lead.partner_id.child_ids.filtered(
                    lambda p: p.company_type == 'person' and p.type == 'contact'
                )
            else:
                lead.contact_ids = self.env['res.partner']

    def _inverse_contact_ids(self):
        # Records created via the inline form already have parent_id set
        # from context (default_parent_id). No additional logic required.
        pass
