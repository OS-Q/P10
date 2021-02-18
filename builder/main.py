from os.path import join
from SCons.Script import (AlwaysBuild, Builder, COMMAND_LINE_TARGETS, Default, DefaultEnvironment)
from colorama import Fore
env = DefaultEnvironment()
print(Fore.GREEN + '<<<<<<<<<<<< '+env.BoardConfig().get("name").upper()+" 2019 Georgi Angelov >>>>>>>>>>>>")
#print( env.Dump )
####################################################
# Build executable and linkable program
####################################################
elf = env.BuildProgram()
AlwaysBuild( elf )
upload = env.Alias(
    "upload", elf,
    [
        env.VerboseAction("$UPLOADCMD", '\033[93m'+"Runing $PROGNAME"),
    ])
AlwaysBuild( upload )
Default( elf )
