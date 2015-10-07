# -*- mode: python -*-
a = Analysis(['Main.py'],
             pathex=['/home/alejandro/esperanza'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Main',
          debug=False,
          strip=None,
          upx=True,
          console=True )
