from odoo import models

class MyModuleCron(models.Model):
    _name = 'my.module.cron'
    _description = 'My Module Cron Job'

    def cron_check_pending_activities(self):
        # Obtener el modelo de las tareas del proyecto
        task_model = self.env['project.task']
        # Buscar tareas pendientes para todos los usuarios
        tasks = task_model.search([
            ('user_id', '!=', False),
            ('stage_id', '=', False)
        ])

        # Agrupar tareas por usuario
        user_tasks = {}
        for task in tasks:
            user_id = task.user_id.id
            if user_id not in user_tasks:
                user_tasks[user_id] = 0
            user_tasks[user_id] += 1

        # Notificar a cada usuario sobre sus tareas pendientes
        for user_id, count in user_tasks.items():
            user = self.env['res.users'].browse(user_id)
            message = f'Tienes {count} actividades pendientes.'
            user.notify_info(message)
