# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This module simply extend from the "dot_parser.py" in pydot.
'''

from dot_parser import *
import dot_parser


def parse_string(data):
    
    dot_parser.top_graphs = list()

    graphparser = graph_definition()
    
    if pyparsing_version >= '1.2':
        graphparser.parseWithTabs()
        
    tokens = graphparser.parseString(data)

    if len(tokens) == 1:
        return tokens[0]
    else:
        return [g for g in tokens]

def parse_file(fn):
    
    from DEUtils import to_unicode
    
    script = open(fn).read()

    script = to_unicode(script)
    
    return parse_string(script)
    
    
if __name__ == '__main__':
    
    g = parse_string('''
    digraph G {
        rankdir=LR;
        111 -> 222;
        111;
    }
    ''')
    print g.to_string()
    