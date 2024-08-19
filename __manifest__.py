{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Alert users with pending project activities upon login',
    'author': 'Nahuel Dumo',
    'category': 'Project',
    'depends': ['base', 'project'],
    'data': [
        'views/project_activity_alert_views.xml',  # Archivo que contiene la vista modificada
        'data/ir_cron_data.xml',  # Archivo que define la tarea cron (si aplica)
    ],
    'installable': True,
    'application': False,
}
