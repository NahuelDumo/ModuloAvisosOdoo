from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    def check_credentials(self, password):
        """Sobreescribimos el método check_credentials para ejecutar la acción después de la autenticación"""
        super(ResUsers, self).check_credentials(password)
        self.check_pending_activities()

    def check_pending_activities(self):
        tasks = self.env['project.task'].search([
            ('user_id', '=', self.env.uid),
            ('stage_id', '=', False)
        ])
        if tasks:
            message = f'Tienes {len(tasks)} actividades pendientes.'
            self.notify_info(message)
