from lib.Cipher import Cipher
from lib.Dictionary import Dictionary

text_to_decode = "YWUY XWDDMTKBT, OR YWUYKBT, KD YLW MPY OE POXQODKBT MBC DWBCKBT WVWPYROBKP XWDDMTWD, YNQKPMVVN POBDKDYKBT OE MVQLMSWYKP MBC BGXWRKP PLMRMPYWRD, SWYHWWB YHO OR XORW GDWRD OE XOSKVW CWIKPWD, CWDAYOQD/VMQYOQD, OR OYLWR YNQW OE POXQMYKSVW POXQGYWR. YWUY XWDDMTWD XMN SW DWBY OIWR M PWVVGVMR BWYHORA, OR XMN MVDO SW DWBY IKM MB KBYWRBWY POBBWPYKOB.YLW YWRX ORKTKBMVVN RWEWRRWC YO XWDDMTWD DWBY GDKBT YLW DLORY XWDDMTW DWRIKPW (DXD). KY LMD TROHB SWNOBC MVQLMBGXWRKP YWUY YO KBPVGCW XGVYKXWCKM XWDDMTWD (ABOHB MD XXD) POBYMKBKBT CKTKYMV KXMTWD, IKCWOD, MBC DOGBC POBYWBY, MD HWVV MD KCWOTRMXD ABOHB MD WXOZK (LMQQN EMPWD, DMC EMPWD, MBC OYLWR KPOBD)."

# load Dictionary
dict = Dictionary("./dictionary.txt")
dict.load()
dict.process_dict_pattern()

# Load Cipher
cip = Cipher()
cip.set_dictionary(dict)
# cip.set_original_text("Hi I am car.")
# cip.encode()
cip.set_cipher_text("OLQIHXIRCKGNZ PLQRZKBZB MPBKSSIPLC")
# cip.set_cipher_text(text_to_decode)
cip.decode()
print("Cipher text:  ", cip.get_cipher_text())
print("Decoded text: ", cip.get_original_text())
