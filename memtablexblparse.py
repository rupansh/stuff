base = """    // name
    {addr, size, res,
     rs_attr, mem_attr,
     hob, type},"""

trn_dict = {"SYS_MEM": "EFI_RESOURCE_SYSTEM_MEMORY",
		"SYS_MEM_CAP": "SYSTEM_MEMORY_RESOURCE_ATTR_CAPABILITIES",
		"Reserv": "EfiReservedMemoryType",
		"WRITE_BACK_XN": "ARM_MEMORY_REGION_ATTRIBUTE_WRITE_BACK",
		"BsData": "EfiBootServicesData",
		"MEM_RES": "EFI_RESOURCE_MEMORY_RESERVED",
		"UNCACHEABLE": "EFI_RESOURCE_ATTRIBUTE_UNCACHEABLE",
		"Reserv": "EfiReservedMemoryType",
		"UNCACHED_UNBUFFERED_XN": "ARM_MEMORY_REGION_ATTRIBUTE_UNCACHED_UNBUFFERED",
		"Conv": "EfiConventionalMemory",
		"MMAP_IO": "EFI_RESOURCE_MEMORY_MAPPED_IO",
		"INITIALIZED": "EFI_RESOURCE_ATTRIBUTE_INITIALIZED",
		"NS_DEVICE": "ARM_MEMORY_REGION_ATTRIBUTE_DEVICE",
		"WRITE_BACK": "ARM_MEMORY_REGION_ATTRIBUTE_WRITE_BACK",
		"RtData": "EfiRuntimeServicesData",
		"MmIO": "EfiMemoryMappedIO"
}

with open('mems.txt', 'r') as mem:
    for line in mem:
        mem = line.rstrip().split(',')
        print(base.replace('name', mem[2].strip()).replace('addr', mem[0].strip()).replace('size', mem[1].strip()).replace('res', trn_dict[mem[4].strip()]).replace('rs_attr', trn_dict[mem[5].strip()]).replace('mem_attr', trn_dict[mem[7].strip()]).replace('hob', mem[3].strip()).replace('type', trn_dict[mem[6].strip()]))
        print()

