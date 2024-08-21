from odoo import models, fields, api

class ActivityReminder(models.Model):
    _name = 'moduloavisosodoo.activity_reminder'
    _description = 'Activity Reminder'

    message = fields.Char(string='Reminder Message', compute='_compute_reminder_message')

    @api.depends('message')
    def _compute_reminder_message(self):
        for record in self:
            record.message = record.get_reminder_message()

    def get_pending_activities(self):
        tasks = self.env['project.task'].search([('user_id', '=', self.env.uid), ('stage_id', '=', False)])
        return len(tasks)

    def get_reminder_message(self):
        pending_activities = self.get_pending_activities()
        if pending_activities > 0:
            return f'Tienes {pending_activities} actividades pendientes. Por favor, revise las tareas asignadas.'
        else:
            return 'No tienes actividades pendientes.'

    def action_show_reminder(self):
        # Actualizar el mensaje de recordatorio
        self.message = self.get_reminder_message()
