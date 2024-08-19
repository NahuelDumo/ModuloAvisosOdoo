{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Alert users with pending project activities upon login',
    'author': 'Nahuel Dumo',
    'category': 'Project',
    'depends': ['base', 'project'],  # No se incluye el módulo "web"
    'data': [
        'data/ir_cron_data.xml',  # Archivo que define la tarea cron
    ],
    'installable': True,
    'application': False,
}
