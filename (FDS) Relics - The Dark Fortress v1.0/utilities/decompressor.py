def getB(number=1):
    return int.from_bytes(rom.read(number), byteorder='little')


with open(infilepath, "rb") as rom:
    with open(outfilepath, "wb") as out:
        while True:
            ins = getB()
            if ins == 0x99:#bypass
                ins = getB()
                out.write(bytes([ins]))
                continue
                
            elif ins == 0xBB:#zerofill
                amo = getB()
                out.write(b'\x00'*amo)
                continue
            
            elif ins == 0xCC:#ff fill
                amo = getB()
                out.write(b'\xFF'*amo)
                continue
            
            elif ins == 0xDD:#repeater
                ins = getB()
                amo = getB()
                out.write(bytes([ins])*amo)
                continue
            
            elif ins == 0xEE:#end!
                break
            
            else:#normie byte
                out.write(bytes([ins]))