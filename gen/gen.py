#!/usr/bin/python

import sys, re

def split_opt(s):
    l = []
    if re.search('\w+_opt\s*', s):
        l = split_opt(re.sub('\w+_opt\s*', '', s, 1))
        l = l + split_opt(re.sub('_opt', '', s, 1))
    else:
        l = [s]
    return l

def sub_spec(s):
    s = s.replace('=>', 'EQGT')
    s = s.replace('/=', 'DIVEQ')
    s = s.replace('/', 'DIV')
    s = s.replace('...', 'ELLIPSIS')
    s = s.replace('..', 'TWODOTS')
    s = s.replace('.', 'DOT')
    s = s.replace('&&', 'ANDAND')
    s = s.replace('&=', 'ANDEQ')
    s = s.replace('&', 'AND')
    s = s.replace('||', 'OROR')
    s = s.replace('|=', 'OREQ')
    s = s.replace('|', 'OR')
    s = s.replace('--', 'DECREMENT')
    s = s.replace('-=', 'MINUSEQ')
    s = s.replace('-', 'MINUS')
    s = s.replace('++', 'INCREMENT')
    s = s.replace('+=', 'PLUSEQ')
    s = s.replace('+', 'PLUS')
    s = s.replace('!<>=', 'NOTSTRANGEEQ')
    s = s.replace('!<>', 'NOTSTRANGE')
    s = s.replace('!>=', 'NOTGTEQ')
    s = s.replace('!>', 'NOTGT')
    s = s.replace('!<=', 'NOTLTEQ')
    s = s.replace('!<', 'NOTLT')
    s = s.replace('!=', 'NOTEQ')
    s = s.replace('!', 'NOT')
    s = s.replace('<>=', 'STRANGEEQ')
    s = s.replace('<>', 'STRANGE')
    s = s.replace('<<=', 'LSHIFTEQ')
    s = s.replace('<<', 'LSHIFT')
    s = s.replace('<=', 'LTEQ')
    s = s.replace('<', 'LT')
    s = s.replace('>>>=', 'URSHIFTEQ')
    s = s.replace('>>>', 'URSHIFT')
    s = s.replace('>>=', 'RSHIFTEQ')
    s = s.replace('>>', 'RSHIFT')
    s = s.replace('>=', 'GTEQ')
    s = s.replace('>', 'GT')
    s = s.replace('(', 'LPAREN')
    s = s.replace(')', 'RPAREN')
    s = s.replace('[', 'LBRACK')
    s = s.replace(']', 'RBRACK')
    s = s.replace('{', 'LBRACE')
    s = s.replace('}', 'RBRACE')
    s = s.replace('?', 'QUESTION')
    s = s.replace(',', 'COMMA')
    s = s.replace(';', 'SEMICOLON')
    s = s.replace(':', 'COLON')
    s = s.replace('$', 'DOLLAR')
    s = s.replace('==', 'EQEQ')
    s = s.replace('^^=', 'XORXOREQ')
    s = s.replace('^^', 'XORXOR')
    s = s.replace('^=', 'XOREQ')
    s = s.replace('^', 'XOR')
    s = s.replace('*=', 'MULTEQ')
    s = s.replace('*', 'MULT')
    s = s.replace('%=', 'MODEQ')
    s = s.replace('%', 'MOD')
    s = s.replace('~=', 'COMPEQ')
    s = s.replace('~', 'COMP')
    s = s.replace('=', 'EQ')
    s = s.replace('@', 'AT')
    s = s.replace('#', 'NUMBER')
    return s

f = open(sys.argv[1], 'rw')
d = f.read()
d = re.sub('\t', ' ', d)
d = re.sub('\r', '', d)
d = re.sub('&amp;', '&', d)
d = re.sub('&amp;', '&', d)
d = re.sub('&lt;', '<', d)
d = re.sub('&gt;', '>', d)
d = re.sub(' _opt', '_opt', d)
d = re.sub('(?<!\.)\.(?!\.)', ' . ', d)
d = re.sub('\(', ' ( ', d)
d = re.sub('\)', ' ) ', d)
d = re.sub('^(?!\n)\s+', '  : ', d, 0, re.MULTILINE)
d = re.sub(' +', ' ', d)
d = re.sub(' $', ' ', d)

for g in re.findall('GRAMMAR_BEGIN\n+(((?!GRAMMAR_BEGIN).)+)\n\nGRAMMAR_END', d, re.MULTILINE | re.DOTALL):
    for r in re.split('\n{2,}', g[0]):
        if re.match('new \( ArgumentList \)', r): continue

        s = r.split('\n')
        print re.sub(':', '', s[0])
        s[1] =  re.sub('^ : ', ' | ', s[1])

        for a in s[1:]:
            m = re.match(' (:|\|) (.+)', a)
            l = split_opt(m.group(2))
            print '  ' + m.group(1) + ' ' + sub_spec(l[0])
            for b in l[1:]:
                print '  : ' + sub_spec(b)

        print '  ;\n'
