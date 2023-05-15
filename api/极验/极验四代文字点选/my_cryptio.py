import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


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
        # 加密函数,使用pkcs7补全
        res = self.aes.encrypt(self.fill_method(encrData))
        # 转换为base64
        # msg = base64.b64encode(res)
        msgs = get_jiami(list(res))
        return msgs


if __name__ == '__main__':
    cbcC = Cbc('1f0f418988d9b75b', '0000000000000000')
    _1 = cbcC.encrypt(
        '{"passtime":1712,"userresponse":[[0,2],[0,1]],"device_id":"2d8aefc681fd34980a026cfbf46e7277","lot_number":"262ed486355f4280ba1a5e97dfe4d86c","pow_msg":"1|0|md5|2023-03-31T15:38:10.282555+08:00|24f56dc13c40dc4a02fd0318567caef5|262ed486355f4280ba1a5e97dfe4d86c||8af82a527977b115","pow_sign":"ba8bfea55ca2c216c31d77c3acdb33c4","geetest":"captcha","lang":"zh","ep":"123","hi5f":"1175422547","em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}')
    print(_1)
