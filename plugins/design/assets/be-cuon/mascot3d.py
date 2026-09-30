"""Linh vật Bé Cuộn: chiếc bánh cuộn doner có khối 3D (đổ bóng bằng dải màu, mờ mềm).
mascot(uid, pose) -> chuỗi SVG, khung 300 x 380.
pose: "chao" (vẫy tay), "like" (giơ ngón cái, nháy mắt), "cam" (ôm chiếc bánh tortilla).
"""


def _defs(u):
    return f"""<defs>
<linearGradient id="{u}tor" x1="0" x2="1"><stop offset="0" stop-color="#B8742A"/><stop offset=".18" stop-color="#E4A850"/><stop offset=".42" stop-color="#FAD48C"/><stop offset=".55" stop-color="#FFE6B2"/><stop offset=".78" stop-color="#E9B05C"/><stop offset="1" stop-color="#A9661F"/></linearGradient>
<linearGradient id="{u}pap" x1="0" x2="1"><stop offset="0" stop-color="#7C0905"/><stop offset=".2" stop-color="#C4130C"/><stop offset=".45" stop-color="#EE2A1C"/><stop offset=".56" stop-color="#FF5B47"/><stop offset=".8" stop-color="#C8140C"/><stop offset="1" stop-color="#6E0804"/></linearGradient>
<linearGradient id="{u}arm" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#FFE3A8"/><stop offset=".6" stop-color="#EDB35E"/><stop offset="1" stop-color="#B8742A"/></linearGradient>
<radialGradient id="{u}in" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#4A220E"/><stop offset="1" stop-color="#7A3B16"/></radialGradient>
<radialGradient id="{u}let" cx=".4" cy=".3" r=".8"><stop offset="0" stop-color="#B6F07A"/><stop offset=".55" stop-color="#6CC23F"/><stop offset="1" stop-color="#2F7D24"/></radialGradient>
<radialGradient id="{u}tom" cx=".35" cy=".3" r=".75"><stop offset="0" stop-color="#FF8A70"/><stop offset=".6" stop-color="#E8352A"/><stop offset="1" stop-color="#A5160F"/></radialGradient>
<radialGradient id="{u}meat" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#C77A44"/><stop offset=".7" stop-color="#8A4A26"/><stop offset="1" stop-color="#5B2C12"/></radialGradient>
<radialGradient id="{u}eye" cx=".4" cy=".35" r=".7"><stop offset="0" stop-color="#5A2A1A"/><stop offset="1" stop-color="#1E0B06"/></radialGradient>
<radialGradient id="{u}blush" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FF6F61" stop-opacity=".75"/><stop offset="1" stop-color="#FF6F61" stop-opacity="0"/></radialGradient>
<radialGradient id="{u}disc" cx=".4" cy=".35" r=".75"><stop offset="0" stop-color="#FFEBC0"/><stop offset=".7" stop-color="#F2C27A"/><stop offset="1" stop-color="#C9893A"/></radialGradient>
<filter id="{u}b3" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>
<filter id="{u}b8" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="8"/></filter>
<clipPath id="{u}body"><path d="M72,112 V300 A78,26 0 0 0 228,300 V112 Z"/></clipPath>
</defs>"""


def _arm(x, y, ang, u, length=58):
    return (f'<g transform="rotate({ang} {x} {y})">'
            f'<rect x="{x - 12}" y="{y}" width="24" height="{length}" rx="12" fill="url(#{u}arm)"/>'
            f'<circle cx="{x}" cy="{y + length}" r="15" fill="url(#{u}arm)"/>'
            f'<circle cx="{x - 4}" cy="{y + length - 5}" r="5" fill="#fff" opacity=".35"/></g>')


def mascot(u="m", pose="chao", logo_path=None):
    s = _defs(u)
    # bóng đất
    s += f'<ellipse cx="150" cy="352" rx="92" ry="14" fill="#000" opacity=".28" filter="url(#{u}b8)"/>'
    # chân
    for x in (118, 182):
        s += f'<ellipse cx="{x}" cy="340" rx="24" ry="14" fill="#3A1410"/><ellipse cx="{x - 6}" cy="335" rx="9" ry="4" fill="#fff" opacity=".18"/>'
    # tay phía sau
    if pose == "chao":
        s += _arm(78, 196, 140, u)
    # thân bánh
    s += f'<path d="M72,112 V300 A78,26 0 0 0 228,300 V112 Z" fill="url(#{u}tor)"/>'
    s += f'<g clip-path="url(#{u}body)">'
    for x, y, rx, ry, o in [(92, 150, 9, 5, .5), (206, 168, 8, 5, .45), (100, 222, 7, 4, .4), (198, 214, 6, 4, .4), (150, 140, 6, 3, .35), (214, 132, 5, 3, .4)]:
        s += f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#8E4E1C" opacity="{o}" filter="url(#{u}b3)"/>'
    s += f'<ellipse cx="150" cy="122" rx="78" ry="26" fill="#6B3514" opacity=".35" filter="url(#{u}b8)"/>'
    # giấy gói
    s += f'<path d="M60,236 Q150,262 240,236 V330 H60 Z" fill="url(#{u}pap)"/>'
    s += f'<path d="M60,236 Q150,262 240,236" fill="none" stroke="#FFB0A4" stroke-width="3" opacity=".6"/>'
    s += f'<path d="M60,244 Q150,272 240,244" fill="none" stroke="#5E0603" stroke-width="3" opacity=".35"/>'
    s += '</g>'
    if logo_path:
        s += logo_path
    # miệng bánh + nhân
    s += f'<ellipse cx="150" cy="112" rx="78" ry="24" fill="url(#{u}in)"/>'
    for cx, cy, r in [(112, 100, 16), (150, 94, 18), (188, 100, 16), (132, 90, 12), (170, 88, 12)]:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{u}meat)"/>'
    let = "M74,112 " + " ".join(f"Q{80 + i * 13},{86 - (i % 2) * 10} {87 + i * 13},{104 - (i % 3) * 4}" for i in range(11)) + " L226,116 Q150,128 74,116 Z"
    s += f'<path d="{let}" fill="url(#{u}let)"/>'
    for cx, cy, r in [(98, 92, 11), (142, 78, 12), (186, 88, 11), (206, 102, 9)]:
        s += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{u}tom)"/><circle cx="{cx - 3}" cy="{cy - 3}" r="{r * .35:.1f}" fill="#FFD2C6" opacity=".7"/>'
    # vành bánh phía trước
    s += f'<path d="M72,112 A78,24 0 0 0 228,112" fill="none" stroke="#FFE9BC" stroke-width="7" stroke-linecap="round"/>'
    s += f'<path d="M72,114 A78,24 0 0 0 228,114" fill="none" stroke="#C88633" stroke-width="2" opacity=".6" transform="translate(0 5)"/>'
    # mặt
    wink = pose == "like"
    if wink:
        s += '<path d="M112,178 q12,-12 24,0" stroke="#1E0B06" stroke-width="6" stroke-linecap="round" fill="none"/>'
    else:
        s += f'<ellipse cx="124" cy="176" rx="10" ry="13" fill="url(#{u}eye)"/><circle cx="127" cy="170" r="4" fill="#fff"/><circle cx="121" cy="181" r="1.8" fill="#fff" opacity=".8"/>'
    s += f'<ellipse cx="176" cy="176" rx="10" ry="13" fill="url(#{u}eye)"/><circle cx="179" cy="170" r="4" fill="#fff"/><circle cx="173" cy="181" r="1.8" fill="#fff" opacity=".8"/>'
    s += '<path d="M136,198 Q150,214 164,198 Q150,206 136,198 Z" fill="#6E1B10" stroke="#1E0B06" stroke-width="3.5" stroke-linejoin="round"/>'
    s += f'<ellipse cx="102" cy="200" rx="17" ry="10" fill="url(#{u}blush)"/><ellipse cx="198" cy="200" rx="17" ry="10" fill="url(#{u}blush)"/>'
    # tay phía trước
    if pose == "chao":
        s += _arm(222, 206, -40, u)
    elif pose == "like":
        s += _arm(78, 206, 36, u) + _arm(222, 190, -150, u, 50)
        s += '<rect x="248" y="118" width="12" height="22" rx="6" fill="#FFE3A8" transform="rotate(-10 254 128)"/>'
    elif pose == "cam":
        s += _arm(84, 210, -30, u, 44) + _arm(216, 210, 30, u, 44)
        s += f'<ellipse cx="150" cy="268" rx="58" ry="20" fill="url(#{u}disc)"/>'
        for dx, dy in [(-30, -3), (5, 6), (28, -6), (-8, -8)]:
            s += f'<ellipse cx="{150 + dx}" cy="{268 + dy}" rx="5" ry="2.6" fill="#9A5A22" opacity=".55"/>'
        s += '<circle cx="104" cy="262" r="14" fill="#F2C27A"/><circle cx="196" cy="262" r="14" fill="#F2C27A"/>'
    # ánh sáng viền thân
    s += '<path d="M84,130 V286" stroke="#fff" stroke-width="6" stroke-linecap="round" opacity=".18"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="20 40 260 330" role="img" aria-label="Linh vật Bé Cuộn">{s}</svg>'
