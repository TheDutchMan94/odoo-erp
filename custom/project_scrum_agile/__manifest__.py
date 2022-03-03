# See LICENSE file for full copyright and licensing details.
{
    'name': 'Project Scrum Management Agile Methodology',
    'version': '13.0.1.0.0',
    'license': 'LGPL-3',
    'author': 'Serpent Consulting Services Pvt. Ltd.,David DRAPEAU',
    'category': 'Project Scrum Management',
    'website': "http://www.serpentcs.com",
    'summary': '''
        This application respects the scrum.org protocol
        and has been developed and is maintained by ITIL Certified Member
        (in course of certification).
        ''',
    'sequence': 1,
    'depends': [
        'sale_timesheet',
        'calendar',
    ],
    'data': [
        'security/project_scrum_security.xml',
        'security/ir.model.access.csv',
        'views/email_template.xml',
        'views/hr_employee_view.xml',
        'views/project_scrum_view.xml',
        'views/account_analytic_line_view.xml',
        'views/project_view.xml',
        'wizard/user_story_sandbox_to_backlog_view.xml',
        'wizard/project_scrum_backlog_create_task_view.xml',
        'views/project_scrum_sandbox_view.xml',
        'views/project_scrum_release_view.xml',
        'views/project_scrum_role_view.xml',
        'wizard/project_scrum_email_view.xml',
        'wizard/analytic_timesheet_view.xml',
        'views/project_scrum_devteam_view.xml',
    ],
    'demo': ['data/project_scrum_extended_data.xml'],
    'images': ['static/description/img/ProjectScrumBanner.png'],
    'installable': True,
    'application': True,
    'price': 145,
    'currency': 'EUR',
}
