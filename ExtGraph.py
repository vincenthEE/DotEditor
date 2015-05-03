# coding=utf8
'''
Copyright (R) 2015 Vincent.H <forever.h@gmail.com>

Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
-------------------------------------------------------------------------------------

This module define the extended functions of graph data. 

The core class base on the PyDot project. (https://github.com/erocarrera/pydot)
'''

import pydot
import wx, sys
import ExtParser
from DEUtils import to_unicode, add_double_quote,\
    remove_double_quote
import tempfile
import DEUtils


TEMP_IMG_FILE = tempfile.gettempdir()+'/.tempimg'

TEMPLATE_DOT = DEUtils.resource_path('GraphTemplate.dot')
INIT_SCRIPT = '''
digraph G {
    rankdir=LR;
    node [fontname="serif"];
    edge [fontname="serif"];
}
'''

INIT_SCRIPT_SUBGRAPH = '''
graph G {
    node [comment="subgraph node wildcard"];
    edge [comment="subgraph edge wildcard"];
}
'''

class ExtGraph(pydot.Dot):
    
    __bitmap = None
    __historys = []
    __history_point = -1
    
    def __init__(self, graph_name='G', obj_dict=None, template_file=None):
        pydot.Dot.__init__(self, graph_name=graph_name, obj_dict=obj_dict)
        
        # If create empty new graph...
        if (obj_dict is None):

            ### Some default setting.
            try:
                if template_file is None:
                    g = ExtParser.parse_file(TEMPLATE_DOT)
                else:
                    g = ExtParser.parse_file(template_file)
            except:
                g = ExtParser.parse_string(INIT_SCRIPT)
                
            self.obj_dict = g.obj_dict
            
        # If create graph from parsing program...
        else:
            # Now check if wildcard nodes existed in every graph and subgraph.
            self.__check_wildcard_existed()
            
        ### Important!!! To make "pydot.Graph.toString()" working correct.
        self.set_parent_graph(self)
        ### -------------------------------------------------------------
        
        self.refresh_bitmap()
        
        return
    
    def __check_wildcard_existed(self, root_graph=None):
        '''Check if wildcard nodes existed in root_graph and all subgraph.'''
        if root_graph is None:
            root_graph = self
        
        for n_name in ['node', 'edge']:
            node = self.EG_get_node_by_name(n_name, root_graph)
            if node is None:
                n = pydot.Node(n_name)
                n.set_comment('Wildcard node added automatic in EG.')
                root_graph.add_node(n)
                
            ### Anyway, push the wildcard node to the front of all other nodes.
            if n_name == 'node':
                root_graph.obj_dict['nodes']['node'][0]['sequence'] = 0.5
            else:
                root_graph.obj_dict['nodes']['edge'][0]['sequence'] = 0
            ### -------------------------------------------------------------
        
        sgs  = root_graph.get_subgraphs()
        for sg in sgs:
            self.__check_wildcard_existed(sg)
        
        return
    
    def create_empty_subgraph(self, name):
        sg = pydot.Subgraph()
        sg.set_name(name)
        
        g = ExtParser.parse_string(INIT_SCRIPT_SUBGRAPH)
        sg.obj_dict['nodes'] = g.obj_dict['nodes']
        
        return sg
    
    def get_bitmap(self):
        "Get the graph image in wx.Bitmap format."
        
        if self.__bitmap is None: ### Generate a image and load it now.
            self.refresh_bitmap()
            
        return self.__bitmap
    
    def refresh_bitmap(self):

        self.write(TEMP_IMG_FILE, self.prog, 'png')
        self.__bitmap = wx.EmptyBitmap(0,0)
        self.__bitmap.LoadFile(TEMP_IMG_FILE, wx.BITMAP_TYPE_PNG)

        return
    
    def EG_append_node(self, nodename, root_graph=None):
        "Add node to 'root_graph' only by name."
        uname = to_unicode(nodename.strip())
        
        if root_graph is None:
            root_graph = self
        
        # Check unique.
        n = self.EG_get_node_by_name(uname, root_graph=root_graph)
        if not(n is None):
            raise Exception('Unique error. The node with name "%s" was existed in the graph.'%uname)
        
        uname = add_double_quote(uname)
        
        n = pydot.Node(uname)
        root_graph.add_node(n)
        
        self.__check_wildcard_existed()
        
        self.refresh_bitmap()
        
        return n

    def EG_append_edge(self, name_pair, root_graph=None):
        "Add edge to 'root_graph' only by node-names of the edge."
        
        nameA = to_unicode(name_pair[0].strip())
        nameB = to_unicode(name_pair[1].strip())
        
        if root_graph is None:
            root_graph = self
        
        ### Check unique.
        e = self.EG_get_edge_by_names((nameA, nameB), root_graph=root_graph)
        if not(e is None):
            raise Exception('Unique error. The edge with same names was existed in the graph.')
        
        nameA = add_double_quote(nameA)
        nameB = add_double_quote(nameB)
        
        e = pydot.Edge(src=nameA, dst=nameB)
        
        root_graph.add_edge(e)
        
        self.__check_wildcard_existed()
        
        self.refresh_bitmap()
        
        return e

    def EG_append_subgraph(self, graphname, root_graph=None):
        "Add node to 'root_graph' only by name."
        uname = to_unicode(graphname.strip())
        
        if root_graph is None:
            root_graph = self
        
        # Check unique.
        n = self.EG_get_subgraph_by_name(uname)
        if not(n is None):
            raise Exception('Unique error. The subgraph with name "%s" was existed in the graph.'%uname)
        
        uname = add_double_quote(uname)
        
        sg = self.create_empty_subgraph(uname)
        root_graph.add_subgraph(sg)
        
        self.refresh_bitmap()
        
        return sg
    
    def EG_get_node_by_name(self, name, root_graph=None):
        '''Get node by name. Return None if not found.'''
        
        if root_graph is None:
            root_graph = self
        
        n_name = remove_double_quote(name)
        
        nodes = root_graph.get_nodes()
        r = None
        for n in nodes:
            _name = remove_double_quote( n.get_name() )
            if _name == n_name:
                r = n
                break
        
        return r
    
    def EG_get_edge_by_names(self, name_pair, root_graph=None):
        '''Get edge by names of source and destination. Return None if not found.'''
        if root_graph is None:
            root_graph = self
        
        nameA = remove_double_quote(name_pair[0])
        nameB = remove_double_quote(name_pair[1])
        
        edges = root_graph.get_edges()
        r = None
        for e in edges:
            n = remove_double_quote( e.get_source() )
            n1 = remove_double_quote( e.get_destination() )
            if ((n == nameA )  
                and (n1 == nameB)):  
                r = e
                break
            
        return r

    def EG_get_subgraph_by_name(self, name, root_graph=None):
        '''Get node by name. Return None if not found.'''
        if root_graph is None:
            root_graph = self
        
        sg_name = remove_double_quote(name)
        
        sgs = root_graph.get_subgraphs()
        r = None
        for sg in sgs:
            _name = remove_double_quote(sg.get_name())
            if _name == sg_name:
                r = sg
                break
        
        return r
    
    def EG_remove_node(self, name, root_graph=None):
        "Remove node from root_graph by name."
        if root_graph is None:
            root_graph = self

        uname = add_double_quote( to_unicode(name) )

        try:
            del root_graph.obj_dict['nodes'][uname]
        except:
            pass
        
        self.refresh_bitmap()
        
        return
    
    def EG_remove_edge(self, name_pair, root_graph=None):
        "Remove edge from root_graph by end points name of the edge."
        if root_graph is None:
            root_graph = self

        nameA = add_double_quote( to_unicode( name_pair[0]) )
        nameB = add_double_quote( to_unicode( name_pair[1]) )

        try:
            del root_graph.obj_dict['edges'][(nameA, nameB)]
        except:
            pass
        
        self.refresh_bitmap()
        
        return
    
    def EG_remove_subgraph(self, name, root_graph=None):
        "Remove subgraph from root_graph by name."
        if root_graph is None:
            root_graph = self

        sg_name = add_double_quote( to_unicode(name) )

        try:
            del root_graph.obj_dict['subgraphs'][sg_name]
        except:
            pass
        
        self.refresh_bitmap()
        
        return
    
    def EG_to_string(self, indent=0, root_graph=None):
        """Returns a string representation of the graph in dot language.
        This version try to make string looking better than to_string().
        """
        idt =  ' '*(4 + indent)
        graph = list()
        
        if root_graph is None:
            root_graph = self
        
        if root_graph != root_graph.get_parent_graph():
            graph.append(' '*indent)
        
        if root_graph.obj_dict.get('strict', None) is not None:
            if root_graph==root_graph.get_parent_graph() and root_graph.obj_dict['strict']:
                graph.append('strict ')
        
        if root_graph.obj_dict['name'] == '':
            graph.append( '{\n' )
        else:
            graph.append( '%s %s {\n' % (root_graph.obj_dict['type'], root_graph.obj_dict['name']) )

        for attr in root_graph.obj_dict['attributes'].keys():
            if root_graph.obj_dict['attributes'].get(attr, None) is not None:
                graph.append( idt+'%s=' % attr )
                val = root_graph.obj_dict['attributes'].get(attr)
                graph.append( pydot.quote_if_necessary(val) )
                graph.append( ';\n' )


        edges_done = set()
        
        edge_obj_dicts = list()
        for e in root_graph.obj_dict['edges'].values():
            edge_obj_dicts.extend(e)
            
        if edge_obj_dicts:
            edge_src_set, edge_dst_set = zip( *[obj['points'] for obj in edge_obj_dicts] )
            edge_src_set, edge_dst_set = set(edge_src_set), set(edge_dst_set)
        else:
            edge_src_set, edge_dst_set = set(), set()
            
        node_obj_dicts = list()
        for e in root_graph.obj_dict['nodes'].values():
            node_obj_dicts.extend(e)

        sgraph_obj_dicts = list()
        for sg in root_graph.obj_dict['subgraphs'].values():
            sgraph_obj_dicts.extend(sg)
        
        obj_list = [ (obj['sequence'], obj) for obj in (edge_obj_dicts + node_obj_dicts + sgraph_obj_dicts) ]
        obj_list.sort()
        
        for _, obj in obj_list:
            if obj['type'] == 'node':
                node = pydot.Node(obj_dict=obj)
                if root_graph.obj_dict.get('suppress_disconnected', False):
                    if (node.get_name() not in edge_src_set and
                        node.get_name() not in edge_dst_set):
                        continue
                    
                graph.append( idt+node.to_string()+'\n' )

            elif obj['type'] == 'edge':
                edge = pydot.Edge(obj_dict=obj)
                if root_graph.obj_dict.get('simplify', False) and edge in edges_done:
                    continue
                
                graph.append( idt+edge.to_string() + '\n' )
                edges_done.add(edge)
                
            else:
                sgraph = pydot.Subgraph(obj_dict=obj)
                sg_str = self.EG_to_string(indent+4, sgraph)
                graph.append( sg_str+'\n' )

        if root_graph != root_graph.get_parent_graph():
            graph.append(' '*indent)
            
        graph.append( '}\n' )
        
        return ''.join(graph)
    
    
    def undo_change(self, step=1):
        "Roll back the change of the graph."
        
        self.refresh_bitmap()
        return
    
    def redo_change(self, step=1):
        "Redo change on the graph."
        
        self.refresh_bitmap()
        return
    
if __name__ == '__main__':

    sd = ExtGraph()
    s = u"中文"
    s1 = s.encode('utf8')

    sd.EG_append_node(s)
    
    sd.EG_append_edge((s,s1))
    
    print sd.to_string()