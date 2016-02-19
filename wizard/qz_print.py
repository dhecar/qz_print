# -*- coding: utf-8 -*-
from osv import fields, osv


class QzPrint(osv.osv):

    _name = 'qz.print'
    _description = 'Qz Print Labels'

    _columns  = {
        'copies': fields.char('Copies:', size=4),
    }

QzPrint()