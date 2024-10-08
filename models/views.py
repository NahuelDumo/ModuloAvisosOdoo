from odoo import http

class TaskController(http.Controller):
    @http.route('/tasks', auth='public')
    def tasks(self, **kw):
        # Logic to fetch tasks (you'll need to adapt this)
        tasks = self.env['project.task'].search([])
        return http.Response(
            html="""
            <ul>
                % for task in tasks:
                    <li style="background-color: %s">
                        %s
                    </li>
                % endfor
            </ul>
            """ % (
                'red' if task.is_due_soon else 'white',
                task.name
            )
        )

# Register the controller
http.route('/tasks', auth='public')(TaskController.tasks)