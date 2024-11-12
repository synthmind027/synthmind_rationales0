import ctypes
from ctypes import wintypes
kernel32 = ctypes.WinDLL('kernel32')
libc = ctypes.CDLL("msvcrt.dll")


machine_code_text = '48 b8 11 00 00 00 00 00 00 00 c3'
machine_code = bytes([int(x,16) for x in machine_code_text.split()])
machine_code_buffer = ctypes.create_string_buffer(machine_code, len(machine_code))

size_machine_code = len(machine_code)


'''
ref:
https://learn.microsoft.com/ko-kr/windows/win32/memory/memory-protection-constants
(PAGE_EXECUTE)
https://learn.microsoft.com/ko-kr/windows/win32/api/memoryapi/nf-memoryapi-virtualalloc
(MEM_COMMIT)
'''
MEM_COMMIT = 0x1000
MEM_RESERVE = 0x2000
PAGE_READWRITE = 0x4
PAGE_EXECUTE_READWRITE = 0x40








VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = [
    wintypes.LPVOID,  # lpAddress
    wintypes.DWORD,   # dwSize
    wintypes.DWORD,   # flAllocationType
    wintypes.DWORD,   # flProtect
]
VirtualAlloc.restype = wintypes.LPVOID

size_to_allocation = size_machine_code
sz = size_to_allocation

exec_mem = VirtualAlloc(None, sz, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE)

if not exec_mem:
    raise Exception("[ERR] Failed to virtual alloc")

#print(f"Memory allocated: {hex(ctypes.addressof(allocated_memory))}")








libc.memcpy.argtypes = [
	ctypes.c_void_p,  # src
	ctypes.c_void_p,  # dst
	ctypes.c_size_t   # size
]
libc.memcpy.restype = ctypes.c_void_p

libc.memcpy(exec_mem, machine_code_buffer, size_machine_code)

#ctypes.memcpy(exec_mem, machine_code_buffer, size_machine_code)







VirtualProtect = kernel32.VirtualProtect
VirtualProtect.argtypes = [
    wintypes.LPVOID,  # lpAddress
    wintypes.DWORD,   # dwSize
    wintypes.DWORD,   # flNewProtect
    ctypes.POINTER(wintypes.DWORD),  # lpflOldProtect
]
VirtualProtect.restype = ctypes.c_bool

size_of_memory_chunk = size_machine_code
sz = size_of_memory_chunk
fl = PAGE_EXECUTE_READWRITE
old_protect = wintypes.DWORD(0)

result = VirtualProtect(exec_mem, sz, fl, ctypes.byref(old_protect))
if not result:
	print('[ERR] Failed to virtual protect')








func = ctypes.CFUNCTYPE(None)(exec_mem)
func.argtypes = []  # specify the argument types
func.restype = ctypes.c_int  # specify the return type

print(func())
