import binascii, construct, os, re, sys
from itertools import islice
print("Klefki (Created by NoahAbc12345)")
unknownMode = False

def showExampleUsage():
    if sys.platform in {"win32", "cygwin"}: print("Usage Example: Klefki.exe otp.bin -unknown")
    else: print("Usage Example: ./Klefki otp.bin -unknown")

if len(sys.argv) not in {2, 3}:
    showExampleUsage(); print("Before using this program, you first need to specify the path to your otp.bin!")
else:   
    fileOTP = sys.argv[1]
    try: unknownMode = True if sys.argv[2] in {"-unknown", "-u"} else False
    except: pass

    structureOTP = construct.Struct(
        "Wii boot1 SHA-1 Hash" / construct.Hex(construct.Bytes(20)),
        "Wii Common Key" / construct.Hex(construct.Bytes(16)),
        "Wii NG ID" / construct.Hex(construct.Bytes(4)),
        "Wii NG Private Key" / construct.Hex(construct.Bytes(28)),
        "Wii NAND HMAC" / construct.Hex(construct.Bytes(20)),
        "Wii NAND Key" / construct.Hex(construct.Bytes(16)),
        "Wii RNG Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 1 (Padding)" / construct.Hex(construct.Bytes(8)),
        "Security Level Flag" / construct.Hex(construct.Bytes(4)),
        "IOStrength Configuration Flag" / construct.Hex(construct.Bytes(4)),
        "SEEPROM Manual CLK Pulse Length" / construct.Hex(construct.Bytes(4)),
        "Signature Type" / construct.Hex(construct.Bytes(4)),
        "Wii U Starbuck Ancast Key" / construct.Hex(construct.Bytes(16)),
        "Wii U SEEPROM Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 2 (Unused)" / construct.Hex(construct.Bytes(16)),
        "Unknown 3 (Unused)" / construct.Hex(construct.Bytes(16)),
        "vWii Common Key" / construct.Hex(construct.Bytes(16)),
        "Wii U Common Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 4 (Unused)" / construct.Hex(construct.Bytes(16)),
        "Unknown 5 (Unused)" / construct.Hex(construct.Bytes(16)),
        "Unknown 6 (Unused)" / construct.Hex(construct.Bytes(16)),
        "SSL RSA Encryption Key" / construct.Hex(construct.Bytes(16)),
        "USB Storage Seed Encryption Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 7 (Used)" / construct.Hex(construct.Bytes(16)),
        "Wii U XOR Key" / construct.Hex(construct.Bytes(16)),
        "Wii U RNG Key" / construct.Hex(construct.Bytes(16)),
        "Wii U SLC Key" / construct.Hex(construct.Bytes(16)),
        "Wii U MLC Key" / construct.Hex(construct.Bytes(16)),
        "SHDD Encryption Key" / construct.Hex(construct.Bytes(16)),
        "DRH WLAN Data Encryption Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 8 (Unused)" / construct.Hex(construct.Bytes(48)),
        "Wii U SLC (NAND) HMAC" / construct.Hex(construct.Bytes(20)),
        "Unknown 9 (Padding)" / construct.Hex(construct.Bytes(12)),
        "Unknown 10 (Unused)" / construct.Hex(construct.Bytes(16)),
        "Unknown 11 (Unused)" / construct.Hex(construct.Bytes(12)),
        "Wii U NG ID" / construct.Hex(construct.Bytes(4)),
        "Wii U NG Private Key" / construct.Hex(construct.Bytes(32)),
        "Wii U NSS Device Certificate Key" / construct.Hex(construct.Bytes(32)),
        "Wii U OTP RNG Seed" / construct.Hex(construct.Bytes(16)),
        "Unknown 12 (Unused)" / construct.Hex(construct.Bytes(16)),
        "Wii U Root Certificate MS ID" / construct.Hex(construct.Bytes(4)),
        "Wii U Root Certificate CA ID" / construct.Hex(construct.Bytes(4)),
        "Wii U Root Certificate NG Key ID" / construct.Hex(construct.Bytes(4)),
        "Wii U Root Certificate NG Signature" / construct.Hex(construct.Bytes(60)),
        "Unknown 13 (Unused)" / construct.Hex(construct.Bytes(24)),
        "Unknown 14 (Locked/Unused)" / construct.Hex(construct.Bytes(32)),
        "Wii Root Certificate MS ID" / construct.Hex(construct.Bytes(4)),
        "Wii Root Certificate CA ID" / construct.Hex(construct.Bytes(4)),
        "Wii Root Certificate NG Key ID" / construct.Hex(construct.Bytes(4)),
        "Wii Root Certificate NG Signature" / construct.Hex(construct.Bytes(60)),
        "Wii Korean Key" / construct.Hex(construct.Bytes(16)),
        "Unknown 15 (Unused)" / construct.Hex(construct.Bytes(8)),
        "Wii NSS Device Certificate Key" / construct.Hex(construct.Bytes(32)),
        "Unknown 16 (Locked/Unused)" / construct.Hex(construct.Bytes(32)),
        "Wii U boot1 Key (Locked)" / construct.Hex(construct.Bytes(16)),
        "Unknown 17 (Locked/Unused)" / construct.Hex(construct.Bytes(16)),
        "Empty Space 1" / construct.Hex(construct.Bytes(32)),
        "Empty Space 2" / construct.Hex(construct.Bytes(4)),
        "OTP Version & Revision" / construct.Hex(construct.Bytes(4)),
        "OTP Date Code" / construct.Hex(construct.Bytes(8)),
        "OTP Version Name String" / construct.Hex(construct.Bytes(8)),
        "Empty Space 3" / construct.Hex(construct.Bytes(4)),
        "JTAG Status" / construct.Hex(construct.Bytes(4))
    )

    try:
        if os.stat(fileOTP).st_size == 1024:
            parsedOTP = structureOTP.parse_file(fileOTP)
            print("Please do not share any values obtained from this program! Many are copyrighted and/or console-unique!")
            for item, value in islice(parsedOTP.items(), 1, None):
                value = str(value); value = value[11:-2].upper()
                if unknownMode: print(f"{f'{item}: ':<37} {value}")
                elif not unknownMode:
                    if re.match(r"Unknown|Unused|Empty Space", item): pass
                    else: print(f"{f'{item}: ':<37} {value}")
        else: showExampleUsage(); print("The path provided does not lead to a valid otp.bin!")
    except: showExampleUsage(); print("The path provided does not lead to a valid otp.bin!")