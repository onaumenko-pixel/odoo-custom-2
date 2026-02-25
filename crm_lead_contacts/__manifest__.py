{
    'name': 'CRM Lead Contacts',
    'version': '17.0.1.0.0',
    'category': 'CRM',
    'summary': 'Add a Contacts tab to CRM leads showing contact persons of the linked company',
    'depends': ['crm', 'contacts'],
    'data': [
        'views/crm_lead_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
