# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

A Dot file Editor to make the great graphviz tools easier to beginner.

This module include the main UI logic of DE. 
To change the UI layout, edit the DotEditor.fbp by "wxFormBuilder". (http://sourceforge.net/projects/wxformbuilder)

The graph core module "ExtGraph.py" base on the PyDot project. (https://github.com/erocarrera/pydot)

To modified the attributes define of dot language, edit the "AttrsDef.py".
'''

import os, wx, types, time, shutil
import wx.propgrid as wxpg
import ExtGraph as ExtGraph

from UIClass import MainFrame, DialogAppend, DialogAbout, DialogGraphSetting
from DotScriptEditor import DS
import ExtParser
import AttrsDef
import ExtPG
from __builtin__ import isinstance
from DEUtils import add_double_quote, to_unicode, remove_double_quote ,\
                    normalize_imglist, get_image_resource, resource_path


### The layout command and export format wildcard define. 
### The "osage", "sfdp" commands are not here because the pydot module has missed them.
G_CMDS = ['circo', 'dot', 'fdp', 'neato', 'twopi']
G_FORMAT_WILDCARD = "Portable Network Graphics format (*.png)|*.png"+\
                    "|Windows Bitmap Format (*.bmp)|*.bmp"+\
                    "|JPEG format (*.jpg)|*.jpg"+\
                    "|Scalable Vector Graphics (*.svg)|*.svg"+\
                    "|PostScript Format (*.ps)|*.ps"+\
                    "|PostScript for PDF (*.ps2)|*.ps2"+\
                    "|GIF Format (*.gif)|*.gif"


class DA(DialogAppend):
    '''Append item dialog.'''
    def __init__(self, parent):
        DialogAppend.__init__(self, parent)
        self.data_graph = parent.data_graph
        self.__refresh_comboBoxA_suggestion()
        
        self.m_comboBox_nodeA.SetFocus()
    
    def __name_add_label(self, name, label):
        '''Add name and label to a new string.'''
        r = name
        if (not label is None) and (label.strip() != ''):
            # Add strange surround symbol, make it easy to find in suggestion_B or get value.
            r = name+' [%%label=%s%%]'%label
        return r
    
    def __name_remove_label(self, name):
        '''Delete label from name if possiable, ref to <self.__name_add_label>.'''
        _pos = name.rfind('[%')
        if _pos >= 0:
            return name[:_pos].strip()
        else:
            return name
    
    def __refresh_comboBoxA_suggestion(self):
        '''Refresh comboxA, filled it with suggested node name.'''
        edges = self.data_graph.get_edges()
        nodes = self.data_graph.get_nodes()
        
        # Save the value in old_v.
        old_v = self.m_comboBox_nodeA.GetValue()
        
        ### Generate suggestion when Appending Node.
        if self.m_radioBox_type.GetSelection() == 0:
            # Get all node's name.
            all_n = set() 
            for n in nodes:
                all_n.add( remove_double_quote(n.get_name()) )
                
            # Get all end-node of edges that not in all_n.
            s_n = set()
            for e in edges:
                nS = remove_double_quote( e.get_source() )
                nD = remove_double_quote( e.get_destination() )
                for n in [nS, nD]:
                    if not (n in all_n):
                        s_n.add(n)
                        
            s_n = list(s_n); s_n.sort()
        
        ### Generate suggestion when Appending Edge.
        else:
            # Get all node name in graph. Include all end-nodes in edges. 
            all_n = set()
            need_remove_nodes = set()
            for n in nodes:
                _n = remove_double_quote( n.get_name() )
                _l = remove_double_quote( n.get_label() )
                _n_text = self.__name_add_label(_n, _l)
                    
                if _n not in ['node', 'edge']: # Exclude wildcard node.
                    all_n.add(_n_text)
                    ### Remove the node without label appended.
                    if _n != _n_text: 
                        need_remove_nodes.add(_n)
            
            for e in edges:
                nS = remove_double_quote( e.get_source() )
                nD = remove_double_quote( e.get_destination() )
                all_n.add(nS); all_n.add(nD)
            s_n = all_n - need_remove_nodes
            s_n = list(s_n); s_n.sort()
        
        self.m_comboBox_nodeA.Clear()
        for n in s_n:
            self.m_comboBox_nodeA.Append(n.decode('utf8'))
        
        # Restore the nodeA value.
        if old_v.encode('utf8') in s_n:
            self.m_comboBox_nodeA.SetValue(old_v)
        
        return
    
    def __refresh_comboBoxB_suggestion(self):
        '''Refresh comboxB, filled it with suggested node name, based on the value of comboxA.'''
        if self.m_radioBox_type.GetSelection() == 0:
            self.m_comboBox_nodeB.Clear()
            return
            
        # Save the value in old_v.
        old_v = self.m_comboBox_nodeB.GetValue()
            
        edges = self.data_graph.get_edges()
        nodes = self.data_graph.get_nodes()
        rawA = self.m_comboBox_nodeA.GetValue().strip().encode('utf8')
        # Remove label part from nA if existed.
        nA = self.__name_remove_label(rawA)
        
        # Get all node's name.
        s_n = set() 
        need_remove_nodes = set()
        for n in nodes:
            
            _n = remove_double_quote( n.get_name() )
            _l = remove_double_quote( n.get_label() )
            _n_text = self.__name_add_label(_n, _l)
                
            if _n not in ['node', 'edge']: # Exclude wildcard node.
                s_n.add(_n_text)
                ### Remove the node without label appended.
                if _n != _n_text: 
                    need_remove_nodes.add(_n)
            
        # Get all end-nodes of edges if start ending not nA.
        for e in edges:
            nS = remove_double_quote( e.get_source() )
            nD = remove_double_quote( e.get_destination() )
            if nA != nS:
                s_n.add(nS); s_n.add(nD)
            else:
                nD = self.__name_remove_label(nD)
                need_remove_nodes.add(nD)
                if nA == nD: ### Find a self connected node.x
                    need_remove_nodes.add(rawA)
                    
        s_n = s_n - need_remove_nodes
        s_n = list(s_n); s_n.sort()
        
        self.m_comboBox_nodeB.Clear()
        for n in s_n:
            self.m_comboBox_nodeB.Append(n.decode('utf8'))
        
        # Restore the nodeA value.
        if old_v.encode('utf8') in s_n:
            self.m_comboBox_nodeB.SetValue(old_v)
        
        return
    
    def getAppendValue(self):
        '''If "append node" checked, return node in string; else return nodes in tuple.'''
        vCheck = self.m_radioBox_type.GetSelection()
        vA = remove_double_quote( self.m_comboBox_nodeA.GetValue().encode('utf8') )
        vB = remove_double_quote( self.m_comboBox_nodeB.GetValue().encode('utf8') )
            
        if vCheck == 0:
            return 'node', self.__name_remove_label(vA)
        elif vCheck == 1:
            return 'edge', (self.__name_remove_label(vA), self.__name_remove_label(vB))
        else:
            return 'subgraph', vA
    
    def onTypeChange(self, event):
        '''Refresh both combox when the value of append_type_checkbox changed.'''
        checked = self.m_radioBox_type.GetSelection() 
        if checked == 0: # Case Node.
            self.m_comboBox_nodeB.Clear()
            self.m_comboBox_nodeB.Disable()
            self.__refresh_comboBoxA_suggestion()
            self.__refresh_comboBoxB_suggestion()
        elif checked == 1: # Case Edge.
            self.m_comboBox_nodeB.Enable()
            self.__refresh_comboBoxA_suggestion()
            self.__refresh_comboBoxB_suggestion()
        else: # Case Subgraph
            self.m_comboBox_nodeB.Disable()
            
            self.m_comboBox_nodeA.Clear()
            self.m_comboBox_nodeA.SetValue('clusterN')
            self.m_comboBox_nodeA.SetFocus()
            self.m_comboBox_nodeA.SetMark(7, -1)
        
    def onNodeAChanged(self, event):
        '''Refill comboxB when value of combox changed.'''
        checked = self.m_radioBox_type.GetSelection() 
        if checked == 1:
            self.__refresh_comboBoxB_suggestion()
        
    def OnOK(self, event):
        v = self.getAppendValue()
        sth_wrong = False
        if v[0] in ['node', 'subgraph']:
            if v[1] == '':
                sth_wrong = True
        else:
            if v[1][0] == '' or v[1][1] == '':
                sth_wrong = True
        if sth_wrong:
            wx.MessageBox('Empty value is NOT allow.')
            return
        else:
            self.EndModal(wx.ID_OK)
    
    
class DGS(DialogGraphSetting):
    '''Dialog to edit graph object high level setting.'''
    
    def __init__(self, parent):
        
        DialogGraphSetting.__init__(self, parent)
        # Init the value of control.
        g = parent.data_graph
        self.m_checkBox_strict.SetValue(g.get_strict(None))
        
        if g.get_type() == 'graph':
            self.m_radioBox_type.SetSelection(1)
        else:
            self.m_radioBox_type.SetSelection(0)
            
        self.m_textCtrl_name.SetValue(g.get_name().strip().decode('utf8'))
        
        self.m_choice_layout_cmd.Clear()
        self.m_choice_layout_cmd.AppendItems(G_CMDS)
        self.m_choice_layout_cmd.SetSelection(G_CMDS.index(g.prog))
        

class MF(MainFrame):
    
    is_data_changed = False
    file_path = None
    
    def __init__(self, parent=None):
        MainFrame.__init__(self, parent)
        
        # Set icon of buttons. (Cause of the resource path problem in pyinstaller~~~)
        for btn_name in ['new', 'open', 'save', 'export', 'script', 'add', 'minus', 'graphsetting']:
            set_s = 'self.m_bpButton_%s.SetBitmap( wx.Bitmap( resource_path("resource/icon/%s.png"), wx.BITMAP_TYPE_ANY ) )' 
            eval(set_s%(btn_name,btn_name))
            set_s = 'self.m_bpButton_%s.SetBitmapHover( wx.Bitmap( resource_path("resource/icon/%s-highlight.png"), wx.BITMAP_TYPE_ANY ) )' 
            eval(set_s%(btn_name, btn_name))
        
        # Set icon.
        self.SetIcon(wx.Icon(resource_path('resource/icon/DE.ico'), wx.BITMAP_TYPE_ICO))    
        self.colorDB = wx.ColourDatabase()
    
        ### Init some icon in m_tree.
        iList = wx.ImageList(16,16)
        self.img_dict = {}
        for icon_name in ['node-color', 'node-gray', 'edge-color', \
                          'edge-gray', 'graph-color', 'graph-gray', \
                          'graph-expand']:
            img = wx.EmptyBitmap(16,16)
            fn = resource_path('resource/icon/%s.png'%icon_name)
            img.LoadFile(fn, wx.BITMAP_TYPE_PNG)
            img_idx = iList.Add(img)
            icon_key = tuple(icon_name.split('-'))
            self.img_dict[icon_key] = img_idx
        
        self.m_tree.AssignImageList(iList)
        
        ### Init some image list used in pg. --------------------------------------
        self.image_list = {}
        # Load colorscheme.
        img_list = [ get_image_resource(None, 'colorscheme', cs) for cs in AttrsDef.E_COLORSCHEME ]
        self.image_list['colorscheme'] = normalize_imglist(img_list)
        
        # Load node shape.
        img_list = [ get_image_resource('node', 'shape', ns) for  ns in AttrsDef.E_SHAPE ]
        self.image_list['node_shape'] = normalize_imglist(img_list)
        
        # Load arrow style.
        img_list = [ get_image_resource('edge', 'arrowhead', es) for  es in AttrsDef.E_ARROWTYPE ]
        self.image_list['arrow_style'] = normalize_imglist(img_list)  
                        
        ### Init graph. -----------------------------------------------------------
        self.update_graph( ExtGraph.ExtGraph(template_file=resource_path('resource/help/hotkey.dot')) )                        
        
        ### Register hotkey.
        self.accel_tb = wx.AcceleratorTable([(wx.ACCEL_CTRL, ord('n'), self.m_bpButton_new.GetId()),
                                             (wx.ACCEL_CTRL, ord('o'), self.m_bpButton_open.GetId()),
                                             (wx.ACCEL_CTRL, ord('s'), self.m_bpButton_save.GetId()),
                                             (wx.ACCEL_CTRL|wx.ACCEL_SHIFT, ord('s'), self.m_button_save_as.GetId()),
                                             (wx.ACCEL_ALT, ord('s'), self.m_bpButton_script.GetId()),
                                             (wx.ACCEL_CTRL, wx.WXK_RETURN, self.m_bpButton_script.GetId()),
                                             (wx.ACCEL_ALT, wx.WXK_RETURN, self.m_bpButton_script.GetId()),
                                             (wx.ACCEL_CTRL, ord('e'), self.m_bpButton_export.GetId()),
                                             (wx.ACCEL_ALT, ord('a'), self.m_bpButton_add.GetId()), 
                                             (wx.ACCEL_ALT, ord('d'), self.m_bpButton_minus.GetId()),
                                             (wx.ACCEL_ALT, ord('g'), self.m_bpButton_graphsetting.GetId()),
                                             ])
        self.SetAcceleratorTable(self.accel_tb)

        ### Bind events.
        self.m_panel_paint.Bind(wx.EVT_ERASE_BACKGROUND, self.onEraseBackground)
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.m_pgManager1.Bind(wxpg.EVT_PG_SELECTED, self.onPGActive)
        
        return
    
    def __spread_tree(self, rootid):
        '''A  recursive function to add all data from graph into m_tree_ctrl.'''
        
        _, graph = self.m_tree.GetItemPyData(rootid)
        
        ### Add wildcard nodes.
        for n in ['node', 'edge']:
            n_id = self.m_tree.AppendItem(rootid, n)
            n_data = self.data_graph.EG_get_node_by_name(n, root_graph=graph)
            self.m_tree.SetItemPyData(n_id, ('node',  n_data))
            self.m_tree.SetItemImage(n_id, self.img_dict[(n, 'gray')])
        
        ### Load nodes.
        for n in graph.get_nodes():
            n_name = remove_double_quote( n.get_name() )
            if n_name.lower() in ['node', 'edge']: ### Skip the wildcard node.
                continue
            
            n_id = self.m_tree.AppendItem(rootid, n_name.decode('utf8'))
            self.m_tree.SetItemPyData(n_id, ('node', n))
            self.m_tree.SetItemImage(n_id, self.img_dict[('node', 'color')])
            
        
        ### Load edges.
        for e in graph.get_edges():
            n1 = remove_double_quote( e.get_source().decode('utf8') )
            n2 = remove_double_quote( e.get_destination().decode('utf8') )
            n_id = self.m_tree.AppendItem(rootid, "%s -> %s"%(n1,n2))
            self.m_tree.SetItemPyData(n_id, ('edge', e))
            self.m_tree.SetItemImage(n_id, self.img_dict[('edge', 'color')])
        
        ### Load subgraphs.
        for sg in graph.get_subgraphs():
            sg_name = remove_double_quote( sg.get_name().decode('utf8') )
            n_id = self.m_tree.AppendItem(rootid, sg_name)
            self.m_tree.SetItemPyData(n_id, ('graph', sg))
            self.m_tree.SetItemImage(n_id, self.img_dict[('graph', 'color')])
            self.__spread_tree(n_id)
        
        return
    
    def update_graph(self, graph=None):
        '''Updata data graph and then refresh the whole UI. IF graph == None, just refresh the preview.'''
        
        if not (graph is None):
            
            self.data_graph = ExtGraph.ExtGraph(obj_dict=graph.obj_dict)
            
            self.m_tree.DeleteAllItems()
            self.m_pgManager1.Clear()
                    
            ### Insert wildcard item at 1st.
            g_name = remove_double_quote(self.data_graph.get_name().decode('utf8'))
            root = self.m_tree.AddRoot(g_name, 1)
            self.m_tree.SetItemPyData(root, ('graph', self.data_graph))
            self.m_tree.SetItemImage(root, self.img_dict[('graph', 'color')])
            
            self.__spread_tree(root)
            
            self.m_tree.ExpandAll()
            self.m_tree.SelectItem(root)
            
        ### Refresh image panel.
        self.data_graph.refresh_bitmap()
        img = self.data_graph.get_bitmap()

        self.m_panel_paint.SetVirtualSize((img.GetWidth(), \
                                           img.GetHeight()))
        self.m_panel_paint.SetScrollRate(20,20)
        self.m_panel_paint.Refresh()
        
        ### Set window title.
        title = 'Dot Editor'
        if self.file_path is None:
            if self.is_data_changed: title += ' - *'
        else:
            if self.is_data_changed:
                title = 'Dot Editor - *'+self.file_path
            else:
                title = 'Dot Editor - '+self.file_path
                
        self.SetTitle(title)
        
        return
    
    def onEraseBackground(self, event):
        
        dc = wx.ClientDC(self.m_panel_paint)
        dc.Clear()
        
        img = self.data_graph.get_bitmap()    
        x1, y1 = self.m_panel_paint.GetViewStart()
        dc.DrawBitmap(img, -1*20*x1,-1*20*y1)
            
        return
    
    def onGraphSetting(self, event):
        dlg = DGS(self)
        r = dlg.ShowModal()
        if r == wx.ID_OK:
            g_strict = dlg.m_checkBox_strict.GetValue()
            if dlg.m_radioBox_type.GetSelection() == 0:
                g_type = 'digraph'
            else:
                g_type = 'graph'
            
            g_name = dlg.m_textCtrl_name.GetValue().strip().encode('utf8')
            g_prog = dlg.m_choice_layout_cmd.GetStringSelection().strip().encode('utf8')
            
            # Update graph settings.
            g = self.data_graph 
            g.set_strict(g_strict)
            g.set_type(g_type)
            g.set_name(g_name)
            g.prog = g_prog
            
            self.update_graph()
    
    def onAppendItem(self, event):
        
        # Find root in m_tree to append.
        i_id = self.m_tree.GetSelection()
        if not i_id.IsOk():
            wx.MessageBox("Please select a item as the append location.", 
                              style=wx.OK|wx.ICON_EXCLAMATION)
            return
        
        _, i_type, i_graph = self.GetSelectedItem()
        if i_type == 'graph':
            root_id = i_id
            root_graph = i_graph
        else:
            root_id = self.m_tree.GetItemParent(i_id)
            root_graph = self.m_tree.GetItemPyData(root_id)[1]
            
        dlg = DA(self)
        r = dlg.ShowModal()
        a_id = None
        if r == wx.ID_OK:
            
            v = dlg.getAppendValue()
            if v[0] == 'node': ### Add node.
                try:
                    a_data = self.data_graph.EG_append_node(v[1], root_graph=root_graph)
                except:
                    wx.MessageBox('Can\'t add item "%s", maybe the same-named item was existed.'%(v[1].decode('utf8')))
                    return
                
                ### Add item to tree.
                a_id = self.m_tree.AppendItem(root_id, v[1].decode('utf8'))
                self.m_tree.SetItemPyData(a_id, ('node', a_data))
                self.m_tree.SetItemImage(a_id, self.img_dict[('node', 'color')])
            elif v[0] == 'edge': ### Add edge.
                n, n1 = v[1]
                try:
                    a_data = self.data_graph.EG_append_edge((n,n1), root_graph=root_graph)
                except:
                    wx.MessageBox('Can\'t add edge "%s -> %s", maybe the edge was existed.'%(n.decode('utf8'),n1.decode('utf8')))
                    return
                ### Add item to tree.
                a_id = self.m_tree.AppendItem(root_id, n.decode('utf8')+' -> '+n1.decode('utf8'))
                self.m_tree.SetItemPyData(a_id, ('edge', a_data))
                self.m_tree.SetItemImage(a_id, self.img_dict[('edge', 'color')])
            else: ### Add subgraph.
                if 1:
                #try:
                    a_data = self.data_graph.EG_append_subgraph(v[1], root_graph=root_graph)
                #except:
                #    wx.MessageBox('Can\'t add item "%s", maybe the same-named subgraph was existed.'%(v[1].decode('utf8')))
                #    return
                ### Add subgraph root to tree.
                a_id = self.m_tree.AppendItem(root_id, v[1].decode('utf8'))
                self.m_tree.SetItemPyData(a_id, ('graph', a_data))
                self.m_tree.SetItemImage(a_id, self.img_dict[('graph', 'color')])
                ### Add wildcard nodes to subgraph.
                for n in ['node', 'edge']:
                    n_id = self.m_tree.AppendItem(a_id, n)
                    n_data = self.data_graph.EG_get_node_by_name(n, root_graph=a_data)
                    self.m_tree.SetItemPyData(n_id, ('node', n_data) )
                    self.m_tree.SetItemImage(n_id, self.img_dict[(n, 'gray')])
                self.m_tree.Expand(a_id)
            
            ### Select the item in tree.
            if not a_id is None:
                self.m_tree.SelectItem(a_id, True)
            
            self.is_data_changed = True
            self.update_graph()
            
        dlg.Destroy()
        return
    
    def onDeleteItem(self, event):
        
        # Skip the root.
        selected_id = self.m_tree.GetSelection()
        if not selected_id.IsOk():
            return 
        if selected_id == self.m_tree.GetRootItem():
            return

        # Warning when delete NOT empty subgraph.
        if self.m_tree.GetChildrenCount(selected_id) > 0:
            md = wx.MessageDialog(self, 
                                  "The selected subgraph not EMPTY, to delete it should "+\
                                  "lead to DATA LOST, continue anyway?",
                                  caption="Confirm to delete", 
                                  style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                  )
            if md.ShowModal() != wx.ID_YES:
                return

        # If no item selected.
        if self.GetSelectedItem() is None:
            return
                
        
        i_name, i_type, _ = self.GetSelectedItem()
        ### Skip wildcard.
        if i_name in ['node', 'edge']:   
            return
        
        # Get root of selected item.
        r_id = self.m_tree.GetItemParent(selected_id)
        root_graph = self.m_tree.GetItemPyData(r_id)[1]
            
        if i_type == 'node':      ### Remove node from graph.
            self.data_graph.EG_remove_node(i_name, root_graph=root_graph)
        elif i_type == 'edge':    ### Remove edge.
            n1, n2 = i_name.split('->')
            self.data_graph.EG_remove_edge((n1,n2), root_graph=root_graph)
        else:                            ### Remove subgraph. 
            self.data_graph.EG_remove_subgraph(i_name, root_graph=root_graph)
            
        ### Delete from listctrl and clear pg panel.
        self.m_tree.Delete(selected_id)
        self.m_pgManager1.Clear()
        
        ### Fill pg panel.
        self.onItemSelected(None)
        
        # Update graph and UI.
        self.is_data_changed = True
        self.update_graph()
        
        return

    def GetSelectedItem(self):
                
        i = self.m_tree.GetSelection()
        if not i.IsOk:
            return None
        
        i_name = self.m_tree.GetItemText(i).strip()
        i_type, item = self.m_tree.GetItemPyData(i)
    
        return i_name, i_type, item

    def onItemSelected(self, event):

        # If no item selected.
        selected_id = self.m_tree.GetSelection()
        if not selected_id.IsOk():
            return 

        i_name, i_type, item = self.GetSelectedItem()
        
        # Change the title of pg.
        _tail = ''
        if i_name in ['node', 'edge']: ### Change the wildcard item's type.
            i_type = i_name
            _tail = '(wildcard)'
        if selected_id == self.m_tree.GetRootItem():
            _tail = '(global graph)'
        pg_title = i_type.capitalize() + ' Properties'+_tail

        self.m_staticText_pg.SetLabelText(pg_title)

        
        ### Read attrs from data_graph.
        data_attrs = {}
        if not item is None:
            data_attrs = item.get_attributes()

        ### Build PGManager. 
        pm = self.m_pgManager1
        pm.Clear()
        pm.AddPage() ### Very important!!! No-page would cause some strange thing happened.
        
        # Get attrs structure of the graph item.
        cates, _, attrs_dict = AttrsDef.get_dot_attr_structure(i_type)
        
        # Append pg items.
        for _c in cates:
            
            cat = wxpg.PropertyCategory(_c)
            pm.Append(cat)
            
            g_dict = attrs_dict[_c]
            groups = g_dict.keys(); # groups.sort()
            for _g in groups:
                a_list = g_dict[_g]
                if not  _g is None:
                    g_attr = wxpg.StringProperty(_g, value='<composed>') ### Magic string to compose child value.
                    g_attr.Enable(False)
                    g_attr.SetHelpString('attributes group of "%s", click left plus to expand.'%_g)
                    g_id = pm.Append(g_attr)

                for a_name in a_list:
                    
                    pg = ExtPG.buildPG(a_name, i_type)
                    if _g is None:
                        pm.Append(pg)
                    else:
                        pm.AppendIn(g_id, pg)

                    # Set attr value read from data_graph.
                    if a_name in data_attrs.keys():
                        v = data_attrs[a_name]
                        pg.SetValue(remove_double_quote(to_unicode(v).decode('utf8')))
                        # Set background to blue if attr value is different from default.
                        pg.SetBackgroundColour('#ffffc0', -1)
                    
                #if not _g is None:
                #    pm.Collapse(g_attr)
        return
    
    def onPGActive(self, event):

        p = self.m_pgManager1.GetSelectedProperty()
        if (not p): ### No property in event or a group parent.
            return
        
        self.m_staticText1_hint.SetLabelText(p.GetHelpString())        
    
    def onPGChanged(self, event):
        
        _, _, item = self.GetSelectedItem()
        
        if item is None:
            raise Exception("Sth strange happend! Can't find item to store attrs.")
            return
        
        p = event.GetProperty()
        if (not p) or (not p.IsEnabled()): ### No property in event or a group parent.
            return 
        
        ### Get attr from property control.
        key = str(p.GetName()) ### Important!!! Make sure 'key' not unicode.
        if key.find('.') > 0: ### If child of a group.
            key = key.split('.')[-1]

        v = p.GetValue()
        if isinstance(v, basestring):
            v = v.strip().encode('utf8')
        elif isinstance(v, types.BooleanType):
            v = str(v).lower()
        else:
            v = str(v)

        ### Update attr.
        uv = to_unicode(v); udv = to_unicode(p.GetDefaultValue())
        if uv == '' or uv == udv:
            try:
                del item.get_attributes()[key]
            except:
                pass
            # Restore the display value to default.
            p.SetValue(p.GetDefaultValue())
            v = p.GetDefaultValue()
        else:
            item.get_attributes()[key] = add_double_quote(v)
                
        ### Change PG background if value is different from default.
        if uv == udv:
            p.SetBackgroundColour(self.m_tree.GetBackgroundColour(), -1)
        else:
            p.SetBackgroundColour('#ffffc0', -1) 
        
        ### Update view.
        self.is_data_changed = True
        self.update_graph()
        
        return
                    
    def onNewGraph(self, event):
        
        if self.is_data_changed:
            md = wx.MessageDialog(self, 
                                  "Current Graph not save yet, create a new graph "+\
                                   "should lead to DATA LOST, continue anyway?",
                                   caption="Confirm to open", 
                                   style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                   )
            if md.ShowModal() != wx.ID_YES:
                return
        
        self.update_graph( ExtGraph.ExtGraph('G') )
        self.is_data_changed = False
            
        return
    
    def onOpenGraph(self, event):
        
        if self.is_data_changed:
            md = wx.MessageDialog(self, 
                                  "Current Graph not save yet, open another graph "+\
                                   "should lead to DATA LOST, continue anyway?",
                                   caption="Confirm to create new",
                                   style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                   )
            if md.ShowModal() != wx.ID_YES:
                return
            
        fd = wx.FileDialog(self, "Open Dot File", "", "", 
                           "Graphviz Dot Script (*.*)|*.*", 
                           wx.OPEN|wx.FD_FILE_MUST_EXIST)
        if fd.ShowModal() == wx.ID_OK:
            fp = fd.GetPath()
        else:
            return ### User canceled

        fd.Destroy()
                
        ### Load graph from fp.
        try:
            g = ExtParser.parse_file(fp)

            self.file_path = fp
            self.is_data_changed = False
            self.update_graph(g)

        except ExtParser.ParseException, _:
            pass
        
        return
        
    
    def onSaveGraph(self, event):
        
        if self.file_path is None:
            fd = wx.FileDialog(self, "Save Dot File", "", "", 
                               "Dot Files (*.*)|*.*", wx.SAVE|wx.FD_SAVE)
            if fd.ShowModal() == wx.ID_OK:
                fp = fd.GetPath()
            else:
                return  ### User canceled.
            
            ### Confirm to overwrite.
            if os.path.isfile(fp):
                md = wx.MessageDialog(self, 'Be sure to overwrite file "%s"'%fp, 
                                      caption="Confirm to save", 
                                      style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                      )
                if md.ShowModal() != wx.ID_YES:
                    return ### User canceled.

        else:
            fp = self.file_path
        
        ### Backup old file.
        if os.path.isfile(fp):
            pn, fn = os.path.split(fp)
            new_fp = os.path.join(pn, time.strftime('backup_%y%m%d%H%M%S') + '_' + fn)
            shutil.copy(fp, new_fp)
        ### Save graph now.
        self.data_graph.write(fp)
        self.file_path = fp
        self.is_data_changed = False
        self.update_graph()
        
        return
    
    def onSaveAs(self, event):
        
        fd = wx.FileDialog(self, "Save Dot File As", "", "", 
                           "Dot Files (*.*)|*.*", wx.SAVE|wx.FD_SAVE)
        if fd.ShowModal() == wx.ID_OK:
            fp = fd.GetPath()
        else:
            return  ### User canceled.
        
        ### Confirm to overwrite.
        if os.path.isfile(fp):
            md = wx.MessageDialog(self, 'Be sure to overwrite file "%s"'%fp, 
                                  caption="Confirm to save",
                                  style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                  )
            if md.ShowModal() != wx.ID_YES:
                return 
                
        ### Backup old file.
        if os.path.isfile(fp):
            pn, fn = os.path.split(fp)
            new_fp = os.path.join(pn, time.strftime('backup_%y%m%d%H%M%S') + '_' + fn)
            shutil.copy(fp, new_fp)
                    
        ### Save graph now.
        self.data_graph.write(fp)
        self.file_path = fp
        self.is_data_changed = False
        self.update_graph()
    
        return
    
    def onExportImage(self, event):

        fd = wx.FileDialog(self, message="Save Image(PNG) File", \
                           wildcard= G_FORMAT_WILDCARD, \
                           style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT|wx.FD_CHANGE_DIR|wx.FD_CHANGE_DIR, \
                           )
        
        if fd.ShowModal() == wx.ID_OK:
            fp = fd.GetPath()
        else:
            return  ### User canceled.
        
        g_format = fp.split('.')[-1]
        self.data_graph.write(fp, self.data_graph.prog, g_format.lower())
        
        fd.Destroy()

    
    def onViewSource(self, event):
        dlg = DS(self)
        dlg.m_text_script.SetValue(self.data_graph.EG_to_string().decode('utf8'))
        if dlg.ShowModal() == wx.ID_OK:
            self.update_graph(dlg.graph)
            self.is_data_changed = True
        dlg.Destroy()
        
        return
         
    def onClose(self, event):
        if self.is_data_changed:
            md = wx.MessageDialog(self, 
                                  "Current Graph not save yet, close the window "+\
                                   "should lead to DATA LOST, continue anyway?",
                                   caption="Confirm to close",
                                   style=wx.YES_NO|wx.NO_DEFAULT|wx.ICON_EXCLAMATION
                                   )
            if md.ShowModal() != wx.ID_YES:
                return
                    
        wx.Exit()
        
    def onAbout(self, event):
        ad = DialogAbout(self)
        ad.ShowModal()
    
def __check_graphviz():    
    import pydot
    if pydot.find_graphviz() is None:
        return False
    
    return True

if __name__ == "__main__":
    
    app = wx.App(redirect=True, filename="./log.txt")
    #app = wx.App()
    
    if not __check_graphviz():
        wx.MessageBox('Please confirm graphviz installed correct in the computer, '+\
                      'Or put "graphviz/bin" in the "PATH" environment parameter.\n'+\
                      'For more infomation about graphviz please visit: http://www.graphviz.org', 
                      "Can't find graphviz", wx.ICON_ERROR)
        app.Exit()
        
    frame = MF(parent=None)
    frame.Show(True)
    app.MainLoop()
    