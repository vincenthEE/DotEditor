# coding=utf8
'''
Copyleft (L) 2015 Vincent.H <forever.h@gmail.com>

This module define all attributes of Graph/Node/Edge in dot language.
'''

###
### Node attrs define.
### 

from DEUtils import resource_path

E_COLORSCHEME = ['x11', 'svg']
# Append Brewer-Color-Scheme.
cs_set = set()
in_f = open(resource_path('resource/color_scheme/colorbrewer.csv'), 'r')
while 1:
    line = in_f.readline()
    if line == '': break
    cb_name = (line.split(',')[0]).split('.')[0]
    cs_set.add(cb_name)
cs_list = list(cs_set)
cs_list.sort()
E_COLORSCHEME.extend(cs_list)

E_IMAGESCALE = ['true','false','width','height','both']
E_LABELLOC = ['c','t','b']

E_SHAPE = ['box', 'polygon', 'ellipse', 'oval', 'circle', 'point', 'egg', 'triangle',
           'plaintext', 'plain', 'diamond', 'trapezium', 'parallelogram', 'house', 
           'pentagon', 'hexagon', 'septagon', 'octagon', 'doublecircle', 'doubleoctagon', 
           'tripleoctagon', 'invtriangle', 'invtrapezium', 'invhouse', 'Mdiamond', 'Msquare', 
           'Mcircle', 'rect', 'rectangle', 'square', 'star', 'none', 'underline', 
           'note', 'tab', 'folder', 'box3d', 'component', 'promoter', 
           'cds', 'terminator', 'utr', 'primersite', 'restrictionsite', 'fivepoverhang', 
           'threepoverhang', 'noverhang', 'assembly', 'signature', 'insulator', 'ribosite', 
           'rnastab', 'proteasesite', 'proteinstab', 'rpromoter', 'rarrow', 'larrow', 'lpromoter']

E_NODE_STYLE = ['solid', 'dashed', 'dotted', 'bold', 'rounded','diagonals', 'filled', 'striped', 'wedged', 'invis']
E_TARGET = ['_blank','_self','_parent','_top']

E_FONTNAME = ['serif', 'sans-serif', 'cursive', 'fantasy', 'monospace']

NODE_ATTRS_DEFINE = [                          
### name,           default_value,  category,   group,          type,        param,          description
    ['color',       'black',        'basic',   'color_attrs',   "color",     None,           'node shape color'                                      ],
    ['colorscheme', 'x11',          'basic',   'color_attrs',   "colorscheme",None,          'scheme for interpreting'                               ],
    ['comment',     None,           'extra',   None,            "string",    None,           'any string(format-dependent)'                          ],
    ['distortion',  0,              'extra',   'shape-param',   "float",     None,           'node distortion for shape=polygon'                     ],
    ['fillcolor',   'lightgrey',    'basic',   'color_attrs',   "color",     None,           'node fill color'                                       ],
    ['fixedsize',   False,          'extra',   None,            "bool",      None,           'label text has no affect on node size'                 ],
    ['fontcolor',   'black',        'basic',   'color_attrs',   "color",     None,           'type face color'                                       ],
    ['fontname',    'Times-Roman',  'basic',   'font',          "enum_edit", E_FONTNAME,     'font family'                                           ],
    ['fontsize',    14,             'basic',   'font',          "int",       None,           'point size of label'                                   ],
    ['group',       None,           'extra',   None,            "string",    None,           'If the end points of an edge belong to the same group,'+\
                                                                                             ' i.e., have the same group attribute, parameters are'+\
                                                                                             ' set to avoid crossings and keep the edges straight.'  ],
    ['height',      .5,             'extra',   'node_size',     "float",     None,           'minimum height in inches'                              ],
    ['width',       .75,            'extra',   'node_size',     "float",     None,           'minimum width in inches'                               ],
    ['id',          None,           'extra',   None,            "string",    None,           'any string(user-defined output object tags)'           ],
    ['image',       None,           'extra',   None,            "img_file",  None,           'image file name'                                       ],
    ['imagescale',  'false',        'extra',   None,            "enum",      E_IMAGESCALE,   'true,width,height,both'                                ],
    ['label',       None,           'basic',   None,            "string",    None,           'any string'                                            ],
    ['labelloc',    'c',            'extra',   None,            "enum",      E_LABELLOC,     'node label vertical alignment(center, top, bottom)'    ],
    ['layer',       None,           'advance', None,            "string",    None,           'all, id or id:id, or a comma-separated list of the former'],
    ['margin',      '0.11,0.55',    'extra',   None,            "string",    None,           'space around label'                                    ],
    ['nojustify',   False,          'extra',   None,            "bool",      None,           'if true, justify to label, not node'                   ],
    ['orientation', 0.0,            'extra',   'shape-param',   "float",     None,           'node rotation angle'                                   ],
    ['penwidth',    1.0,            'basic',   None,            "float",     None,           'width of pen for drawing boundaries, in points'        ],
    ['peripheries', None,           'extra',   'shape-param',   "int",       None,           'number of node boundaries'                             ],
    ['regular',     False,          'extra',   'shape-param',   "bool",      None,           'force polygon to be regular'                           ],
    ['samplepoints',8,              'advance', None,            "int",       None,           'number vertices to convert circle or ellipse'          ],
    ['shape',       'ellipse',      'basic',   None,            "enum_nodeshape",E_SHAPE,    'node shape'                                            ],
    ['sides',       4,              'extra',   'shape-param',   "int",       None,           'number of sides for shape=polygon'                     ],
    ['skew',        0.0,            'extra',   'shape-param',   "float",     None,           'skewing of node for shape=polygon'                     ],
    ['style',       None,           'basic',   None,            "enum_combine",E_NODE_STYLE, 'graphics options.'                                     ],
    ['target',      None,           'extra',   'link',          "enum",      E_TARGET,       'if URL is set, determines browser window for URL'      ],
    ['tooltip',     None,           'extra',   None,            "string",    None,           'tooltip annotation'                                    ],
    ['URL',         None,           'extra',   'link',          "string",    None,           'URL associated with node (format-dependent)'           ],
]

###
### Edge attrs define.
### 
E_ARROWTYPE = ['box', 'crow', 'curve', 'icurve', 'diamond', 
               'dot', 'inv', 'none', 'normal', 'tee', 'vee']

# E_ARROWTYPE = ['normal', 'dot', 'odot', 'none', 'empty', \
#                'diamond', 'ediamond', 'box', 'open', 'vee', \
#                'inv', 'invdot', 'invodot', 'tee', 'invempty',\
#                'odiamond', 'crow', 'obox', 'halfopen', 'circle']

E_DIRECTION = ['forward','back','both','none']
E_PORTPOS   = ['n','ne','e','se','s','sw','w','nw','c','_']
E_EDGE_STYLE = ['solid', 'dashed', 'dotted', 'bold', 'tapered', 'invis']

EDGE_ATTRS_DEFINE = [
### name,           default_value,  category,   group,       type,          param,          description
    ['arrowhead',   'normal',       'basic',    'arrow',     "enum_arrowtype",E_ARROWTYPE,  'style of arrowhead at head end'                        ],
    ['arrowsize',   1.0,            'basic',    'arrow',     "float",       None,           'scaling factor for arrowheads'                         ],
    ['arrowtail',   'normal',       'basic',    'arrow',     "enum_arrowtype",E_ARROWTYPE,  'style of arrowhead at tail end'                        ],
    ['color',       'black',        'basic',    'color_attrs',"color",      None,           'edge stroke color'                                     ],
    ['colorscheme', 'x11',          'basic',    'color_attrs',"colorscheme", None,          'scheme for interpreting color names'                   ],
    ['comment',     None,           'extra',    None,        "string",      None,           'any string(format-dependent)'                          ],
    ['constraint',  True,           'extra',    None,        "bool",        None,           'use edge to affect node ranking'                       ],
    ['decorate',    False,          'extra',    None,        "bool",        None,           'if set, draws a line connecting labels with their edges'],
    ['dir',         'forward',      'basic',    'arrow',     "enum",        E_DIRECTION,    'arrow direction, forward, back, both, or none'         ],
    ['edgeURL',     None,           'extra',    None,        "string",      None,           'URL attached to non-label part of edge'                ],
    ['edgehref',    None,           'extra',    None,        "string",      None,           'synonym for edgeURL'                                   ],
    ['edgetarget',  None,           'advance',  None,        "enum",        E_TARGET,       'if URL is set, determines browser window for URL'      ],
    ['edgetooltip', None,           'advance',  None,        "string",      None,           'tooltip annotation for non-label part of edge'         ],
    ['fontcolor',   'black',        'basic',    'color_attrs', "color",     None,           'type face color'                                       ],
    ['fontname',    'Times-Roman',  'basic',    'font',      "enum_edit",   E_FONTNAME,     'font family'                                           ],
    ['fontsize',    14,             'basic',    'font',      "int",         None,           'point size of label'                                   ],
    ['headclip',    True,           'extra',    'head',      "bool",        None,           'if false, edge is not clipped to head node boundary'   ],
    ['headURL',    None,            'extra',    'head',      "string",      None,           'URL attached to head label'                            ],
    ['headhref',    None,           'extra',    'head',      "string",      None,           'synonym for headURL'                                   ],
    ['headlabel',   None,           'extra',    'head',      "string",      None,           'label placed near head of edge'                        ],
    ['headport',    'c',            'extra',    'head',      "enum",        E_PORTPOS,      'Indicates where on the head node to attach the head of the edge'],
    ['headtarget',  None,           'extra',    'head',      "string",      E_TARGET,       'if headURL is set, determines browser window for URL'  ],
    ['headtooltip', None,           'extra',    'head',      "string",      None,           'tooltip annotation near head of edge'                  ],
    ['href',        None,           'extra',    None,        "string",      None,           'alias for URL'                                         ],
    ['id',          None,           'extra',    None,        "string",      None,           'any string(user-defined output object tags)'           ],
    ['label',       None,           'basic',    None,        "string",      None,           'edge label'                                            ],
    ['labelangle',  -25.0,          'extra',    'label_attr',"float",       None,           'angle in degrees which head or tail label is rotated off edge'],
    ['labeldistance', 1.0,          'extra',    'label_attr',"float",       None,           'scaling factor for distance of head or tail label from node'],
    ['labelfloat',  False,          'extra',    'label_attr',"bool",        None,           'lessen constraints on edge label placement'            ],
    ['labelfontcolor', 'black',     'extra',    'color_attrs',"color",      None,           'type face color for head and tail labels'              ],
    ['labelfontname',  'Times-Roman', 'extra',  'label_attr',"enum_edit",   E_FONTNAME,     'font family for head and tail labels'                  ],
    ['labelfontsize',  14,          'extra',    'label_attr',"int",         None,           'point size for head and tail labels'                   ],
    ['labelhref',   None,           'extra',    'label_attr',"string",      None,           'synonym for labelURL'                                  ],
    ['labelURL',    None,           'extra',    'label_attr',"string",      None,           'URL for label, overrides edge URL'                     ],
    ['labeltarget', None,           'extra',    'label_attr',"enum",        E_TARGET,       'if URL or labelURL is set, determines browser window for URL'],
    ['labeltooltip',None,           'extra',    'label_attr',"string",      None,           'tooltip annotation near label'                         ],
    ['layer',       None,           'advance',  None,        "string",      None,           'all, id or id:id, or a comma-separated list of the former'],
    ['lhead',       None,           'advance',  None,        "string",      None,           'name of cluster to use as head of edge'                ],
    ['ltail',       None,           'advance',  None,        "string",      None,           'name of cluster to use as tail of edge'                ],
    ['minlen',      1,              'advance',  None,        "int",         None,           'minimum rank distance between head and tail'           ],
    ['penwidth',    1.0,            'basic',    None,        "float",       None,           'width of pen for drawing edge stroke, in points'       ],
    ['samehead',    None,           'advance',  None,        "string",      None,           'tag for head node; edge heads with the same tag are merged onto the same port'],
    ['sametail',    None,           'advance',  None,        "string",      None,           'tag for tail node; edge tails with the same tag are merged onto the same port'],
    ['style',       None,           'basic',    None,        "enum_combine",E_EDGE_STYLE,   'graphics options, e.g. bold, dotted, filled'           ],
    ['tailclip',    True,           'extra',    'tail',      "bool",        None,           'if false, edge is not clipped to tail node boundary'   ],
    ['tailURL',     None,           'extra',    'tail',      "string",      None,           'URL attached to tail label'                            ],
    ['tailhref',    None,           'extra',    'tail',      "string",      None,           'synonym for tailURL'                                   ],
    ['taillabel',   None,           'extra',    'tail',      "string",      None,           'label placed near tail of edge'                        ],
    ['tailport',    'c',            'extra',    'tail',      "enum",        E_PORTPOS,      'Indicates where on the tail node to attach the tail of the edge'],
    ['tailtarget',  None,           'extra',    'tail',      "string",      E_TARGET,       'if tailURL is set, determines browser window for URL'  ],
    ['tailtooltip', None,           'extra',    'tail',      "string",      None,           'tooltip annotation near tail of edge'                  ],
    ['target',      None,           'advance',  None,        "enum_edit",   E_TARGET,       'if URL is set, determines browser window for URL'      ],
    ['tooltip',     None,           'extra',    None,        "string",      None,           'tooltip annotation'                                    ],
    ['weight',      1,              'basic',    None,        "int",         None,           'integer cost of stretching an edge'                    ],    
    ['URL',         None,           'extra',    None,        'string',      None,           'URL associated with edge (format-dependent)'           ],
]

###
### Graph attrs define.
###  
E_CLUSTERRANK = ['local','global','none']
E_LABELJUST = ['c','l','r']
E_ORDERING = ['out', 'in']
E_ORIENTATION = ['portrait', 'landscape']
E_OUTPUTORDER = ['breadthfirst', 'nodesfirst', 'edgesfirst']
E_RANK = ['same', 'min', 'source', 'max', 'sink']
E_RANKDIR = ['TB', 'LR']
E_RATIO = ['fill', 'compress', 'expand', 'auto']
E_SPLINES= ['none', 'line', 'true', 'false', 'polyline','curved','ortho', 'compound']
E_GRAPH_STYLE = ['solid', 'dashed', 'dotted', 'bold', 'rounded', 'filled', 'striped', 'invis']

GRAPH_ATTRS_DEFINE = [
### name,           default_value,  category,   group,      type,           param,          description
    ['bgcolor',     '#ffffff00',    'basic',    'color_attrs','color',      None,           'background color for drawing, plus initial fill color' ],
    ['center',      False,          'basic',    None,       'bool',         None,           'center drawing on page'                                ],                  
    ['clusterrank', 'local',        'extra',    'cluster',  'enum',         E_CLUSTERRANK,  'mode used for handling clusters.'                      ],
    ['color',       'black',        'extra',    'color_attrs','color',      None,           'for clusters, outline color, and fill color if "fillcolor" not defined'],
    ['colorscheme', 'x11',          'extra',    'color_attrs','colorscheme',None,           'scheme for interpreting color names'                   ],
    ['comment',     None,           'extra',    None,       'string',       None,           'any string (format-dependent)'                         ],
    ['compound',    False,          'extra',    None,       'bool',         None,           'allow edges between clusters'                          ],
    ['concentrate', False,          'extra',    None,       'bool',         None,           'enables edge concentrators'                            ],
    ['dpi',         96,             'extra',    None,       'int',          None,           'dots per inch for image output'                        ],
    ['fillcolor',   'black',        'extra',    'color_attrs','color',      None,           'cluster fill color'                                    ],
    ['fontcolor',   'black',        'basic',    'color_attrs','color',      None,           'type face color'                                       ],
    ['fontname',    'Times-Roman',  'basic',    'graph_font','enum_edit',   E_FONTNAME,     'font family'                                           ],
    ['fontnames',   None,           'advance',  None,       'string',       None,           'svg,ps,gd(SVG only)'                                   ],
    ['fontpath',    None,           'advance',  None,       'string',       None,           'list of directories to search for fonts'               ],
    ['fontsize',    None,           'basic',    'graph_font','int',         None,           'point size of label'                                   ],
    ['id',          None,           'extra',    None,       'string',       None,           'any string (user-defineed output object tags'          ],
    ['label',       None,           'basic',    None,       'string',       None,           'any string'                                            ],
    ['labeljust',   'c',            'extra',    'cluster',  'enum',         E_LABELJUST,    '"l" and "r" for left- and right-justified cluster labels, respectively'],
    ['labelloc',    't',            'extra',    'cluster',  'enum',         E_LABELLOC,     '"t" and "b" for top- and bottom-justified cluster labels, respectively'],
    ['landscape',   False,          'extra',    None,       'bool',         None,           'if true, means orientation=landscape'                  ],
    ['layers',      None,           'advance',  None,       'string',       None,           'id:id:id...'                                           ],
    ['layersep',    ':',            'advance',  None,       'string',       None,           'specifies separator character to split layers'         ],
    ['margin',      0.5,            'extra',    None,       'float',        None,           'margin included in page, inches'                       ],
    ['mindist',     1.0,            'extra',    None,       'float',        None,           'minimum separation between all nodes (not dot)'        ],
    ['nodesep',     0.25,           'extra',    None,       'float',        None,           'separation between nodes, in inches.'                  ],
    ['nojustify',   False,          'extra',    None,       'bool',         None,           'if true, justify to label, not graph'                  ],
    ['ordering',    None,           'extra',    None,       'enum_edit',    E_ORDERING,     'if "out" out edge order is preserved'                  ],
    ['orientation', 'portrait',     'extra',    None,       'enum',         E_ORIENTATION,  'if rotate is not used and the value is "landscape", use landscape orientation'],
    ['outputorder', 'breadthfirst', 'extra',    None,       'enum',         E_OUTPUTORDER,  'specify order in which nodes and edges are drawn.'     ],
    ['page',        None,           'advance',  None,       'string',       None,           'unit of pagination, e.g. "8.5,11"'                     ],
    ['pagedir',     'BL',           'advance',  None,       'string',       None,           'traversal order of pages',                             ],
    ['pencolor',    'black',        'extra',    'cluster',  'color',        None,           'color for drawing cluster boundaries'                  ],
    ['penwidth',    1.0,            'extra',    'cluster',  'float',        None,           'width of pen for drawing boundaries, in points'        ],
    ['peripheries', 1,              'extra',    'cluster',  'enum',         ['0','1'],      'number of cluster boundaries'                          ],
    ['rank',        None,           'advance',  'rank_attr','enum',         E_RANK,         'rank constraints on the nodes in a subgraph.'          ],
    ['rankdir',     'TB',           'advance',  'rank_attr','enum',         E_RANKDIR,      'LR (left to right) or TB (top to bottom)'              ],
    ['ranksep',     0.75,           'advance',  'rank_attr','float',        None,           'separation between ranks, in inches'                   ],
    ['ratio',       None,           'extra',    None,       'enum_edit',    E_RATIO,        'sets the aspect ratio (drawing height/drawing width) for the drawing.'],
    ['rotate',      0,              'basic',    None,       'enum',         ['0','90'],     'if 90, set orientation to landscape'                   ],
    ['samplepoints',8,              'advance',  None,       'int',          None,           'number of points used to represent ellipses and circles on output.'],
    ['searchsize',  30,             'advance',  None,       'int',          None,           'maximum edges with negative cut values to check when looking for a minimum one during network simplex'],
    ['size',        None,           'advance',  None,       'string',       None,           'maximum drawing size, in inches'                       ],
    ['splines',     None,           'extra',    None,       'enum',         E_SPLINES,      'draw edges as splines, polylines,lines'                ],
    ['style',       None,           'basic',    None,       'enum_combine', E_GRAPH_STYLE,  'graphics options, e.g. filled for clusters'            ],
    ['stylesheet',  None,           'advance',  None,       'string',       None,           'pathname or URL to XML style sheet for SVG'            ],
    ['target',      None,           'advance',  None,       'enum_edit',    E_TARGET,       'if URL is set, determines browser window for URL'      ],
    ['tooltip',     None,           'extra',    'cluster',  'string',       None,           'tooltipannotation for cluster'                         ],
    ['truecolor',   None,           'advance',  None,       'bool',         None,           'if set, force 24 bit or indexed color in image output' ],
    ['viewport',    None,           'advance',  None,       'string',       None,           'clipping window on output'                             ],
    ['URL',         None,           'extra',    None,       'string',       None,           'URL associated with graph (format-dependent)'          ],
]

###
### Some util functions to access information of attributes.
###
def get_dot_attr(attr_name, g_type):
    '''Get the attribute infomation by name and g_type. g_type should in ['node', 'group', 'graph']. Return a dict include all info.'''
    
    if g_type not in ['node', 'edge', 'graph']: raise Exception('g_type "%s" not valid'%g_type)
    AD = eval(g_type.upper()+'_ATTRS_DEFINE')
    
    result = {}
    for line in AD:
        a_name = line[0]
        if a_name == attr_name:
              
            result['name']              = line[0]
            result['default_value']     = line[1]
            result['category']          = line[2]
            result['group']             = line[3]
            result['type']              = line[4]
            result['param']             = line[5]
            result['description']       = line[6]
            
    if len(result) == 0:
        raise KeyError("Can't find the attr_name '%s' in '%s' attributes define."%(attr_name, g_type))
    
    return result

def get_dot_attr_structure(g_type):
    '''
    Put attributs structure in a dict like:{'cate1':{None:[attr_name1, attr_name2, ...], 
                                                     'group1':[attr_name3, attr_name4], ...},
                                            'cate2':{...},
                                            ...}
    Pay attention the 'None' group inclue all attr names not in any group.
    return value is tuple(category_list, group_list, attrs_structure_dict).
    '''
    
    if g_type not in ['node', 'edge', 'graph']: raise Exception('g_type "%s" not valid'%g_type)
    AD = eval(g_type.upper()+'_ATTRS_DEFINE')

    ### List all category and groups, and attrs in each group.
    cates = []; groups = []; cate_dict={}; group_dict = {}
    for line in AD:
        ### Build cates list.
        c = line[2]
        if c not in cates: cates.append(c)
        
        ### Init cate_dict key place.
        if not cate_dict.has_key(c): cate_dict[c] = []
        
        ### Build groups list.
        g = line[3]
        if (not g is None) and (g not in groups): groups.append(g)
        
        ### Put g(if not None) into the FIRST category has the group name.
        if not g is None:
            is_g_in_any_category = False
            for _cate in cate_dict:
                if g in cate_dict[_cate]:
                    is_g_in_any_category = True
                    break
            if not is_g_in_any_category:
                cate_dict[c].append(g)

        ### Build group_dict.
        a_name = line[0]
        # Create a group "cate_name_None" to store that attrs without group.
        if g is None: g = c+"_None" 
        if not group_dict.has_key(g):
            group_dict[g] = []
        group_dict[g].append(a_name)

    ### Build tree structure as result.
    result = {}
    for c in cates:
        result[c] = {}
        for g in cate_dict[c]:
            result[c][g] = group_dict[g]
        ### Don't forget the 'cate_name_None' group.
        result[c][None] = group_dict[c+"_None"]
        
    return cates, groups, result

def __test_get_structure(g_type):

    c,g,s = get_dot_attr_structure(g_type)
    c_count = len(c); g_count = len(g)
    a_count = 0
    for c in s:
        _c = s[c]
        for g in _c:
            a_count += len(_c[g])
    
    return

if __name__ == '__main__':
    
    __test_get_structure('node')
    __test_get_structure('edge')

