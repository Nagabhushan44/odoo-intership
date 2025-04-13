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
    'name': 'Restaurant Optimizer',
    'version': '1.0',
    'summary': 'AI-driven optimization for restaurant operations',
    'description': """
        Smart waste tracking, dynamic pricing, and staff analytics
        for restaurant management.
    """,
    'author': 'Your Company',
    'depends': ['point_of_sale', 'stock', 'hr'],
    'data': [
        
    ],
    'assets': {
        'point_of_sale.assets': [
            'restaurant_optimizer/static/src/js/pos_optimizer.js',
        ],
    },
    'installable': True,
    'application': True,
}