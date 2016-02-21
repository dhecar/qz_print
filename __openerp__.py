# -*- coding: utf-8 -*-
##############################################################################
#
#
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name" : "Qz Print",
    "version" : "1.0",
    "author" : "Sinergia Informatica",
    "category" : "Tools",
    "website" : "http://sinergiainformatica.net",
    "description": """
    Adaptation to print labels with qz-print
    """,
    "author": "David Hernández",
    "depends": ['product', 'base_report_to_printer', 'web'],
    #"js": ['static/src/js/labels.js'],
    #"css": ['static/src/css/labels.css'],
    #'qweb': ['static/src/xml/labels.xml'],
    "update_xml": ['views/qz_print_config_view.xml', 'views/product_view.xml'],
    "data": [],
    "installable": True,
    "auto_install": False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: