from odoo import api, fields, models
from datetime import datetime, timedelta

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_due_soon = fields.Boolean(string="Due Soon", compute="_compute_is_due_soon", store=True)

    @api.depends('date_deadline')
    def _compute_is_due_soon(self):
        for task in self:
            if task.date_deadline:
                due_date = fields.Date.from_string(task.date_deadline)
                task.is_due_soon = due_date <= datetime.today().date() + timedelta(days=2)
            else:
                task.is_due_soon = False
