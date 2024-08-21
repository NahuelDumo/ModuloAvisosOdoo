from odoo import models

class ResUsers(models.Model):
    _inherit = 'res.users'

    def cron_check_pending_activities(self):
        tasks = self.env['project.task'].search([
            ('user_id', '=', self.env.uid),
            ('stage_id', '=', False)
        ])
        if tasks:
            message = f'Tienes {len(tasks)} actividades pendientes.'
            self.notify_info(message)
