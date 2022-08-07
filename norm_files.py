0<1# :: ^
""" Со след строки bat-код до последнего :: и тройных кавычек
@setlocal enabledelayedexpansion & py -3 -x "%~f0" %*
@(IF !ERRORLEVEL! NEQ 0 echo ERRORLEVEL !ERRORLEVEL! & pause)
@exit /b !ERRORLEVEL! :: Со след строки py-код """

# print(dir())
ps_ = '__cached__' not in dir() or not __doc__

import re, os, sys
from time import localtime, sleep, strftime
from pathlib import Path

debug = True
debug = False

dirs = [
    [r'in\0', r'out\0'],
    [r'in\1', r'out\1'],
]
#-------------------------------------------------------------------------------

# ============================================================================
def norm_Types(dir_in, dir_out):
    fpne = 'designer_Types.asm'
    txt = Path().joinpath(dir_in, fpne).read_text('cp1251')

    frags = list(filter(len, re.split(
        r'(?ms)(^;-{20,}.+?\n{2,}(?=^;-{20,}|^;={20,}))', txt)))
    frags[1:-1] = sorted(frags[1:-1])
#    print(dir_in, fpne)
#    print(len(frags), [len(s) for s in frags])
#    ss = frags[4].splitlines()
#    frags[4] = '\n'.join(ss[:2] + sorted(ss[2:])) + '\n'
    txt = ''.join(frags)

    Path().joinpath(dir_out, fpne).write_text(txt, 'cp1251')
#-------------------------------------------------------------------------------

# ============================================================================
def norm_Consts(dir_in, dir_out):
    fpne = 'designer_ConstsLCD.asm'
    txt = Path().joinpath(dir_in, fpne).read_text('cp1251')
    frags = re.split(r'(?m)(^;={20,}\n)', txt)
#    print(dir_in, fpne)
#    print(len(frags), [len(s) for s in frags])
    ss = frags[4].splitlines()
    frags[4] = '\n'.join(ss[:2] + sorted(ss[2:])) + '\n'
    txt = ''.join(frags)
    Path().joinpath(dir_out, fpne).write_text(txt, 'cp1251')
#-------------------------------------------------------------------------------

# ============================================================================
def main():

#    return
    for dir_in, dir_out in dirs:
        norm_Consts(dir_in, dir_out)
        norm_Types(dir_in, dir_out)
#-------------------------------------------------------------------------------

# ============================================================================
if __name__ == '__main__':
    if 'debug' in [arg.lower() for arg in sys.argv[1:]]:
        debug = True
    elif not ps_:
        debug = False

    main()

    if not (ps_ or '--waitendno' in sys.argv):
        os.system('timeout /t 60')
# ----------------------------------------------------------------------------
