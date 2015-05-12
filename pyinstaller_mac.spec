# -*- mode: python -*-
#
# Copyright (R) 2015 Vincent.H <forever.h@gmail.com>
#
# Published under Apache 2.0 License (http://www.apache.org/licenses/LICENSE-2.0.html).
#-------------------------------------------------------------------------------------

a = Analysis(['DotEditor.py'])
pyz = PYZ(a.pure)

res_tree = Tree('./resource', prefix='resource')
a.datas += [('GraphTemplate.dot', './GraphTemplate.dot', 'DATA')]
a.datas += res_tree

exe = EXE(pyz, 
		  a.scripts, 
		  exclude_binaries=True,
		  name='DotEditor',
		  debug=True, 
		  strip=None,
		  console=False)

coll = COLLECT(exe, 
			   a.binaries,
			   a.zipfiles,
			   a.datas,
			   name='DotEditor')
			   
app = BUNDLE(coll,
			 name='DotEditor.app',
			 icon='./resource/icon/DE.icns')