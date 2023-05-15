function ce(e) {
    var t = [
        "down",
        "move",
        "up",
        "scroll"
    ]
    if (t.indexOf())
        return t.indexOf(e)
    for (var n = 0, r = t.length; n < r; n += 1)
        if (t[n] === e)
            return n;
    return -1;
}

function CCGCq(e) {
    var t = 32767;
    return "number" != typeof e ? e : (t < e ? e = t : e < -t && (e = -t),
        Math.round(e));
}

function guijichuli(e) {
    var t = 0
        , n = 0
        , r = []
        , o = this
        , i = 0;
    if (e.length <= 0)
        return [];
    for (var s = null, a = null, c = e, _ = c.length, l = _ < 300 ? 0 : _ - 300; l < _; l += 1) {
        var u = c[l]
            , p = u[0];
        -1 < new ce(p) ? (s || (s = u),
            a = u,
            r.push([p, [u[1] - t, u[2] - n], CCGCq(i ? u[3] - i : i)]),
            t = u[1],
            n = u[2],
            i = u[3]) : -1 < new ce(p) && (r.push([p, CCGCq(i ? u[1] - i : i)]),
            i = u[1]);
    }
    return this["$_BGBw"] = s,
        this['$_BGCx'] = a,
        r;
}

function guiji_ency(e) {
    var p = {
        "move": 0,
        "down": 1,
        "up": 2,
        "scroll": 3,
        "focus": 4,
        "blur": 5,
        "unload": 6,
        "unknown": 7
    };

    function h(e, t) {
        var $_DEEGF = VIPVz.$_Ds()[8][14];

        for (; $_DEEGF !== VIPVz.$_Ds()[8][12];) {
            switch ($_DEEGF) {
                case VIPVz.$_Ds()[4][14]:
                    for (var n = e[$_CCHDD(73)](2), r = $_CCHDD(226), o = n[$_CCHCH(54)] + 1; o <= t; o += 1) r += $_CCHDD(218);

                    $_DEEGF = VIPVz.$_Ds()[8][13];
                    break;

                case VIPVz.$_Ds()[4][13]:
                    return n = r + n;
                    break;
            }
        }
    }

    function f(e) {
        var $_DEEHb = VIPVz.$_Ds()[0][14];

        for (; $_DEEHb !== VIPVz.$_Ds()[0][13];) {
            switch ($_DEEHb) {
                case VIPVz.$_Ds()[8][14]:
                    var t = [];
                    var n = e[$_CCHCH(54)];
                    var r = 0;

                    while (r < n) {
                        var o = e[r];
                        var i = 0;

                        while (1) {
                            if (16 <= i) break;
                            var s = r + i + 1;
                            if (n <= s) break;
                            if (e[s] !== o) break;
                            i += 1;
                        }

                        r = r + 1 + i;
                        var a = p[o];

                        if (0 != i) {
                            t[$_CCHDD(95)](8 | a);
                            t[$_CCHDD(95)](i - 1);
                        } else {
                            t[$_CCHDD(95)](a);
                        }
                    }

                    for (var c = h(32768 | n, 16), _ = $_CCHCH(226), l = 0, u = t[$_CCHDD(54)]; l < u; l += 1) _ += h(t[l], 4);

                    return c + _;
                    break;
            }
        }
    }

    function _(e, t) {
        var $_DEEIm = VIPVz.$_Ds()[4][14];

        for (; $_DEEIm !== VIPVz.$_Ds()[0][13];) {
            switch ($_DEEIm) {
                case VIPVz.$_Ds()[8][14]:
                    for (var n = [], r = 0, o = e[$_CCHCH(54)]; r < o; r += 1) n[$_CCHCH(95)](t(e[r]));

                    return n;
                    break;
            }
        }
    }

    function g(e, t) {
        var $_DEEJc = VIPVz.$_Ds()[8][14];

        for (; $_DEEJc !== VIPVz.$_Ds()[4][13];) {
            switch ($_DEEJc) {
                case VIPVz.$_Ds()[4][14]:
                    e = function c(e) {
                        var $_CCHHx = VIPVz.$_CG;
                        var $_CCHGy = ["$_CCIAs"].concat($_CCHHx);
                        var $_CCHIe = $_CCHGy[1];
                        $_CCHGy.shift();
                        var $_CCHJg = $_CCHGy[0];
                        var t = 32767;

                        var n = (e = _(e, function (e) {
                            var $_CCICs = VIPVz.$_CG;
                            var $_CCIBA = ["$_CCIFJ"].concat($_CCICs);
                            var $_CCIDg = $_CCIBA[1];
                            $_CCIBA.shift();
                            var $_CCIEN = $_CCIBA[0];
                            return t < e ? t : e < -t ? -t : e;
                        }))[$_CCHHx(54)];

                        var r = 0;
                        var o = [];

                        while (r < n) {
                            var i = 1;
                            var s = e[r];
                            var a = Math[$_CCHIe(518)](s);

                            while (1) {
                                if (n <= r + i) break;
                                if (e[r + i] !== s) break;
                                if (127 <= a || 127 <= i) break;
                                i += 1;
                            }

                            1 < i ? o[$_CCHHx(95)]((s < 0 ? 49152 : 32768) | i << 7 | a) : o[$_CCHHx(95)](s);
                            r += i;
                        }

                        return o;
                    }(e);

                    var n;
                    var r = [];
                    var o = [];

                    _(e, function (e) {
                        var $_CCIH_ = VIPVz.$_CG;
                        var $_CCIGv = ["$_CCJAU"].concat($_CCIH_);
                        var $_CCIIz = $_CCIGv[1];
                        $_CCIGv.shift();
                        var $_CCIJI = $_CCIGv[0];
                        var t = Math[$_CCIH_(17)](function n(e, t) {
                            var $_CCJCL = VIPVz.$_CG;
                            var $_CCJBO = ["$_CCJFN"].concat($_CCJCL);
                            var $_CCJDf = $_CCJBO[1];
                            $_CCJBO.shift();
                            var $_CCJEZ = $_CCJBO[0];
                            return 0 === e ? 0 : Math[$_CCJCL(932)](e) / Math[$_CCJCL(932)](t);
                        }(Math[$_CCIH_(518)](e) + 1, 16));
                        0 === t && (t = 1);
                        r[$_CCIIz(95)](h(t - 1, 2));
                        o[$_CCIIz(95)](h(Math[$_CCIIz(518)](e), 4 * t));
                    });

                    var i = r[$_CCHCH(633)]($_CCHCH(226));
                    var s = o[$_CCHCH(633)]($_CCHCH(226));
                    return t ? n = _(function a(e, t) {
                        var $_CCJHT = VIPVz.$_CG;
                        var $_CCJGq = ["$_CDAAY"].concat($_CCJHT);
                        var $_CCJIu = $_CCJGq[1];
                        $_CCJGq.shift();
                        var $_CCJJk = $_CCJGq[0];
                        var n = [];
                        return _(e, function (e) {
                            var $_CDACX = VIPVz.$_CG;
                            var $_CDABE = ["$_CDAFI"].concat($_CDACX);
                            var $_CDADU = $_CDABE[1];
                            $_CDABE.shift();
                            var $_CDAEC = $_CDABE[0];

                            if (t(e)) {
                                n[$_CDADU(95)](e);
                            }
                        }), n;
                    }(e, function (e) {
                        var $_CDAHu = VIPVz.$_CG;
                        var $_CDAGf = ["$_CDBAg"].concat($_CDAHu);
                        var $_CDAIS = $_CDAGf[1];
                        $_CDAGf.shift();
                        var $_CDAJY = $_CDAGf[0];
                        return 0 != e && e >> 15 != 1;
                    }), function (e) {
                        var $_CDBCM = VIPVz.$_CG;
                        var $_CDBBD = ["$_CDBFh"].concat($_CDBCM);
                        var $_CDBD_ = $_CDBBD[1];
                        $_CDBBD.shift();
                        var $_CDBEp = $_CDBBD[0];
                        return e < 0 ? $_CDBCM(987) : $_CDBD_(218);
                    })[$_CCHDD(633)]($_CCHCH(226)) : n = $_CCHCH(226), h(32768 | e[$_CCHDD(54)], 16) + i + s + n;
                    break;
            }
        }
    }

    return function (e) {
        var $_CDBHL = VIPVz.$_CG;
        var $_CDBGA = ["$_CDCAo"].concat($_CDBHL);
        var $_CDBIm = $_CDBGA[1];
        $_CDBGA.shift();
        var $_CDBJI = $_CDBGA[0];

        for (var t = [], n = [], r = [], o = [], i = 0, s = e[$_CDBHL(54)]; i < s; i += 1) {
            var a = e[i];
            var c = a[$_CDBHL(54)];
            t[$_CDBIm(95)](a[0]);
            n[$_CDBIm(95)](2 === c ? a[1] : a[2]);
            3 === c && (r[$_CDBHL(95)](a[1][0]), o[$_CDBIm(95)](a[1][1]));
        }

        var _ = f(t) + g(n, !1) + g(r, !0) + g(o, !0);

        var l = _[$_CDBHL(54)];

        return l % 6 != 0 && (_ += h(0, 6 - l % 6)), function u(e) {
            var $_CDCCL = VIPVz.$_CG;
            var $_CDCBb = ["$_CDCFg"].concat($_CDCCL);
            var $_CDCDQ = $_CDCBb[1];
            $_CDCBb.shift();
            var $_CDCEY = $_CDCBb[0];

            for (var t = $_CDCDQ(226), n = e[$_CDCCL(54)] / 6, r = 0; r < n; r += 1) t += $_CDCCL(977)[$_CDCDQ(480)](window[$_CDCCL(965)](e[$_CDCCL(87)](6 * r, 6 * (r + 1)), 2));

            return t;
        }(_);
    }(e);
}


function main_guiji(e) {
    let v1_guiji = guijichuli(e);
    let v2_guiji = guiji_ency(v1_guiji);
}