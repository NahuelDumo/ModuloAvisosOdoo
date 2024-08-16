{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Notifica al usuario sobre actividades pendientes al iniciar sesión.',
    'author': 'Nahuel Dumo',
    'category': 'Productivity',
    'depends': ['base', 'project'],
    'data': [
        'data/ir_cron_data.xml',  # Archivo XML con la definición del cron job
    ],
    'installable': True,
    'application': False,
}
