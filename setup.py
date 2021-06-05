import sys
from cx_Freeze import setup,Executable

build_exe_options = {"packages":["sys","pygame","moviepy","sys","os","time"], "excludes":['tkinter']}


base = None
setup(	name="Mito da caverna",
	version="1.0",
	description = "Jogo",
	options = {"build_exe":build_exe_options},
	executables = [Executable("main.py",base=base)])
