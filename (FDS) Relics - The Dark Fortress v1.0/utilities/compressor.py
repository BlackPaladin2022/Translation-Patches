def getB(number=1):
    return int.from_bytes(rom.read(number), byteorder='little')

def splitpak(nums):
    result = []
    current = []
    for num in nums:
        if current and current[-1] != num:
            result.append(current)
            current = []
        current.append(num)
    if current:
        result.append(current)
    return result

nopes = [0x99, 0xBB, 0xCC, 0xDD, 0xEE]

with open(infilepath, "rb") as rom:
    with open(outfilepath, "wb") as out:
        binary_data = list(bytearray(rom.read()))
        
        binary_set = splitpak(binary_data)
        
        while binary_set:
            ins = binary_set.pop(0)
            
            if len(ins) == 1:
                oub = ins[0]
                if oub in nopes:
                    out.write(b'\x99')
                    out.write(bytes([oub]))
                else:
                    out.write(bytes([oub]))
            
            elif ins[0] in nopes:
                for i in ins:
                    out.write(b'\x99')
                    out.write(bytes([i]))
            
            elif ins[0] == 0x00:
                out.write(b'\xBB')
                out.write(bytes([len(ins)]))
                
            elif ins[0] == 0xFF:
                out.write(b'\xCC')
                out.write(bytes([len(ins)]))
                
            elif len(ins) > 3:
                out.write(b'\xDD')
                out.write(bytes([ins[0]]))
                out.write(bytes([len(ins)]))
            else:
                for i in ins:
                    out.write(bytes([i]))