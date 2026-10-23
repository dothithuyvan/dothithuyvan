import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kit import *
# Townhall · Trang chủ (ảnh townhall/01) · Thông báo (02) · hôm nay 28/10/2026
CH = ['Toàn chuỗi', 'Văn phòng Điện Biên Phủ', 'Khối Nhà hàng', 'Bếp trung tâm', 'Miwaku', 'Kohaku']
css = '''<style>.tw{display:grid;grid-template-columns:600px 300px 1fr;gap:18px;padding:16px 20px;overflow:hidden;align-items:start}
.cp{padding:14px}.cp .in{display:flex;align-items:center;gap:10px;color:#9CA3AF;font-size:13.5px}.cp .ac{display:flex;gap:18px;margin-top:12px;padding-top:10px;border-top:1px solid #F3F4F6;font-size:12.5px;color:#374151}
.cp .ac span{display:flex;align-items:center;gap:6px}.ru{display:flex;align-items:center;margin:16px 0 10px;font-weight:700;font-size:14px}.ru small{margin-left:auto;font-weight:500;color:#6B7280;font-size:12px;display:flex;gap:14px}
.po{padding:14px}.po .ph{display:flex;align-items:center;gap:10px;font-size:13px}.po .ph b{color:#111827}.po .ph em{font-style:normal;color:#2563EB}
.an{margin-top:12px;border-radius:12px;padding:22px 20px;text-align:center;background:linear-gradient(135deg,#FFF7ED,#FDF2F8);position:relative;overflow:hidden}
.an::before{content:"";position:absolute;inset:0;background-image:radial-gradient(#F59E0B 1.5px,transparent 1.5px),radial-gradient(#3B82F6 1.5px,transparent 1.5px);background-size:46px 46px,62px 62px;background-position:0 0,20px 30px;opacity:.35}
.an *{position:relative}.an .row1{display:flex;align-items:center;justify-content:center;gap:16px}.an .bg{font-size:11px;font-weight:700;letter-spacing:.08em;color:#B45309}
.an .big{width:82px;height:82px;border-radius:50%;background:#DC2626;color:#fff;display:grid;place-items:center;font-size:30px;font-weight:700}.an .yr{font-size:15px;font-weight:700;color:#B45309}
.an h3{margin:14px 0 4px;font-size:22px;color:#111827}.an p{margin:6px 0 0;font-size:14px;color:#374151}.an .sm{font-size:12.5px;color:#6B7280}
.pf{display:flex;gap:16px;margin-top:12px;font-size:12px;color:#6B7280}.pf span{display:flex;align-items:center;gap:5px}
.lt .im{height:120px;background:#E5ECF6;display:grid;place-items:center;color:#94A3B8;position:relative}.lt .im em{position:absolute;left:10px;bottom:10px;font-style:normal;font-size:11px;background:rgba(15,23,42,.5);color:#fff;padding:2px 7px;border-radius:5px}
.lt .bx{padding:12px 14px}.lt .cap{font-size:10.5px;font-weight:700;letter-spacing:.06em;color:#6B7280}.lt h4{margin:6px 0 0;font:700 17px/1.3 Georgia,serif;color:#111827}
.la{padding:14px}.la h5{margin:0 0 10px;font-size:14px}.la .it{display:flex;gap:8px;margin-bottom:10px;font-size:13px}.la .it b{display:block;font-weight:600;color:#111827}.la .it small{color:#6B7280;font-size:11.5px}
.pp .cap{font-size:10.5px;font-weight:700;letter-spacing:.06em;color:#6B7280;margin:8px 0}.stk{display:flex}.stk .av{border:2px solid #fff;margin-left:-6px}.stk .av:first-child{margin-left:0}
.co{background:#C8102E;color:#fff;border-radius:10px;height:84px;display:grid;place-items:center;font-weight:700;font-size:18px}.mv{margin-top:14px;font-size:10.5px;font-weight:700;letter-spacing:.06em;color:#6B7280}.mv+p{margin:4px 0 0;font:14px/1.45 Georgia,serif;color:#111827}
.bk{margin-top:16px;border:1.5px dashed #D1D5DB;border-radius:10px;padding:12px;font-size:12px;color:#6B7280;line-height:1.5}
.ah{display:flex;align-items:center;gap:10px}.ann{max-width:900px;margin:22px auto 0}.ann h3{font-size:16px;margin:0 0 14px}.ann h3 em{font-style:normal;color:#6B7280;font-weight:500;font-size:13px;margin-left:6px}
.ac2{padding:16px 18px;margin-bottom:14px}.ac2 .t{display:flex;align-items:center;gap:8px;font-size:12.5px}.ac2 .t b{color:#111827}.ac2 .t time{margin-left:auto;color:#6B7280}
.ac2 h4{margin:10px 0 6px;font-size:17px;color:#111827}.ac2 p{margin:0;font-size:13px;color:#4B5563;line-height:1.55}</style>'''
def side(on):
    r = lambda ic, n, k: f'<div class="row {"on" if k == on else ""}">{ic}<span>{n}</span></div>'
    ch = ''.join(f'<div class="row" style="padding-left:24px;border-left:1px solid #E5E7EB;margin-left:16px;border-radius:0 7px 7px 0">{c}</div>' for c in CH)
    return f'''<div class="side"><div class="tt">{I('megaphone', 16)}Townhall</div>{r(I('house', 16), 'Trang chủ', 'home')}{r(av('Trần Ngọc Hân', 18), 'Trần Ngọc Hân', 'me')}{r(I('megaphone', 16), 'Thông báo', 'ann')}
<div class="sec">SOL</div>{r(I('mail', 16), 'Thư', 'l')}{r(I('book-open', 16), 'Nền tảng', 'f')}{r(I('cake', 16), 'Kỷ niệm', 'a')}{r(I('image', 16), 'Ảnh', 'p')}{r(I('calendar', 16), 'Sự kiện', 'e')}
<div class="sec">KÊNH</div><div class="row"><span class="ws" style="padding:0;height:auto"><i style="width:18px;height:18px;font-size:10px">S</i></span><span>SOL · {len(CH)}</span>{I('chevron-down', 13)}</div>{ch}
<div class="foot"><div class="row">{I('circle-check', 16)}<span>Phê duyệt</span></div><div class="row">{I('layout-grid', 16)}<span>Danh bạ</span></div><div class="row">{I('settings', 16)}<span>Cài đặt</span></div><div class="ws"><i>S</i>SOL</div></div></div>'''

ANN = [('Hành chính Nhân sự', 'Điều chỉnh quy định ca đóng cửa từ 01/11/2026', 'Ca đóng cửa kết thúc 23:30 tại các nhà hàng Miwaku và Kohaku. Giờ làm sau 22:00 tính phụ cấp làm đêm, chi tiết trong sổ tay nhân viên.', '28/10'),
       ('Bếp trung tâm', 'Lịch giao hàng nguyên liệu tươi tháng 11', 'Bếp trung tâm giao hai chuyến mỗi ngày, 06:30 và 14:00. Các nhà hàng chốt đơn nguyên liệu trước 21:00 hôm trước.', '26/10'),
       ('Toàn chuỗi', 'Chúc mừng Miwaku Thảo Điền đạt điểm hài lòng 4,8/5 quý III', 'Cảm ơn toàn đội nhà hàng. Kudos đã được gửi tới các thành viên trên Output.', '24/10'),
('Hành chính Nhân sự', 'Lịch làm việc dịp Tết Dương lịch 2027 tại các nhà hàng', 'Các nhà hàng mở cửa xuyên Tết Dương lịch. Nhân viên làm ngày 01/01/2027 được tính lương ngày lễ theo quy định; trưởng ca chốt lịch ca trên Timesheets trước 15/12.', '27/10'),
       ('Đào tạo', 'Mở đăng ký khoá Quản lý nhà hàng khoá 3', 'Dành cho trưởng ca có thâm niên từ 12 tháng. Học 6 buổi tại Văn phòng Điện Biên Phủ, kết thúc bằng 2 tuần điều hành độc lập tại nhà hàng. Đăng ký qua quản lý trực tiếp.', '22/10')]
CHC = {'Bếp trung tâm': ('#CCFBF1', '#0F766E'), 'Toàn chuỗi': ('#EDE9FE', '#6D28D9'), 'Hành chính Nhân sự': ('#FEF3C7', '#A16207'), 'Đào tạo': ('#DBEAFE', '#1D4ED8')}
chip = lambda c: f'<span class="chip" style="background:{CHC[c][0]};color:{CHC[c][1]}">{c}</span>'

home = f'''<div data-sc="0" style="flex:1;display:flex;min-width:0">{side('home')}<div class="main"><div class="tw">
<div><div class="card cp"{ad(0)}><div class="in">{av('Trần Ngọc Hân', 30)}Chia sẻ điều gì đó với cả đội…</div><div class="ac"><span>{I('file-text', 14)}Cập nhật</span><span>{I('sparkles', 14)}Định dạng</span><span>{I('megaphone', 14)}Thông báo</span><span>{I('chart-column', 14)}Bình chọn</span><span style="margin-left:auto">{I('plus', 14)}Thêm{I('chevron-down', 12)}</span></div></div>
<div class="ru">Cập nhật thường xuyên<small><span>Kênh trang chủ ▾</span><span>Cập nhật gần đây ▾</span></small></div>
<div class="card po"{ad(1, 160)}><div class="ph">{av('Trần Ngọc Hân', 30)}<div><b>Trần Ngọc Hân</b> đã chia sẻ một kỷ niệm › <em>Toàn chuỗi, Miwaku</em><div style="color:#9CA3AF;font-size:11.5px;margin-top:2px">28/10</div></div><span class="ml">{I('ellipsis', 16)}</span></div>
<div class="an"><div class="row1"><span class="bg">🎉 KỶ NIỆM</span><span class="big">PB</span><span class="yr">2 NĂM</span></div><h3>Phan Gia Bảo – 2 năm ở bếp Miwaku Thảo Điền</h3><div class="sm">Phan Gia Bảo · 28/10/2026</div><p>Từ phụ bếp ngày đầu đến người giữ khu sơ chế chuẩn nhất chuỗi. Chúc mừng Bảo!</p></div>
<div class="pf"><span>{I('circle-check', 13)}Đã xem 46 người</span><span>{I('smile', 13)}Bày tỏ</span><span>{I('message-square', 13)}Bình luận</span><span>{I('bookmark', 13)}Lưu</span><span>{I('pin', 13)}Ghim</span></div></div>
<div class="card po" style="margin-top:12px"{ad(2, 220)}><div class="ph">{av('Nguyễn Hoàng Phúc', 30)}<div><b>Nguyễn Hoàng Phúc</b> đã đăng một cập nhật › <em>Miwaku</em><div style="color:#9CA3AF;font-size:11.5px;margin-top:2px">27/10</div></div><span class="ml">{I('ellipsis', 16)}</span></div>
<p style="margin:12px 0 0;font-size:14px;color:#1F2937;line-height:1.55">Miwaku Landmark 81 đã nghiệm thu bếp và PCCC. Tuần sau 22 bạn mới bắt đầu 2 tuần đào tạo tại Miwaku Thảo Điền, mỗi bạn có một người kèm. Cảm ơn đội Thảo Điền nhận thêm việc này!</p>
<div class="pf"><span>{I('circle-check', 13)}Đã xem 128 người</span><span>{I('smile', 13)}Bày tỏ · 34</span><span>{I('message-square', 13)}Bình luận · 9</span><span>{I('bookmark', 13)}Lưu</span></div></div></div>
<div><div class="card lt"{ad(2, 220)}><div class="im">{I('mail', 30)}<em>20/10/2026</em></div><div class="bx"><div class="cap">THƯ BAN ĐIỀU HÀNH · SOL</div><h4>Mùa cao điểm cuối năm: ba việc mỗi nhà hàng cần làm</h4></div></div>
<div class="card la" style="margin-top:14px"{ad(3, 260)}><h5>Thông báo mới nhất</h5>{''.join(f'<div class="it">{I("megaphone", 15)}<div><b>{t}</b><small>Trần Ngọc Hân · {d}</small></div></div>' for _, t, _, d in ANN)}</div>
<div class="card la pp" style="margin-top:14px"{ad(4, 300)}><h5>Con người SOL</h5><div class="cap">MỚI GIA NHẬP</div><div class="stk">{''.join(av(n, 26) for n in ['Trần Bảo Châu', 'Lâm Gia Huy', 'Phùng Thảo My', 'Phạm Quốc Thái', 'Đinh Gia Hưng', 'Nguyễn Khánh Vy'])}</div>
<div class="cap" style="margin-top:12px">KỶ NIỆM GẦN ĐÂY</div><div class="it" style="display:flex;gap:8px;align-items:center;font-size:13px">{av('Đặng Thanh Tú', 24)}<div><b>Đặng Thanh Tú</b><small style="display:block;color:#6B7280">Thứ Bảy</small></div></div></div></div>
<div{ad(5, 340)}><div class="co">SOL</div><div class="mv">SỨ MỆNH</div><p>Chuỗi nhà hàng phong cách Nhật Bản với nhiều thương hiệu được yêu thích.</p><div class="mv">TẦM NHÌN</div><p>200 nhà hàng vào năm 2028.</p>
<div class="bk">Bạn chưa đánh dấu trang Nền tảng nào. Ghim sổ tay nhân viên hoặc giá trị cốt lõi để hiện ở đây.</div></div></div></div></div>'''

annp = f'''<div data-sc="1" style="flex:1;display:flex;min-width:0">{side('ann')}<div class="main"><div class="hd"><span class="t">Thông báo</span><span class="chip c-b">● {len(ANN)} chưa đọc</span><span class="ml"></span>{I('search', 16)}<span style="font-size:13px;color:#374151">Lọc ›</span><span class="btn gh">{I('plus', 14)}Thông báo mới</span></div>
<div class="ann"><h3>Thông báo trước đó<em>{len(ANN)}</em></h3>{''.join(f'<div class="card ac2"{ad(i, 140, 90)}><div class="t">{av("Trần Ngọc Hân", 30)}<b>Trần Ngọc Hân</b>{chip("Toàn chuỗi")}{chip(c)}<time>{d}</time></div><h4>{t}</h4><p>{m}</p></div>' for i, (c, t, m, d) in enumerate(ANN))}</div></div></div>'''

open('sol/townhall.html', 'w').write(page('SOL trên Townhall', '/townhall/home', 'Townhall', logo('townhall'), css + home + annp, 2))
print('ok')
