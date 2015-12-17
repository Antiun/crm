# -*- coding: utf-8 -*-
# © 2015 Antiun Ingenieria S.L. - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "NACE Activities in CRM",
    "version": "8.0.1.0.0",
    "category": "Customer Relationship Management",
    "website": "http://www.antiun.com",
    "author": "Antiun Ingeniería S.L., "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "crm",
        "partner_nace"
    ],
    "data": [
        "views/crm_lead_view.xml",
    ]
}
