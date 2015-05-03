a = Analysis(['DotEditor.py'])
pyz = PYZ(a.pure)
res_tree = Tree('./resource', prefix='resource')
a.datas += [('GraphTemplate.dot', './GraphTemplate.dot', 'DATA')]
a.datas += res_tree
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas, name='DotEditor.exe', console=0, icon='resource/icon/DE.ico')
#dist = COLLECT(exe, a.binaries, res_tree, name="dist")
