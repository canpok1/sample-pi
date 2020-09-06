import binascii
import nfc

def on_connect(tag):
    idm = binascii.hexlify(tag._nfcid)
    print("IDm : " + str(idm))

clf = nfc.ContactlessFrontend('usb')
try:
    clf.connect(rdwr={'on-connect': on_connect})
finally:
    clf.close()
