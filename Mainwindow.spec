# -*- mode: python -*-
import sys
sys.setrecursionlimit(9000)


block_cipher = None


a = Analysis(['Mainwindow.py'],
             pathex=['D:\\5Project\\lvzheng-qt5'],
             binaries=[],
             datas=[],
             hiddenimports=['scipy._lib.messagestream', 'scipy'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Mainwindow',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Mainwindow')
