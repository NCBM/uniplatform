from collections import namedtuple
import platform as pf

OSPlatform = namedtuple("OSPlatform", ("os", "arch", "bits"))


def oskind(osname: str):
    if osname.startswith("arm") or osname.startswith("aarch"):
        # armv7(32), armv8(64), aarch64, arm64, ...
        return "arm"
    elif "86" in osname:
        # x86, i386, i686, x86_64
        return "x86"
    elif osname.startswith("ppc"):
        return "powerpc"
    elif osname.startswith("mips"):
        return "mips"
    elif "risc" in osname:
        return "risc"
    elif osname.startswith("sparc"):
        return "sparc"
    return osname


def osbits(osname: str):
    if "64" in osname:
        return 64
    elif osname.startswith("armv8"):
        return 64
    else:
        return 32


def osplatform():
    system, machine = pf.system(), pf.machine()
    return OSPlatform(system, oskind(machine), osbits(machine))
