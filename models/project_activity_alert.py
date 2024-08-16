from odoo import models, fields, api

class ProjectActivityAlert(models.Model):
    _inherit = 'res.users'

    @api.model
    def check_pending_activities(self):
        user = self.env.user
        pending_activities = self.env['project.task'].search([
            ('user_id', '=', user.id),
            ('stage_id.fold', '=', False),
            ('date_deadline', '<=', fields.Date.today()),  # Corregido: 'fields' desde 'odoo'
        ])

        if pending_activities:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Actividades Pendientes',
                    'message': f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\n Por favor revisalas.',
                    'sticky': False,
                }
            }

    @api.model
    def _login(self, db, login, password):
        # Llamamos a la función original de inicio de sesión
        res = super(ProjectActivityAlert, self)._login(db, login, password)
        # Verificamos actividades pendientes
        self.check_pending_activities()
        return res
