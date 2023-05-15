import json

import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def de249(e, t):
    return (e >> t) & 1


def de254(e):
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789()"
    if e < 0 or e >= len(t):
        return "."
    return t[e]


def jiami_v3(e):
    def t(e, t):
        n = 0
        for r in range(24 - 1, -1, -1):
            if de249(t, r) == 1:
                n = (n << 1) + de249(e, r)
        return n

    n = ""
    r = ""
    o = len(e)
    _ = 0
    while _ < o:
        if _ + 2 < o:
            a = (e[_] << 16) + (e[_ + 1] << 8) + e[_ + 2]
            n += de254(t(a, 7274496)) + de254(t(a, 9483264)) + de254(t(a, 19220)) + de254(t(a, 235))
            _ += 3
        else:
            c = o % 3
            if c == 2:
                a = (e[_] << 16) + (e[_ + 1] << 8)
                n += de254(t(a, 7274496)) + de254(t(a, 9483264)) + de254(t(a, 19220))
                r = "."
            elif c == 1:
                a = e[_] << 16
                n += de254(t(a, 7274496)) + de254(t(a, 9483264))
                r = "." + "."
            _ += 3

    return n + r

def pNqz(e):
    t = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    return "=" if e < 0 or e >= len(t) else t[e]

def KEdi(e, t):
    return e >> t & 1

def get_shenzhi_v2(e):
    def r(e, t):
        n = 0
        for r in range(24 - 1, -1, -1):
            if KEdi(t, r) == 1:
                n = (n << 1) + KEdi(e, r)
        return n

    a = ""
    s = ""
    u = len(e)
    for c in range(0, u, 3):
        if c + 2 < u:
            t = (e[c] << 16) + (e[c + 1] << 8) + e[c + 2]
            a += pNqz(r(t, 16515072)) + pNqz(r(t, 258048)) + pNqz(r(t, 4032)) + pNqz(r(t, 63))
        elif (n := u % 3) == 2:
            t = (e[c] << 16) + (e[c + 1] << 8)
            a += pNqz(r(t, 16515072)) + pNqz(r(t, 258048)) + pNqz(r(t, 4032))
            s = "="
        elif n == 1:
            t = e[c] << 16
            a += pNqz(r(t, 16515072)) + pNqz(r(t, 258048))
            s = "=="
    return a + s



def get_jiami(e):
    t = [0] * len(e) * 2
    n = 0
    i = 0
    while i < 2 * len(e):
        t[i >> 3] |= int(e[n]) << (24 - i % 8 * 4)
        n += 1
        i += 2

    r = []
    s = 0
    while s < len(e):
        o = t[s >> 2] >> (24 - s % 4 * 8) & 255
        r.append((o >> 4 & 15).to_bytes(1, byteorder="big").hex()[1:])
        r.append((o & 15).to_bytes(1, byteorder="big").hex()[1:])
        s += 1

    return "".join(r)


class Rsa:
    def __init__(self):
        e = '10001'
        e = int(e, 16)
        n = '00C1E3934D1614465B33053E7F48EE4EC87B14B95EF88947713D25EECBFF7E74C7977D02DC1D9451F79DD5D1C10C29ACB6A9B4D6FB7D0A0279B6719E1772565F09AF627715919221AEF91899CAE08C0D686D748B20A3603BE2318CA6BC2B59706592A9219D0BF05C9F65023A21D2330807252AE0066D59CEEFA5F2748EA80BAB81'
        n = int(n, 16)
        self.pub_key = rsa.PublicKey(e=e, n=n)

    def Rencrypt(self, pwd):
        text = rsa.encrypt(pwd.encode(), self.pub_key)
        return text.hex()


def jiami(e):
    t = []
    n = 0
    for i in range(0, 2 * len(e), 2):
        t.append((int(str(e[n]), 16) << (24 - i % 8 * 4)) & 0xFFFFFFFF)
        n += 1
    r = []
    for s in range(len(e)):
        o = (t[s >> 2] >> (24 - s % 4 * 8)) & 0xFF
        r.append(hex(o >> 4)[2:])
        r.append(hex(o & 0xF)[2:])

    return "".join(r)


class Cbc:
    def __init__(self, key, iv):
        # 初始化密钥
        self.key = key
        # 初始化数据块大小
        self.length = AES.block_size
        # 初始化AES,ECB模式的实例
        self.aes = AES.new(self.key.encode("utf-8"), AES.MODE_CBC, iv=iv.encode("utf-8"))
        # 截断函数，去除填充的字符
        self.unpad = lambda date: date[0:-ord(date[-1])]

    def fill_method(self, aes_str):
        '''pkcs7补全'''
        pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')

        return pad_pkcs7

    def encrypt(self, encrData):
        print(encrData)
        # 加密函数,使用pkcs7补全
        res = self.aes.encrypt(self.fill_method(encrData))
        # 转换为base64
        # msg = base64.b64encode(res)
        msgs = get_jiami(list(res))
        return msgs

    def v3_ncrypt(self, encrData):
        # 加密函数,使用pkcs7补全
        res = self.aes.encrypt(self.fill_method(encrData))
        # 转换为base64
        # msg = base64.b64encode(res)
        msgs = jiami_v3(list(res))

        return msgs

    def Shenzhi_v2(self,encrData):
        res = self.aes.encrypt(self.fill_method(encrData))
        # 转换为base64
        # msg = base64.b64encode(res)
        msgs = get_shenzhi_v2(list(res))

        return msgs

if __name__ == '__main__':
    cbcC = Cbc('9675bc740e64dd38', '0000000000000000')
    cbcC1 = Cbc('9675bc740e64dd38', '0000000000000000')
    # _1 = cbcC.encrypt(
    #     '{"passtime":1712,"userresponse":[[0,2],[0,1]],"device_id":"2d8aefc681fd34980a026cfbf46e7277","lot_number":"262ed486355f4280ba1a5e97dfe4d86c","pow_msg":"1|0|md5|2023-03-31T15:38:10.282555+08:00|24f56dc13c40dc4a02fd0318567caef5|262ed486355f4280ba1a5e97dfe4d86c||8af82a527977b115","pow_sign":"ba8bfea55ca2c216c31d77c3acdb33c4","geetest":"captcha","lang":"zh","ep":"123","hi5f":"1175422547","em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}')
    # print(_1)
    o = {"lang": "zh-cn", "passtime": 696, "a": "7640_5354",
         "pic": "/captcha_v3/batch/v3/32548/2023-04-17T12/icon/98fd75d8fc2148d882b0ef97b4af8eec.jpg",
         "tt": "M2jUp8Pjp8Pb-Up8P:9U)@1b(55:0((7-Z((5T?bgI59(bb(.-)SSM9ODOEK-O4C.*2?8-1-111VVKEK.*)A1/L5MMbMjq0GEK*O2.L-1/111/(MbNkMMMdDS*,O2K-*2-CRkK-O0S,*2K4JONI)AM.?n((,(q8((85(,5(5,5(5e(8bbFebnq?)(1-,B/J@:CM91d/)(U9(ME-U?(b9-c(?(E1(bE-51)(NF6?N1(E-(1)(E-(1)ME(Y-,1d(j9(3)(,M92.1j-*MU/)M)*)(?/*()MU,)(?8)ME1(((8q(p(0(7*((j((/(0N5pE0NSE()M)M)S(E(LS)TM/(E(((K60.Fh*-*.7XdecA917OYG91.(MG.(M5,)95*A**UVb14(MF0(-b:b1-5-(**7URMM3/k0MM9Q2)N(1E9*PdS*,1F*A*(91,)(:b15W8(bUb9.(M2*:b53d8-*,WNU:W:UA,(b1((((((8qqqM((((",
         "ep": {"ca": [{"x": 1063, "y": 124, "t": 1, "dt": 57675}, {"x": 1070, "y": 363, "t": 3, "dt": 4303},
                       {"x": 917, "y": 216, "t": 1, "dt": 7744}, {"x": 1040, "y": 433, "t": 3, "dt": 607},
                       {"x": 1027, "y": 76, "t": 1, "dt": 54681}, {"x": 1068, "y": 433, "t": 3, "dt": 1338},
                       {"x": 907, "y": 282, "t": 1, "dt": 47382}, {"x": 1088, "y": 384, "t": 3, "dt": 623},
                       {"x": 1039, "y": 205, "t": 1, "dt": 256642}, {"x": 1068, "y": 374, "t": 3, "dt": 696}],
                "v": "3.0.8", "$_FI": False, "$_Jp": True,
                "tm": {"a": 1681708433213, "b": 0, "c": 0, "d": 0, "e": 0, "f": 1681708433213, "g": 1681708433213,
                       "h": 1681708433213, "i": 1681708433213, "j": 1681708433213, "k": 0, "l": 1681708433260,
                       "m": 1681708433777, "n": 1681708433782, "o": 1681708433808, "p": 1681708434224,
                       "q": 1681708434224, "r": 1681708434226, "s": 1681708434230, "t": 1681708434230,
                       "u": 1681708434230}}, "h9s9": "1816378497", "rp": "be4ea888d929f07af752218c18114007"}
    w = str(cbcC.v3_ncrypt(json.dumps(o, indent=None, separators=(',', ':'))))
    print(w)
