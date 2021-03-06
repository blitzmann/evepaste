"""
tests.parsers.bill_of_material
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Asset list table tests

"""
from evepaste import parse_bill_of_materials
from tests import TableTestGroup


BOM_TABLE = TableTestGroup(parse_bill_of_materials)
BOM_TABLE.add_test('Zydrine - [You: 12783 - Perfect: 11625]',
                   ([{'perfect': 11625,
                     'you': 12783,
                     'name': 'Zydrine'}], []))
BOM_TABLE.add_test('Tritanium [899052]',
                   ([{'name': 'Tritanium',
                      'quantity': 899052}], []))
BOM_TABLE.add_test('''
Bill of Materials does not take into consideration the efficiency of an \
installation.

Extra Materials are not affected by skills and are not returned when \
recycling the manufactured product.

Isogen - [You: 1313]
Megacyte - [You: 3124 - Perfect: 2841]
Mexallon - [You: 731960 - Perfect: 665650]
Nocxium - [You: 50170 - Perfect: 45625]
Pyerite - [You: 3274449 - Perfect: 2977809]
Tritanium - [You: 11903378 - Perfect: 10825023]
Zydrine - [You: 12783 - Perfect: 11625]
Tritanium [899052]
No Item
''',
                   ([{'perfect': 1313,
                     'you': 1313,
                     'name': 'Isogen'},
                    {'perfect': 2841,
                     'you': 3124,
                     'name': 'Megacyte'},
                    {'perfect': 665650,
                     'you': 731960,
                     'name': 'Mexallon'},
                    {'perfect': 45625,
                     'you': 50170,
                     'name': 'Nocxium'},
                    {'perfect': 2977809,
                     'you': 3274449,
                     'name': 'Pyerite'},
                    {'perfect': 10825023,
                     'you': 11903378,
                     'name': 'Tritanium'},
                    {'perfect': 11625,
                     'you': 12783,
                     'name': 'Zydrine'},
                    {'name': 'Tritanium',
                     'quantity': 899052}], []))
