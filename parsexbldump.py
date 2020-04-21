import os

USER = "/Users/rupansh"
ANDR = "/Volumes/android/edk2/edk2-ber2/beryllium"
BASE = f"{USER}/Downloads/fw_beryllium_miui_POCOF1Global_V11.0.6.0.QEJMIXM_e45c83a2db_10.0/firmware-update/volume-532480/file-9e21fd93-9c72-4c15-8c4b-e77f1db2d792/volume-8"
BINDIR = "beryllium/Binary"
TEMPLATE = '''  FILE DRIVER = hash {
    SECTION DXE_DEPEX = beryllium/Binary/binfile/binfile.depex
    SECTION PE32 = beryllium/Binary/binfile/binfile.efi
    SECTION UI = "binfile"
  }'''


data = None
with open("dump.txt", 'r') as dump:
	next(dump)
	next(dump)
	next(dump)
	next(dump)
	next(dump)
	next(dump)
	data = dump.read().split('File ')

ddict = dict()
for file in data:
	if 'Name' in file:
		ddict[file.split('Name: ')[-1].strip().replace('\n', '')] = f"{file.split(':')[1].split()[0]}".strip().replace('\n', '')

def get_full(file_name):
	return TEMPLATE.replace('binfile', file_name).replace('hash', ddict[file_name])

def get_path(file_name):
	return f"{BASE}/file-{ddict[file_name]}"

def add_file(file_name):
	if not os.path.exists(f"{ANDR}/Binary/{file_name}"):
		os.mkdir(f"{ANDR}/Binary/{file_name}")
		os.system(f"cp {get_path(file_name)}/section0.dxe.depex {ANDR}/Binary/{file_name}/{file_name}.depex")
		os.system(f"cp {get_path(file_name)}/section1.pe {ANDR}/Binary/{file_name}/{file_name}.efi")

	print('Done!')
	print(get_full(file_name))
	print()

add_file('UsbDeviceDxe')
add_file('UsbMsdDxe')
