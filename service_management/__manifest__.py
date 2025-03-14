# -*- coding: utf-8 -*-
{
    'name': 'Service Management',
    "summary": 'This module will help a hypothetical IT company manage its customer services (IT support tickets)',
    'author': 'rvcsdev',
    'website': 'https://github.com/rvcsdev',
    'version': '1.0',
    'category': 'Services/Helpdesk',
    'license': 'AGPL-3',
    'depends': ['base','mail','contacts'],
    'data': [
        'security/service_ticket_security.xml',
        'security/ir.model.access.csv',
        'data/mail_template_data.xml',
        'views/service_ticket_views.xml',
        'report/ticket_summary_report_views.xml',
    ],
    'demo': [
        'data/service_ticket_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}