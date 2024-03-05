import sys
import re

def tokenize(code):
    token_specification = [
        ('NUM',        r'\d+'),             
        ('SELECT',     r'Select'),
        ('FROM',       r'from'),
        ('WHERE',      r'where'),
        ('SIMB',       r'==|>=|<='),            
        ('NEWLINE',    r'\n'),           
        ('SKIPSPACE',  r'[ \t]+'),     
        ('COMMA',      r','),
        ('VAR',        r'\w+'),
        ('ERRO',       r'.')          
    ]

    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    reconhecidos = []
    linha = 1
    mo = re.finditer(tok_regex, code)
    for m in mo:
        dic = m.groupdict()
        if dic['NUM'] is not None:
            t = ("NUM", int(dic['NUM']), linha, m.span())
        elif dic['SELECT'] is not None:
            t = ("SELECT", "SELECT", linha, m.span())
        elif dic['FROM'] is not None:
            t = ("FROM", dic['FROM'], linha, m.span())
        elif dic['WHERE'] is not None:
            t = ("WHERE", dic['WHERE'], linha, m.span())
        elif dic['SIMB'] is not None:
            t = ("SIMB", dic['SIMB'], linha, m.span())
        elif dic['NEWLINE'] is not None:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
        elif dic['SKIPSPACE'] is not None:
            t = ("SKIPSPACE", dic['SKIPSPACE'], linha, m.span())
        elif dic['COMMA'] is not None:
            t = ("COMMA", dic['COMMA'], linha, m.span())
        elif dic['VAR'] is not None:
            t = ("VAR", dic['VAR'], linha, m.span())
        else:
            t = ("ERRO", m.group(), linha, m.span())
        reconhecidos.append(t)

    return reconhecidos

linha ='''Select id, noun, salario 
    from empregados 
        where salario >= 820
'''

for tok in tokenize(linha):
    print(tok)