'''
Docstring for ch15-firmware.ghidra_projects.upgrade_proj.rep.decompile_pyghidra
Author: cch
Date: 2026-02-18
Description: Decompile the upgrade.cgi binary using PyGhidra and export the results to a text file.
License: MIT License
수정 사항: binary_path 경로, 본인 환경에 맞게 수정 필요
'''

import pyghidra
from pathlib import Path

# Binary to analyze
binary_path = "/home/cch/class/Linux/ch15-firmware/_a6004nm_kr_10_068.bin.extracted/squashfs-root/cgibin/upgrade.cgi"
output_file = "upgrade_decompile.c"

# Launch Ghidra
with pyghidra.open_program(binary_path, analyze=True) as flat_api:
    program = flat_api.getCurrentProgram()
    
    # Get the decompiler interface
    from ghidra.app.decompiler import DecompInterface
    decompiler = DecompInterface()
    decompiler.openProgram(program)
    
    # Get function manager
    function_manager = program.getFunctionManager()
    
    with open(output_file, 'w') as f:
        for function in function_manager.getFunctions(True):
            f.write("=" * 60 + "\n")
            f.write(f"Function: {function.getName()}\n")
            f.write(f"Entry: {function.getEntryPoint()}\n")
            f.write("=" * 60 + "\n")
            
            # Decompile
            results = decompiler.decompileFunction(function, 60, flat_api.getMonitor())
            
            if results.decompileCompleted():
                f.write(results.getDecompiledFunction().getC())
            else:
                f.write("<< Decompile Failed >>\n")
            
            f.write("\n\n\n")
    
    print(f"Decompile export completed -> {output_file}")
