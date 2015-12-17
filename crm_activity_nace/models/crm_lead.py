# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    main_nace_id = fields.Many2one(comodel_name='res.partner.nace',
                                   string="Main activity")
    secondary_nace_ids = fields.Many2many(comodel_name='res.partner.nace',
                                          string="Other activities")

    def _lead_create_contact(self, cr, uid, lead, name, is_company,
                             parent_id=False, context=None):
        """Propagate NACE activity to created partner.
        """
        partner_id = super(CrmLead, self)._lead_create_contact(
            cr, uid, lead, name, is_company, parent_id=parent_id,
            context=context)
        data = {
            'main_nace_id': lead.main_nace_id.id,
            'secondary_nace_ids': [(4, x.id) for x in lead.secondary_nace_ids]}
        self.pool['res.partner'].write(cr, uid, partner_id, data,
                                       context=context)
        return partner_id
