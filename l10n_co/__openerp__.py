# -*- coding: utf-8 -*-
##############################################################################
#
# OpenERP, Open Source Management Solution
# Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
{
    'name': 'Colombian - Accounting',
    'version': '0.1',
    'category': 'Localization/Account Charts',
    'description': 'Colombian Accounting and Tax Preconfiguration',
    'author': """
David Arnold BA HSG (devCO),

Juan Pablo Arias (devCO),

Hector Ivan Valencia (TIX)
""",
    'depends': [
        'account',
        'base_vat',
        'account_chart',
    ],
    'data': [
    	'data/account.account.type.csv',
    	'data/account.account.template.csv',
        'data/account.tax.code.template.csv',
        'data/account_chart_template.xml',
        'data/account.tax.template.csv',
    	'wizard/account_wizard.xml',
    ],
    'demo': [],
    'installable': True,
    'images': [],
}
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

