import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# Goals (goals.base.com.vn) · theo hồ sơ goal/ho-so.md + ảnh Home, Objectives · hôm nay T4 28/10/2026 = Q4 tuần 5/13
# Người đăng nhập: Võ Minh Quân, Quản lý nhà hàng Miwaku Thảo Điền. Số liệu, mục tiêu là giả định.
WEEK, WEEKS = 5, 13
PACE = round((WEEK - 1 + 0.6) / WEEKS * 100)          # mức kỳ vọng hôm nay (%)
ME = 'Võ Minh Quân'
fmtn = lambda v: (f'{v:,.1f}'.rstrip('0').rstrip('.') if isinstance(v, float) else f'{v:,}').replace(',', '#').replace('.', ',').replace('#', '.')
# goal: [tên, service, board, căn chỉnh lên target, [KR: tên, hiện tại, mục tiêu, trọng số %]]
GOALS = [
 ('Miwaku Thảo Điền đạt doanh thu Q4/2026: 9,6 tỷ', 'Miwaku', 'Miwaku Thảo Điền', 'Q4: Doanh thu Miwaku đạt 28 tỷ',
  [('Doanh thu quý đạt 9,6 tỷ', 3.1, 9.6, 50), ('Tiệc đặt trước đạt 36 tiệc', 12, 36, 20), ('Lượt đặt bàn qua app đạt 1.200', 310, 1200, 20), ('Bán 900 suất omakase', 150, 900, 10)]),
 ('Trải nghiệm khách nhất quán theo chuẩn Omotenashi', 'Miwaku', 'Miwaku Thảo Điền', 'Q4: Điểm hài lòng toàn chuỗi đạt 4,6/5',
  [('Ca lên món dưới 12 phút đạt 90%', 32, 90, 40), ('Đánh giá 5 sao trên Google đạt 300', 64, 300, 30), ('19/19 nhân viên hoàn thành khoá Omotenashi', 15, 19, 30)]),
]
def krp(k): return round(k[1] / k[2] * 100)
def gscore(g): return round(sum(krp(k) * k[3] for k in g[4]) / 100)
def status(p):
    r = p / PACE
    return ('on', 'On track') if r >= .8 else ('risk', 'At risk') if r >= .5 else ('off', 'Off track')
KRS = [k for g in GOALS for k in g[4]]
QS = round(sum(gscore(g) for g in GOALS) / len(GOALS))
MIX = {s: sum(1 for k in KRS if status(krp(k))[0] == s) for s in ('on', 'risk', 'off')}
COL = {'on': '#16A34A', 'risk': '#EA580C', 'off': '#DC2626'}
STL = {'on': 'Đúng tiến độ', 'risk': 'Có rủi ro', 'off': 'Chậm'}

css = '''<style>.gw{display:grid;grid-template-columns:1fr 300px;gap:24px;padding:18px 24px;overflow:hidden}
.g3{display:grid;grid-template-columns:1fr 1.3fr 1.2fr;border:1px solid #E5E7EB;border-radius:10px;margin:18px 24px 0}.g3>div{padding:18px 22px}.g3>div+div{border-left:1px solid #E5E7EB}
.g3 small{display:block;font-size:13px;color:#4B5563}.qs{font:700 40px/1.1 Inter;color:#111827;margin:12px 0 10px}.bh{font-size:12.5px;color:#EA580C}
.pr{display:grid;grid-template-columns:70px 1fr 44px;align-items:center;gap:8px;margin-top:12px;font-size:12.5px;color:#374151}.pr b{text-align:right;font-weight:600}
.dots{display:flex;gap:4px}.dots i{width:12px;height:7px;border-radius:4px;background:#E5E7EB}.dots i.p{background:#9CA3AF}.dots i.c{background:#111827}
.bar{position:relative;height:6px;border-radius:3px;background:#E5E7EB}.bar i{position:absolute;left:0;top:0;bottom:0;border-radius:3px}.bar u{position:absolute;top:-4px;bottom:-4px;width:2px;background:#111827}
.mix{display:flex;gap:3px;margin:12px 0 10px}.mix i{height:7px;border-radius:4px}.lgd{display:flex;gap:12px;font-size:12.5px;color:#374151}.lgd b{font-weight:700}
.sh{display:flex;align-items:center;gap:10px;margin:20px 0 10px}.sh b{font-size:16px;color:#111827}.sh span{font-size:13px;color:#6B7280}.sh a{margin-left:auto;font-size:13px;color:#2563EB}
.wk{display:flex;gap:4px;margin-left:auto}.wk i{width:14px;height:3px;border-radius:2px;background:#2563EB}
.ok{border:1.5px dashed #E5E7EB;border-radius:10px;padding:12px 16px;font-size:13px;color:#4B5563;display:flex;align-items:center;gap:8px}
.gc{border:1px solid #BBF7D0;border-radius:10px;overflow:hidden;margin-bottom:14px}.gc .gh{background:#F0FDF4;padding:14px 16px}.gc .t{display:flex;align-items:flex-start;gap:10px}.gc .t b{font-size:15.5px;color:#111827}
.okr{font-size:10.5px;font-weight:700;border:1px solid #D1D5DB;border-radius:4px;padding:1px 5px;color:#374151;margin-left:6px}.gc .sc{margin-left:auto;text-align:right}.gc .sc b{font-size:22px}.gc .sc small{display:block;font-size:11.5px;color:#16A34A}
.chip2{font-size:11.5px;font-weight:600;padding:3px 9px;border-radius:6px;background:#fff;border:1px solid #E5E7EB;margin-left:14px;white-space:nowrap}
.gc .ln{font-size:12px;color:#6B7280;margin:4px 0 10px}.seg{display:flex;gap:0;height:6px;width:520px;background:#E5E7EB;border-radius:3px;position:relative}.seg span{height:6px;position:relative}.seg span i{position:absolute;left:0;top:0;bottom:0}
.seg u{position:absolute;top:-5px;bottom:-5px;width:2px;background:#111827}.gc .nt{font-size:11px;color:#9CA3AF;margin-top:6px}
.kr{display:grid;grid-template-columns:34px 1fr 190px 46px 72px;align-items:center;gap:12px;padding:9px 16px;border-top:1px solid #F3F4F6}.kr .rg{width:28px;height:28px;border-radius:50%;border:2.5px solid #E5E7EB;display:grid;place-items:center;font-size:10px;font-weight:700;color:#374151}
.kr b{font-size:13.5px;font-weight:500;color:#111827}.kr small{display:block;font-size:11.5px;color:#9CA3AF}.kr .pc{text-align:right;font-weight:600;font-size:13px}.kr .up{background:#EFF6FF;color:#1D4ED8;font-size:12.5px;font-weight:600;text-align:center;padding:6px 0;border-radius:7px}
.gf{display:flex;justify-content:space-between;padding:10px 16px;border-top:1px solid #F3F4F6;font-size:12px;color:#6B7280}.gf a{color:#2563EB}
.ct{padding:12px 0;border-bottom:1px solid #F3F4F6}.ct .r{display:flex;gap:10px;font-size:13.5px;font-weight:600;color:#111827}.ct .r em{margin-left:auto;font-style:normal}.ct .bar{margin-top:8px}.ct p{margin:6px 0 0;font-size:12px;color:#6B7280;line-height:1.45}
.act{display:flex;gap:10px;padding:8px 0;font-size:12.5px;color:#374151;line-height:1.45}.act b{color:#111827}.act small{display:block;color:#9CA3AF}
.on2{background:#2563EB;color:#fff;font-weight:600}.sub2{width:200px;flex:none;border-right:1px solid #E5E7EB;padding:12px 10px}.sub2 .tt{font-weight:700;font-size:15px;padding:4px 8px 10px}
.sub2 .r{display:flex;align-items:center;gap:9px;height:31px;padding:0 9px;border-radius:7px;font-size:13px}.sub2 .r em{margin-left:auto;font-style:normal;color:#9CA3AF;font-size:12px}.sub2 .r.on{background:#EFF6FF;color:#1D4ED8;font-weight:600}
.cbx{width:16px;height:16px;border-radius:4px;border:1.5px solid #D1D5DB;display:grid;place-items:center;color:#fff}.cbx.on{background:#2563EB;border-color:#2563EB}
.ob td{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}.ob td b,.ob td small{display:block;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.ob td .nm b{display:block}.mb{display:inline-block;width:60px;height:5px;border-radius:3px;background:#F3F4F6;position:relative;vertical-align:middle;margin-right:8px}.mb i{position:absolute;left:0;top:0;bottom:0;border-radius:3px}</style>'''

SVC = ['Khối Nhà hàng', 'Miwaku', 'Kohaku Sushi', 'Kohaku Sashimi & Yakiniku', 'Bếp trung tâm', 'Marketing', 'Tài chính – Kế toán', 'Hành chính Nhân sự', 'Đào tạo']
ALN = ['KH Kinh doanh & Mở rộng chuỗi', 'KH Vận hành & Chất lượng', 'KH Con người & Đào tạo']
def side(on):
    r = lambda ic, n, k: f'<div class="row {"on" if k == on else ""}">{I(ic, 16)}<span>{n}</span></div>'
    return f'''<div class="side"><div class="tt">{I('target', 16)}Goals</div>{r('house', 'Trang chủ', 'home')}{r('list-checks', 'Mục tiêu', 'obj')}
<div class="sec">GOAL SERVICES</div>{''.join(r('circle-dot', n, '') for n in SVC)}
<div class="sec">CĂN CHỈNH CHIẾN LƯỢC</div>{''.join(r('layers', n, '') for n in ALN)}
<div class="foot"><div class="row">{I('users', 16)}<span>Danh bạ</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''

def bar(p, c, w='100%'):
    return f'<div class="bar" style="width:{w}"><i style="width:{min(p, 100)}%;background:{c}"></i><u style="left:{PACE}%"></u></div>'

def goal_card(g, i):
    sc = gscore(g); st = status(sc)
    seg = ''.join(f'<span style="width:{k[3]}%"><i style="width:{krp(k)}%;background:{COL[status(krp(k))[0]]}"></i></span>' for k in g[4])
    krs = ''.join(f'''<div class="kr"><span class="rg" style="border-color:{COL[status(krp(k))[0]]}">{krp(k)}</span><div><b>{k[0]}</b><small>{fmtn(k[1])} / {fmtn(k[2])} · Trọng số {k[3]}% · Cập nhật 1 ngày trước</small></div>
<div>{bar(krp(k), COL[status(krp(k))[0]])}<small style="margin-top:4px">{'+' + str(round(krp(k) * .12)) + '% tuần này' if i == 0 and k is g[4][0] else 'Không đổi tuần này'}</small></div><span class="pc" style="color:{COL[status(krp(k))[0]]}">{krp(k)}%</span><span class="up">Cập nhật</span></div>''' for k in g[4])
    gap = PACE - sc
    return f'''<div class="gc"{ad(i, 300, 120)}><div class="gh"><div class="t">{I('chevron-down', 15)}<div><b>{g[0]}</b><span class="okr">OKR</span><div class="ln">{g[1]} · {g[2]} · căn chỉnh lên <b style="font-size:12px">{g[3]}</b></div>
<div class="seg">{seg}<u style="left:{PACE}%"></u></div><div class="nt">Mỗi đoạn là một key result, dài theo trọng số</div></div>
<div class="sc"><b>{sc}%</b><small>{abs(gap)} điểm {"sau" if gap > 0 else "trước"} tiến độ</small></div><span class="chip2" style="color:{COL[st[0]]}">{STL[st[0]]}</span></div></div>{krs}
<div class="gf"><span>{len(g[4])}/{len(g[4])} key result đã cập nhật tuần này · check-in tiếp theo T6, 30/10</span><a>Mở mục tiêu ›</a></div></div>'''

CT = [('O1. Mở rộng chuỗi đúng kế hoạch, nhà hàng mới có lãi từ tháng thứ 6', 24, f'Mục tiêu của bạn: {GOALS[0][0]} ({gscore(GOALS[0])}%)'),
      ('O2. Trải nghiệm khách kiểu Nhật nhất quán ở mọi nhà hàng', 29, f'Mục tiêu của bạn: {GOALS[1][0]} ({gscore(GOALS[1])}%)'),
      ('O3. Vận hành hiệu quả, giảm hao hụt nguyên liệu', 21, 'Bạn chưa có mục tiêu ở đây'),
      ('O4. Đội ngũ quản lý đào tạo từ nội bộ', 33, 'Bạn chưa có mục tiêu ở đây')]
ACT = [('Trương Mỹ Linh', 'ghi nhận <b>12</b> cho <b>Tiệc đặt trước đạt 36 tiệc</b>', '1 ngày trước'),
       ('Võ Minh Quân', f'báo cáo <b>{gscore(GOALS[0])}%</b> cho <b>{GOALS[0][0]}</b><br><span style="color:#6B7280">Tuần này nhận 4 tiệc công ty, lượt đặt bàn qua app tăng sau chương trình tháng 10.</span><small>1 ngày trước · Độ tin cậy cao</small>', ''),
       ('Hồ Tấn Phát', 'ghi nhận <b>150</b> cho <b>Bán 900 suất omakase</b>', '2 ngày trước'),
       ('Nguyễn Hoàng Phúc', f'thêm key result <b>Ca lên món dưới 12 phút đạt 90%</b> vào <b>{GOALS[1][0]}</b>', '3 tuần trước')]

def home():
    dots = ''.join(f'<i class="{"c" if w == WEEK else "p" if w < WEEK else ""}"></i>' for w in range(1, WEEKS + 1))
    mixb = ''.join(f'<i style="flex:{MIX[s] or .001};background:{COL[s]}"></i>' for s in ('on', 'risk', 'off'))
    ct = ''.join(f'<div class="ct"><div class="r"><span>{n}</span><em style="color:{COL[status(p)[0]]}">{p}%</em></div>{bar(p, COL[status(p)[0]])}<p>{y}</p></div>' for n, p, y in CT)
    act = ''.join(f'<div class="act">{av(n, 26)}<div><b>{n}</b> {a}{f"<small>{t}</small>" if t else ""}</div></div>' for n, a, t in ACT)
    gap = PACE - QS
    return f'''<div class="main" data-sc="0"><div class="hd"><span class="t">Chào mừng quay lại, Quân</span><span class="n">Q4 2026 · Tuần {WEEK}/{WEEKS}</span><span class="ml"></span><span class="btn gh">Q4 2026{I('chevron-down', 13)}</span><span class="btn">{I('plus', 14)}Mục tiêu mới</span></div>
<div class="scr"><div class="g3"{ad(0, 60)}><div><small>Điểm quý</small><div class="qs">{QS}%</div><div class="bh">{abs(gap)} điểm {"sau" if gap > 0 else "trước"} mức {PACE}% kỳ vọng hôm nay</div></div>
<div><small>Tiến độ so với thời gian</small><div class="pr"><span>Đã qua</span><div class="dots">{dots}</div><b>{PACE}%</b></div><div class="pr"><span>Tiến độ</span>{bar(QS, '#2563EB')}<b>{QS}%</b></div><small style="margin-top:12px;color:#9CA3AF;font-size:12px">Tuần {WEEK}/{WEEKS} · kết thúc 31/12</small></div>
<div><small>{len(KRS)} key result</small><div class="mix">{mixb}</div><div class="lgd"><span><i class="dot" style="background:#15803D"></i> <b>0</b> xong</span><span><i class="dot" style="background:#86EFAC"></i> <b>{MIX['on']}</b> đúng tiến độ</span><span><i class="dot" style="background:#EA580C"></i> <b>{MIX['risk']}</b> rủi ro</span><span><i class="dot" style="background:#DC2626"></i> <b>{MIX['off']}</b> chậm</span></div></div></div>
<div class="gw"><div><div class="sh"><b>Check-in hằng tuần</b><span>Hạn T6, 30/10 · {len(KRS)}/{len(KRS)} key result đã cập nhật tuần này</span><span class="wk">{'<i></i>' * len(KRS)}</span></div>
<div class="ok"{ad(1, 200)}>{I('circle-check', 16, 2, '#16A34A')}Đã xong — mọi key result đều có số của tuần này.</div>
<div class="sh"><b>Mục tiêu của tôi</b><span>{len(GOALS)} mục tiêu · | là mức kỳ vọng hôm nay</span><a>Tất cả mục tiêu ›</a></div>{''.join(goal_card(g, i) for i, g in enumerate(GOALS))}</div>
<div><div class="sh"><b>Mục tiêu công ty</b><a>Xem tất cả ›</a></div><div{ad(2, 260)}>{ct}</div><div class="sh"><b>Hoạt động</b><a>Xem tất cả ›</a></div><div{ad(3, 320)}>{act}</div></div></div></div></div>'''

# ---- Objectives ----
TG = [('Q4: Doanh thu Miwaku đạt 28 tỷ', 'Execution', 'Nguyễn Hoàng Phúc', 'QLTH Miwaku', 27, 'KH Kinh doanh & Mở rộng chuỗi'),
      ('Q4: Điểm hài lòng toàn chuỗi đạt 4,6/5', 'Execution', 'Nguyễn Hoàng Phúc', 'QLTH Miwaku', 31, 'KH Vận hành & Chất lượng'),
      ('Doanh thu Miwaku 2026 đạt 96 tỷ', 'Planning', 'Nguyễn Hoàng Phúc', 'QLTH Miwaku', 74, 'KH Kinh doanh & Mở rộng chuỗi')]
def objectives(sc, view):
    rows = []
    if view in ('all', 'goal'):
        rows += [(g[0], f'{I("target", 12)} Mục tiêu · 0/{len(g[4])} KR xong', ME, 'Quản lý nhà hàng', gscore(g), 'Miwaku') for g in GOALS]
    if view == 'all':
        rows += [(t[0], f'{I("circle-dot", 12)} Target · {t[1]}', t[2], t[3], t[4], t[5]) for t in TG]
    if view in ('all', 'kr'):
        rows += [(k[0], f'{I("list-checks", 12)} Key result · ↳ {g[0]}', ME if j % 2 == 0 else 'Trương Mỹ Linh', 'Quản lý nhà hàng' if j % 2 == 0 else 'Trưởng ca', krp(k), 'Miwaku') for g in GOALS for j, k in enumerate(g[4])]
    n_all = len(GOALS) + len(TG) + len(KRS)
    nav = lambda ic, t, k, c: f'<div class="r {"on" if k == view else ""}">{I(ic, 15)}<span>{t}</span><em>{c}</em></div>'
    cb = lambda t, c, on=False: f'<div class="r"><span class="cbx {"on" if on else ""}">{I("check", 11, 3) if on else ""}</span><span>{t}</span><em>{c}</em></div>'
    tr = ''.join(f'''<tr{ad(i, 120, 35)}><td style="width:36px"><span class="cbx"></span></td><td><b>{r[0]}</b><small style="display:flex;align-items:center;gap:4px">{r[1]}</small></td><td><div class="nm">{av(r[2], 28)}<div><b style="font-weight:500">{r[2]}</b><small>{r[3]}</small></div></div></td>
<td><span class="mb"><i style="width:{min(r[4], 100)}%;background:{COL[status(r[4])[0]]}"></i></span><b style="display:inline;color:{COL[status(r[4])[0]]}">{r[4]}%</b></td><td>Q4 2026</td><td style="color:#4B5563">{r[5]}</td><td style="color:#6B7280">1 ngày trước</td></tr>''' for i, r in enumerate(rows))
    title = {'all': 'Mục tiêu của tôi', 'goal': 'Mục tiêu (goal) của tôi', 'kr': 'Key result của tôi'}[view]
    return f'''<div data-sc="{sc}" style="flex:1;display:flex;min-width:0"><div class="sub2"><div class="tt">Mục tiêu</div>{nav('layers', 'Tất cả', 'all', n_all)}{nav('target', 'Mục tiêu (goal)', 'goal', len(GOALS))}{nav('circle-dot', 'Target', 'tg', len(TG))}{nav('list-checks', 'Key result', 'kr', len(KRS))}{nav('eye', 'Check-in', 'ci', 9)}
<div class="sec">TRẠNG THÁI</div>{cb('Tất cả trạng thái', n_all, True)}{cb('Đang thực hiện', n_all)}{cb('Hoàn thành', 0)}{cb('Bỏ qua', 0)}
<div class="sec">PHẠM VI</div>{cb('Tất cả phạm vi', n_all, True)}{cb('Công ty', 0)}{cb('Planning', 1)}{cb('Execution', 2)}</div>
<div class="main"><div class="hd"><span class="t">{title}</span>{I('chevron-down', 13)}<span class="n">{len(rows)} mục</span><span class="ml"></span><span class="q">{I('search', 14)}Tìm mục tiêu…</span><span class="btn">{I('plus', 14)}Tạo mới{I('chevron-down', 13)}</span></div>
<div class="scr"><table class="tbl ob" style="table-layout:fixed"><colgroup><col style="width:44px"><col style="width:370px"><col style="width:230px"><col style="width:130px"><col style="width:84px"><col style="width:170px"><col></colgroup><tr><th></th><th>TÊN</th><th>NGƯỜI PHỤ TRÁCH</th><th>ĐIỂM</th><th>KỲ</th><th>NGỮ CẢNH</th><th>CẬP NHẬT</th></tr>{tr}</table></div><div style="padding:10px 22px;font-size:12.5px;color:#6B7280;border-top:1px solid #F3F4F6">Hiển thị 1–{len(rows)} / {len(rows)}</div></div></div>'''

body = css + f'<div data-sc="0" style="display:contents">{side("home")}</div><div data-sc="1 2" style="display:contents">{side("obj")}</div>' + home() + objectives('1', 'all') + objectives('2', 'kr')
open('sol/goal.html', 'w').write(page('SOL trên Goals', '/goals', 'Goals', 'letter:G', body, 3))
print('ok', QS, PACE, MIX, [gscore(g) for g in GOALS])
