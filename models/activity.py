# file: models/cron_job.py
from odoo import models

class MyModuleCron(models.Model):
    _name = 'my.module.cron'
    _description = 'My Module Cron'

    def cron_check_pending_activities(self):
        users = self.env['res.users'].search([])
        for user in users:
            tasks = self.env['project.task'].search([
                ('user_id', '=', user.id),
                ('stage_id', '=', False)
            ])
            if tasks:
                message = f'Tienes {len(tasks)} actividades pendientes.'
                user.notify_info(message)
