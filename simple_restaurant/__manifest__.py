# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2025 ZestyBeanz Technologies(<http://www.zbeanztech.com>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Simple Restaurant',
    'version': '18.0.1.0.0',
    'summary': 'Basic Restaurant Management',
    'description': 'Manage menu items and customer orders',
    'category':'service',
    'author': 'Nagabhushan',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': ['base'],
    'data': [
                'security/ir.model.access.csv',
                'views/menu_item_views.xml',
                'views/restaurant_order_views.xml',
    ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
