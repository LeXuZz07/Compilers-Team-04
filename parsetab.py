
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'statementBOOL BOOL_FALSE BOOL_TRUE BRACKETS BREAK DIVISION DO ELSE EQUALS EXPONENTIAL FLOAT FOR ID IF INT LESS LKEY LPAREN MODULE MORE MULTIPLICATION NULL NUMBER OPERATORS RETURN RKEY RPAREN SIMPLE_LITERAL SPECIAL SPOT WHILEstatement : type ID EQUALS valuetype : INT\n            | FLOAT\n            | BOOLvalue : NUMBERvalue : SPOTvalue : BOOL_TRUE\n             | BOOL_FALSE'
    
_lr_action_items = {'INT':([0,],[3,]),'FLOAT':([0,],[4,]),'BOOL':([0,],[5,]),'$end':([1,8,9,10,11,12,],[0,-1,-5,-6,-7,-8,]),'ID':([2,3,4,5,],[6,-2,-3,-4,]),'EQUALS':([6,],[7,]),'NUMBER':([7,],[9,]),'SPOT':([7,],[10,]),'BOOL_TRUE':([7,],[11,]),'BOOL_FALSE':([7,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'type':([0,],[2,]),'value':([7,],[8,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> type ID EQUALS value','statement',4,'p_statement_assign','analizador_sitactico.py',12),
  ('type -> INT','type',1,'p_type','analizador_sitactico.py',28),
  ('type -> FLOAT','type',1,'p_type','analizador_sitactico.py',29),
  ('type -> BOOL','type',1,'p_type','analizador_sitactico.py',30),
  ('value -> NUMBER','value',1,'p_value_int','analizador_sitactico.py',35),
  ('value -> SPOT','value',1,'p_value_float','analizador_sitactico.py',41),
  ('value -> BOOL_TRUE','value',1,'p_value_bool','analizador_sitactico.py',47),
  ('value -> BOOL_FALSE','value',1,'p_value_bool','analizador_sitactico.py',48),
]