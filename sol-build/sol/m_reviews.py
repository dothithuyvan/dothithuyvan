import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# Reviews · Trang chủ có dữ liệu (ảnh reviews/02) · người đăng nhập: Võ Minh Quân, Quản lý nhà hàng · hôm nay T4 28/10/2026
SVC = 'Đánh giá hiệu suất Quý 4/2026 – Khối Nhà hàng'
T = [('Trương Mỹ Linh', 'Trưởng ca'), ('Hồ Tấn Phát', 'Đầu bếp sushi'), ('Ngô Bảo Trâm', 'Đầu bếp sushi'), ('Lý Minh Khang', 'Nhân viên phục vụ'), ('Mai Đức Thịnh', 'Phụ bếp')]
css = '''<style>.rv{display:grid;grid-template-columns:1fr 300px;gap:20px;padding:22px 26px;overflow:hidden}
.gm{display:flex;align-items:baseline;gap:14px;margin-bottom:16px}.gm b{font-size:28px;font-weight:700;color:#111827}.gm span{font-size:13px;color:#6B7280}
.mt .h{display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid #F3F4F6}.mt .h b{font-size:15px}.mt .h small{color:#6B7280;font-size:12px}
.seg{margin-left:auto;display:flex;gap:2px;background:#F3F4F6;border-radius:8px;padding:3px;font-size:12px}.seg span{padding:4px 10px;border-radius:6px;color:#4B5563}.seg span.on{background:#fff;color:#111827;font-weight:600;box-shadow:0 1px 2px rgba(0,0,0,.06)}
.seg em{font-style:normal;color:#9CA3AF;margin-left:5px}.gl2{display:flex;align-items:center;gap:6px;padding:12px 16px 4px;font-size:11px;font-weight:700;letter-spacing:.05em;color:#D97706}
.tr{display:flex;align-items:center;gap:12px;padding:10px 16px;border-bottom:1px solid #F9FAFB}.tr .who b{font-size:13.5px;color:#111827}.tr .who small{display:block;font-size:12px;color:#6B7280}
.rl{font-size:10px;font-weight:700;letter-spacing:.05em;padding:2px 6px;border-radius:4px;background:#DCFCE7;color:#15803D;margin-left:8px}.rl.s{background:#DBEAFE;color:#1D4ED8}
.du{margin-left:auto;text-align:right;font-size:12px;color:#6B7280}.du b{display:block;color:#D97706;font-size:12.5px}.fill{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border:1px solid #E5E7EB;border-radius:7px;font-size:12.5px;font-weight:600}
.sv th{background:#fff}.bar{height:6px;border-radius:3px;background:#E5E7EB;width:180px;position:relative}.bar i{position:absolute;left:0;top:0;bottom:0;border-radius:3px;background:#2563EB}
.rc{padding:14px 16px;margin-bottom:14px}.rc .h{display:flex;align-items:center;font-weight:700;font-size:14px;margin-bottom:8px}.rc .h a{margin-left:auto;font-size:12px;font-weight:500;color:#2563EB}
.rc p{margin:0;font-size:12.5px;color:#6B7280;line-height:1.5}.cu{display:flex;gap:12px}.cu .d{width:44px;height:48px;border:1px solid #E5E7EB;border-radius:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:10px;color:#6B7280;flex:none}.cu .d b{font-size:17px;color:#111827}</style>'''
side = f'''<div class="side"><div class="tt">{I('star', 16)}Reviews</div><div class="row on">{I('house', 16)}<span>Trang chủ</span></div><div class="row">{I('user', 16)}<span>Hồ sơ của tôi</span></div>
<div class="sec">DỊCH VỤ ĐÁNH GIÁ</div><div class="row">{I('clipboard-check', 15)}<span>{SVC}</span></div>
<div class="foot"><div class="row">{I('users', 16)}<span>Nhân sự</span></div><div class="row">{I('git-branch', 16)}<span>Sơ đồ người đánh giá</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''
tasks = ''.join(f'''<div class="tr"{ad(i, 160, 60)}>{av(n, 32)}<div class="who"><b>{n}<span class="rl">QUẢN LÝ</span></b><small>{SVC}</small></div><div class="du"><b>còn 13 ngày</b>Hạn 10/11 · ~20 phút</div><span class="fill"{' data-hi="1"' if i == 0 else ''}>Điền {I('arrow-up-right', 13)}</span></div>''' for i, (n, t) in enumerate(T))
self_ = f'''<div class="gl2" style="color:#6B7280">{I('calendar', 13)}SAU ĐÓ 1</div><div class="tr">{av('Võ Minh Quân', 32)}<div class="who"><b>Tự đánh giá<span class="rl s">TỰ ĐÁNH GIÁ</span></b><small>{SVC}</small></div><div class="du"><b style="color:#111827">Chưa có hạn</b>~25 phút</div><span class="fill">Điền {I('arrow-up-right', 13)}</span></div>'''
N = len(T) + 1
main = f'''<div class="main"><div class="hd">{I('house', 16)}<span class="t">Trang chủ</span><span class="n">Thứ Tư, 28 tháng 10</span><span class="ml"></span><span class="btn" data-hi="1">{I('arrow-up-right', 14)}Bắt đầu tiếp: {T[0][0]} · ~20 phút</span></div>
<div class="rv"><div><div class="gm"><b>Chào buổi sáng, Quân</b><span>{N} việc đang mở · 1 dịch vụ đang chạy</span></div>
<div class="card mt"><div class="h"><b>Việc của tôi</b><small>~{len(T) * 20 + 25} phút còn lại</small><div class="seg"><span class="on">Tất cả<em>{N}</em></span><span>Quá hạn<em>0</em></span><span>Hạn trong 13 ngày<em>{len(T)}</em></span><span>Đã nộp<em>0</em></span></div></div>
<div class="gl2">{I('clock', 13)}HẠN TRONG 13 NGÀY {len(T)}</div>{tasks}{self_}</div>
<div class="card" style="margin-top:16px"><div class="mt"><div class="h"><b>Dịch vụ</b><div class="seg"><span class="on">Tất cả<em>1</em></span><span>Đánh giá<em>1</em></span><span>Xếp hạng<em>0</em></span><span>Lịch<em>0</em></span></div></div></div>
<table class="tbl sv"><tr><th>DỊCH VỤ</th><th>CHU KỲ</th><th>TIẾN ĐỘ HOÀN THÀNH</th><th>TRẠNG THÁI</th><th></th></tr>
<tr><td><div class="nm">{I('clipboard-check', 16)}<div><b>{SVC}</b><small>2 biểu mẫu</small></div></div></td><td>—</td><td><div style="display:flex;align-items:center;gap:10px"><div class="bar"><i style="width:0%"></i></div>0/{N}</div></td><td><span class="chip c-x">Chưa bắt đầu</span></td><td>{I('chevron-right', 15)}</td></tr></table></div></div>
<div><div class="card rc"><div class="h">Kết quả gần nhất của tôi<a>Xem báo cáo</a></div><p>Điểm sẽ hiện ở đây khi kỳ đánh giá đóng.</p></div>
<div class="card rc"><div class="h">Sắp tới<a style="color:#6B7280">60 ngày tới</a></div><div class="cu"><div class="d">THG 11<b>10</b></div><div><b style="font-size:13px">{len(T)} phiếu quản lý đánh giá đến hạn</b><p>{", ".join(n for n, _ in T)}</p></div></div></div>
<div class="card rc"><div class="h">Hoạt động gần đây</div><p>Chưa có hoạt động.</p></div></div></div></div>'''
open('sol/reviews.html', 'w').write(page('SOL trên Reviews', '/reviews/home', 'Reviews', logo('review'), css + side + main, 2))
print('ok')
