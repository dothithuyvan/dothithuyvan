import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# Interviews · danh sách (ảnh thư viện interviews/03, 10) · hôm nay T4 28/10/2026
# [ứng viên, ghi chú dưới tên, buổi phỏng vấn, loại, khi, thời lượng, hội đồng, xác nhận, trạng thái, điểm]
R = [
 ['Trần Quốc Bảo', 'Quản lý nhà hàng', 'PV quản lý nhà hàng – Vòng 2', 'onsite', 'Hôm nay', '15:00 · 1h', ['Nguyễn Hoàng Phúc', 'Trần Ngọc Hân'], 'ok', 'sch', None],
 ['Lâm Thanh Tùng', 'Quản lý nhà hàng', 'PV quản lý nhà hàng – Vòng 2', 'onsite', '27/10/2026', '14:00 · 1h', ['Nguyễn Hoàng Phúc', 'Trần Ngọc Hân'], 'ok', 'done', 4.4],
 ['Ngô Thị Minh Châu', 'Nhân viên phục vụ', 'Thử ca tại nhà hàng – 4 giờ', 'onsite', '27/10/2026', '10:00 · 4h', ['Võ Minh Quân'], 'ok', 'done', 4.6],
 ['Vũ Hải Đăng', 'Nhân viên phục vụ', 'Thử ca tại nhà hàng – 4 giờ', 'onsite', '26/10/2026', '17:00 · 4h', ['Trương Mỹ Linh'], 'ok', 'done', 4.2],
 ['Cao Thị Bích Ngọc', 'Phụ bếp', 'Thử tay nghề bếp', 'onsite', '26/10/2026', '09:00 · 2h', ['Lê Thị Thu Thảo'], 'ok', 'done', 3.8],
 ['Phạm Đức Long', 'Nhân viên phục vụ', 'Phỏng vấn vòng 1 – Sàng lọc', 'video', '25/10/2026', '09:30 · 30p', ['Trần Ngọc Hân'], 'no', 'noshow', None],
 ['Lưu Hoàng Yến', 'Nhân viên phục vụ', 'Phỏng vấn vòng 1 – Sàng lọc', 'phone', '24/10/2026', '10:15 · 20p', ['Trần Ngọc Hân'], 'ok', 'done', 3.9],
 ['Đinh Công Sơn', 'Quản lý nhà hàng', 'Phỏng vấn vòng 1 – Sàng lọc', 'video', '24/10/2026', '14:00 · 45p', ['Trần Ngọc Hân'], 'ok', 'done', 3.2],
 ['Triệu Văn Hòa', 'Nhân viên phục vụ', 'Phỏng vấn vòng 1 – Sàng lọc', 'phone', '23/10/2026', '16:00 · 20p', ['Trần Ngọc Hân'], 'ok', 'done', 3.5],
 ['Kiều Minh Khôi', 'Nhân viên phục vụ', 'Phỏng vấn vòng 1 – Sàng lọc', 'video', 'Ngày mai', '09:00 · 30p', ['Trần Ngọc Hân'], 'wait', 'sch', None],
 ['Hồ Văn Thắng', 'Quản lý nhà hàng', 'PV quản lý nhà hàng – Vòng 2', 'onsite', '21/10/2026', '15:00 · 1h', ['Nguyễn Hoàng Phúc', 'Trần Ngọc Hân'], 'ok', 'done', 4.7],
 ['Tạ Hữu Nghĩa', 'Phụ bếp', 'Phỏng vấn vòng 1 – Sàng lọc', 'phone', '20/10/2026', '11:00 · 20p', ['Trần Ngọc Hân'], 'ok', 'done', 2.6],
]
TOTAL = 26   # tổng buổi trong service (12 dòng hiện trang 1)
TY = {'onsite': ('Tại chỗ', '#16A34A'), 'video': ('Video', '#7C3AED'), 'phone': ('Điện thoại', '#2563EB')}
ST = {'sch': ('Đã lên lịch', 'c-b'), 'done': ('Hoàn thành', 'c-g'), 'noshow': ('Vắng mặt', 'c-r')}
CF = {'ok': ('Đã xác nhận', '#16A34A', 'circle-check'), 'wait': ('Chờ xác nhận', '#D97706', 'clock'), 'no': ('Chưa phản hồi', '#9CA3AF', 'circle-x')}
cnt = lambda k: sum(1 for r in R if r[8] == k)
done = [r for r in R if r[8] == 'done']

def rows(rs, sc):
    out = ''
    for i, r in enumerate(rs):
        ty = TY[r[3]]; st = ST[r[8]]; cf = CF[r[7]]
        sc_ = f'<span style="white-space:nowrap"><b style="font-size:14px;color:{"#15803D" if r[9] >= 4 else "#B45309" if r[9] >= 3 else "#B91C1C"}">{str(r[9]).replace(".", ",")}</b><span style="color:#9CA3AF;font-size:12px"> / 5</span></span>' if r[9] else '<span style="color:#9CA3AF">—</span>'
        panel = ''.join(f'<span style="margin-left:{-6 if j else 0}px;border:2px solid #fff;border-radius:50%;display:inline-flex">{av(p, 24)}</span>' for j, p in enumerate(r[6]))
        out += f'''<tr{ad(i, 120, 40)}><td><div class="nm">{av(r[0], 30)}<div><b>{r[0]}</b><small>{r[1]}</small></div></div></td><td>{r[2]}</td>
<td><span style="display:inline-flex;align-items:center;gap:6px;white-space:nowrap"><i class="dot" style="background:{ty[1]}"></i>{ty[0]}</span></td>
<td><b style="font-weight:500">{r[4]}</b><small>{r[5]}</small></td><td>{panel}</td>
<td><span style="display:inline-flex;align-items:center;gap:5px;color:{cf[1]};font-size:12px;font-weight:500;white-space:nowrap">{I(cf[2], 13)}{cf[0]}</span></td>
<td><span class="chip {st[1]}">{st[0]}</span></td><td>{sc_}</td></tr>'''
    return out

def filt(sel):
    def cb(lbl, n, on): return f'<div class="fr"><span class="cbx {"on" if on else ""}">{I("check", 11, 3) if on else ""}</span><span>{lbl}</span><em>{n}</em></div>'
    return f'''<div class="flt"><div class="ft">Bộ lọc</div><div class="sec">TRẠNG THÁI</div>
{cb('Tất cả trạng thái', len(R), sel == 'all')}{cb('Đã lên lịch', cnt('sch'), False)}{cb('Đang diễn ra', 0, False)}{cb('Hoàn thành', cnt('done'), sel == 'done')}{cb('Đã huỷ', 0, False)}{cb('Vắng mặt', cnt('noshow'), False)}
<div class="sec">LOẠI</div>{cb('Tất cả loại', len(R), True)}{cb('Tại chỗ', sum(1 for r in R if r[3]=='onsite'), False)}{cb('Điện thoại', sum(1 for r in R if r[3]=='phone'), False)}{cb('Video', sum(1 for r in R if r[3]=='video'), False)}{cb('Trực tuyến', 0, False)}</div>'''

side = f'''<div class="side"><div class="tt">{I('radar', 16)}Interviews</div>
<div class="row">{I('house', 16)}<span>Trang chủ</span></div><div class="row on">{I('calendar', 16)}<span>Phỏng vấn</span></div><div class="row">{I('clipboard-check', 16)}<span>Đánh giá</span></div><div class="row">{I('message-square', 16)}<span>Câu hỏi</span></div>
<div class="sec">PHỎNG VẤN TRỰC TIẾP</div><div class="row">{I('users', 15)}<span>Phỏng vấn khối Nhà hàng</span></div><div class="row">{I('users', 15)}<span>Phỏng vấn khối Bếp</span></div>
<div class="foot"><div class="row">{I('layers', 16)}<span>Mẫu phỏng vấn</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''

css = '''<style>.flt{width:220px;flex:none;border-right:1px solid #E5E7EB;padding:14px 12px}.flt .ft{font-weight:700;font-size:14px;padding:0 4px 6px}
.fr{display:flex;align-items:center;gap:9px;height:30px;padding:0 4px;font-size:13px}.fr em{margin-left:auto;font-style:normal;color:#9CA3AF;font-size:12px}
.cbx{width:16px;height:16px;border-radius:4px;border:1.5px solid #D1D5DB;display:grid;place-items:center;color:#fff}.cbx.on{background:#2563EB;border-color:#2563EB}
.pg{display:flex;align-items:center;gap:8px;padding:12px 18px;font-size:12.5px;color:#6B7280;border-top:1px solid #F3F4F6}</style>'''

def screen(sel, sc):
    rs = R if sel == 'all' else done
    return f'''<div class="app" data-sc="{sc}" style="flex:1;display:flex;min-width:0">{filt(sel)}<div class="main">
<div class="hd"><span class="t">Phỏng vấn</span><span class="n">{len(rs)} buổi phỏng vấn</span><span class="ml"></span><span class="q">{I('search', 14)}Tìm buổi phỏng vấn…</span><span class="btn">{I('plus', 14)}Lên lịch phỏng vấn</span></div>
<div class="scr"><table class="tbl"><colgroup><col style="width:220px"><col style="width:240px"><col style="width:100px"><col style="width:112px"><col style="width:84px"><col style="width:140px"><col style="width:112px"><col></colgroup>
<tr><th>ỨNG VIÊN</th><th>BUỔI PHỎNG VẤN</th><th>LOẠI</th><th>THỜI GIAN</th><th>HỘI ĐỒNG</th><th>XÁC NHẬN</th><th>TRẠNG THÁI</th><th>ĐIỂM</th></tr>{rows(rs, sc)}</table></div>
<div class="pg">Hiển thị 1–{len(rs)} / {len(rs)}</div></div></div>'''

body = side + css + screen('all', '0') + screen('done', '1')
open('sol/interview.html', 'w').write(page('SOL trên Interviews', '/interviews/list', 'Interviews', logo('interview'), body, 2))
print('ok', len(R), cnt('done'))
