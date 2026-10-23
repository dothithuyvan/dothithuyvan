import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
import base64
WR_LOGO = 'letter:W'
GOAL_LOGO = 'letter:G'

# ================= GOAL · màn Goals (ảnh home/04) =================
G = [  # tên, dự án, người, hạn, trạng thái
 ('Tuyển đủ 22 nhân sự khai trương', 'Khai trương Miwaku Landmark 81', 'Trần Ngọc Hân', '25/10/2026', 'p'),
 ('Doanh thu quý IV đạt 100% kế hoạch', 'Miwaku Thảo Điền', 'Võ Minh Quân', '31/12/2026', 'p'),
 ('Điểm hài lòng khách từ 4,7/5', 'Miwaku Thảo Điền', 'Võ Minh Quân', '31/12/2026', 'p'),
 ('Đào tạo nhân viên mới 2 tuần', 'Khai trương Miwaku Landmark 81', 'Võ Minh Quân', '14/11/2026', 'p'),
 ('Chuẩn hoá công thức 12 món omakase', 'Bếp trung tâm', 'Lê Thị Thu Thảo', '30/11/2026', 'p'),
 ('Giảm hao hụt nguyên liệu tươi xuống 3%', 'Bếp trung tâm', 'Lê Thị Thu Thảo', '31/12/2026', 'p'),
 ('Tỷ lệ nghỉ việc dưới 5% mỗi quý', 'Khối Nhà hàng', 'Nguyễn Hoàng Phúc', '31/12/2026', 'p'),
 ('100% trưởng ca hoàn thành khoá Quản lý nhà hàng', 'Đào tạo', 'Trần Ngọc Hân', '15/12/2026', 'p'),
 ('Kiểm tra ATTP nội bộ đạt từ 95/100', 'Kohaku Sushi', 'Phạm Gia Huy', '30/11/2026', 'p'),
 ('Chạy thử nội bộ (soft opening)', 'Khai trương Miwaku Landmark 81', 'Võ Minh Quân', '18/11/2026', 'p'),
 ('Khai trương chính thức', 'Khai trương Miwaku Landmark 81', 'Nguyễn Hoàng Phúc', '22/11/2026', 'p'),
 ('Đưa thực đơn mùa đông vào 6 nhà hàng Kohaku', 'Kohaku Sushi', 'Phạm Gia Huy', '01/12/2026', 'p'),
]
GS = {'all': 86, 'p': 19, 'pl': 52, 'd': 13, 'f': 2}
assert GS['all'] == GS['p'] + GS['pl'] + GS['d'] + GS['f']
def goal_page():
    css = '''<style>.grl{width:70px;flex:none;border-right:1px solid #E5E7EB;display:flex;flex-direction:column;align-items:center;padding:10px 0;gap:6px}
.grl div{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10px;color:#6B7280;width:62px}.grl div i{width:32px;height:32px;border-radius:50%;display:grid;place-items:center}.grl div.on i{background:#DBEAFE;color:#1D4ED8}.grl div.on{color:#1D4ED8;font-weight:600}
.gfl .r{display:flex;align-items:center;gap:9px;height:30px;padding:0 8px;font-size:13px}.cbx{width:16px;height:16px;border-radius:4px;border:1.5px solid #D1D5DB;display:grid;place-items:center;color:#fff}.cbx.on{background:#2563EB;border-color:#2563EB}
.gls{max-width:960px;margin:0 auto;padding:14px 0}.gsh{display:flex;align-items:center;gap:8px;font-size:11px;font-weight:700;letter-spacing:.06em;color:#374151;margin:6px 0}
.gro{display:flex;align-items:center;gap:10px;height:40px;border-bottom:1px solid #F3F4F6;font-size:13.5px}.gro b{font-weight:600;color:#111827}.gro .pc{font-size:11px;padding:2px 7px;border-radius:5px;background:#F3F4F6;color:#4B5563;max-width:210px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.gro .pj{font-size:11px;padding:2px 7px;border-radius:5px;border:1px solid #E5E7EB;color:#6B7280}.gro .ow{font-size:12px;color:#6B7280}.gro .du{margin-left:auto;font-size:12px;color:#DC2626;font-weight:500}.gro .du.f{color:#6B7280}</style>'''
    rail = ''.join(f'<div class="{"on" if n == "Mục tiêu" else ""}"><i>{I(ic, 17)}</i>{n}</div>' for ic, n in [('house', 'Trang chủ'), ('calendar', 'Lịch'), ('list-checks', 'Việc cần làm'), ('square-check', 'Công việc'), ('mail', 'Hộp thư'), ('bookmark', 'Đánh dấu'), ('notebook', 'Ghi chú'), ('target', 'Mục tiêu'), ('id-card', 'Hồ sơ HR'), ('timer', 'Khối lượng'), ('award', 'Đầu ra')])
    cb = lambda n, on, ic: f'<div class="r"><span class="cbx {"on" if on else ""}">{I("check", 11, 3) if on else ""}</span>{I(ic, 14)}<span>{n}</span></div>'
    def row(g, i, sc):
        t, p, o, d, s = g
        return f'<div class="gro"{ad(i, 150, 40)}><i class="dot" style="background:#2563EB"></i><b>{t}</b><span class="pc">{p}</span><span class="pj">Project</span><span class="ow">{o}</span><span class="du {"" if (int(d[3:5]), int(d[:2])) < (10, 28) else "f"}">{d}</span></div>'
    mine = [g for g in G if g[2] == 'Võ Minh Quân']
    def screen(sc, sel):
        rs = G if sel == 'all' else mine
        return f'''<div class="main" data-sc="{sc}"><div class="hd"><span class="t">{"Tất cả mục tiêu" if sel == "all" else "Mục tiêu của tôi"}</span><span class="n">{GS["all"] if sel == "all" else len(mine)} mục tiêu</span><span class="ml"></span><span class="q">{I("search", 14)}Tìm mục tiêu…</span></div>
<div class="scr"><div class="gls"><div class="gsh"><i class="dot" style="background:#2563EB"></i>ĐANG THỰC HIỆN <span style="color:#9CA3AF">{GS["p"] if sel == "all" else len(mine)}</span></div>{"".join(row(g, i, sc) for i, g in enumerate(rs))}</div></div></div>'''
    side = f'''<div class="side gfl" style="width:220px"><div class="tt">{I('menu', 15)}Mục tiêu</div>
<div class="row" data-sc="0" style="background:#2563EB;color:#fff;font-weight:600">{I('target', 15)}<span>Tất cả mục tiêu</span></div><div class="row" data-sc="1">{I('target', 15)}<span>Tất cả mục tiêu</span></div>
<div class="row" data-sc="0">{I('user', 15)}<span>Tôi phụ trách</span></div><div class="row" data-sc="1" style="background:#2563EB;color:#fff;font-weight:600">{I('user', 15)}<span>Tôi phụ trách</span></div>
<div class="row">{I('eye', 15)}<span>Đang theo dõi</span></div>
<div class="sec">TRẠNG THÁI</div>{cb('Tất cả trạng thái', False, 'layers')}{cb('Đang thực hiện', True, 'circle-dot')}{cb('Kế hoạch', False, 'clock')}{cb('Hoàn thành', False, 'circle-check')}{cb('Thất bại', False, 'circle-x')}</div>'''
    body = css + f'<div class="grl">{rail}</div>' + side + screen('0', 'all') + screen('1', 'mine')
    open('sol/goal.html', 'w').write(page('SOL trên Goals', '/goals', 'Goals', GOAL_LOGO, body, 2))

# ================= WORK RULES · minh hoạ (thư viện chưa có ảnh app này) =================
CAT = [('Công, ca và chấm công', 'Ca làm việc, đổi ca, đi muộn, quên chấm công', 6, 'Quy định ca làm việc tại nhà hàng', '01/10/2026', 731),
       ('Nghỉ phép và tăng ca', 'Quỹ phép, nghỉ lễ, tăng ca và nghỉ bù', 4, 'Làm việc ngày lễ, Tết', '15/09/2026', 820),
       ('An toàn thực phẩm', 'Vệ sinh cá nhân, bảo quản nguyên liệu, kiểm tra ATTP', 5, 'Ghi nhãn ngày mở nguyên liệu', '20/10/2026', 767),
       ('Tiêu chuẩn phục vụ', 'Chào khách, giới thiệu món, xử lý phàn nàn', 7, 'Quy trình phục vụ omakase', '05/10/2026', 731),
       ('Đồng phục và tác phong', 'Đồng phục theo thương hiệu, tác phong tại nhà hàng', 3, 'Đồng phục mùa đông 2026', '12/10/2026', 820),
       ('Phúc lợi nhân viên', 'Giảm 20% khi dùng bữa tại hệ thống, đào tạo miễn phí', 2, 'Ưu đãi dùng bữa của nhân viên', '01/07/2026', 820)]
def rules_page():
    css = '''<style>.wl2{max-width:1000px;margin:0 auto;padding:22px 0}.wl2 .cap{font-size:11px;font-weight:700;letter-spacing:.2em;color:#6B7280;text-align:center}
.wl2 h1{margin:8px 0 6px;text-align:center;font:700 40px/1.1 Georgia,serif;color:#111827}.wl2 .ds{text-align:center;font:15px/1.5 Georgia,serif;color:#4B5563;margin-bottom:16px}
.cr{display:grid;grid-template-columns:40px 1fr 150px 120px;gap:14px;align-items:center;padding:14px 4px;border-top:1px solid #F3F4F6}.cr .n{font:400 24px Georgia,serif;color:#9CA3AF}
.cr b{font:700 19px Georgia,serif;color:#111827}.cr p{margin:3px 0 4px;font-size:13px;color:#4B5563}.cr small{font-size:11.5px;color:#6B7280}.cr small i{font-style:italic;color:#374151}
.ak{font-size:12px;color:#6B7280}.ak b{display:block;font:600 14px Inter;color:#111827}.pbx{height:5px;border-radius:3px;background:#E5E7EB;margin-top:5px;position:relative}.pbx i{position:absolute;left:0;top:0;bottom:0;border-radius:3px;background:#16A34A}
.rd{display:grid;grid-template-columns:1fr 300px;gap:22px;padding:20px 26px;overflow:hidden}.doc{border:1px solid #E5E7EB;border-radius:12px;padding:26px 34px}.doc .bc{font-size:11px;font-weight:700;letter-spacing:.12em;color:#2563EB}
.doc h2{margin:10px 0 6px;font:700 28px/1.2 Georgia,serif;color:#111827}.doc .mt{font-size:12.5px;color:#6B7280;margin-bottom:14px}.doc h4{margin:16px 0 6px;font-size:14px;color:#111827}
.doc li{font-size:13.5px;color:#374151;line-height:1.6}.doc ul{margin:0;padding-left:18px}.sc2{padding:14px 16px;margin-bottom:14px}.sc2 .h{font-size:11px;font-weight:700;letter-spacing:.05em;color:#6B7280;margin-bottom:8px}
.kv2{display:flex;justify-content:space-between;font-size:13px;padding:5px 0}.kv2 span{color:#6B7280}.kv2 b{font-weight:600;color:#111827}
.ack{display:flex;align-items:center;gap:10px;font-size:13px;padding:6px 0}.ack em{margin-left:auto;font-style:normal;font-size:12px}.tagm{position:absolute;right:16px;bottom:12px;font-size:11px;color:#9CA3AF}</style>'''
    side = f'''<div class="side"><div class="tt">{I('book-open', 16)}Work rules</div>
<div class="row" data-sc="0" style="background:#2563EB;color:#fff;font-weight:600">{I('book-open', 16)}<span>Thư viện quy định</span></div><div class="row" data-sc="1">{I('book-open', 16)}<span>Thư viện quy định</span></div>
<div class="row">{I('circle-check', 16)}<span>Cần tôi xác nhận</span><em>2</em></div><div class="row">{I('history', 16)}<span>Lịch sử ban hành</span></div>
<div class="sec">NHÓM QUY ĐỊNH</div>{''.join(f'<div class="row" {"data-sc=\"1\" style=\"background:#DBEAFE;color:#1D4ED8;font-weight:600\"" if i == 0 else ""}>{I("file-text", 15)}<span>{c[0]}</span><em>{c[2]}</em></div>' + (f'<div class="row" data-sc="0">{I("file-text", 15)}<span>{c[0]}</span><em>{c[2]}</em></div>' if i == 0 else '') for i, c in enumerate(CAT))}
<div class="foot"><div class="row">{I('chart-column', 16)}<span>Báo cáo</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''
    rows = ''.join(f'''<div class="cr"{ad(i, 160, 60)}><span class="n">{i + 1}</span><div><b>{c[0]}</b><p>{c[1]}</p><small>MỚI NHẤT · <i>{c[3]}</i> · {c[4]}</small></div>
<div class="ak"><b>{c[2]} quy định</b>áp dụng {c[5]} người</div><div class="ak"><b>{round(c[5] * (0.96 - i * 0.03))}/{c[5]}</b>đã xác nhận<div class="pbx"><i style="width:{(0.96 - i * 0.03) * 100:.0f}%"></i></div></div></div>''' for i, c in enumerate(CAT))
    lib = f'''<div class="main" data-sc="0"><div class="hd"><span class="t">Thư viện quy định</span><span class="ml"></span><span class="q">{I('search', 14)}Tìm quy định…</span><span class="btn">{I('plus', 14)}Ban hành quy định</span></div>
<div class="scr"><div class="wl2"><div class="cap">SOL · WORK RULES</div><h1>Quy định làm việc tại SOL</h1><div class="ds">Một nơi cho mọi quy định: văn phòng, bếp trung tâm và từng nhà hàng.<br>Mỗi lần cập nhật, nhân viên nhận thông báo và xác nhận đã đọc.</div>{rows}</div></div><span class="tagm">Giao diện minh hoạ</span></div>'''
    acks = [('Võ Minh Quân', 'Đã xác nhận', '#16A34A'), ('Trương Mỹ Linh', 'Đã xác nhận', '#16A34A'), ('Lý Minh Khang', 'Đã xác nhận', '#16A34A'), ('Trần Bảo Châu', 'Chưa đọc', '#D97706')]
    det = f'''<div class="main" data-sc="1"><div class="hd"><span class="n">Thư viện quy định › Công, ca và chấm công ›</span><span class="t">Quy định ca làm việc tại nhà hàng</span><span class="ml"></span><span class="btn gh">{I('pencil', 13)}Sửa</span><span class="btn">{I('send', 13)}Gửi nhắc xác nhận</span></div>
<div class="rd"><div class="doc"{ad(0, 120)}><div class="bc">CÔNG, CA VÀ CHẤM CÔNG · PHIÊN BẢN 3</div><h2>Quy định ca làm việc tại nhà hàng</h2><div class="mt">Hiệu lực từ 01/10/2026 · Áp dụng: Khối Vận hành nhà hàng · Ban hành bởi Phòng Hành chính Nhân sự</div>
<h4>1. Ca làm việc</h4><ul><li>Ca sáng 09:00–17:00, ca tối 14:00–22:00, ca đóng cửa 15:30–23:30.</li><li>Quản lý nhà hàng xếp ca theo tuần trên Timesheets, công bố trước thứ Sáu.</li><li>Mỗi nhân viên nghỉ 1 ngày trong tuần, ưu tiên từ thứ Hai đến thứ Sáu.</li></ul>
<h4>2. Đổi ca</h4><ul><li>Gửi yêu cầu đổi ca trên app trước ít nhất 24 giờ, trưởng ca duyệt.</li></ul>
<h4>3. Chấm công</h4><ul><li>Chấm công vào, ra tại máy của nhà hàng; quên chấm công giải trình trên app trong ngày.</li><li>Làm sau 22:00 được tính phụ cấp làm đêm theo quy định pháp luật.</li></ul></div>
<div><div class="card sc2"{ad(1, 200)}><div class="h">THÔNG TIN</div><div class="kv2"><span>Trạng thái</span><b style="color:#16A34A">Đang hiệu lực</b></div><div class="kv2"><span>Phiên bản</span><b>3 · 01/10/2026</b></div><div class="kv2"><span>Áp dụng</span><b>731 người</b></div><div class="kv2"><span>Liên kết</span><b>Timesheets</b></div></div>
<div class="card sc2"{ad(2, 260)}><div class="h">XÁC NHẬN ĐÃ ĐỌC · 702/731</div><div class="pbx" style="margin:0 0 10px"><i style="width:96%"></i></div>{''.join(f'<div class="ack">{av(n, 24)}{n}<em style="color:{c}">{s}</em></div>' for n, s, c in acks)}</div></div></div><span class="tagm">Giao diện minh hoạ</span></div>'''
    body = css + side + lib + det
    open('sol/rules.html', 'w').write(page('SOL trên Work rules', '/workrules', 'Work rules', WR_LOGO, body, 2))

goal_page(); rules_page(); print('ok')
