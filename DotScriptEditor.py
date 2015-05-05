# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This module realized a simple dot language editor.
'''

import wx
from UIClass import DialogScript
import ExtParser
import ExtGraph
import ply.lex as lex

def get_lexer():
    '''Generate a very lexer to parse the dot script.'''
    ### All tokens.
    tokens = (
              'QUOTED_STRING',
              'COMMENT',    
              'KEYWORD',
              'EDGE_LINK',
              'PAREN',
              )

    t_QUOTED_STRING =  r'(\"(.|\n)*?\")'
    t_COMMENT = r'(/\*(.|\n)*?\*/)|(//.*)'
    t_KEYWORD = r'(?i)strict|digraph|graph|node|edge|subgraph'
    t_PAREN = r'\[|\]|\{|\}'
    t_EDGE_LINK = r'--|-\>'
    
    def t_error(t):
        #print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
    
    lexer = lex.lex()
    
    return lexer

def parse_dot(script):
    '''Parse dot script, return list of (token, begin_pos, end_pos).'''
    lexer = get_lexer()
    lexer.input(script)
    
    result = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        r = tok.type, tok.lexpos, tok.lexpos+len(tok.value)
        result.append(r)
        
    return result

def _is_same_color(textAtt1, textAtt2):
    if textAtt1.GetTextColour().GetRGB() == textAtt2.GetTextColour().GetRGB():
        return True
    else:
        return False
    
class DS(DialogScript):
    '''Dialog to edit dot script.'''
    def __init__(self, parent):
        DialogScript.__init__(self, parent)
        
        self.m_text_script.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, 
                                           wx.FONTSTYLE_NORMAL, 
                                           wx.FONTWEIGHT_NORMAL, 
                                           faceName='Consolas')
                                   )
        
        colors = [wx.Colour(31, 120, 180), \
                  wx.Colour(51, 160, 44), \
                  wx.Colour(227, 26, 28), \
                  wx.Colour(255, 127, 0), \
                  ]
        
        self.font_dict = {
            'PLAIN':            wx.TextAttr('#000000'),
            'QUOTED_STRING':    wx.TextAttr(colors[0]),
            'COMMENT':          wx.TextAttr(colors[1]), 
            'STRICT':           wx.TextAttr(colors[3]), 
            'KEYWORD':          wx.TextAttr(colors[3]),
            'EDGE_LINK':        wx.TextAttr(colors[3]),
            'PAREN':            wx.TextAttr(colors[2]),                
        }
        
        #self.m_text_script.Bind(wx.EVT_KEY_DOWN, self.onTab)
        self.Bind(wx.EVT_CHILD_FOCUS, self.onTextEnter)
        

    def onTab(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_TAB:
            event.EventObject.Navigate()
        event.Skip()
    
    def light_script_line(self, line):
        '''Syntax highlight the specified line.'''
        l_begin = self.m_text_script.XYToPosition(0, line)
        l_len = len(self.m_text_script.GetLineText(line))
        l_end = self.m_text_script.XYToPosition(l_len, line)

        script = self.m_text_script.GetValue()
        
        ttable = parse_dot(script)

        for t in ttable:
            if l_begin <= t[1] <= l_end or l_begin <= t[2] <= l_end: 
                self.m_text_script.SetStyle(t[1], t[2], self.font_dict[t[0]])
                if t[2] < l_end:
                    self.m_text_script.SetStyle(t[2], l_end, self.font_dict['PLAIN'])
        return
    
    def light_script_all(self):
        '''Syntax highlight all script.'''
        script = self.m_text_script.GetValue()
        ttable = parse_dot(script)

        for t in ttable:
            self.m_text_script.SetStyle(t[1], t[2], self.font_dict[t[0]])
    
    # A lock var to disable onText function when SetScript working.
    highlight_lock = False
        
    def SetScript(self, text):
        self.m_text_script.SetValue(text)
        
        self.highlight_lock = True
        self.light_script_all()
        self.highlight_lock = False
        
    def onText(self, event):
        
        if self.highlight_lock:
            return
        
        pos = self.m_text_script.GetInsertionPoint()
        _, line = self.m_text_script.PositionToXY(pos)
        
        self.light_script_line(line)
        
        return
    
    def onTextEnter(self, event):

        pos = self.m_text_script.GetInsertionPoint()
        _, line = self.m_text_script.PositionToXY(pos)

        if line -1 > 0:
            self.light_script_line(line-1)

        return
    
    def onOK(self, event):
        '''
        If script is ok, store script in graph objcet and return to main window.
        Else highlight the error line in editor. 
        '''
        script = self.m_text_script.GetValue().strip()
        ### Get strict status here.
        strict_status = False
        if script[:6].lower() == 'strict':
            strict_status = True
            
        try:
            g = ExtParser.parse_string(script.encode('utf8'))
            ### Hack the strcit status cause bug of pydot.
            g.set_strict(strict_status)
            
            self.graph = ExtGraph.ExtGraph(obj_dict=g.obj_dict)
            self.EndModal(wx.ID_OK)

        except ExtParser.ParseException, err:
            
            pos = self.m_text_script.XYToPosition(0, err.lineno-1)
            w = self.m_text_script.GetLineLength(err.lineno-1)
            
            self.m_text_script.SetFocus()
            self.m_text_script.SetSelection(pos, pos+w)
            
            wx.MessageBox("Parse Script Error.\n"+20*"-"+"\n%s"%err)
        
        return
    
def __test_lexer():
    script = '''
digraph G {
    rankdir=LR;
    penwidth=0.1;
    node [fontname="serif", fontsize=13, colorscheme="brbg3", color=1, comment="Wildcard node"];
    edge [fontname="sans-serif", fontsize=10, colorscheme="brbg3", color=3, fontcolor=3, comment="Wildcard edge"];
    "n1" [label="Welcome to DotEditor :)\n\n <--- select 'n1' and click minus to delete me."];
    n1 -> n2
}
    '''
    parse_dot(script)

if __name__ == '__main__':
    __test_lexer()
