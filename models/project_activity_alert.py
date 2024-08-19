from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    def _check_pending_activities(self):
        print("Checking pending activities for user:", self.env.user.name)
        user = self.env.user
        pending_activities = self.env['project.task'].search([
            ('user_id', '=', user.id),
            ('stage_id.fold', '=', False),
            ('date_deadline', '<=', fields.Date.today()),
        ])

        if pending_activities:
            message = f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\nPor favor revísalas.'
            print("Sending notification:", message)
            user.notify_warning(message=message)
        else:
            print("No pending activities found.")

    @api.model
    def _login(self):
        print("User login method called.")
        result = super(ResUsers, self)._login()
        print("Checking for pending activities after login.")
        self._check_pending_activities()
        return result
