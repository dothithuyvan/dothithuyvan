# Đổi dữ liệu mock Academy (khung TOANPHAT) sang SOL · hôm nay T4 28/10/2026
import os, re
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
s = open('src/academy_goc.html').read()
def R(o, n, cnt=None):
    global s
    if o not in s: raise SystemExit('THIẾU: ' + o[:90])
    s = s.replace(o, n) if cnt is None else s.replace(o, n, cnt)
def RX(pat, n):
    global s
    s2 = re.sub(pat, n, s, flags=re.S)
    if s2 == s: raise SystemExit('THIẾU regex: ' + pat[:80])
    s = s2

RX(r"const P = \{.*?\n\};", """const P = {
  bao: { name: 'Nguyễn Thu Trang', t: 'Chuyên viên Marketing', g: '96,165,250|29,78,216', e: 'trang.nt' },
  khai: { name: 'Trương Mỹ Linh', t: 'Trưởng ca', g: '253,186,116|234,88,12', e: 'linh.tm' },
  anh: { name: 'Trần Ngọc Hân', t: 'Chuyên viên C&B', g: '249,168,212|219,39,119', e: 'han.tn' },
  hanh: { name: 'Lê Thị Thu Thảo', t: 'Bếp trưởng thương hiệu', g: '94,234,212|13,148,136', e: 'thao.ltt' },
  phuc: { name: 'Nguyễn Hoàng Phúc', t: 'Quản lý thương hiệu Miwaku', g: '134,239,172|22,163,74', e: 'phuc.nh' },
  trang: { name: 'Đoàn Thị Kim Oanh', t: 'Trưởng phòng Đào tạo', g: '253,164,175|225,29,72', e: 'oanh.dtk' },
  long: { name: 'Võ Minh Quân', t: 'Quản lý nhà hàng', g: '252,211,77|202,138,4', e: 'quan.vm' },
  thu: { name: 'Phạm Gia Huy', t: 'Quản lý thương hiệu Kohaku Sushi', g: '103,232,249|8,145,178', e: 'huy.pg' },
  tam: { name: 'Hồ Tấn Phát', t: 'Đầu bếp sushi', g: '165,180,252|79,70,229', e: 'phat.ht' },
  ngan: { name: 'Đặng Thanh Tú', t: 'Quản lý nhà hàng', g: '216,180,254|147,51,234', e: 'tu.dt' },
};""")
R("<b>toanphat.base.vn</b>", "<b>sol.base.vn</b>")
R("<div class=\"ws\"><i>T</i>TOANPHAT Group", "<div class=\"ws\"><i style=\"background:#C8102E\">S</i>SOL")
R("const PROG = 'Chuẩn bị lên Kỹ sư vận hành';", "const PROG = 'Chuẩn bị lên Quản lý nhà hàng';")
RX(r"const COURSES = \[.*?\n\];", """const COURSES = [ // [mã màu, tên, số bài, thời lượng, tiến độ %, trạng thái, học viên, sao]
  ['#2563EB', 'An toàn thực phẩm và vệ sinh bếp Nhật', 8, '3h 30m', 100, 'done', 212, '4,7'],
  ['#0D9488', 'Omotenashi: phục vụ theo phong cách Nhật', 12, '6h', 100, 'done', 186, '4,8'],
  ['#D97706', 'Quản lý ca và lập lịch ca (bắt buộc)', 14, '7h 20m', 64, 'act', 58, '4,6'],
  ['#7C3AED', 'Kiểm soát chi phí và hao hụt nguyên liệu', 10, '5h', 0, 'up', 41, '4,5'],
  ['#DB2777', 'Xử lý phàn nàn và giữ chân khách', 6, '3h', 0, 'up', 37, '4,9'],
];""")
R("'An toàn bức xạ (bắt buộc)'", "'An toàn thực phẩm (bắt buộc)'")
R("'Kho lạnh & xe nâng an toàn'", "'Đầu bếp sushi cơ bản'")
# trang chủ
R("<b>Chào Trí 👋</b><small>Thứ Tư, 14 tháng 10</small>", "<b>Chào Linh 👋</b><small>Thứ Tư, 28 tháng 10</small>")
R("Chào mừng quay lại, Trí!", "Chào mừng quay lại, Linh!")
R("Bài 10/14 · Giới hạn liều một lần vào vùng kiểm soát", "Bài 10/14 · Định biên ca theo lượt khách")
R("const ev = { 15: 1, 19: 1, 21: 1 };", "const ev = { 29: 1, 30: 1, 31: 1 };")
R("${d === 14 ? 'td' : ''}", "${d === 28 ? 'td' : ''}")
R("<b>Diễn tập: ứng phó sự cố kẹt nguồn Cobalt-60</b><span>Thứ Năm 15/10 · 14:30 · Phòng đào tạo Nhà máy Chiếu xạ</span>", "<b>Hạn nộp bài kiểm tra chương 3</b><span>Thứ Năm 29/10 · 17:00</span>")
R("<b>Hạn nộp bài kiểm tra chương 3</b><span>Thứ Hai 19/10 · 17:00</span>", "<b>Khai giảng: Kiểm soát chi phí và hao hụt nguyên liệu</b><span>Thứ Sáu 30/10 · 08:30 · Văn phòng Điện Biên Phủ</span>")
R("<b>Khai giảng: Quy trình chứng từ xuất khẩu đi Mỹ (APHIS)</b><span>Thứ Tư 21/10 · 08:30</span>", "<b>Thực hành: điều hành ca tối thứ Bảy</b><span>Thứ Bảy 31/10 · 17:00 · Miwaku Thảo Điền</span>")
# chương trình
R("Chương trình cho nhân viên vận hành chuẩn bị lên bậc Kỹ sư vận hành chiếu xạ, gắn với lộ trình Nhân viên vận hành → Kỹ sư vận hành chiếu xạ trên Careers.",
  "Chương trình cho trưởng ca chuẩn bị lên Quản lý nhà hàng, gắn với kế hoạch thăng cấp Trưởng ca → Quản lý nhà hàng trên Careers.")
# khoá học
R("['Chương 1 · Bức xạ ion hoá và đơn vị liều', 4, '1h 50m', 'd'], ['Chương 2 · Nguồn Cobalt-60 và hệ thống che chắn', 4, '2h 10m', 'd'], ['Chương 3 · Kiểm soát liều cá nhân', 3, '1h 40m', 'c'], ['Chương 4 · Ứng phó sự cố và báo cáo', 3, '1h 40m', '']",
  "['Chương 1 · Vai trò của trưởng ca và quản lý nhà hàng', 4, '1h 50m', 'd'], ['Chương 2 · Dự báo lượt khách theo giờ', 4, '2h 10m', 'd'], ['Chương 3 · Định biên và lập lịch ca', 3, '1h 40m', 'c'], ['Chương 4 · Xử lý thiếu người và đổi ca', 3, '1h 40m', '']")
R("PL-2026-0044 · Lên Kỹ sư vận hành chiếu xạ", "PL-2026-0014 · Lên Quản lý nhà hàng")
# học bài
R("const CH3 = [['9', 'Liều kế cá nhân và cách đọc kết quả', '12:40', 'd', 'play'], ['10', 'Giới hạn liều một lần vào vùng kiểm soát', '14:30', 'c', 'play']",
  "const CH3 = [['9', 'Đọc báo cáo lượt khách theo giờ', '12:40', 'd', 'play'], ['10', 'Định biên ca theo lượt khách', '14:30', 'c', 'play']")
R("const LC = [10000, 20000, 30000], HT = [4, 6, 8], DER = { 4: 1, 6: 1, 8: 1 };\nconst cap = (lc, h) => Math.round(lc * h / 1000 * DER[h]);",
  "// số phục vụ cần = lượt khách mỗi giờ ÷ số khách một người phục vụ được mỗi giờ; ca tối có 6 phục vụ (giả định)\nconst LC = [20, 40, 60], HT = [4, 6, 8];\nconst cap = (lc, h) => Math.ceil(lc / h);")
R("const c = v <= 100 ? 'g' : v <= 160 ? 'y' : 'r'; return `<td class=\"${c}${lc === 20000 && h === 4 ? ' base' : ''}\">${v.toLocaleString('vi-VN')} µSv</td>`;",
  "const c = v <= 6 ? 'g' : v <= 8 ? 'y' : 'r'; return `<td class=\"${c}${lc === 40 && h === 6 ? ' base' : ''}\">${v} người</td>`;")
R("<th>Suất liều \\\\ Thời gian</th>${HT.map(h => `<th>${String(h).replace('.', ',')} giờ</th>`).join('')}", "<th>Khách/giờ \\\\ Khách mỗi phục vụ</th>${HT.map(h => `<th>${h} khách/giờ</th>`).join('')}")
R("<th>${(lc / 1000).toLocaleString('vi-VN')} µSv/h</th>", "<th>${lc} khách/giờ</th>")
R("${ch('Chương 1 · Bức xạ ion hoá và đơn vị liều', 4, 4, 'd')}${ch('Chương 2 · Nguồn Cobalt-60 và hệ thống che chắn', 4, 4, 'd')}${ch('Chương 3 · Kiểm soát liều cá nhân', '<span id=\"c3k\">1</span>', 3, '', 1)}${ch('Chương 4 · Ứng phó sự cố và báo cáo', 0, 3, '')}",
  "${ch('Chương 1 · Vai trò của trưởng ca và quản lý', 4, 4, 'd')}${ch('Chương 2 · Dự báo lượt khách theo giờ', 4, 4, 'd')}${ch('Chương 3 · Định biên và lập lịch ca', '<span id=\"c3k\">1</span>', 3, '', 1)}${ch('Chương 4 · Xử lý thiếu người và đổi ca', 0, 3, '')}")
R("<b>Liều tích luỹ theo suất liều và thời gian ở vùng kiểm soát</b>", "<b>Số phục vụ cần theo lượt khách mỗi giờ</b>")
R("Liều = suất liều × thời gian · tự vào tới <b>100 µSv</b> · trên <b>160 µSv</b> không được vào", "Ca tối có <b>6 phục vụ</b> · 7–8 người: gọi thêm bán thời gian · trên <b>8 người</b>: mở thêm khu, giới hạn khách vào")
R("<h1>Giới hạn liều một lần vào vùng kiểm soát</h1>", "<h1>Định biên ca theo lượt khách</h1>")
R("Đổi suất liều và thời gian để thấy liều tích luỹ một lần vào; ô vàng (100–160 µSv) cần Tổ An toàn bức xạ cấp phép, ô đỏ vượt 160 µSv, không được vào.",
  "Đổi lượt khách và năng suất phục vụ để thấy số người cần trong ca; ô vàng cần gọi thêm nhân viên bán thời gian trên Timesheets, ô đỏ phải mở thêm khu hoặc giới hạn khách.")
R("Bang_tra_lieu_tich_luy_vung_kiem_soat.xlsx", "Bang_dinh_bien_ca_theo_luot_khach.xlsx")
# báo cáo
pass
# bài kiểm tra
RX(r"const QZ = \[.*?\n\];", """const QZ = [
  ['Giờ cao điểm tối thứ Bảy tại Miwaku thường rơi vào khung nào?', 'Trắc nghiệm · 1 điểm'],
  ['Báo cáo lượt khách theo giờ lấy từ đâu?', 'Trắc nghiệm · 1 điểm'],
  ['Một phục vụ phục vụ tốt tối đa bao nhiêu khách mỗi giờ khi có omakase?', 'Trắc nghiệm · 1 điểm'],
  ['Lịch ca tuần sau phải công bố trên Timesheets trước ngày nào?', 'Trắc nghiệm · 1 điểm'],
  ['Ai duyệt yêu cầu đổi ca của nhân viên phục vụ?', 'Trắc nghiệm · 1 điểm'],
  ['Đổi ca phải gửi trước ít nhất bao lâu?', 'Trắc nghiệm · 1 điểm'],
  ['Nhân viên bán thời gian được xếp tối đa mấy ca mỗi tuần?', 'Trắc nghiệm · 1 điểm'],
  ['Làm sau 22:00 được tính phụ cấp gì?', 'Trắc nghiệm · 1 điểm'],
  ['Khi thiếu người đột xuất, việc đầu tiên trưởng ca làm là gì?', 'Trắc nghiệm · 1 điểm'],
  ['Tối thứ Bảy dự kiến 40 khách/giờ, mỗi phục vụ được 6 khách/giờ, ca có 6 người…', 'Chấm bằng AI · 5 điểm', 1],
];""")
R("const QTXT = 'Trưởng ca báo suất liều tại cửa buồng chiếu xạ là 20 µSv/h, việc bảo trì băng tải dự kiến làm 6 giờ. Anh/chị xử lý thế nào trước khi cho người vào vùng kiểm soát, và vì sao?';",
  "const QTXT = 'Tối thứ Bảy nhà hàng dự kiến 40 khách/giờ từ 18:00 đến 21:00, mỗi phục vụ phục vụ tốt 6 khách/giờ, ca tối hiện có 6 phục vụ. Anh/chị xử lý thế nào trước giờ mở cửa, và vì sao?';")
RX(r"const RUB = '.*?';", "const RUB = 'Điểm tối đa khi: (1) tính đúng cần 7 phục vụ, (2) nêu đúng phải gọi thêm 1 nhân viên bán thời gian hoặc đổi ca trên Timesheets trước 24 giờ, (3) đề xuất mở thêm khu và báo bếp khi lượt khách vượt 48/giờ. Một nửa điểm nếu có 2 trong 3 ý. Không điểm nếu giữ nguyên 6 người.';")
# sổ điểm
RX(r"const GBR = \[.*?\n\];", """const GBR = [ // [tên, nhà hàng, đã học %, ch1, ch2, ch3, điểm khoá]
  ['Trương Mỹ Linh', 'Miwaku Thảo Điền', 71, 90, 85, 'p', ''],
  ['Bùi Quang Vinh', 'Miwaku Thảo Điền', 100, 95, 90, 86, 90],
  ['Nguyễn Thị Diễm', 'Kohaku Sushi Phan Xích Long', 79, 100, 95, 'p', ''],
  ['Lương Văn Hậu', 'Kohaku Sashimi & Yakiniku Q1', 100, 80, 88, 79, 82],
  ['Châu Thanh Tâm', 'Miwaku Phú Mỹ Hưng', 79, 88, 90, 'p', ''],
  ['Đỗ Quốc Khánh', 'Kohaku Ramen & Udon', 64, 60, 72, '', ''],
  ['Lê Hoài Nam', 'Machida Shoten', 79, 92, 80, 'p', ''],
  ['Phan Thị Yến', 'Miwaku Lê Thánh Tôn', 100, 85, '65x2', 92, 81],
  ['Mai Thanh Hà', 'S79 Teppanyaki', 79, 78, 84, 'p', ''],
  ['Trần Đức Duy', 'Kohaku Sushi Phan Xích Long', 100, 92, 94, 88, 91],
  ['Tạ Minh Nhật', 'Date Nariya', 79, 86, 76, 'p', ''],
  ['Lâm Ngọc Trâm', 'Kohaku Ramen & Udon', 50, 55, 60, '', ''],
  ['Ngô Gia Bảo', 'Machida Shoten', 36, 70, '', '', ''],
];""")
s = s.replace('chuan-bi-len-ky-su-van-hanh', 'chuan-bi-len-quan-ly-nha-hang').replace('huan-luyen-an-toan-buc-xa-dinh-ky', 'quan-ly-ca-va-lap-lich-ca')
s = re.sub(r'<title>[^<]*</title>', '<title>SOL · Academy</title>', s, count=1)
s = s.replace('TOANPHAT Group', 'SOL').replace('TOANPHAT', 'SOL')
# nhúng vào deck: nhận postMessage({mockGo:N}) và ẩn thanh bước khi nằm trong iframe
s = s + ("""<script>(function(){if(window.parent===window)return;var st=document.createElement('style');st.textContent='html,body{background:transparent!important}#stepi{display:none!important}body{padding:0!important;margin:0!important}';document.head.appendChild(st);addEventListener('message',function(e){var m=e.data;if(m&&m.mockGo!=null)show(m.mockGo,m.anim!==false)})})();</script>""")
s = '\n'.join(l for l in s.split('\n') if not (l.lstrip().startswith('//') and re.search(r'µSv|chiếu xạ|bức xạ|Trí|Gamma|TOANPHAT', l)))
open('sol/academy.html', 'w').write(s)
left = [w for w in ['Cobalt', 'µSv', 'chiếu xạ', 'bức xạ', 'Trí', 'Gamma', 'APHIS', 'toanphat'] if w in re.sub(r'data:[^"\']+', '', s)]
print('ok', left)
s2 = open('sol/academy.html').read().replace('15/10/2025 – 14/10/2026', '29/10/2025 – 28/10/2026')
open('sol/academy.html', 'w').write(s2)
s3 = open('sol/academy.html').read().replace('production (beedemo, ', 'production (')
open('sol/academy.html', 'w').write(s3)
