# mod_r_m_destruction(rex, mod_r_m) > (A,B)
# mod_r_m_construction(A, B) > rex, mod_r_m

A0 = [
	'[RAX]',
	'[RCX]',
	'[RDX]',
	'[RBX]',
	'[sib]',
	'[RIP+32]',
	'[RSI]',
	'[RDI]',
	'[RAX+8]',
	'[RCX+8]',
	'[RDX+8]',
	'[RBX+8]',
	'[sib+8]',
	'[RBP+8]',
	'[RSI+8]',
	'[RDI+8]',
	'[RAX+32]',
	'[RCX+32]',
	'[RDX+32]',
	'[RBX+32]',
	'[sib+32]',
	'[RBP+32]',
	'[RSI+32]',
	'[RDI+32]',
	'RAX',
	'RCX',
	'RDX',
	'RBX',
	'RSP',
	'RBP',
	'RSI',
	'RDI',
]
AB = [
	'[R8]',
	'[R9]',
	'[R10]',
	'[R11]',
	'[sib]',
	'[RIP+32]',
	'[R14]',
	'[R15]',
	'[R8+8]',
	'[R9+8]',
	'[R10+8]',
	'[R11+8]',
	'[sib+8]',
	'[R13+8]',
	'[R14+8]',
	'[R15+8]',
	'[R8+32]',
	'[R9+32]',
	'[R10+32]',
	'[R11+32]',
	'[sib+32]',
	'[R13+32]',
	'[R14+32]',
	'[R15+32]',
	'R8',
	'R9',
	'R10',
	'R11',
	'R12',
	'R13',
	'R14',
	'R15',
]
R0 = [
	'RAX',
	'RCX',
	'RDX',
	'RBX',
	'RSP',
	'RBP',
	'RSI',
	'RDI',
]
RR = [
	'R8',
	'R9',
	'R10',
	'R11',
	'R12',
	'R13',
	'R14',
	'R15',
]

D0 = '''\
AL/AX/EAX/RAX/ST0/MM0/XMM0	R8B/R8W/R8D/R8/ST0/MM0/XMM8
CL/CX/ECX/RCX/ST1/MM1/XMM1	R9B/R9W/R9D/R9/ST1/MM1/XMM9	
DL/DX/EDX/RDX/ST2/MM2/XMM2	R10B/R10W/R10D/R10/ST2/MM2/XMM10	
BL/BX/EBX/RBX/ST3/MM3/XMM3	R11B/R11W/R11D/R11/ST3/MM3/XMM11	
AH/SP/ESP/RSP/ST4/MM4/XMM4	R12B/R12W/R12D/R12/ST4/MM4/XMM12	
CH/BP/EBP/RBP/ST5/MM5/XMM5	R13B/R13W/R13D/R13/ST5/MM5/XMM13	
DH/SI/ESI/RSI/ST6/MM6/XMM6	R14B/R14W/R14D/R14/ST6/MM6/XMM14	
BH/DI/EDI/RDI/ST7/MM7/XMM7	R15B/R15W/R15D/R15/ST7/MM7/XMM15\
'''

# 4th row is opcode.
D2 = '''\
ES/CR0/DR0/0	CR8
CS/---/DR1/1	---
SS/CR2/DR2/2	---
DS/CR3/DR3/3	---
FS/CR4/DR4/4	---
GS/---/DR5/5	---
--/---/DR6/6	---
--/---/DR7/7	---\
'''


def mod_r_m_destruct(rex, mod_r_m):
	pass


def mod_r_m_construction()