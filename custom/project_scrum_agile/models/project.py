# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    def _compute_backlog_count(self):
        product_backlog_obj = self.env['project.scrum.product.backlog']
        for project in self:
            project.backlog_count = \
                product_backlog_obj.search_count(
                    [('project_id', '=', project.id)])

    is_scrum = fields.Boolean('Is it a Scrum Project ?', default=True)
    goal = fields.Text(
        'Goal',
        help="The document that includes the project,"
             "jointly between the team and the customer")
    scrum_master_id = fields.Many2one(
        'res.users',
        'Scrum Master',
        domain=lambda self: [('groups_id', 'in', self.env.ref(
            'project_scrum_agile.group_scrum_master').ids)],
        ondelete='restrict')
    product_owner_id = fields.Many2one(
        'res.users',
        'Product Owner',
        domain=lambda self: [('groups_id', 'in', self.env.ref(
            'project_scrum_agile.group_scrum_owner').ids)],
        ondelete='restrict')
    team_id = fields.Many2one('project.scrum.devteam', 'Team')
    backlog_count = fields.Integer(
        compute='_compute_backlog_count',
        string="Number of Backlog"
    )

    @api.model
    def create(self, vals):
        res = super(ProjectProject, self).create(vals)
        if self.env.registry.in_test_mode():
            return res
        domain = ['|', ('default_view', '=', True), ('fold', '=', True)]
        for stage_ids in self.env['project.task.type'].search(domain):
            stage_ids.sudo().write({'project_ids': [(4, res.id)]})
        return res


class ProjectTaskType(models.Model):
    _inherit = 'project.task.type'

    default_view = fields.Boolean(
        'Default View',
        help="This stage will show you in kanban and form as well"
    )


class ResUserExtended(models.Model):
    _inherit = 'res.users'

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=50):
        """
        This method used to filter as per group in the dropdown,
        Scrum master, product owner in project.

        """
        if self._context.get('filter_product_owner', False):
            scrum_owner = self.env.ref('project_scrum_agile.group_scrum_owner')
            if scrum_owner and scrum_owner.users:
                args += [('id', 'in', scrum_owner.users.ids)]
        if self._context.get('filter_scrum_master', False):
            scrum_mst = self.env.ref('project_scrum_agile.group_scrum_master')
            if scrum_mst and scrum_mst.users:
                args += [('id', 'in', scrum_mst.users.ids)]
        return super(ResUserExtended, self).name_search(
            name=name, args=args, operator=operator, limit=limit)
