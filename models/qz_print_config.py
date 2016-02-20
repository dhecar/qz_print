# -*- coding: utf-8 -*-
from osv import fields, osv


class QzConfig(osv.osv):
    _name = 'qz.config'
    _table = 'qz_config'
    _rec_name = 'qz_printer'
    _description = 'Qz Print configuration'

    _columns = {
        'qz_printer': fields.char('Printer', size=100),
        'qz_paper_size': fields.selection([('25x55', '25x55')], 'Paper Size'),
        'qz_model_id': fields.many2one('ir.model', 'Model', required=True, select=1),
        'qz_field_ids': fields.one2many("qz.fields", 'qz_field_id', 'Fields'),
        'qz_model_list': fields.char('Model List', size=256)
    }

    def onchange_model(self, cr, uid, ids, qz_model_id):
        model_list = ""
        if qz_model_id:
            model_obj = self.pool.get('ir.model')
            model_data = model_obj.browse(cr, uid, qz_model_id)
            model_list = "[" + str(qz_model_id) + ""
            active_model_obj = self.pool.get(model_data.model)
            if active_model_obj._inherits:
                for key, val in active_model_obj._inherits.items():
                    model_ids = model_obj.search(cr, uid, [('model', '=', key)])
                    if model_ids:
                        model_list += "," + str(model_ids[0]) + ""
            model_list += "]"
        return {'value': {'qz_model_list': model_list}}


QzConfig()


class QzFields(osv.osv):
    _name = "qz.fields"
    _rec_name = "qz_field_id"

    _columns = {
        # 'sequence': fields.integer("Sequence", required=True),
        'qz_field_id': fields.many2one('ir.model.fields', 'Fields', required=False),
        'qz_field_type': fields.selection([('barcode', 'Barcode'), ('text', 'Text')], 'Type'),
        'h_start_p1': fields.float('Horizontal Start (dots)'),
        'v_start_p2': fields.float('Vertical Start (dots)'),
        'rotation_p3': fields.selection([('0', 'No rotation'), ('1', '90 degrees'), ('2', '180 degrees'),
                                         ('3', '270 degrees')], 'Rotation'),
        'font_p4': fields.selection([('1', '203 dpi(8 x 12 dots) or 300 dpi(12 x 20 dots)'),
                                     ('2', '203 dpi(10 x 16 dots) or 300 dpi(16 x 28 dots)'),
                                     ('3', '203 dpi(12 x 20 dots) or 300 dpi(20 x 36 dots)'),
                                     ('4', '203 dpi(14 x 24 dots) or 300 dpi(24 x 44 dots)'),
                                     ('5', '203 dpi(32 x 48 dots) or 300 dpi(48 x 80 dots)')],
                                    'Font Type'),

        'h_multiplier_p5': fields.selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                                             ('6', '6'), ('8', '8')], 'Horizontal Multiplier'),
        'v_multiplier_p6': fields.selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'),
                                             ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9')], 'Vertical Multiplier'),
        'n_r_p7': fields.selection([('N', 'Normal'), ('R', 'Reverse')], 'Normal/Reverse'),
        'bar_sel_p4': fields.selection([('3', 'Code 39 std. or extended'),
                                        ('3C', 'Code 39 with check digit'),
                                        ('9', 'Code 93'),
                                        ('0', 'Code 128 UCC'),
                                        ('1', 'Code 128 auto A, B, C modes'),
                                        ('1A', 'Code 128 mode A'),
                                        ('1B', 'Code 128 mode B'),
                                        ('1C', 'Code 128 mode C'),
                                        ('K', 'Codabar'),
                                        ('E80', 'EAN8'),
                                        ('E82', 'EAN8 2 digit add-on'),
                                        ('E85', 'EAN8 5 digit add-on'),
                                        ('E30', 'EAN13'),
                                        ('E32', 'EAN13 2 digit add-on'),
                                        ('E35', 'EAN13 5 digit add-on'),
                                        ('2G', 'German Post Code'),
                                        ('2', 'Interleaved 2 of 5'),
                                        ('2C', 'Interleaved 2 of 5 with mod 10 check digit'),
                                        ('2D', 'Interleaved 2/5 readable check digit'),
                                        ('P', 'Postnet 5, 9, 11 & 13 digit'),
                                        ('J', 'Japanese Postnet'),
                                        ('1E', 'UCC/EAN 128*'),
                                        ('UA0', 'UPC A'),
                                        ('UA2', 'UPC A 2 digit add-on'),
                                        ('UA5', 'UPC A 5 digit add-on'),
                                        ('UE0', 'UPC E'),
                                        ('UE2', 'UPC E 2 digit add-on'),
                                        ('UE5', 'UPC E 5 digit add-on'),
                                        ('2U', 'UPC Interleaved 2 of 5'),
                                        ('L', 'Plessey (MSI-1) with mod. 10 check digit'),
                                        ('M', 'MSI-3 with mod. 10 check digit')], 'Barcode Type'),
        'n_bar_w_p5': fields.float('Narrow Bar width in dots'),
        'w_bar_w_p6': fields.float('Wide bar width in dots'),
        'bar_height_p7': fields.float('Barcode Height in dots'),
        'human_read_p8': fields.selection([('B', 'Yes'), ('N', 'No')], 'Human Readable'),

    }

    _defaults = {
        'qz_field_type': 'barcode',
        'rotation_p3': '0',
        'font_p4': '1',
        'h_multiplier_p5': '1',
        'v_multiplier_p6': '1',
        'n_r_p7': 'N'
    }


QzFields()
