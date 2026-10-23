import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# Output · Mục tiêu (ảnh output/03) · Phản hồi (01) · Ghi nhận – The Wall (04) · hôm nay 28/10/2026
RAIL = [('award', 'Đầu ra'), ('target', 'Mục tiêu'), ('trending-up', 'Dự báo'), ('message-circle', 'Phản hồi'), ('circle-check', 'Check-in'), ('gift', 'Ghi nhận'), ('star', 'Xếp hạng')]
def rail(on):
    it = ''.join(f'<div class="ri {"on" if n == on else ""}"><i>{I(ic, 17)}</i><span>{n}</span></div>' for ic, n in RAIL)
    return f'<div class="rail">{it}<div class="rf">{I("settings", 17)}<span class="wsq">S</span></div></div>'

css = '''<style>.rail{width:70px;flex:none;border-right:1px solid #E5E7EB;display:flex;flex-direction:column;align-items:center;padding:10px 0;gap:4px}
.ri{display:flex;flex-direction:column;align-items:center;gap:3px;font-size:10px;color:#6B7280;width:62px;padding:4px 0}.ri i{width:34px;height:34px;border-radius:50%;display:grid;place-items:center}
.ri.on i{background:#DBEAFE;color:#1D4ED8}.ri.on{color:#1D4ED8;font-weight:600}.rf{margin-top:auto;display:flex;flex-direction:column;align-items:center;gap:12px;color:#6B7280}
.wsq{width:26px;height:26px;border-radius:7px;background:#C8102E;color:#fff;display:grid;place-items:center;font-size:12px;font-weight:700}
.s2{width:210px;flex:none;border-right:1px solid #E5E7EB;padding:12px 10px;display:flex;flex-direction:column;gap:2px}.s2 .tt{display:flex;align-items:center;gap:8px;font-weight:700;font-size:14px;padding:4px 8px 10px}
.gk{display:grid;grid-template-columns:repeat(5,1fr);gap:14px;margin:20px 60px 0}.gk .kpi b{font-size:30px}.gk .k1{border:1.5px solid #2563EB}
.gh{display:flex;align-items:center;gap:10px;margin:22px 60px 6px;font-weight:700;font-size:15px;color:#111827}.gh .tg{font-size:11px;font-weight:600;background:#F3F4F6;color:#4B5563;padding:2px 7px;border-radius:5px}
.gh .pr{margin-left:auto;display:flex;align-items:center;gap:8px;font-size:12px;font-weight:500;color:#6B7280}.gh .pr i{width:120px;height:4px;border-radius:2px;background:#E5E7EB;position:relative;overflow:hidden}.gh .pr i b{position:absolute;left:0;top:0;bottom:0;background:#2563EB}
.gl{margin:0 60px;border-top:1px solid #F3F4F6}.gr{display:flex;align-items:center;gap:12px;height:40px;border-bottom:1px solid #F3F4F6;font-size:13.5px;font-weight:600;color:#111827}
.gr.dn .tx{text-decoration:line-through;color:#9CA3AF;font-weight:500}.gr .rt{margin-left:auto;display:flex;align-items:center;gap:12px;font-size:12px;color:#6B7280;font-weight:500}
.gr .od{color:#DC2626}.gr .ok{color:#16A34A}.gr .ci{color:#9CA3AF}
.fb{margin:0 22px;border:1px solid #E5E7EB;border-radius:10px}.fbr{display:flex;gap:12px;padding:14px 16px;border-bottom:1px solid #F3F4F6}.fbr:last-child{border-bottom:0}
.fbr .tx b{font-size:14px;color:#111827}.fbr .tx p{margin:4px 0 6px;font-size:13px;color:#4B5563;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:820px}
.fbr .mt{display:flex;align-items:center;gap:8px;font-size:12px;color:#6B7280}.fbr .em{margin-left:auto;align-self:center}
.tabs{display:flex;gap:18px;font-size:13px;color:#6B7280;height:56px;align-items:center}.tabs span.on{color:#111827;font-weight:600;box-shadow:inset 0 -2px #2563EB;height:56px;display:flex;align-items:center}
.wl{display:grid;grid-template-columns:1fr 290px;gap:18px;padding:18px 22px}.wk{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:16px}
.kd{border:1px solid #E5E7EB;border-radius:10px;overflow:hidden;margin-bottom:14px}.kd .bn{height:44px;background:#EA580C;background-image:radial-gradient(rgba(255,255,255,.18) 1.5px,transparent 1.5px);background-size:12px 12px;color:#fff;display:flex;align-items:center;padding:0 14px;font-size:11.5px;font-weight:700;letter-spacing:.06em}
.kd .bn em{margin-left:auto;font-style:normal;display:flex;align-items:center;gap:5px}.kd .bd{padding:12px 14px}.kd .fl{display:flex;align-items:center;gap:8px;font-size:13px;font-weight:600}
.kd .msg{margin:8px 0;font-size:13px;color:#374151}.ht{display:inline-block;font-size:11px;padding:2px 7px;border-radius:5px;margin-right:6px;font-weight:600}
.kd .ft{display:flex;align-items:center;gap:12px;padding:8px 14px;border-top:1px solid #F3F4F6;font-size:12px;color:#6B7280}.kd .ft span:last-child{margin-left:auto}
.tp{padding:14px}.tp .h{font-size:11px;font-weight:700;letter-spacing:.05em;color:#6B7280;margin-bottom:8px}.tpr{display:flex;align-items:center;gap:10px;height:34px;font-size:13px;font-weight:600}
.tpr i{width:20px;height:20px;border-radius:5px;display:grid;place-items:center;font-style:normal;font-size:11px;background:#F3F4F6}.tpr i.g{background:#FDE68A}.tpr em{margin-left:auto;font-style:normal;font-size:11.5px;background:#FEF3C7;color:#A16207;padding:2px 7px;border-radius:5px}</style>'''

# ---- 1 · Mục tiêu (từ Project: dự án khai trương nhà hàng) ----
G = [  # [tên, trạng thái d/p/o, ngày, người]
 ('Ký hợp đồng mặt bằng Miwaku Landmark 81', 'd', 'Xong 12/08', 'Nguyễn Hoàng Phúc'),
 ('Hoàn thiện thiết kế và thi công nội thất', 'd', 'Xong 30/09', 'Nguyễn Hoàng Phúc'),
 ('Lắp đặt bếp, nghiệm thu PCCC', 'd', 'Xong 15/10', 'Lê Thị Thu Thảo'),
 ('Chốt thực đơn và công thức chuẩn', 'd', 'Xong 20/10', 'Lê Thị Thu Thảo'),
 ('Hồ sơ giấy phép ATTP', 'd', 'Xong 24/10', 'Trần Ngọc Hân'),
 ('Tuyển đủ 22 nhân sự khai trương', 'o', '25/10', 'Trần Ngọc Hân'),
 ('Đào tạo nhân viên mới 2 tuần tại Miwaku Thảo Điền', 'p', '01/11 – 14/11', 'Võ Minh Quân'),
 ('Điều chuyển trưởng ca từ các nhà hàng Miwaku', 'p', '03/11', 'Nguyễn Hoàng Phúc'),
 ('Chạy thử nội bộ (soft opening)', 'p', '18/11', 'Võ Minh Quân'),
 ('Khai trương chính thức', 'p', '22/11', 'Nguyễn Hoàng Phúc'),
]
GK = (86, 52, 19, 13, 2)   # tất cả, kế hoạch, đang làm, hoàn thành, thất bại
assert GK[0] == sum(GK[1:])
nd = sum(1 for g in G if g[1] == 'd')
def goals():
    rows = ''
    for i, (t, s, d, p) in enumerate(G):
        ico = I('circle-check', 17, 2, '#16A34A') if s == 'd' else I('circle-dot' if s == 'o' else 'circle', 17, 2, '#9CA3AF')
        dt = f'<span class="ok">{I("check", 13)}</span><span>{d}</span>' if s == 'd' else f'<span class="od" style="display:flex;align-items:center;gap:4px">{I("triangle-alert", 13)}{d}</span>' if s == 'o' else f'<span class="ci" style="display:flex;align-items:center;gap:4px">{I("clock", 13)}<span style="color:#6B7280">{d}</span></span>'
        rows += f'<div class="gr {"dn" if s == "d" else ""}"{ad(i, 200, 45)}>{ico}<span class="tx">{t}</span><span class="rt">{dt}{av(p, 22)}</span></div>'
    kp = ''.join(f'<div class="card kpi {"k1" if i == 0 else ""}"{ad(i, 60, 40)}><span>{n}</span><b style="color:{c}">{v}</b></div>' for i, (n, v, c) in enumerate([('Tất cả mục tiêu', GK[0], '#111827'), ('Kế hoạch', GK[1], '#6B7280'), ('Đang làm', GK[2], '#2563EB'), ('Hoàn thành', GK[3], '#16A34A'), ('Thất bại', GK[4], '#DC2626')]))
    return f'''<div data-sc="0" style="flex:1;display:flex;min-width:0">{rail('Mục tiêu')}<div class="s2"><div class="tt">{I('menu', 15)}Mục tiêu</div><div class="row on">{I('target', 15)}<span>Tất cả mục tiêu</span></div>
<div class="foot"><div class="row">{I('chart-column', 15)}<span>Báo cáo</span></div><div class="row">{I('file-text', 15)}<span>Mẫu</span></div></div></div>
<div class="main"><div class="hd">{I('target', 16)}<span class="t">Mục tiêu</span><span class="n">{GK[0]} mục tiêu từ 1 ứng dụng</span><span class="ml"></span><span class="q">{I('search', 14)}Tìm mục tiêu…</span></div>
<div class="gk">{kp}</div><div class="gh">Khai trương Miwaku Landmark 81<span class="tg">Project</span><span class="pr"><i><b style="width:{nd/len(G)*100:.0f}%"></b></i>{nd}/{len(G)} hoàn thành</span></div><div class="gl">{rows}</div></div></div>'''

# ---- 2 · Phản hồi ----
F = [('Phản hồi 1:1 tháng 10 – Trương Mỹ Linh', 'Linh điều hành ca tối rất chắc, giờ cao điểm thứ Bảy không để bàn chờ quá 10 phút. Cần luyện thêm phần lập lịch ca cả tháng trước khi lên quản lý.', 'Tuyệt vời', 'c-v'),
     ('Phản hồi sau đợt kiểm tra ATTP – Lê Thị Thu Thảo', 'Bếp Miwaku Thảo Điền đạt 96/100 điểm kiểm tra nội bộ. Ghi nhãn ngày mở hộp nguyên liệu đầy đủ; khu sơ chế hải sản cần sắp lại kệ.', 'Tốt', 'c-g'),
     ('Phản hồi 1:1 tháng 10 – Hồ Tấn Phát', 'Tay nghề sushi ổn định, khách phản hồi tốt món omakase. Nên kèm thêm hai phụ bếp mới trong tháng 11.', 'Tốt', 'c-g'),
     ('Phản hồi 1:1 tháng 10 – Ngô Bảo Trâm', 'Chuẩn bị nguyên liệu đầu ca nhanh hơn tháng trước 15 phút. Cần chú ý độ đều của cơm sushi giờ cao điểm.', 'Tốt', 'c-g'),
     ('Phản hồi sau ca đông khách thứ Bảy – Mai Đức Thịnh', 'Giữ bếp gọn trong giờ cao điểm, không để món chờ quá 12 phút. Nên học thêm khâu sơ chế cá hồi.', 'Tốt', 'c-g'),
     ('Phản hồi kết thúc thử việc – Châu Ngọc Ánh', 'Hoàn thành checklist hội nhập, đạt bài kiểm tra ATTP. Đề xuất ký hợp đồng chính thức từ 01/11.', 'Tuyệt vời', 'c-v'),
     ('Phản hồi sau tiệc đặt trước 40 khách – Lý Minh Khang', 'Phục vụ tiệc 27/10 đúng kịch bản, khách đặt lại tiệc cuối năm. Lưu ý xác nhận dị ứng thực phẩm trước khi lên món.', 'Tốt', 'c-g')]
def feedbacks():
    rows = ''.join(f'''<div class="fbr"{ad(i, 120, 70)}>{av('Võ Minh Quân', 30)}<div class="tx"><b>{t}</b><p>{m}</p><div class="mt">Bạn · <span class="chip c-b">{I('message-square', 12)}Phản hồi 1:1 và sau sự kiện</span> · 27/10/2026</div></div><span class="em chip {c}">{I('smile', 13)}{e}</span></div>''' for i, (t, m, e, c) in enumerate(F))
    return f'''<div data-sc="1" style="flex:1;display:flex;min-width:0">{rail('Phản hồi')}<div class="s2"><div class="tt">{I('menu', 15)}Phản hồi</div><div class="row on">{I('message-square', 15)}<span>Phản hồi</span></div><div class="row">{I('user-plus', 15)}<span>Được giao</span></div>
<div class="sec">PHẢN HỒI VẬN HÀNH</div><div class="row">{I('message-square', 15)}<span>Phản hồi 1:1 và sau sự kiện</span></div>
<div class="foot"><div class="row">{I('chart-column', 15)}<span>Báo cáo</span></div><div class="row">{I('file-text', 15)}<span>Mẫu</span></div></div></div>
<div class="main"><div class="hd" style="height:56px"><span class="t">Phản hồi</span><div class="tabs" style="margin-left:14px"><span class="on">Tất cả</span><span>Đã gửi</span><span>Đã nhận</span></div><span class="ml"></span><span class="q">{I('search', 14)}Tìm phản hồi…</span><span class="btn gh">Tất cả dịch vụ{I('chevron-down', 13)}</span><span class="btn">{I('plus', 14)}Mới</span></div>
<div style="padding:16px 22px 8px;font-size:11px;font-weight:700;letter-spacing:.06em;color:#6B7280">GẦN ĐÂY <span style="background:#F3F4F6;padding:1px 6px;border-radius:5px">{len(F)}</span></div><div class="fb">{rows}</div></div></div>'''

# ---- 3 · Ghi nhận · The Wall ----
K = [('Nguyễn Hoàng Phúc', 'Võ Minh Quân', 60, [('#lanh-dao-ca', '#EDE9FE', '#6D28D9')], ''),
     ('Võ Minh Quân', 'Hồ Tấn Phát', 50, [('#vi-khach-hang', '#FFEDD5', '#C2410C')], 'Cảm ơn Phát ở lại hỗ trợ tiệc 40 khách tối 27/10, sushi platter lên đúng giờ.'),
     ('Trương Mỹ Linh', 'Lý Minh Khang', 40, [('#dong-doi-tin-cay', '#DBEAFE', '#1D4ED8')], 'Khang nhận thêm ca đóng cửa khi bạn trong ca nghỉ ốm, không để nhà hàng thiếu người.'),
     ('Lê Thị Thu Thảo', 'Mai Đức Thịnh', 30, [('#dung-chuan', '#DCFCE7', '#15803D')], 'Thịnh giữ khu sơ chế sạch nhất đợt kiểm tra ATTP tháng 10.')]
TOP = [('Hồ Tấn Phát', 120), ('Lý Minh Khang', 90), ('Trương Mỹ Linh', 80), ('Ngô Bảo Trâm', 60), ('Mai Đức Thịnh', 50)]
def wall():
    kd = ''.join(f'''<div class="kd"{ad(i, 200, 90)}><div class="bn">GHI NHẬN ĐỒNG ĐỘI (KUDOS)<em>{I('link', 13)}{p}</em></div><div class="bd"><div class="fl">{av(a, 26)}{a}<span style="color:#9CA3AF">→</span>{av(b, 22)}{b}</div><div style="height:8px"></div>{''.join(f'<span class="ht" style="background:{bg};color:{fg}">{h}</span>' for h, bg, fg in hs)}</div>
<div class="ft"><span style="display:flex;align-items:center;gap:4px">{I('heart', 13)}3</span><span style="display:flex;align-items:center;gap:4px">{I('message-square', 13)}1</span><span>28/10/2026</span></div></div>''' for i, (a, b, p, hs, m) in enumerate(K))
    tp = ''.join(f'<div class="tpr"><i class="{"g" if i == 0 else ""}">{i + 1}</i>{n}<em>{v}</em></div>' for i, (n, v) in enumerate(TOP))
    wk = ''.join(f'<div class="card kpi"><span>{n}</span><b style="color:{c}">{v}<small style="display:inline;font-size:12px;font-weight:500"> {u}</small></b></div>' for n, v, c, u in [('Số dư của bạn', 260, '#EA580C', 'điểm'), ('Nhận trong tháng', 40, '#111827', 'điểm'), ('Đã tặng trong tháng', 120, '#111827', 'điểm'), ('Danh mục', 1, '#111827', '')])
    return f'''<div data-sc="2" style="flex:1;display:flex;min-width:0">{rail('Ghi nhận')}<div class="s2"><div class="tt">{I('menu', 15)}Ghi nhận</div><div class="row on">{I('layout-grid', 15)}<span>The Wall</span></div><div class="row">{I('user', 15)}<span>Hồ sơ của tôi</span></div>
<div class="sec">GHI NHẬN</div><div class="row">{I('layers', 15)}<span>Danh mục</span></div><div class="row">{I('gift', 15)}<span>Danh mục quà</span></div><div class="row">{I('users', 15)}<span>Nhân sự</span></div>
<div class="sec">QUẢN TRỊ</div><div class="row">{I('wallet', 15)}<span>Ngân sách</span></div><div class="row">{I('receipt-text', 15)}<span>Giao dịch</span></div>
<div class="foot"><div class="row">{I('layers', 15)}<span>Dịch vụ</span></div><div class="row">{I('settings', 15)}<span>Cài đặt</span></div></div></div>
<div class="main"><div class="hd"><span class="t">The Wall</span>{I('chevron-right', 14)}<div class="tabs"><span class="on">Tất cả kudos</span><span>Đã nhận</span><span>Đã tặng</span></div><span class="ml"></span><span class="btn">{I('plus', 14)}Tặng kudos</span></div>
<div class="wl" style="overflow:hidden"><div><div class="wk">{wk}</div>{kd}</div><div><div class="card tp"><div class="h">NHẬN NHIỀU NHẤT THÁNG NÀY</div>{tp}</div><div class="card tp" style="margin-top:14px"><div class="h">DANH MỤC</div><div style="display:flex;align-items:center;gap:8px;font-size:13px"><i class="dot" style="background:#EA580C"></i>Ghi nhận đồng đội (Kudos)</div></div></div></div></div></div>'''

body = css + goals() + feedbacks() + wall()
open('sol/output.html', 'w').write(page('SOL trên Output', '/output/goals', 'Output', logo('output'), body, 3))
print('ok')
