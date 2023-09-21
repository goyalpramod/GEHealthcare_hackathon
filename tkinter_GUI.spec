# -*- mode: python ; coding: utf-8 -*-


block_cipher = None
import glob
image_files = [(f, '.') for f in glob.glob("D:\Projects\GE\GEHealthcare_hackathon\images\*")]

a = Analysis(
    ['tkinter_exe.py'],
    pathex=['D:\Projects\GE\GEHealthcare_hackathon\.venv\Lib\site-packages'],
    binaries=[],
    datas=[('D:\Projects\GE\GEHealthcare_hackathon\.venv\Lib\site-packages\mediapipe','mediapipe')]+image_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='tkinter_GUI',
    debug=True,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
