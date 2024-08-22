from odoo import models, api

class MyModuleCron(models.Model):
    _name = 'my.module.cron'

    @api.model
    def cron_check_pending_activities(self):
        users = self.env['res.users'].search([])
        for user in users:
            tasks = self.env['project.task'].search([
                ('user_ids', '=', user.id),
            ])
            if tasks:
                # Almacenar el número de tareas pendientes en un parámetro de sistema
                self.env['ir.config_parameter'].set_param(f'user.{user.id}.pending_tasks', len(tasks))
            else:
                # Limpiar el parámetro si no hay tareas pendientes
                self.env['ir.config_parameter'].set_param(f'user.{user.id}.pending_tasks', 0)

    @api.model
    def get_pending_tasks_message(self):
        user_id = self.env.uid
        pending_tasks = self.env['ir.config_parameter'].get_param(f'user.{user_id}.pending_tasks', default=0)
        if pending_tasks:
            return f'Tienes {pending_tasks} actividades pendientes.'
        return False