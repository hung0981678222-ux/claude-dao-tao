"""Bé Cuộn bản có tính cách: nhiều biểu cảm, tư thế, đạo cụ, và lớp để tạo chuyển động.

be_cuon(uid, mat, tay, nghieng=0, dao_cu=None, chan="dung")
  mat: cuoi | nhay | ngac | le | mat_tim | nham
  tay: chao | like | tim | hai_tay | chay | om_tui | cam
  chan: dung | chay
Nhóm tay vẫy có class "vay", cả thân có class "nhun" để CSS làm chuyển động.
"""
from mascot3d import _defs, _arm

HANDLE = "#FFE3A8"


def _mat(u, mat):
    s = ""
    if mat in ("cuoi", "le", "ngac"):
        for x in (124, 176):
            s += (f'<ellipse cx="{x}" cy="176" rx="10" ry="13" fill="url(#{u}eye)"/>'
                  f'<circle cx="{x + 3}" cy="170" r="4" fill="#fff"/><circle cx="{x - 3}" cy="181" r="1.8" fill="#fff" opacity=".8"/>')
    elif mat == "nhay":
        s += '<path d="M112,178 q12,-12 24,0" stroke="#1E0B06" stroke-width="6" stroke-linecap="round" fill="none"/>'
        s += f'<ellipse cx="176" cy="176" rx="10" ry="13" fill="url(#{u}eye)"/><circle cx="179" cy="170" r="4" fill="#fff"/>'
    elif mat == "nham":
        for x in (124, 176):
            s += f'<path d="M{x - 12},172 q12,12 24,0" stroke="#1E0B06" stroke-width="6" stroke-linecap="round" fill="none"/>'
    elif mat == "mat_tim":
        for x in (124, 176):
            s += (f'<path d="M{x},186 C{x - 18},174 {x - 10},160 {x},168 C{x + 10},160 {x + 18},174 {x},186 Z" fill="#E8352A"/>'
                  f'<circle cx="{x - 5}" cy="170" r="2.5" fill="#fff" opacity=".8"/>')
    # miệng
    if mat == "ngac":
        s += '<ellipse cx="150" cy="204" rx="9" ry="11" fill="#6E1B10" stroke="#1E0B06" stroke-width="3.5"/>'
    elif mat == "le":
        s += ('<path d="M134,198 Q150,216 166,198 Q150,206 134,198 Z" fill="#6E1B10" stroke="#1E0B06" stroke-width="3.5" stroke-linejoin="round"/>'
              '<path d="M152,206 q8,14 16,2 q-6,-6 -16,-2 Z" fill="#FF6F7A" stroke="#1E0B06" stroke-width="2.5"/>')
    else:
        s += '<path d="M134,198 Q150,216 166,198 Q150,206 134,198 Z" fill="#6E1B10" stroke="#1E0B06" stroke-width="3.5" stroke-linejoin="round"/>'
    s += f'<ellipse cx="102" cy="200" rx="17" ry="10" fill="url(#{u}blush)"/><ellipse cx="198" cy="200" rx="17" ry="10" fill="url(#{u}blush)"/>'
    return s


def _than(u, logo=""):
    s = f'<path d="M72,112 V300 A78,26 0 0 0 228,300 V112 Z" fill="url(#{u}tor)"/>'
    s += f'<g clip-path="url(#{u}body)">'
    for x, y, rx, ry, o in [(92, 150, 9, 5, .5), (206, 168, 8, 5, .45), (100, 222, 7, 4, .4), (198, 214, 6, 4, .4), (150, 140, 6, 3, .35), (214, 132, 5, 3, .4)]:
        s += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#8E4E1C" opacity="{o}" filter="url(#{u}b3)"/>'
    s += f'<ellipse cx="150" cy="122" rx="78" ry="26" fill="#6B3514" opacity=".35" filter="url(#{u}b8)"/>'
    s += f'<path d="M60,236 Q150,262 240,236 V330 H60 Z" fill="url(#{u}pap)"/>'
    s += '<path d="M60,236 Q150,262 240,236" fill="none" stroke="#FFB0A4" stroke-width="3" opacity=".6"/>'
    s += '</g>' + logo
    s += f'<ellipse cx="150" cy="112" rx="78" ry="24" fill="url(#{u}in)"/>'
    for cx, cy, r in [(112, 100, 16), (150, 94, 18), (188, 100, 16), (132, 90, 12), (170, 88, 12)]:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{u}meat)"/>'
    let = "M74,112 " + " ".join(f"Q{80 + i * 13},{86 - (i % 2) * 10} {87 + i * 13},{104 - (i % 3) * 4}" for i in range(11)) + " L226,116 Q150,128 74,116 Z"
    s += f'<path d="{let}" fill="url(#{u}let)"/>'
    for cx, cy, r in [(98, 92, 11), (142, 78, 12), (186, 88, 11), (206, 102, 9)]:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{u}tom)"/><circle cx="{cx - 3}" cy="{cy - 3}" r="{r * .35:.1f}" fill="#FFD2C6" opacity=".7"/>'
    s += '<path d="M72,112 A78,24 0 0 0 228,112" fill="none" stroke="#FFE9BC" stroke-width="7" stroke-linecap="round"/>'
    s += '<path d="M84,130 V286" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".18"/>'
    return s


def _tim(x, y, sc=1.0, col="#E8352A"):
    return (f'<path transform="translate({x} {y}) scale({sc})" d="M0,14 C-26,-4 -14,-26 0,-12 C14,-26 26,-4 0,14 Z" fill="{col}" stroke="#8E0C07" stroke-width="2"/>'
            f'<circle cx="{x - 7 * sc:.1f}" cy="{y - 10 * sc:.1f}" r="{3 * sc:.1f}" fill="#fff" opacity=".7"/>')


def be_cuon(u="bc", mat="cuoi", tay="chao", nghieng=0, dao_cu=None, chan="dung", mark=""):
    s = _defs(u)
    s += f'<ellipse cx="150" cy="352" rx="92" ry="14" fill="#000" opacity=".28" filter="url(#{u}b8)"/>'
    body = ""
    # chân
    if chan == "chay":
        body += '<ellipse cx="112" cy="336" rx="24" ry="13" fill="#3A1410" transform="rotate(-18 112 336)"/>'
        body += '<ellipse cx="194" cy="318" rx="24" ry="13" fill="#3A1410" transform="rotate(24 194 318)"/>'
    else:
        for x in (118, 182):
            body += f'<ellipse cx="{x}" cy="340" rx="24" ry="14" fill="#3A1410"/><ellipse cx="{x - 6}" cy="335" rx="9" ry="4" fill="#fff" opacity=".18"/>'
    # tay phía sau
    back = {"chao": _arm(78, 200, 30, u), "hai_tay": "", "chay": _arm(222, 200, -40, u, 50)}.get(tay, "")
    body += back
    body += _than(u, mark)
    body += _mat(u, mat)
    # tay phía trước
    if tay == "chao":
        body += f'<g class="vay" style="transform-origin:222px 206px">{_arm(222, 206, -150, u)}</g>'
    elif tay == "like":
        body += _arm(78, 206, 36, u) + _arm(222, 190, -150, u, 50)
        body += f'<rect x="248" y="118" width="12" height="22" rx="6" fill="{HANDLE}" transform="rotate(-10 254 128)"/>'
    elif tay == "tim":
        body += _arm(90, 200, -58, u, 40) + _arm(210, 200, 58, u, 40) + _tim(150, 250, 1.5)
    elif tay == "hai_tay":
        body += f'<g class="vay" style="transform-origin:78px 200px">{_arm(78, 200, 150, u)}</g>'
        body += f'<g class="vay2" style="transform-origin:222px 200px">{_arm(222, 200, -150, u)}</g>'
    elif tay == "chay":
        body += _arm(78, 200, 50, u, 50)
    elif tay == "om_tui":
        body += _arm(84, 210, -40, u, 40) + _arm(216, 210, 40, u, 40)
        body += ('<path d="M104,236 h92 l-6,76 h-80 z" fill="#FFF6E6" stroke="#C8B08A" stroke-width="2"/>'
                 '<path d="M126,236 q24,-26 48,0" fill="none" stroke="#A90F09" stroke-width="5" stroke-linecap="round"/>')
        body += dao_cu or ""
    elif tay == "cam":
        body += _arm(84, 210, -30, u, 44) + _arm(216, 210, 30, u, 44)
        body += f'<ellipse cx="150" cy="268" rx="58" ry="20" fill="url(#{u}disc)"/>'
        for dx, dy in [(-30, -3), (5, 6), (28, -6), (-8, -8)]:
            body += f'<ellipse cx="{150 + dx}" cy="{268 + dy}" rx="5" ry="2.6" fill="#9A5A22" opacity=".55"/>'
    if chan == "chay":
        for i, y in enumerate((150, 190, 230)):
            s += f'<path d="M{8 + i * 6},{y} H{52 - i * 4}" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".7"/>'
    s += f'<g class="nhun" transform="rotate({nghieng} 150 330)">{body}</g>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 30 300 340" role="img" aria-label="Linh vật Bé Cuộn">{s}</svg>'
