import sys
sys.path.insert(0,'sol'); from common import *
s=open('mk/car.html').read()
s=swap_ledger(s); s=hris_block(s)
a=s.index('const ONB = ['); b=s.index('const ST = {')
s=s[:a]+'''const ONB = [
  ['Trần Bảo Châu', 'chau.tran@sol.com.vn', 'Nhân viên phục vụ', 'Hội nhập Nhà hàng', 'Võ Minh Quân', '3 thg 11, 2026', 'in 6d', 'hn'],
  ['Lâm Gia Huy', 'huy.lam@sol.com.vn', 'Phụ bếp', 'Hội nhập Bếp', 'Lê Thị Thu Thảo', '1 thg 11, 2026', 'in 4d', 'hn'],
  ['Phùng Thảo My', 'my.phung@sol.com.vn', 'Lễ tân', 'Hội nhập Nhà hàng', 'Võ Minh Quân', '27 thg 10, 2026', '1d ago', 'ss'],
  ['Phạm Quốc Thái', 'thai.pham@sol.com.vn', 'Phụ bếp', 'Hội nhập Bếp trung tâm', 'Đoàn Văn Lực', '15 thg 10, 2026', '13d ago', 'ht'],
  ['Châu Ngọc Ánh', 'anh.chau@sol.com.vn', 'Phụ bếp', 'Hội nhập Bếp', 'Lê Thị Thu Thảo', '1 thg 9, 2026', '57d ago', 'ht'],
  ['Nguyễn Khánh Vy', 'vy.nguyen@sol.com.vn', 'Lễ tân', 'Hội nhập Nhà hàng', 'Trần Quốc Duy', '1 thg 9, 2026', '57d ago', 'ht'],
];
'''+s[b:]
a=s.index('const DEC = ['); b=s.index('const DT = {')
s=s[:a]+'''const DEC = [
  ['Võ Minh Quân', 2, 'Thăng chức', 'PR-2026-0014', 'Thăng chức Khối Nhà hàng', 'Quản lý khu vực', 'từ Quản lý nhà hàng', 22000000, '+25.7%', '1 thg 11, 2026', 'cho'],
  ['Bùi Quang Vinh', 4, 'Thăng chức', 'PR-2026-0015', 'Thăng chức Khối Nhà hàng', 'Quản lý nhà hàng', 'từ Điều phối ca', 15500000, '+24.0%', '1 thg 11, 2026', 'cho'],
  ['Nguyễn Văn An', 0, 'Điều chuyển', 'EX-2026-0007', 'Điều chuyển nội bộ', 'Phục vụ · Miwaku Thảo Điền', 'từ Kohaku Sushi Phan Xích Long', 8500000, 'không đổi', '15 thg 10, 2026', 'kh'],
  ['Châu Ngọc Ánh', 1, 'Tăng lương', 'RA-2026-0029', 'Ký chính thức sau thử việc', '—', '', 8000000, '+0%', '1 thg 11, 2026', 'kh'],
  ['Đặng Thanh Tú', 7, 'Thăng chức', 'PR-2026-0011', 'Thăng chức Khối Nhà hàng', 'Quản lý nhà hàng', 'từ Trưởng ca', 16500000, '+17.9%', '1 thg 9, 2026', 'kh'],
  ['Mai Đức Thịnh', 5, 'Tăng lương', 'RA-2026-0018', 'Tăng lương định kỳ', '—', '', 9000000, '+5.9%', '1 thg 7, 2026', 'kh'],
];
'''+s[b:]
R=[("si('award', 'Hội nhập Khối Kho') + si('award', 'Hội nhập Livestream') + si('award', 'Hội nhập Cửa hàng') + si('award', 'Hội nhập Văn phòng')","si('award', 'Hội nhập Nhà hàng') + si('award', 'Hội nhập Bếp') + si('award', 'Hội nhập Bếp trung tâm') + si('award', 'Hội nhập Văn phòng')"),
("${o[2]} · Kho HCM · Bắt đầu","${o[2]} · Miwaku Thảo Điền · Bắt đầu"),("f('Văn phòng', 'Kho HCM', 'hrm')","f('Văn phòng', 'Miwaku Thảo Điền', 'hrm')"),
("'Bằng cấp cao nhất'","'Giấy chứng nhận ATTP'"),
("<small>Tổ trưởng Kho lẻ</small>","<small>Quản lý nhà hàng</small>"),("Đề xuất bởi <b>Ngô Thanh Trúc</b>","Đề xuất bởi <b>Trần Ngọc Hân</b>"),
("box('CẤP BẬC', 'L2', 'S-K01')","box('CẤP BẬC', 'L2', 'S-0398')"),
("<b>Tổ trưởng Kho lẻ</b><em>${vndH(11000000)}","<b>Quản lý nhà hàng</b><em>${vndH(17500000)}"),
("20 thg 10, 2026 · Ngô Thanh Trúc","20 thg 10, 2026 · Trần Ngọc Hân"),("Trưởng phòng Vận hành kho","Giám đốc Vận hành"),
("CC-ONB-0412","SOL-ONB-0412")]
s=rep(s,R,'car')
s=scrub(s)
open('sol/car.html','w').write(s)
# ---- dày thêm dữ liệu ----
s=s.replace("""  ['Nguyễn Khánh Vy', 'vy.nguyen@sol.com.vn', 'Lễ tân', 'Hội nhập Nhà hàng', 'Trần Quốc Duy', '1 thg 9, 2026', '57d ago', 'ht'],
];""","""  ['Nguyễn Khánh Vy', 'vy.nguyen@sol.com.vn', 'Lễ tân', 'Hội nhập Nhà hàng', 'Trần Quốc Duy', '1 thg 9, 2026', '57d ago', 'ht'],
  ['Hoàng Gia Khiêm', 'khiem.hoang@sol.com.vn', 'Đầu bếp sushi', 'Hội nhập Bếp', 'Lê Thị Thu Thảo', '5 thg 11, 2026', 'in 8d', 'hn'],
  ['Võ Thị Kim Ngân', 'ngan.vo@sol.com.vn', 'Thu ngân', 'Hội nhập Nhà hàng', 'Đặng Thanh Tú', '3 thg 11, 2026', 'in 6d', 'hn'],
  ['Trịnh Quốc Bảo', 'bao.trinh@sol.com.vn', 'Nhân viên phục vụ', 'Hội nhập Nhà hàng', 'Huỳnh Bảo Ngọc', '26 thg 10, 2026', '2d ago', 'ss'],
  ['Lê Hoàng Anh', 'anh.le@sol.com.vn', 'Chuyên viên Marketing', 'Hội nhập Văn phòng', 'Nguyễn Thu Trang', '20 thg 10, 2026', '8d ago', 'ht'],
  ['Đỗ Minh Tâm', 'tam.do@sol.com.vn', 'Nhân viên phục vụ', 'Hội nhập Nhà hàng', 'Võ Minh Quân', '15 thg 10, 2026', '13d ago', 'ht'],
];""")
s=s.replace("const foot = st('#2563EB', 'Đang hoạt động', 2) + st('#D97706', 'Đang duyệt', 0, 1) + st('#7C3AED', 'Sẵn sàng', 1) + st('#6B7280', 'Tháng này', 4);",
 "const foot = st('#2563EB', 'Đang hoạt động', ONB.filter(o => o[7] === 'hn').length) + st('#D97706', 'Đang duyệt', 0, 1) + st('#7C3AED', 'Sẵn sàng', ONB.filter(o => o[7] === 'ss').length) + st('#6B7280', 'Tháng này', ONB.filter(o => / 10, 2026/.test(o[5])).length);")
s=s.replace("flt('Tất cả trạng thái (6)', 'clock')","flt('Tất cả trạng thái (' + ONB.length + ')', 'clock')")
s=s.replace("""  ['Mai Đức Thịnh', 5, 'Tăng lương', 'RA-2026-0018', 'Tăng lương định kỳ', '—', '', 9000000, '+5.9%', '1 thg 7, 2026', 'kh'],
];""","""  ['Mai Đức Thịnh', 5, 'Tăng lương', 'RA-2026-0018', 'Tăng lương định kỳ', '—', '', 9000000, '+5.9%', '1 thg 7, 2026', 'kh'],
  ['Huỳnh Bảo Ngọc', 3, 'Thăng chức', 'PR-2026-0009', 'Thăng chức Khối Nhà hàng', 'Quản lý nhà hàng', 'từ Trưởng ca', 16500000, '+17.9%', '1 thg 7, 2026', 'kh'],
  ['Phan Gia Bảo', 6, 'Tăng lương', 'RA-2026-0016', 'Tăng lương định kỳ', '—', '', 8500000, '+6.3%', '1 thg 7, 2026', 'kh'],
  ['Ngô Bảo Trâm', 8, 'Điều chuyển', 'EX-2026-0005', 'Điều chuyển nội bộ', 'Sushi · Miwaku Thảo Điền', 'từ Kohaku Sushi Phan Xích Long', 12000000, 'không đổi', '1 thg 6, 2026', 'kh'],
  ['Tạ Thu Uyên', 9, 'Tăng lương', 'RA-2026-0012', 'Ký chính thức sau thử việc', '—', '', 8500000, '+6.3%', '1 thg 5, 2026', 'kh'],
];""")
s=s.replace("const foot = st('#16A34A', 'Hiệu lực', 4) + st('#D97706', 'Chờ duyệt', 2, 1)","const foot = st('#16A34A', 'Hiệu lực', DEC.filter(x => x[10] === 'kh').length) + st('#D97706', 'Chờ duyệt', DEC.filter(x => x[10] === 'cho').length, 1)")
open('sol/car.html','w').write(s)
