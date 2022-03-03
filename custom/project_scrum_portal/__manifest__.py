# See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Scrum Portal Agile',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'maintainer': 'Serpent Consulting Services Pvt. Ltd.',
    'license': 'LGPL-3',
    'description': """This application respects the scrum.org protocol
        and has been developed and is maintained by ITIL Certified Member
        (in course of certification).
        """,
    'summary': """This application respects the scrum.org protocol.""",
    'category': 'Project',
    'website': 'http://www.serpentcs.com',
    'version': '13.0.1.0.1',
    'sequence': 1,
    'depends': [
        'website',
        'project_scrum_agile',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/meetings.xml',
        'views/templates.xml',
        'views/backlog.xml',
        'views/sprints.xml',
    ],
    'images': ['static/description/ProjectScrumBanner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': 149,
    'currency': 'EUR',
}
