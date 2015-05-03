# -*- mode: python -*-
a = Analysis(['DotEditor.py'],
             pathex=['D:\\Users\\wxm\\workspace_pydev\\DotEditor'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='DotEditor.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
