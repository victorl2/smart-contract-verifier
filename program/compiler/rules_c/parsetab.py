
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftLEGEleftLTGTleftEQNEleftMINUSPLUSleftMULTDIVrightIDCOMMA DIV DO ELSE EQ EQUAL FLOAT FNUMBER FOR GE GT ID IF INT LBRACE LBRACKET LE LPAREN LT MINUS MULT NE NUMBER PLUS RBRACE RBRACKET RETURN RPAREN SEMICOLON WHILEprogram : declist funclist\n                   | declist\n                   | funclistdeclist : declaration\n                   | declist declarationfunclist : function\n                    | funclist functiondeclaration : type identlist SEMICOLONidentlist : identifier\n                     | identlist COMMA identifieridentifier : ID\n                      | ID LBRACKET NUMBER RBRACKETparamlist : parameter\n                     | paramlist COMMA parameterparameter : type identifierfunction : type ID LPAREN RPAREN compoundstmt\n                    | type ID LPAREN paramlist RPAREN compoundstmttype : INT\n                | FLOATcompoundstmt : LBRACE RBRACE\n                        | LBRACE stmtlist RBRACE\n                        | LBRACE declist stmtlist RBRACE\n                        | LBRACE declist RBRACEstmtlist : stmt\n                    | stmtlist stmtstmt : assignstmt\n                | callstmt\n                | retstmt\n                | while\n                | for\n                | if\n                | compoundstmt\n                | SEMICOLONassignstmt : assign SEMICOLONassign : ID EQUAL expr\n                  | ID LBRACKET expr RBRACKET EQUAL exprcallstmt : call SEMICOLONcall : ID LPAREN RPAREN\n                | ID LPAREN arglist RPARENarglist : arg\n                   | arglist COMMA argarg : exprretstmt : RETURN SEMICOLON\n                   | RETURN expr SEMICOLONexpr : expr MINUS expr\n                | expr PLUS expr\n                | expr MULT expr\n                | expr DIV expr\n                | expr LE expr\n                | expr GE expr\n                | expr GT expr\n                | expr LT expr\n                | expr EQ expr\n                | expr NE expr\n                | call\n                | NUMBER\n                | FNUMBER\n                | id\n                | LPAREN expr RPARENid : ID\n              | ID LBRACKET expr RBRACKETwhile : WHILE LPAREN expr RPAREN stmt\n                 | DO stmt WHILE LPAREN expr RPAREN SEMICOLONfor : FOR LPAREN assign SEMICOLON expr SEMICOLON assign RPAREN stmtif : IF LPAREN expr RPAREN stmt\n              | IF LPAREN expr RPAREN stmt ELSE stmt'
    
_lr_action_items = {'INT':([0,2,3,4,5,9,10,11,17,19,29,30,32,34,36,55,57,60,78,],[7,7,7,-4,-6,7,-5,-7,-8,7,-16,7,7,-20,7,-17,-21,-23,-22,]),'FLOAT':([0,2,3,4,5,9,10,11,17,19,29,30,32,34,36,55,57,60,78,],[8,8,8,-4,-6,8,-5,-7,-8,8,-16,8,8,-20,8,-17,-21,-23,-22,]),'$end':([1,2,3,4,5,9,10,11,17,29,34,55,57,60,78,],[0,-2,-3,-4,-6,-1,-5,-7,-8,-16,-20,-17,-21,-23,-22,]),'RBRACE':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,57,58,59,60,61,62,63,78,79,123,126,133,135,137,],[-4,-5,-8,34,-20,57,60,-24,-26,-27,-28,-29,-30,-31,-32,-33,-21,-25,78,-23,-34,-37,-43,-22,-44,-62,-65,-63,-66,-64,]),'SEMICOLON':([4,10,13,14,15,17,21,22,30,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,51,57,58,59,60,61,62,63,64,65,66,67,68,70,78,79,94,97,99,103,104,105,106,107,108,109,110,111,112,113,115,118,120,122,123,125,126,129,131,132,133,135,136,137,],[-4,-5,17,-11,-9,-8,-10,-11,45,-12,-20,45,45,-24,-26,-27,-28,-29,-30,-31,-32,-33,61,62,63,45,-21,-25,45,-23,-34,-37,-43,79,-55,-56,-57,-58,-60,-22,-44,117,-35,-38,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,45,45,-39,-61,-62,130,-65,133,45,-36,-63,-66,45,-64,]),'RETURN':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,49,-20,49,49,-24,-26,-27,-28,-29,-30,-31,-32,-33,49,-21,-25,49,-23,-34,-37,-43,-22,-44,49,49,-62,-65,49,-63,-66,49,-64,]),'WHILE':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,72,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,50,-20,50,50,-24,-26,-27,-28,-29,-30,-31,-32,-33,50,-21,-25,50,-23,-34,-37,-43,93,-22,-44,50,50,-62,-65,50,-63,-66,50,-64,]),'DO':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,51,-20,51,51,-24,-26,-27,-28,-29,-30,-31,-32,-33,51,-21,-25,51,-23,-34,-37,-43,-22,-44,51,51,-62,-65,51,-63,-66,51,-64,]),'FOR':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,52,-20,52,52,-24,-26,-27,-28,-29,-30,-31,-32,-33,52,-21,-25,52,-23,-34,-37,-43,-22,-44,52,52,-62,-65,52,-63,-66,52,-64,]),'IF':([4,10,17,30,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,53,-20,53,53,-24,-26,-27,-28,-29,-30,-31,-32,-33,53,-21,-25,53,-23,-34,-37,-43,-22,-44,53,53,-62,-65,53,-63,-66,53,-64,]),'LBRACE':([4,10,17,24,30,31,34,35,36,37,38,39,40,41,42,43,44,45,51,57,58,59,60,61,62,63,78,79,115,118,123,126,131,133,135,136,137,],[-4,-5,-8,30,30,30,-20,30,30,-24,-26,-27,-28,-29,-30,-31,-32,-33,30,-21,-25,30,-23,-34,-37,-43,-22,-44,30,30,-62,-65,30,-63,-66,30,-64,]),'ID':([4,6,7,8,10,12,17,18,23,30,34,35,36,37,38,39,40,41,42,43,44,45,46,49,51,57,58,59,60,61,62,63,69,71,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,115,116,117,118,121,123,126,127,130,131,133,135,136,137,],[-4,14,-18,-19,-5,16,-8,22,22,54,-20,54,54,-24,-26,-27,-28,-29,-30,-31,-32,-33,22,70,54,-21,-25,54,-23,-34,-37,-43,70,70,95,70,70,70,70,-22,-44,70,70,70,70,70,70,70,70,70,70,70,54,70,70,54,70,-62,-65,70,95,54,-63,-66,54,-64,]),'COMMA':([13,14,15,21,22,25,26,28,33,56,65,66,67,68,70,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,120,122,128,],[18,-11,-9,-10,-11,32,-13,-15,-12,-14,-55,-56,-57,-58,-60,-38,121,-40,-42,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,-39,-61,-41,]),'LPAREN':([14,16,49,50,52,53,54,69,70,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,93,116,117,121,127,],[19,19,69,71,73,74,77,69,77,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,116,69,69,69,69,]),'LBRACKET':([14,22,54,70,95,],[20,20,76,91,76,]),'RPAREN':([19,22,25,26,28,33,56,65,66,67,68,70,77,90,92,96,97,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,120,122,124,128,132,134,],[24,-11,31,-13,-15,-12,-14,-55,-56,-57,-58,-60,99,113,115,118,-35,-38,120,-40,-42,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,-39,-61,129,-41,-36,136,]),'NUMBER':([20,49,69,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,116,117,121,127,],[27,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'RBRACKET':([27,65,66,67,68,70,98,99,103,104,105,106,107,108,109,110,111,112,113,114,120,122,],[33,-55,-56,-57,-58,-60,119,-38,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,122,-39,-61,]),'ELSE':([34,38,39,40,41,42,43,44,45,57,60,61,62,63,78,79,123,126,133,135,137,],[-20,-26,-27,-28,-29,-30,-31,-32,-33,-21,-23,-34,-37,-43,-22,-44,-62,131,-63,-66,-64,]),'FNUMBER':([49,69,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,116,117,121,127,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'EQUAL':([54,95,119,],[75,75,127,]),'MINUS':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[80,-55,-56,-57,-58,-60,80,80,80,80,80,-38,80,-45,-46,-47,-48,80,80,80,80,80,80,-59,80,-39,-61,80,80,80,]),'PLUS':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[81,-55,-56,-57,-58,-60,81,81,81,81,81,-38,81,-45,-46,-47,-48,81,81,81,81,81,81,-59,81,-39,-61,81,81,81,]),'MULT':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[82,-55,-56,-57,-58,-60,82,82,82,82,82,-38,82,82,82,-47,-48,82,82,82,82,82,82,-59,82,-39,-61,82,82,82,]),'DIV':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[83,-55,-56,-57,-58,-60,83,83,83,83,83,-38,83,83,83,-47,-48,83,83,83,83,83,83,-59,83,-39,-61,83,83,83,]),'LE':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[84,-55,-56,-57,-58,-60,84,84,84,84,84,-38,84,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,84,-39,-61,84,84,84,]),'GE':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[85,-55,-56,-57,-58,-60,85,85,85,85,85,-38,85,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-59,85,-39,-61,85,85,85,]),'GT':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[86,-55,-56,-57,-58,-60,86,86,86,86,86,-38,86,-45,-46,-47,-48,86,86,-51,-52,-53,-54,-59,86,-39,-61,86,86,86,]),'LT':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[87,-55,-56,-57,-58,-60,87,87,87,87,87,-38,87,-45,-46,-47,-48,87,87,-51,-52,-53,-54,-59,87,-39,-61,87,87,87,]),'EQ':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[88,-55,-56,-57,-58,-60,88,88,88,88,88,-38,88,-45,-46,-47,-48,88,88,88,88,-53,-54,-59,88,-39,-61,88,88,88,]),'NE':([64,65,66,67,68,70,90,92,96,97,98,99,102,103,104,105,106,107,108,109,110,111,112,113,114,120,122,124,125,132,],[89,-55,-56,-57,-58,-60,89,89,89,89,89,-38,89,-45,-46,-47,-48,89,89,89,89,-53,-54,-59,89,-39,-61,89,89,89,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,30,],[2,36,]),'funclist':([0,2,],[3,9,]),'declaration':([0,2,30,36,],[4,10,4,10,]),'function':([0,2,3,9,],[5,5,11,11,]),'type':([0,2,3,9,19,30,32,36,],[6,6,12,12,23,46,23,46,]),'identlist':([6,46,],[13,13,]),'identifier':([6,18,23,46,],[15,21,28,15,]),'paramlist':([19,],[25,]),'parameter':([19,32,],[26,56,]),'compoundstmt':([24,30,31,35,36,51,59,115,118,131,136,],[29,44,55,44,44,44,44,44,44,44,44,]),'stmtlist':([30,36,],[35,59,]),'stmt':([30,35,36,51,59,115,118,131,136,],[37,58,37,72,58,123,126,135,137,]),'assignstmt':([30,35,36,51,59,115,118,131,136,],[38,38,38,38,38,38,38,38,38,]),'callstmt':([30,35,36,51,59,115,118,131,136,],[39,39,39,39,39,39,39,39,39,]),'retstmt':([30,35,36,51,59,115,118,131,136,],[40,40,40,40,40,40,40,40,40,]),'while':([30,35,36,51,59,115,118,131,136,],[41,41,41,41,41,41,41,41,41,]),'for':([30,35,36,51,59,115,118,131,136,],[42,42,42,42,42,42,42,42,42,]),'if':([30,35,36,51,59,115,118,131,136,],[43,43,43,43,43,43,43,43,43,]),'assign':([30,35,36,51,59,73,115,118,130,131,136,],[47,47,47,47,47,94,47,47,134,47,47,]),'call':([30,35,36,49,51,59,69,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,115,116,117,118,121,127,131,136,],[48,48,48,65,48,48,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,48,65,65,48,65,65,48,48,]),'expr':([49,69,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,116,117,121,127,],[64,90,92,96,97,98,102,103,104,105,106,107,108,109,110,111,112,114,124,125,102,132,]),'id':([49,69,71,74,75,76,77,80,81,82,83,84,85,86,87,88,89,91,116,117,121,127,],[68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,68,]),'arglist':([77,],[100,]),'arg':([77,121,],[101,128,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist funclist','program',2,'p_program','rules_yacc.py',17),
  ('program -> declist','program',1,'p_program','rules_yacc.py',18),
  ('program -> funclist','program',1,'p_program','rules_yacc.py',19),
  ('declist -> declaration','declist',1,'p_declist','rules_yacc.py',26),
  ('declist -> declist declaration','declist',2,'p_declist','rules_yacc.py',27),
  ('funclist -> function','funclist',1,'p_funclist','rules_yacc.py',34),
  ('funclist -> funclist function','funclist',2,'p_funclist','rules_yacc.py',35),
  ('declaration -> type identlist SEMICOLON','declaration',3,'p_declaration','rules_yacc.py',42),
  ('identlist -> identifier','identlist',1,'p_identlist','rules_yacc.py',46),
  ('identlist -> identlist COMMA identifier','identlist',3,'p_identlist','rules_yacc.py',47),
  ('identifier -> ID','identifier',1,'p_identifier','rules_yacc.py',54),
  ('identifier -> ID LBRACKET NUMBER RBRACKET','identifier',4,'p_identifier','rules_yacc.py',55),
  ('paramlist -> parameter','paramlist',1,'p_paramlist','rules_yacc.py',62),
  ('paramlist -> paramlist COMMA parameter','paramlist',3,'p_paramlist','rules_yacc.py',63),
  ('parameter -> type identifier','parameter',2,'p_parameter','rules_yacc.py',70),
  ('function -> type ID LPAREN RPAREN compoundstmt','function',5,'p_function','rules_yacc.py',74),
  ('function -> type ID LPAREN paramlist RPAREN compoundstmt','function',6,'p_function','rules_yacc.py',75),
  ('type -> INT','type',1,'p_type','rules_yacc.py',82),
  ('type -> FLOAT','type',1,'p_type','rules_yacc.py',83),
  ('compoundstmt -> LBRACE RBRACE','compoundstmt',2,'p_compoundstmt','rules_yacc.py',87),
  ('compoundstmt -> LBRACE stmtlist RBRACE','compoundstmt',3,'p_compoundstmt','rules_yacc.py',88),
  ('compoundstmt -> LBRACE declist stmtlist RBRACE','compoundstmt',4,'p_compoundstmt','rules_yacc.py',89),
  ('compoundstmt -> LBRACE declist RBRACE','compoundstmt',3,'p_compoundstmt','rules_yacc.py',90),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist','rules_yacc.py',99),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','rules_yacc.py',100),
  ('stmt -> assignstmt','stmt',1,'p_stmt','rules_yacc.py',107),
  ('stmt -> callstmt','stmt',1,'p_stmt','rules_yacc.py',108),
  ('stmt -> retstmt','stmt',1,'p_stmt','rules_yacc.py',109),
  ('stmt -> while','stmt',1,'p_stmt','rules_yacc.py',110),
  ('stmt -> for','stmt',1,'p_stmt','rules_yacc.py',111),
  ('stmt -> if','stmt',1,'p_stmt','rules_yacc.py',112),
  ('stmt -> compoundstmt','stmt',1,'p_stmt','rules_yacc.py',113),
  ('stmt -> SEMICOLON','stmt',1,'p_stmt','rules_yacc.py',114),
  ('assignstmt -> assign SEMICOLON','assignstmt',2,'p_assignstmt','rules_yacc.py',118),
  ('assign -> ID EQUAL expr','assign',3,'p_assign','rules_yacc.py',122),
  ('assign -> ID LBRACKET expr RBRACKET EQUAL expr','assign',6,'p_assign','rules_yacc.py',123),
  ('callstmt -> call SEMICOLON','callstmt',2,'p_callstmt','rules_yacc.py',130),
  ('call -> ID LPAREN RPAREN','call',3,'p_call','rules_yacc.py',134),
  ('call -> ID LPAREN arglist RPAREN','call',4,'p_call','rules_yacc.py',135),
  ('arglist -> arg','arglist',1,'p_arglist','rules_yacc.py',142),
  ('arglist -> arglist COMMA arg','arglist',3,'p_arglist','rules_yacc.py',143),
  ('arg -> expr','arg',1,'p_arg','rules_yacc.py',150),
  ('retstmt -> RETURN SEMICOLON','retstmt',2,'p_retstmt','rules_yacc.py',154),
  ('retstmt -> RETURN expr SEMICOLON','retstmt',3,'p_retstmt','rules_yacc.py',155),
  ('expr -> expr MINUS expr','expr',3,'p_expr','rules_yacc.py',162),
  ('expr -> expr PLUS expr','expr',3,'p_expr','rules_yacc.py',163),
  ('expr -> expr MULT expr','expr',3,'p_expr','rules_yacc.py',164),
  ('expr -> expr DIV expr','expr',3,'p_expr','rules_yacc.py',165),
  ('expr -> expr LE expr','expr',3,'p_expr','rules_yacc.py',166),
  ('expr -> expr GE expr','expr',3,'p_expr','rules_yacc.py',167),
  ('expr -> expr GT expr','expr',3,'p_expr','rules_yacc.py',168),
  ('expr -> expr LT expr','expr',3,'p_expr','rules_yacc.py',169),
  ('expr -> expr EQ expr','expr',3,'p_expr','rules_yacc.py',170),
  ('expr -> expr NE expr','expr',3,'p_expr','rules_yacc.py',171),
  ('expr -> call','expr',1,'p_expr','rules_yacc.py',172),
  ('expr -> NUMBER','expr',1,'p_expr','rules_yacc.py',173),
  ('expr -> FNUMBER','expr',1,'p_expr','rules_yacc.py',174),
  ('expr -> id','expr',1,'p_expr','rules_yacc.py',175),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr','rules_yacc.py',176),
  ('id -> ID','id',1,'p_id','rules_yacc.py',185),
  ('id -> ID LBRACKET expr RBRACKET','id',4,'p_id','rules_yacc.py',186),
  ('while -> WHILE LPAREN expr RPAREN stmt','while',5,'p_while','rules_yacc.py',193),
  ('while -> DO stmt WHILE LPAREN expr RPAREN SEMICOLON','while',7,'p_while','rules_yacc.py',194),
  ('for -> FOR LPAREN assign SEMICOLON expr SEMICOLON assign RPAREN stmt','for',9,'p_for','rules_yacc.py',201),
  ('if -> IF LPAREN expr RPAREN stmt','if',5,'p_if','rules_yacc.py',206),
  ('if -> IF LPAREN expr RPAREN stmt ELSE stmt','if',7,'p_if','rules_yacc.py',207),
]
