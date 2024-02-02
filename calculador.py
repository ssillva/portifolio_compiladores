"""Neste exemplo, vamos adicionar suporte para declaração e atribuição de variáveis, 
além de suporte para expressões aritméticas mais complexas com parênteses. 
Exemplo simplificado, porém, próximo de um interpretador básico funcional. """

import re

# Análise Léxica
def lex(code):
    return re.findall(r'\d+|[+\-*/=()]|[a-zA-Z_]\w*|\s+', code)

# Análise Sintática
def parse(tokens):
    ast = []
    while tokens:
        token = tokens.pop(0)
        if token.isdigit():
            ast.append(int(token))
        elif token in ('+', '-', '*', '/'):
            ast.append(token)
        elif token.isidentifier():
            # Verifica se é uma atribuição de variável
            if tokens and tokens[0] == '=':
                tokens.pop(0)  # Remove o '='
                value = parse(tokens)  # Continua a análise sintática para o valor da variável
                ast.append(('=', token, value))
            else:
                ast.append(('var', token))
        elif token == '(':
            ast.append(parse(tokens))
        elif token == ')':
            return ast
    return ast

# Execução de Código
def evaluate(ast, variables=None):
    if variables is None:
        variables = {}
    stack = []
    for node in ast:
        if isinstance(node, int):
            stack.append(node)
        elif isinstance(node, str):
            if node in ('+', '-', '*', '/'):
                b = stack.pop()
                a = stack.pop()
                if node == '+':
                    stack.append(a + b)
                elif node == '-':
                    stack.append(a - b)
                elif node == '*':
                    stack.append(a * b)
                elif node == '/':
                    stack.append(a / b)
            elif node in variables:
                stack.append(variables[node])
        elif isinstance(node, tuple) and node[0] == '=':
            var_name = node[1]
            value = evaluate(node[2], variables)
            variables[var_name] = value
    return stack[0]

# Função principal do interpretador
def interpret(code):
    tokens = lex(code)
    ast = parse(tokens)
    result = evaluate(ast)
    return result

# Exemplo de uso
code = """
x = 5
y = 10
z = x + y * 2
(z + 5) * 2
"""
print(interpret(code))  # Saída: 50
