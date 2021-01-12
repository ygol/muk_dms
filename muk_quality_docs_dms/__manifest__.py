###################################################################################
#
#    Copyright (c) 2017-2019 MuK IT GmbH.
#
#    This file is part of MuK QMS Documents DMS Support 
#    (see https://mukit.at).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###################################################################################

{
    "name": "MuK QMS Documents DMS Support",
    "summary": """Quality Management System DMS Support""",
    "version": "12.0.2.0.1",
    "author": "MuK IT",
    "category": "Document Management",
    "license": "LGPL-3",
    "website": "http://www.mukit.at",
    'live_test_url': 'https://mukit.at/r/SgN',
    "depends": [
        "muk_quality_docs",
        "muk_dms_field",
        "muk_web_preview",
    ],
    "contributors": [
        "Kerrim Abdelhamed <kerrim.abdelhamed@mukit.at>",
        "Mathias Markl <mathias.markl@mukit.at>",
    ],
    "data": [
        "template/assets.xml",
        "views/document_view.xml",
        "views/template_view.xml",
        "views/res_config_view.xml",
    ],
    "demo": [
    ],
    "qweb": [
        "static/src/xml/*.xml",
    ],
    "images": [
        'static/description/banner.png'
    ],
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "installable": True,
    "auto_install": False,
    "application": False,
}
