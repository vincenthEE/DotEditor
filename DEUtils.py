# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This module include some util functions.
'''

import csv
import ExtParser
import wx
import os, sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for "--onefile" in PyInstaller. """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def remove_double_quote(s):
    '''Remove double quote if nessary.'''
    if not isinstance(s, basestring):
        return s

    s = s.strip()    
    if s == '':
        return ''
    
    if s[0] == '"' and s[-1] == '"':
        s = s[1:-1]
        
    return s

def add_double_quote(s):
    '''Add double quote around s if nessary.'''
    if not isinstance(s, basestring):
        return s
    
    s = s.strip()
    if s == '':
        return '""'
    
    if s[0] != '"' and s[-1] != '"':
        s = '"'+s+'"'
        
    return s

def to_unicode(s):
    "Try convert 's' into unicode anyway."
    s = s.strip()
    
    u_str = None
    try:
        u_str = unicode(s)
    except:
        u_str = s.decode('utf8')
    
    return u_str.encode('utf8')

def gen_arrow_image(arrowtype, out_filepath):
    script = '''
digraph G {
    rankdir=LR;
    edge [colorscheme="blues3", color=3];
//    node [style="invis"];
    node [fontname="sans-serif", colorscheme="x11", fontsize=12, color="lightgray", fontcolor="lightgray", style=" ", penwidth=0.5];
    "n1" [label="A"];
    "n2" [label="B"];
    "n1" -> "n2"  [arrowhead="dot"];
}
    '''

    g = ExtParser.parse_string(script)    
    e1 = g.get_edge('"n1"', '"n2"')
    e1.get_attributes()['arrowhead'] = add_double_quote('%s'%arrowtype)
    g.write(out_filepath, 'dot', 'png')
        
    return

def get_colors_in_schcme(scheme_name):
    ### Build dict of scheme.
    # X11.
    if scheme_name == 'x11':
        in_f = open(resource_path('resource/color_scheme/rgb.txt'))
        in_f.readline() # Skip 1st line.
        x11_dict = {}
        while 1:
            line = in_f.readline()
            if line == "":
                break
            c = line[:11]
            r,g,b = map(int, [c[:3], c[4:7], c[8:]])
            c_name = line[11:].strip()
            x11_dict[c_name] = (r,g,b)
            
        return x11_dict

    # Svg.
    elif scheme_name == 'svg':
        svg_dict = {}
        in_f = open(resource_path('resource/color_scheme/svg.csv'), 'rb')
        cr = csv.reader(in_f, delimiter=',')
        for row in cr:
            svg_dict[row[0]] = tuple(map(int, row[1:]))
        in_f.close()
    
        return svg_dict

    # Colorbrewer.
    else:
        all_cb_dict = {}
        in_f = open(resource_path('resource/color_scheme/colorbrewer.csv'), 'rb')
        cr = csv.reader(in_f, delimiter=',')
        for row in cr:
            cb_name, cb_idx = row[0].split('.')
            if cb_name not in all_cb_dict:
                all_cb_dict[cb_name] = {}
                
            all_cb_dict[cb_name][cb_idx] = tuple(map(int, row[1:]))
        
        in_f.close()
        
        return all_cb_dict[scheme_name]
        
    return None

def get_image_resource(item_type, attr_name, value_str):
    '''Get image resouce by item_type(in ['node', 'edge', 'graph']), attr_name and value_str(in enum list).'''
    if item_type == 'node' and attr_name == 'shape':
        fn = resource_path('resource/node_shape/%s.png'%value_str)
        img = wx.Image(fn)
        return img
    elif item_type == 'edge' and attr_name in ['arrowhead', 'arrowtail']:
        fn = resource_path('resource/edge_arrowtype/%s.png'%value_str)
        img = wx.Image(fn)
        return img
    elif item_type is None and attr_name == 'colorscheme':
        fn = resource_path('resource/palette/%s.png'%value_str)
        img = wx.Image(fn)
        return img
    return None

def normalize_imglist(image_list):
    '''
    Make image in list to the same size. 
    The image_list should be a list of wxBitmap.
    Return a wxImageList as result.
    '''
    max_w, max_h = (0,0)
    for img in image_list:
        w,h = img.GetSize()
        if w > max_w: max_w = w
        if h > max_h: max_h = h
    
    il = wx.ImageList(max_w, max_h)
    
    for img in image_list:
        w,h = img.GetSize()
        if w==max_w and h==max_h:
            il.Add(img.ConvertToBitmap())
        else:
            pos_x = int((max_w-w)/2)
            pos_y = int((max_h-h)/2)
    
            new_img = wx.EmptyImage(max_w, max_h)
            new_img.Clear(0xff)
            new_img.Paste(img, pos_x, pos_y)
            il.Add(new_img.ConvertToBitmap())
    
    return il

if __name__ == '__main__':
    pass
        
    #print gen_CB_palette_img('PuBu')
    
    