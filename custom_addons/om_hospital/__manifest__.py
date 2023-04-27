{
    'name': "Hospital Management",
    'version': '1.0.0',
    'category': 'Hospital',
    'summary': 'Hospital Manangement System',
    'description': """
    Hospital Management System
    """,

    'depends': ['mail','product'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment_view.xml',
        'views/patient_tag_view.xml',
    ],

    'demo': [],

    'auto_install': False,
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}