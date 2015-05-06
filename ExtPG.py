# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This module define all propgrid class and functions used in main_frame.

Some editor dialog use the singleton method to promote efficiency.
'''

import wx.propgrid as wxpg
import AttrsDef
import wx, types, colour
import re
from DEUtils import remove_double_quote, get_colors_in_schcme
from UIClass import ImageSingleChoiceDialog, ArrowTypeDialog, \
                    ColorSingleChoiceDialog, ColorSchemeDialog, \
                    DialogTextEditor
import DEUtils
import tempfile

### Some global var.
CS_DIALOG = None
NS_DIALOG = None
AT_DIALOG = None

BUG_NO_DOUBLEQUOTE_MESSAGE = "I'm very Sorry, because the limit of 'Pydot' module, current "+\
                             "all text in DotEditor not support including double-quote< \" >, "+\
                             "you can delete them or replace them with single-quote< \' >. "+\
                             "Sorry again :("

def get_root_window(window):
    
    p = window
    while 1:
        r1 = p.GetParent()
        if r1 is None:
            return p
        else:
            p = r1 
            
    return None

class CSDialog(ColorSchemeDialog):
    '''A Dialog to select a colorscheme.'''
    
    @staticmethod
    def get_dialog(parent, scheme='x11'):
        '''A factory method to return singleton.'''
        global CS_DIALOG
        if CS_DIALOG is None:
            CS_DIALOG = CSDialog(parent, scheme)
        
        CS_DIALOG.reset()
        return CS_DIALOG
    
    def __init__(self, parent, scheme='x11'):
        
        ColorSchemeDialog.__init__(self, parent)
        
        self.choice = AttrsDef.E_COLORSCHEME
        
        il = get_root_window(self).image_list['colorscheme']
        self.m_list.AssignImageList(il, 0)
        
        # Change dialog size to fit the image size.        
        w, h = il.GetBitmap(0).GetSize()
        self.SetSizeWH(int(w*4.5), h*4)
        
        self.updateList()
        
        self.m_list.Bind(wx.EVT_LEFT_DCLICK, self.onOK)
    
    def reset(self):
        self.m_searchCtrl.SetValue('')
        self.onSearch(None)
    
    def SetColorScheme(self, scheme):
        s = scheme.strip().lower()
        idx = self.m_list.FindItem(0, s)
        if idx < 0:
            return
        self.m_list.Select(idx, True)
        self.m_list.Focus(idx)
    
    def onSearch(self, event):
        s_text = self.m_searchCtrl.GetValue()
        scheme_list = self.choice
        
        search_result = filter(lambda s:s.find(s_text) > -1, scheme_list)
        self.updateList(search_result)
    
    def GetColorScheme(self):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return ''
        else:
            return self.m_list.GetItemText(idx)
    
    def updateList(self, scheme_list=None):
        
        all_scheme = self.choice
        if scheme_list is None:
            scheme_list = all_scheme
        
        self.m_list.ClearAll()
        for x in range(len(scheme_list)):
            c = scheme_list[x]
            img_idx = all_scheme.index(c)
            self.m_list.InsertImageStringItem(x, c, img_idx)
            
        return

    def onOK(self, event):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return
        
        self.EndModal(wx.ID_OK)

class CSCDialog(ColorSingleChoiceDialog):
    '''A Dialog to select a color.'''
    
    def __init__(self, parent, scheme='x11'):
        ColorSingleChoiceDialog.__init__(self, parent)
        
        self.SetTitle('Pick a color')
        self.m_staticText_message.SetLabel('Select a color in "%s":'%scheme)
        
        self.choice = get_colors_in_schcme(scheme)
        
        self.updateList()
        
        self.m_list.Bind(wx.EVT_LEFT_DCLICK, self.onOK)
        
    def SetColorString(self, color):
        s = color.strip().lower()
        idx = self.m_list.FindItem(0, s)
        if idx < 0:
            return
        self.m_list.Select(idx, True)
        self.m_list.Focus(idx)
        self.m_list.SetFocus()
    
    def onSearch(self, event):
        s_text = self.m_searchCtrl.GetValue()
        color_list = self.choice.keys()
        color_list.sort()
        
        search_result = filter(lambda s:s.find(s_text) > -1, color_list)
        self.updateList(search_result)
    
    def GetColorString(self):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return ''
        else:
            return self.m_list.GetItemText(idx)
    
    def updateList(self, color_list=None):
        
        if color_list is None:
            color_list = self.choice.keys()
            color_list.sort()
        
        self.m_list.ClearAll()
        self.m_list.InsertColumn(0, 'COLOR NAME')
        w, _ = self.m_list.GetSize()
        self.m_list.SetColumnWidth(0, w*0.92)
        for x in range(len(color_list)):
            c = color_list[x]
            self.m_list.InsertStringItem(x, c)
            r,g,b = self.choice[c]
            v = max(r,g,b)/255.0
            if v < 0.5:
                self.m_list.SetItemTextColour(x, wx.Colour(255,255,255))
            self.m_list.SetItemBackgroundColour(x, wx.Colour(r,g,b))
            
        return

    def onOK(self, event):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return
        
        self.EndModal(wx.ID_OK)
        

class NodeShapeDialog(ImageSingleChoiceDialog):
    '''A Dialog to select node shape.'''
    
    @staticmethod
    def get_dialog(parent):
        '''A factory method to return singleton.'''
        global NS_DIALOG
        if NS_DIALOG is None:
            NS_DIALOG = NodeShapeDialog(parent)
        
        return NS_DIALOG
    
    def __init__(self, parent):
        
        ImageSingleChoiceDialog.__init__(self, parent)
        
        self.SetTitle('Select node shape')
        self.m_message.SetLabel('Choice a node shape below:')
        
        self.choices = AttrsDef.E_SHAPE
        
        il = get_root_window(self).image_list['node_shape']
        self.m_list.AssignImageList(il, 0)

        # Change dialog size to fit the image size.        
        w, h = il.GetBitmap(0).GetSize()
        self.SetSizeWH(int(w*8), h*6)
        
        for x in range(len(self.choices)):
            c = self.choices[x]
            self.m_list.InsertImageStringItem(x, c, x)
        
        self.m_list.Bind(wx.EVT_LEFT_DCLICK, self.onOK)
        
        return

    def SetSelectedString(self, nodeshape):
        
        idx = self.m_list.FindItem(0, nodeshape)
        if idx < 0:
            return False
        
        self.m_list.Select(idx, True)
        self.m_list.Focus(idx)
        return True

    def GetSelectedString(self):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return None
        
        return self.m_list.GetItemText(idx)
    
    def onOK(self, event):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return
        
        self.EndModal(wx.ID_OK)
        
class ATDialog(ArrowTypeDialog):
    '''A Dialog to select arrow type.'''
    @staticmethod
    def get_dialog(parent):
        '''A factory method to return singleton.'''
        global AT_DIALOG
        if AT_DIALOG is None:
            AT_DIALOG = ATDialog(parent)
        
        return AT_DIALOG
    
    def __init__(self, parent):
        ArrowTypeDialog.__init__(self, parent)
        self.base_at_list = AttrsDef.E_ARROWTYPE
        
        il = get_root_window(self).image_list['arrow_style']
        self.m_list.AssignImageList(il, 0)

        # Change dialog size to fit the image size.        
        w, h = il.GetBitmap(0).GetSize()
        self.SetSizeWH(int(w*3.2), h*8)
        
        for x in range(len(self.base_at_list )):
            c = self.base_at_list[x]
            self.m_list.InsertImageStringItem(x, c, x)
        
        self.m_list.Bind(wx.EVT_LEFT_DCLICK, self.onOK)

    def getArrowType(self):
        
        # Get value from UI.
        ta = self.m_list.GetFirstSelected()
        if ta == -1:
            return None
        
        v_side =  self.m_radioBox_arrowpart.GetSelection()
        v_o = self.m_checkBox_arrowfilled.GetValue()
        
        # Generate arrow type string.
        s_o = ''
        if v_o == False: s_o ='o'
        s_side = ''
        if v_side == 1:
            s_side = 'l'
        elif v_side == 2:
            s_side = 'r'
        s_ta = self.base_at_list[ta]
        
        return ''.join([s_o, s_side, s_ta])
    
    def setArrayType(self, str_arraytype):
        sa = str_arraytype.lower()
        
        ### Let begin a stupid yacc program :)
        is_filled = True
        l_side = ""
        at = ''
        if sa[0] == 'o':
            is_filled = False
            if sa[1] in ['l', 'r']:
                l_side = sa[1]
                at = sa[2:]
            else:
                at = sa[1:]
        elif sa[0] in ['l', 'r']:
            l_side = sa[0]
            at = sa[1:]
        else:
            at = sa
        
        self.m_checkBox_arrowfilled.SetValue(is_filled)
        
        if l_side == "":
            self.m_radioBox_arrowpart.SetSelection(0)
        elif l_side == 'l':
            self.m_radioBox_arrowpart.SetSelection(1)
        else:
            self.m_radioBox_arrowpart.SetSelection(2)
        
        idx = self.base_at_list.index(at)
        self.m_list.Select(idx, True)    
        self.m_list.Focus(idx)
        
        return

    def onATSelected(self, event):
        i = self.m_list.GetFirstSelected()
        if i == -1:
            return None
        at_s = self.base_at_list[i]
        
        ### Do some limit as the official document.
        ### (http://www.graphviz.org/content/arrow-shapes)
        if at_s in ['crow', 'curve', 'icurve', 'tee', 'vee']:
            self.m_checkBox_arrowfilled.SetValue(True)
            self.m_checkBox_arrowfilled.Disable()
        else:
            self.m_checkBox_arrowfilled.Enable()
            
        if at_s in ['dot']:
            self.m_radioBox_arrowpart.SetSelection(0)
            self.m_radioBox_arrowpart.Disable()
        else:
            self.m_radioBox_arrowpart.Enable()
    
        self.refresh_preview()
    
    def onArrowChanged(self, event):
        self.refresh_preview()
    
    def refresh_preview(self):
        
        # Gen image.
        at = self.getArrowType()
        fn = tempfile.gettempdir()+'/.atpreview'
        DEUtils.gen_arrow_image(at, fn)
        img = wx.Image(fn)
        
        # Cut the center part for preview. 
        w,h=img.GetSize()
        img = img.GetSubImage(wx.Rect((w-h)/2, 0, h, h))
        
        self.m_bitmap_preview.SetSize((h,h))
        self.m_bitmap_preview.SetBitmap(img.ConvertToBitmap())
        self.m_bitmap_preview.UpdateWindowUI()
        
        return
    
    def onOK(self, event):
        idx = self.m_list.GetFirstSelected()
        if idx == -1:
            return
        
        self.EndModal(wx.ID_OK)



class DotStringProperty(wxpg.PyProperty):
    '''
    Why this? This class existed because the build-in wxpg.PyStringProperty not trigger event when zero-length string input. 
    '''
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
        
    def GetClassName(self):
        return 'DotStringProperty'

    def GetEditor(self):
        return 'TextCtrl'
    
    def ValueToString(self, v, flags):
        return v

    def StringToValue(self, s, flags):
        return True, s
    
    def ValidateValue(self, value, validationInfo):
        """ Let's limit the value NOT inclue double-quote.
        """
        # Mark the cell if validaton failred
        validationInfo.SetFailureBehavior(wxpg.PG_VFB_MARK_CELL)

        if value.find('"') >= 0:
            wx.MessageBox(BUG_NO_DOUBLEQUOTE_MESSAGE,
                          "Sorry, can't do this", 
                          style=wx.OK|wx.ICON_INFORMATION)
            return False

        return (True, value)

class DotBigStringProperty(DotStringProperty):
    '''
    A PG to edit big text such as label.
    '''
    def GetClassName(self):
        return 'DotBigStringProperty'

    def GetEditor(self):
        return 'TextCtrlAndButton'
    
    def OnEvent(self, propgrid, primaryEditor, event):
        
        ok = False
        
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:

            dlg = DialogTextEditor(propgrid)
            dlg.SetTitle('Input the label text')
            
            text = self.GetValue()
            dlg.m_text.SetValue(text)
    
            if dlg.ShowModal() == wx.ID_OK:
                text = dlg.m_text.GetValue()
                self.m_value = text
                self.SetValueInEvent(text)
                ok = True
                
        return ok

class DotFloatProperty(wxpg.PyFloatProperty):
    
    def ValueToString(self, v, flags):
        c_str = str(v)
        ### If no decimal point, add .0
        if c_str.isdigit():
            c_str += '.0'
        return c_str
    
    def DoGetValue(self):
        
        return self.ValueToString(self.m_value, None)

class DotColorSchemeProperty(wxpg.PyProperty):
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
        self.choices = AttrsDef.E_COLORSCHEME
    
    def GetClassName(self):
        return 'DotColorSchemeProperty'
    
    def GetEditor(self):
        return "TextCtrlAndButton"
        
    def StringToValue(self, s, flags):
        s = s.strip().lower()
        if s in self.choices:
            return True, s
        
        return False

    def ValueToString(self, v, flags):
        return v.strip().lower()
    
    def OnEvent(self, propgrid, primaryEditor, event):
        
        ok = False
        
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:

            dlg = CSDialog.get_dialog(propgrid)
            if isinstance(self.m_value, basestring):
                dlg.SetColorScheme(self.m_value)
    
            if dlg.ShowModal() == wx.ID_OK:
                cs = dlg.GetColorScheme()
                self.m_value = cs
                self.SetValueInEvent(cs)
                ok = True
                
        return ok

class DotColorProperty(wxpg.PyProperty):
    '''The value of pg should be 3 type:
        1. A color name in string.
        2. A RGB/RGBA value in tuple(r,g,b in 0~255).
        3. A int to point out the index in colorscheme. 
    '''

    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
    
    def GetClassName(self):
        return 'DotColorProperty'
    
    def GetEditor(self):
        return "TextCtrlAndButton"
    
    def StringToValue(self, s, flags):
        
        s = remove_double_quote(s).strip()
        # For emtpy value.
        if s == '': 
            return True, None
        
        # Try to parse hex string.
        if s[0] == '#':
            try:
                if len(s) == 7: # RGB.
                    r, g, b = colour.hex2rgb(s)
                    return True, (255*r,255*g,255*b)
                elif len(s) == 9: # RGBA.
                    r, g, b = colour.hex2rgb(s[:-2])
                    a = int(s[-2:], 16)
                    return True, (255*r,255*g,255*b,a)
                else:
                    return False
            except:
                return False
        # Try to parse HSV string.
        elif s[0].isdigit() or s[0] == '.': # Try to parse numbers
            try:
                # If get single int value.
                if s.isdigit():
                    return True, int(s)
                else:
                    h,s,v = map(float, s.split(' '))
                    rgb = wx.Image.HSVtoRGB(wx.Image_HSVValue(h,s,v))
                    return True, (rgb.red, rgb.green, rgb.blue)
            except:
                return False
            
        # Color in string.
        else:
            scheme = self.__get_current_scheme()
            if scheme is None:
                return True, s
            
            colors = get_colors_in_schcme(scheme).keys()
            if s.lower() not in colors:
                return False
            
            return True, s

    def ValueToString(self, value, flags):

        if value is None:
            return ''
        
        if isinstance(value, basestring):
            return value
        elif isinstance(value, types.IntType):
            return str(value)
        elif isinstance(value, types.TupleType):
            if len(value) == 3:
                return '#%02x%02x%02x'%value
            elif len(value) == 4:
                return '#%02x%02x%02x%02x'%value
            else:
                return ''
        else:
            return ''

    def __get_current_scheme(self):
        # Get the colorscheme in the same propgrid.
        grid = self.GetGrid()
        if grid is None:
            return None
        cs_pg = grid.GetPropertyByLabel('colorscheme')
        if cs_pg is None:
            return None
            
        scheme = cs_pg.GetValue().lower().strip()
        
        return scheme

    def OnEvent(self, propgrid, primaryEditor, event):
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:

            scheme = self.__get_current_scheme()
            if scheme is None:
                scheme = 'x11'
            
            dlg = CSCDialog(propgrid, scheme)
            if isinstance(self.m_value, basestring):
                dlg.SetColorString(self.m_value)
    
            if dlg.ShowModal() == wx.ID_OK:
                color = dlg.GetColorString()
                self.m_value = color
                self.SetValueInEvent(color)
                return True
            
        return False    
    
    def SetChoices(self, choices):
        self.choices = choices
        
    def DoGetValue(self):
        c_str = self.ValueToString(self.m_value, None)
         
        return c_str 

class DotEnumProperty(wxpg.PyProperty):
    
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
    
    def GetClassName(self):
        return 'DotEnumProperty'
    
    def GetEditor(self):
        return "ComboBox"

    def StringToValue(self, s, flags):

        if s == '' or s in self.GetChoices().GetLabels():
            return True, s
        else:
            return False
         
    def ValueToString(self, value, flags):

        return str(value)

class DotEnumCombineProperty(wxpg.PyProperty):
    
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
        
    def GetClassName(self):
        return 'DotEnumCombineProperty'
    
    def GetEditor(self):
        return "TextCtrlAndButton"

    def OnEvent(self, propgrid, primaryEditor, event):
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:
            dlg = wx.MultiChoiceDialog(propgrid,'Check all wanted %ss below:'%self.GetLabel(),'Make Choices',self.choices)
            if len(self.m_value.strip()) > 0:
                sels = [ self.choices.index(x.strip()) for x in self.m_value.split(',') ]
                dlg.SetSelections(sels)
                
            if dlg.ShowModal() == wx.ID_OK:
                sels = dlg.GetSelections()
                if len(sels) == 0:
                    self.m_value = ''
                    return True
                v = ''
                for idx in sels:
                    v += self.choices[idx] +', '
                v = v[:-2]

                self.m_value = v
                self.SetValueInEvent(v)
                return True
            
        return False    
        
    def SetChoices(self, choices):
        self.choices = choices

    def StringToValue(self, s, flags):
        
        s = s.strip()
        if s == '':
            return True, s
    
        styles = s.split(',')
        for sty in styles:
            if sty.strip() not in self.choices:
                return False
        
        return True, s
    
    def ValueToString(self, value, flags):

        return str(value)

class DotEnumNodeShapeProperty(wxpg.PyProperty):
    
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
        self.choices = AttrsDef.E_SHAPE
        
    def GetClassName(self):
        return 'DotEnumNodeShapeProperty'
    
    def GetEditor(self):
        return "TextCtrlAndButton"

    def OnEvent(self, propgrid, primaryEditor, event):
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:
            dlg = NodeShapeDialog.get_dialog(propgrid)
            # Set the current value.
            if self.m_value:
                dlg.SetSelectedString(self.m_value)
            
            if dlg.ShowModal() == wx.ID_OK:
                v = dlg.GetSelectedString()
                self.m_value = v
                self.SetValueInEvent(v)
                return True
            
        return False    

    def StringToValue(self, s, flags):

        s = s.strip()

        if s == '' or s in self.choices:
            return True, s
        else:
            return False
        
        return False
    
    def ValueToString(self, value, flags):

        return str(value)
    
class DotEnumArrowTypeProperty(wxpg.PyProperty):
    
    def __init__(self, label, name=wxpg.LABEL_AS_NAME, value=''):
        wxpg.PyProperty.__init__(self, label, name)
        self.SetValue(value)
        
    def GetClassName(self):
        return 'DotEnumArrowTypeProperty'
    
    def GetEditor(self):
        return "TextCtrlAndButton"

    def OnEvent(self, propgrid, primaryEditor, event):
        if event.GetEventType() == wx.wxEVT_COMMAND_BUTTON_CLICKED:
            
            dlg = ATDialog.get_dialog(propgrid)
            # Show the current arrow_type in m_value.
            if self.m_value:
                dlg.setArrayType(self.m_value)
            
            if dlg.ShowModal() == wx.ID_OK:
                v = dlg.getArrowType()
                self.m_value = v
                self.SetValueInEvent(v)
                return True
            
        return False    

    def StringToValue(self, s, flags):

        s = s.strip()
        a_names = AttrsDef.E_ARROWTYPE
        test = re.compile(r'(?i)o{0,1}(l|r){0,1}(%s)\b'%('|'.join(a_names)))
        if test.match(s) is None:
            return False
        else:
            return True, s
    
    def ValueToString(self, value, flags):
        return str(value)

class DotEditEnumProperty(wxpg.PyStringProperty):
    
    def GetEditor(self):
        return "ComboBox"
    
map_type2class = {'string':         DotStringProperty, 
                  'bigstring':      DotBigStringProperty,
                  'int':            wxpg.UIntProperty,
                  'bool':           wxpg.BoolProperty,
                  'float':          DotFloatProperty,
                  'color':          DotColorProperty,
                  'colorscheme':    DotColorSchemeProperty,
                  'enum':           DotEnumProperty,
                  'enum_edit':      DotEditEnumProperty,
                  'enum_combine':   DotEnumCombineProperty,
                  'enum_nodeshape': DotEnumNodeShapeProperty,
                  'enum_arrowtype': DotEnumArrowTypeProperty,
                  'img_file':       wxpg.ImageFileProperty, 
                  } 


def buildPG(attr_name, g_type):
    '''Build PropGridProperty instance by attr_name and g_type.'''
    info = AttrsDef.get_dot_attr(attr_name, g_type)
    pg_class = map_type2class[info['type']]
    
    pg_item = pg_class(attr_name)
    
    if info['type'] in ['enum', 'enum_edit', 'enum_combine']:
        pg_item.SetChoices(info['param'])
    
    elif info['type'] == 'bool':
        pg_item.SetEditor('CheckBox')
    
    elif info['type'] == 'img_file':
        pg_item.SetAttribute(wxpg.PG_FILE_WILDCARD, 
                             "Support Image File (*.png;*.gif)|*.png;*.gif"+\
                             "|PNG File (*.png)|*.png"+\
                             "|Gif File (*.gif)|*.gif")
    
    v = info['default_value']
    if v is None:
        pg_item.SetDefaultValue('')
    else:
        pg_item.SetDefaultValue(str(v).strip())
        pg_item.SetValueFromString(str(v))

    pg_item.SetHelpString(info['description'])
    
    return pg_item
    
    