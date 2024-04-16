# -*- coding: utf-8 -*-

from analise.lexer import AnalisadorLexico
from sintese.sintatico import AnalisadorSintatico
from analise.semantica import AnalisadorSemantico

# Realizando etapa de analise lexica
lexico = AnalisadorLexico()
lexico.analisa()
# Realizando etapa de analise sintatica
#sintatico = AnalisadorSintatico()
#sintatico.start()
# Realizando etapa de analise semantica
# semantico = AnalisadorSemantico()
# semantico.analisa()

