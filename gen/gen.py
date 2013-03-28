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
    s = s.replace('..', 'RANGE')
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
    s = s.replace('^^=', 'POWEQ')
    s = s.replace('^^', 'POW')
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
    s = re.sub('(?<![A-z_])abstract(?![A-z_])', 'ABSTRACT', s)
    s = re.sub('(?<![A-z_])alias(?![A-z_])', 'ALIAS', s)
    s = re.sub('(?<![A-z_])align(?![A-z_])', 'ALIGN', s)
    s = re.sub('(?<![A-z_])asm(?![A-z_])', 'ASM', s)
    s = re.sub('(?<![A-z_])assert(?![A-z_])', 'ASSERT', s)
    s = re.sub('(?<![A-z_])auto(?![A-z_])', 'AUTO', s)
    s = re.sub('(?<![A-z_])body(?![A-z_])', 'BODY', s)
    s = re.sub('(?<![A-z_])bool(?![A-z_])', 'BOOL', s)
    s = re.sub('(?<![A-z_])break(?![A-z_])', 'BREAK', s)
    s = re.sub('(?<![A-z_])byte(?![A-z_])', 'BYTE', s)
    s = re.sub('(?<![A-z_])case(?![A-z_])', 'CASE', s)
    s = re.sub('(?<![A-z_])cast(?![A-z_])', 'CAST', s)
    s = re.sub('(?<![A-z_])catch(?![A-z_])', 'CATCH', s)
    s = re.sub('(?<![A-z_])cdouble(?![A-z_])', 'CDOUBLE', s)
    s = re.sub('(?<![A-z_])cent(?![A-z_])', 'CENT', s)
    s = re.sub('(?<![A-z_])cfloat(?![A-z_])', 'CFLOAT', s)
    s = re.sub('(?<![A-z_])char(?![A-z_])', 'CHAR', s)
    s = re.sub('(?<![A-z_])class(?![A-z_])', 'CLASS', s)
    s = re.sub('(?<![A-z_])const(?![A-z_])', 'CONST', s)
    s = re.sub('(?<![A-z_])continue(?![A-z_])', 'CONTINUE', s)
    s = re.sub('(?<![A-z_])creal(?![A-z_])', 'CREAL', s)
    s = re.sub('(?<![A-z_])dchar(?![A-z_])', 'DCHAR', s)
    s = re.sub('(?<![A-z_])debug(?![A-z_])', 'DEBUG', s)
    s = re.sub('(?<![A-z_])default(?![A-z_])', 'DEFAULT', s)
    s = re.sub('(?<![A-z_])delegate(?![A-z_])', 'DELEGATE', s)
    s = re.sub('(?<![A-z_])delete(?![A-z_])', 'DELETE', s)
    s = re.sub('(?<![A-z_])deprecated(?![A-z_])', 'DEPRECATED', s)
    s = re.sub('(?<![A-z_])do(?![A-z_])', 'DO', s)
    s = re.sub('(?<![A-z_])double(?![A-z_])', 'DOUBLE', s)
    s = re.sub('(?<![A-z_])else(?![A-z_])', 'ELSE', s)
    s = re.sub('(?<![A-z_])enum(?![A-z_])', 'ENUM', s)
    s = re.sub('(?<![A-z_])export(?![A-z_])', 'EXPORT', s)
    s = re.sub('(?<![A-z_])extern(?![A-z_])', 'EXTERN', s)
    s = re.sub('(?<![A-z_])false(?![A-z_])', 'FALSE', s)
    s = re.sub('(?<![A-z_])final(?![A-z_])', 'FINAL', s)
    s = re.sub('(?<![A-z_])finally(?![A-z_])', 'FINALLY', s)
    s = re.sub('(?<![A-z_])float(?![A-z_])', 'FLOAT', s)
    s = re.sub('(?<![A-z_])for(?![A-z_])', 'FOR', s)
    s = re.sub('(?<![A-z_])foreach(?![A-z_])', 'FOREACH', s)
    s = re.sub('(?<![A-z_])foreach_reverse(?![A-z_])', 'FOREACH_REVERSE', s)
    s = re.sub('(?<![A-z_])function(?![A-z_])', 'FUNCTION', s)
    s = re.sub('(?<![A-z_])goto(?![A-z_])', 'GOTO', s)
    s = re.sub('(?<![A-z_])if(?![A-z_])', 'IF', s)
    s = re.sub('(?<![A-z_])ifloat(?![A-z_])', 'IFLOAT', s)
    s = re.sub('(?<![A-z_])immutable(?![A-z_])', 'IMMUTABLE', s)
    s = re.sub('(?<![A-z_])import(?![A-z_])', 'IMPORT', s)
    s = re.sub('(?<![A-z_])in(?![A-z_])', 'IN', s)
    s = re.sub('(?<![A-z_])inout(?![A-z_])', 'INOUT', s)
    s = re.sub('(?<![A-z_])int(?![A-z_])', 'INT', s)
    s = re.sub('(?<![A-z_])interface(?![A-z_])', 'INTERFACE', s)
    s = re.sub('(?<![A-z_])invariant(?![A-z_])', 'INVARIANT', s)
    s = re.sub('(?<![A-z_])ireal(?![A-z_])', 'IREAL', s)
    s = re.sub('(?<![A-z_])is(?![A-z_])', 'IS', s)
    s = re.sub('(?<![A-z_])lazy(?![A-z_])', 'LAZY', s)
    s = re.sub('(?<![A-z_])long(?![A-z_])', 'LONG', s)
    s = re.sub('(?<![A-z_])macro(?![A-z_])', 'MACRO', s)
    s = re.sub('(?<![A-z_])mixin(?![A-z_])', 'MIXIN', s)
    s = re.sub('(?<![A-z_])module(?![A-z_])', 'MODULE', s)
    s = re.sub('(?<![A-z_])new(?![A-z_])', 'NEW', s)
    s = re.sub('(?<![A-z_])nothrow(?![A-z_])', 'NOTHROW', s)
    s = re.sub('(?<![A-z_])null(?![A-z_])', 'NULL', s)
    s = re.sub('(?<![A-z_])out(?![A-z_])', 'OUT', s)
    s = re.sub('(?<![A-z_])override(?![A-z_])', 'OVERRIDE', s)
    s = re.sub('(?<![A-z_])package(?![A-z_])', 'PACKAGE', s)
    s = re.sub('(?<![A-z_])pragma(?![A-z_])', 'PRAGMA', s)
    s = re.sub('(?<![A-z_])private(?![A-z_])', 'PRIVATE', s)
    s = re.sub('(?<![A-z_])protected(?![A-z_])', 'PROTECTED', s)
    s = re.sub('(?<![A-z_])public(?![A-z_])', 'PUBLIC', s)
    s = re.sub('(?<![A-z_])pure(?![A-z_])', 'PURE', s)
    s = re.sub('(?<![A-z_])real(?![A-z_])', 'REAL', s)
    s = re.sub('(?<![A-z_])ref(?![A-z_])', 'REF', s)
    s = re.sub('(?<![A-z_])return(?![A-z_])', 'RETURN', s)
    s = re.sub('(?<![A-z_])scope(?![A-z_])', 'SCOPE', s)
    s = re.sub('(?<![A-z_])shared(?![A-z_])', 'SHARED', s)
    s = re.sub('(?<![A-z_])short(?![A-z_])', 'SHORT', s)
    s = re.sub('(?<![A-z_])static(?![A-z_])', 'STATIC', s)
    s = re.sub('(?<![A-z_])struct(?![A-z_])', 'STRUCT', s)
    s = re.sub('(?<![A-z_])super(?![A-z_])', 'SUPER', s)
    s = re.sub('(?<![A-z_])switch(?![A-z_])', 'SWITCH', s)
    s = re.sub('(?<![A-z_])synchronized(?![A-z_])', 'SYNCHRONIZED', s)
    s = re.sub('(?<![A-z_])template(?![A-z_])', 'TEMPLATE', s)
    s = re.sub('(?<![A-z_])this(?![A-z_])', 'THIS', s)
    s = re.sub('(?<![A-z_])throw(?![A-z_])', 'THROW', s)
    s = re.sub('(?<![A-z_])true(?![A-z_])', 'TRUE', s)
    s = re.sub('(?<![A-z_])try(?![A-z_])', 'TRY', s)
    s = re.sub('(?<![A-z_])typedef(?![A-z_])', 'TYPEDEF', s)
    s = re.sub('(?<![A-z_])typeid(?![A-z_])', 'TYPEID', s)
    s = re.sub('(?<![A-z_])typeof(?![A-z_])', 'TYPEOF', s)
    s = re.sub('(?<![A-z_])ubyte(?![A-z_])', 'UBYTE', s)
    s = re.sub('(?<![A-z_])ucent(?![A-z_])', 'UCENT', s)
    s = re.sub('(?<![A-z_])uint(?![A-z_])', 'UINT', s)
    s = re.sub('(?<![A-z_])ulong(?![A-z_])', 'ULONG', s)
    s = re.sub('(?<![A-z_])union(?![A-z_])', 'UNION', s)
    s = re.sub('(?<![A-z_])unittest(?![A-z_])', 'UNITTEST', s)
    s = re.sub('(?<![A-z_])ushort(?![A-z_])', 'USHORT', s)
    s = re.sub('(?<![A-z_])version(?![A-z_])', 'VERSION', s)
    s = re.sub('(?<![A-z_])void(?![A-z_])', 'VOID', s)
    s = re.sub('(?<![A-z_])volatile(?![A-z_])', 'VOLATILE', s)
    s = re.sub('(?<![A-z_])wchar(?![A-z_])', 'WCHAR', s)
    s = re.sub('(?<![A-z_])while(?![A-z_])', 'WHILE', s)
    s = re.sub('(?<![A-z_])with(?![A-z_])', 'WITH', s)
    s = re.sub('(?<![A-z_])__FILE__(?![A-z_])', '__FILE__', s)
    s = re.sub('(?<![A-z_])__MODULE__(?![A-z_])', '__MODULE__', s)
    s = re.sub('(?<![A-z_])__LINE__(?![A-z_])', '__LINE__', s)
    s = re.sub('(?<![A-z_])__FUNCTION__(?![A-z_])', '__FUNCTION__', s)
    s = re.sub('(?<![A-z_])__PRETTY_FUNCTION__(?![A-z_])', '__PRETTY_FUNCTION__', s)
    s = re.sub('(?<![A-z_])__gshared(?![A-z_])', '__GSHARED', s)
    s = re.sub('(?<![A-z_])__traits(?![A-z_])', '__TRAITS', s)
    s = re.sub('(?<![A-z_])__vector(?![A-z_])', '__VECTOR', s)
    s = re.sub('(?<![A-z_])__parameters(?![A-z_])', '__PARAMETERS', s)
    return s

d = sys.stdin.read()
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
