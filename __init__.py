import mach
import struct


class Memory(object):

    def __init__(self, pid):
        self.pid = pid
        self.task = mach.task_for_pid(pid)

    def read(self, f, addr):
        s = struct.Struct(f)
        try:
            raw = mach.vm_read(self.task, addr, s.size);
        except mach.MachError as e:
            print("failed reading {}b at {}: ".format(s.size, addr), e)
        else:
            return s.unpack(raw)[0]

    def read_n(self, addr, n):
        return mach.vm_read(self.task, addr, n)

    def write(self, f, addr, val):
        s = struct.Struct(f)
        raw = s.pack(val)
        mach.vm_write(self.task, addr, raw)
