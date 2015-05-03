# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This file mainly used to generate resource used in DE.
'''

import colorbrewer, types
import AttrsDef
import ExtGraph, ExtParser
from DEUtils import add_double_quote
import DEUtils
import math, numpy, cv2
import wx

def build_CB_dict():
    __all_stuff = dir(colorbrewer)
    c_dict = {}
    for s in __all_stuff:
        c_cate = eval('colorbrewer.'+s)
        if s[0] >= 'A' and s[0] <= 'Z' and isinstance(c_cate , types.DictType):
            for c_idx in c_cate.keys():
                c_dict[s.lower()+str(c_idx)] = c_cate[c_idx]
    
    return c_dict

def store_colorbrewer():
    
    cd = build_CB_dict()
    ckeys = cd.keys()
    ckeys.sort()

    out_f = open('./resource/color_scheme/colorbrewer.csv', 'w')
    for k in ckeys:
        cs = cd[k]
        for x in range(len(cs)):
            r,g,b = cs[x]
            l_str = "%s.%d,%d,%d,%d\n"%(k,x+1,r,g,b,)
            out_f.write(l_str)
    out_f.close()
    
    return

def generate_node_shape_images():
    
    g = ExtParser.parse_file(ExtGraph.TEMPLATE_DOT)
    
    n1 = g.get_node('"n1"')
    n1.set_label('')
    n1.get_attributes()['colorscheme'] = add_double_quote('blues3')
    n1.get_attributes()['color'] = add_double_quote('3')
    n1.get_attributes()['fillcolor'] = add_double_quote('1')
    n1.get_attributes()['style'] = add_double_quote('filled')
    
    for shape in AttrsDef.E_SHAPE:
        
        n1.get_attributes()['shape'] = add_double_quote(shape)
        g.write('resource/node_shape/%s.png'%shape, 'dot', 'png')
        
    return
 
def generate_arrowtype_images():

    for at in AttrsDef.E_ARROWTYPE:
        
        DEUtils.gen_arrow_image(at, 'resource/edge_arrowtype/%s.png'%at)
                
    return

def generate_platte():
    max_w, max_h = 90, 120
    
    all_files = []
    
    for scheme in AttrsDef.E_COLORSCHEME:
        fn = 'resource/palette/%s.png'%scheme
        all_files.append(fn)
        color_dict = DEUtils.get_colors_in_schcme(scheme)
        c_num = len(color_dict) 
        if c_num > 20: ### Too many color, use small rectangle to arrange.
            # Calc color rect.
            x = int(math.sqrt(c_num))
            h = x - x%10
            w = c_num / h
            r = c_num % h
            if r > 0:
                w += 1
            blank_num = w*h - c_num
            # Arrange color.
            colors = color_dict.keys()
            colors.sort()
            pixels = []
            for c in colors:
                r,g,b = color_dict[c]
                pixels.append([b,g,r])
                
            [ pixels.append([255,255,255]) for b in range(blank_num) ]
            pixels = numpy.array(pixels)
            pixels = pixels.reshape(h,w,3)
        else:
            colors = color_dict.keys()
            colors.sort()
            pixels = []
            for c in colors:
                r,g,b = color_dict[c]
                pixels.append([b,g,r])
            
            pixels = numpy.array(pixels)
            pixels = pixels.reshape(1,c_num,3)
            
        ### Now enlarge the pixels.
        w, h, _ = pixels.shape
        
        bx = max_w/w ; by = max_h/h
        bz = min(bx, by)

        if w == 1:
            h_k = max_w / bz
        else:
            h_k = 1
        
        large_p = []
        for x in range(w):
            for _ in range(bz*h_k): ### Repeat bz times in line.
                for y in range(h):
                    ### Repeat bz times in pixel.
                    [ large_p.append(pixels[x,y]) for _ in range(bz) ] 
        large_p = numpy.array(large_p)
        large_p = large_p.reshape(w*bz*h_k, h*bz, 3)
         
        cv2.imwrite(fn, large_p)
    
    ### Normalize all image. 
    image_list = [ (fn, wx.Image(fn)) for fn in all_files ]
    
    max_w, max_h = (0,0)
    for img in image_list:
        w,h = img[1].GetSize()
        if w > max_w: max_w = w
        if h > max_h: max_h = h
    
    for img in image_list:
        w,h = img[1].GetSize()
        if w==max_w and h==max_h:
            img[1].SaveFile(img[0], wx.BITMAP_TYPE_PNG)
        else:
            pos_x = int((max_w-w)/2)
            pos_y = int((max_h-h)/2)
    
            new_img = wx.EmptyImage(max_w, max_h)
            new_img.Clear(0xff)
            new_img.Paste(img[1], pos_x, pos_y)
            new_img.SaveFile(img[0], wx.BITMAP_TYPE_PNG)

    return
        
if __name__ == '__main__':
    #generate_node_shape_images()
    #store_colorbrewer()
    generate_platte()
    
    
    
    