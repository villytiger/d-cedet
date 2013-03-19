#!/usr/bin/python

import sys, re

f = open(sys.argv[1], 'rw')
d = f.read()
d = re.sub('\r', '', d)
d = re.sub('&amp;', '&', d)
d = re.sub('&lt;', '<', d)
d = re.sub('&gt;', '>', d)
d = re.sub(';', 'SEMICOLON', d)
d = re.sub('^(?!\n)\s+', '\t', d, 0, re.MULTILINE)

for g in re.findall('GRAMMAR_BEGIN\n+(((?!GRAMMAR_BEGIN).)+)\n\nGRAMMAR_END', d, re.MULTILINE | re.DOTALL):
    for r in re.split('\n{2,}', g[0]):
        s = r.split('\n')
        print re.sub(':', '', s[0])
        print re.sub('^\t', '  : ', s[1])
        for a in s[2:]:
            print re.sub('^\t', '  | ', a)
        print '  ;\n'
