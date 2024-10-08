{
    'name': 'Project Task Extension',
    'version': '1.0',
    'category': 'Project',
    'summary': 'Ordenar tareas por fecha de vencimiento y resaltar tareas próximas a vencer',
    'description': """
        Este módulo extiende el módulo de Proyecto para ordenar las tareas por fecha de vencimiento y resaltar en rojo aquellas que tienen menos de 2 días para vencer.
    """,
    'depends': ['project'],
    'data': [
        'views/project_task_view.xml',
    ],
    'installable': True,
    'application': False,
}
