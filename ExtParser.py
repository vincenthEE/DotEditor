# coding=utf8
from dot_parser import *
import dot_parser
from DEUtils import to_unicode

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
    