import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# ESOPs · Tổng quan (ảnh esop/01) · Cấp quyền (07) · tiền ₫ · số liệu là giả định
fmt = lambda n: f'{n:,}'.replace(',', '.')
PPS = 25000
# [người, chức danh, số quyền chọn, đã vesting, trạng thái, ngày]
OF = [('Võ Minh Quân', 'Quản lý nhà hàng', 5000, 0, 'draft', '01/11/2026'),
      ('Nguyễn Hoàng Phúc', 'Quản lý thương hiệu Miwaku', 20000, 5000, 'vest', '01/01/2026'),
      ('Phạm Gia Huy', 'Quản lý thương hiệu Kohaku Sushi', 20000, 5000, 'vest', '01/01/2026'),
      ('Lê Thị Thu Thảo', 'Bếp trưởng thương hiệu', 15000, 3750, 'vest', '01/01/2026'),
      ('Đặng Thanh Tú', 'Quản lý nhà hàng', 8000, 0, 'vest', '01/07/2026'),
      ('Huỳnh Bảo Ngọc', 'Quản lý nhà hàng', 8000, 0, 'vest', '01/07/2026'),
      ('Bùi Quang Vinh', 'Điều phối ca', 5000, 0, 'draft', '01/11/2026'),
      ('Trần Ngọc Hân', 'Chuyên viên C&B', 5000, 1250, 'vest', '01/01/2026'),
      ('Nguyễn Thu Trang', 'Chuyên viên Marketing', 5000, 1250, 'vest', '01/01/2026'),
      ('Võ Minh Quân', 'Quản lý nhà hàng', 8000, 2000, 'vest', '01/01/2026')]
GA = sum(o[2] for o in OF if o[4] == 'vest')
GRANT = sum(o[2] for o in OF); VEST = sum(o[3] for o in OF)
NV = sum(1 for o in OF if o[4] == 'vest'); ND = len(OF) - NV
POOL = 300000
css = '''<style>.eg{padding:20px 24px;overflow:hidden}.wl h2{margin:0;font-size:24px;color:#111827}.wl p{margin:4px 0 16px;font-size:13px;color:#6B7280}
.k4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.k5{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;padding:16px 22px 0}
.kc{position:relative}.kc .i{position:absolute;right:14px;top:14px;width:30px;height:30px;border-radius:8px;display:grid;place-items:center}
.dg{display:grid;grid-template-columns:1fr 320px;gap:18px;margin-top:18px}.st{display:flex;align-items:center;font-weight:700;font-size:15px;margin:0 0 10px}.st a{margin-left:auto;font-size:12px;font-weight:500;color:#2563EB}
.svs{display:grid;grid-template-columns:1fr 1fr;gap:12px}.sv{padding:12px 14px;border-top:3px solid #7C3AED}.sv.sh{border-top-color:#0D9488}.sv .t{display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:600}
.sv .mm{display:flex;justify-content:space-between;font-size:11.5px;color:#6B7280;margin:10px 0 5px}.pb{height:5px;border-radius:3px;background:#E5E7EB;position:relative}.pb i{position:absolute;left:0;top:0;bottom:0;border-radius:3px}
.sv small{display:block;margin-top:8px;font-size:11.5px;color:#6B7280}.ln{padding:12px 14px;display:flex;align-items:center;gap:10px;font-size:13px;margin-bottom:8px}.ln b{color:#111827;font-weight:600}.ln small{display:block;color:#6B7280;font-size:11.5px;margin-top:3px}
.ln.cp{border-left:3px solid #D97706}.qa{padding:12px 14px}.qa .r{display:flex;align-items:center;gap:10px;height:40px;font-size:13px;font-weight:500;border-bottom:1px solid #F3F4F6}.qa .r:last-child{border:0}.qa .r span.ml{color:#9CA3AF}
.qa .r i{width:28px;height:28px;border-radius:8px;display:grid;place-items:center;background:#F3F4F6}.pr{padding:14px}.pr b{font-size:28px;color:#111827}.pr small{font-size:12px;color:#6B7280}
.vs{padding:14px}.vs .r{display:flex;justify-content:space-between;font-size:12px;color:#6B7280;margin-bottom:6px}
.tabs2{display:flex;gap:4px;margin-left:14px}.tabs2 span{font-size:12.5px;color:#4B5563;padding:4px 9px;border-radius:6px}.tabs2 span.on{background:#EFF6FF;color:#1D4ED8;font-weight:600}.tabs2 em{font-style:normal;color:#9CA3AF;margin-left:4px;font-size:11.5px}
.vb{display:flex;align-items:center;gap:8px;justify-content:flex-end}.vb .pb{width:60px}</style>'''
side = f'''<div class="side"><div class="tt"><img src="{logo('esop')}" style="width:18px;height:18px;border-radius:4px">ESOPs</div>
<div class="row" data-on="0">{I('house', 16)}<span>Tổng quan</span></div><div class="row">{I('pie-chart', 16)}<span>Cổ phần của tôi</span></div><div class="row">{I('file-text', 16)}<span>Kế hoạch của tôi</span></div><div class="row">{I('message-square', 16)}<span>Bản tin cổ đông</span></div>
<div class="sec">VẬN HÀNH</div><div class="row" data-on="1">{I('award', 16)}<span>Cấp quyền</span><em>{len(OF)}</em></div><div class="row">{I('send', 16)}<span>Đề xuất</span><em>1</em></div><div class="row">{I('flag', 16)}<span>Mốc điều kiện</span></div>
<div class="sec">CÔNG TY</div><div class="row">{I('users', 16)}<span>Cổ đông</span></div><div class="row">{I('table', 16)}<span>Bảng cơ cấu vốn</span></div><div class="row">{I('folder', 16)}<span>Tài liệu</span></div>
<div class="foot"><div class="row">{I('chart-column', 16)}<span>Báo cáo</span></div><div class="row">{I('layers', 16)}<span>Chương trình cổ phần</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''
def kc(lbl, v, sub, ic, bg, fg, col='#111827', i=0):
    return f'<div class="card kpi kc"{ad(i, 60, 50)}><span>{lbl}</span><b style="color:{col}">{v}</b><small>{sub}</small><span class="i" style="background:{bg};color:{fg}">{I(ic, 15)}</span></div>'

dash = f'''<div class="main" data-sc="0"><div class="eg"><div class="wl"><h2>Chào Hân</h2><p>Tình hình các chương trình cổ phần của SOL.</p></div>
<div class="k4">{kc('Giá mỗi cổ phần', fmt(PPS) + ' ₫', 'Định giá nội bộ 2026 — 30/06/2026', 'dollar-sign', '#DCFCE7', '#16A34A', i=0)}{kc('Cổ đông', 18, '16 nội bộ, 2 bên ngoài', 'users', '#EFF6FF', '#2563EB', i=1)}
{kc('Đợt cấp đang hiệu lực', NV, fmt(GA) + ' quyền chọn đã cấp', 'file-text', '#EDE9FE', '#7C3AED', i=2)}{kc('Cần xử lý', 3, '2 bản nháp, 1 mốc điều kiện', 'triangle-alert', '#FFEDD5', '#EA580C', i=3)}</div>
<div class="dg"><div><div class="st">Chương trình<a>Xem tất cả ›</a></div><div class="svs">
<div class="card sv"{ad(4, 200)}><div class="t">ESOP 2026–2029 — Quyền chọn quản lý chủ chốt<span class="chip c-v">QUYỀN CHỌN</span></div><div class="mm"><span>{fmt(GA)} đã cấp</span><span>{fmt(POOL - GA)} còn lại</span></div><div class="pb"><i style="width:{GA / POOL * 100:.0f}%;background:#7C3AED"></i></div><small>{NV} đợt cấp đang hiệu lực</small></div>
<div class="card sv sh"{ad(5, 200)}><div class="t">Cổ phần công ty<span class="chip c-t">CỔ PHẦN</span></div><div class="mm"><span>Theo điều lệ</span><span>—</span></div><div class="pb"><i style="width:100%;background:#0D9488"></i></div><small>0 đợt cấp đang hiệu lực</small></div></div>
<div class="st" style="margin-top:18px">Đề xuất đang chờ<a>Xem tất cả ›</a></div><div class="card ln"{ad(6, 260)}><div style="flex:1"><b>Đề xuất cấp {fmt(OF[0][2])} quyền chọn cho {OF[0][0]} — thăng chức Quản lý khu vực</b><small>{OF[0][0]} — {fmt(OF[0][2])} quyền chọn</small></div><span class="chip c-b">ĐANG MỞ</span>{I('chevron-right', 15)}</div>
<div class="st" style="margin-top:14px">Mốc điều kiện đang mở<a>Xem tất cả ›</a></div><div class="card ln cp"{ad(7, 300)}><div style="flex:1"><b>Miwaku đạt 100% doanh thu kế hoạch năm 2026</b><small>Hạn 31/12/2026</small></div><span class="chip c-o">CHỜ XÁC NHẬN</span>{I('chevron-right', 15)}</div></div>
<div><div class="card qa"{ad(4, 240)}><div style="font-size:13px;color:#6B7280;margin-bottom:6px">Thao tác nhanh</div><div class="r"><i>{I('plus', 14)}</i>Đề xuất mới<span class="ml">{I('chevron-right', 14)}</span></div><div class="r"><i>{I('file-text', 14)}</i>Xem đợt cấp<span class="ml">{I('chevron-right', 14)}</span></div><div class="r"><i>{I('user-plus', 14)}</i>Thêm cổ đông<span class="ml">{I('chevron-right', 14)}</span></div></div>
<div class="card pr" style="margin-top:14px"{ad(5, 280)}><div style="font-size:13px;color:#6B7280">Giá cổ phần</div><b>{fmt(PPS)} ₫</b><div><small>mỗi cổ phần · <span class="chip c-y">dự kiến</span></small></div><small style="display:block;margin-top:6px">Theo Định giá nội bộ 2026 — 30/06/2026</small></div>
<div class="card vs" style="margin-top:14px"{ad(6, 320)}><div style="font-size:13px;font-weight:600;margin-bottom:10px">Tổng hợp vesting</div><div class="r"><span>Đã vesting</span><span>{VEST / GA * 100:.0f}%</span></div><div class="pb"><i style="width:{VEST / GA * 100:.0f}%;background:#16A34A"></i></div></div></div></div></div></div>'''

def orow(o, i):
    n, t, g, v, s, d = o
    pct = v / g * 100
    vest = f'<div class="vb"><b>{fmt(v)}</b></div><div class="vb" style="margin-top:4px"><div class="pb"><i style="width:{pct:.0f}%;background:#2563EB"></i></div><small style="display:inline;margin:0">{pct:.0f}%</small></div>' if s == 'vest' else '<div class="vb"><b>0</b></div>'
    return f'''<tr{ad(i, 160, 50)}><td><div class="nm"><span style="color:#6B7280">{I('clock' if s == 'draft' else 'circle-dot', 17)}</span><b>{n} — {fmt(g)} quyền chọn</b></div></td>
<td><div class="nm">{av(n, 26)}<div><b>{n}</b><small>{t}</small></div></div></td><td style="color:#4B5563">ESOP 2026–2029 — Quy…</td><td><span class="chip c-v">QUYỀN CHỌN</span></td>
<td style="text-align:right"><b>{fmt(g)}</b></td><td style="text-align:right">{vest}</td><td><span class="chip {"c-x" if s == "draft" else "c-b"}">{"Nháp" if s == "draft" else "Đang vesting"}</span></td><td style="color:#4B5563">{d}</td></tr>'''
offers = f'''<div class="main" data-sc="1"><div class="hd"><span class="t">Cấp quyền</span>{I('chevron-right', 14)}<div class="tabs2"><span class="on">Tất cả<em>{len(OF)}</em></span><span>Nháp<em>{ND}</em></span><span>Đang vesting<em>{NV}</em></span><span>Đã dừng</span><span>Hoàn tất<em>0</em></span></div>
<span class="ml"></span><span class="q">{I('search', 14)}Tìm đợt cấp… (Enter)</span><span class="btn gh">{I('upload', 14)}Nhập</span><span class="btn">{I('plus', 14)}Cấp quyền mới{I('chevron-down', 13)}</span></div>
<div class="k5">{kc('Tổng đợt cấp', len(OF), '', 'file-text', '#F3F4F6', '#6B7280', i=0)}{kc('Đang vesting', NV, '', 'circle-dot', '#EFF6FF', '#2563EB', '#2563EB', 1)}{kc('Nháp', ND, '', 'clock', '#FFEDD5', '#EA580C', '#EA580C', 2)}{kc('Tổng đã cấp', fmt(GRANT), '', 'trending-up', '#EDE9FE', '#7C3AED', '#7C3AED', 3)}{kc('Tổng đã vesting', fmt(VEST), '', 'circle-check', '#DCFCE7', '#16A34A', '#16A34A', 4)}</div>
<div style="margin:16px 22px 0" class="card"><table class="tbl"><colgroup><col style="width:300px"><col style="width:240px"><col style="width:170px"><col style="width:110px"><col style="width:90px"><col style="width:120px"><col style="width:110px"><col></colgroup>
<tr><th>ĐỢT CẤP</th><th>NGƯỜI NHẬN</th><th>CHƯƠNG TRÌNH</th><th>LOẠI</th><th style="text-align:right">ĐÃ CẤP</th><th style="text-align:right">ĐÃ VESTING</th><th>TRẠNG THÁI</th><th>NGÀY</th></tr>{''.join(orow(o, i) for i, o in enumerate(OF))}</table></div></div>'''

body = css + side + dash + offers
body = body.replace('<div class="row" data-on="0">', '<div class="row on" data-sc="0">').replace('<div class="row" data-on="1">', '<div class="row" data-sc="0">')
# mục sidebar sáng theo cảnh: nhân bản 2 dòng cho cảnh 1
body = body.replace(f'<div class="row" data-sc="0">{I("award", 16)}', f'<div class="row on" data-sc="1">{I("award", 16)}<span>Cấp quyền</span><em>{len(OF)}</em></div><div class="row" data-sc="0">{I("award", 16)}', 1)
body = body.replace(f'<div class="row on" data-sc="0">{I("house", 16)}<span>Tổng quan</span></div>', f'<div class="row on" data-sc="0">{I("house", 16)}<span>Tổng quan</span></div><div class="row" data-sc="1">{I("house", 16)}<span>Tổng quan</span></div>', 1)
open('sol/esop.html', 'w').write(page('SOL trên ESOPs', '/esop/dashboard', 'ESOPs', logo('esop'), body, 2))
print('ok', GRANT, VEST)
