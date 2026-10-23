import sys,re
sys.path.insert(0,'sol'); from common import *
s=open('mk/ts.html').read()
a=s.index('// ===== Sổ cái — The Cocoon (Công ty CP Y&B) · hôm nay T4'); b=s.index('const HOL = {};')
import re as _re
logo=_re.search(r"const LOGO = '[^']*';",s[a:b]).group(0)
s=s[:a]+'''// ===== Sổ cái — SOL (Công ty CP Sense Of Life) · hôm nay T4 28/10/2026 =====
// Nguồn công khai: chuỗi nhà hàng Nhật, nhân viên toàn thời gian và bán thời gian. Giờ ca, tên người, mã nhân sự, sự kiện chấm công là giả định.
// Ba lịch ca: Văn phòng Điện Biên Phủ 08:30–17:30 (T2–T6, T7 cách tuần) · Miwaku Thảo Điền xoay ca theo tuần (sáng, tối, đóng cửa; nghỉ 1 ngày trong tuần, làm cuối tuần) · Bếp trung tâm 06:00–14:30 (T2–T7).
const LOGO = 'DATA_LOGO_KEEP';
const GRP = [
  { sched: 'Văn phòng Điện Biên Phủ', ts: 'Văn phòng Điện Biên Phủ', col: '#2563EB' },
  { sched: 'Miwaku Thảo Điền · xoay ca', ts: 'Miwaku Thảo Điền · xoay ca', col: '#C8102E' },
  { sched: 'Bếp trung tâm', ts: 'Bếp trung tâm', col: '#0F9488' },
];
// [tên loại ca, giờ, số giờ công]
const SHIFT = {
  hc: ['Ca hành chính VP', '08:30–17:30', 8],
  K1: ['Ca sáng', '09:00–17:00', 8],
  K2: ['Ca tối', '14:00–22:00', 8],
  D: ['Ca đóng cửa', '15:30–23:30', 8],
  tt: ['Ca bếp trung tâm', '06:00–14:30', 8],
};
// [tên, mã, chức danh, nhóm, kiểu lịch, tham số xoay ca, tham số ngày nghỉ] — hc: T7 đi làm tuần chẵn/lẻ; nhà hàng: xoay sáng → tối → đóng cửa theo tuần, nghỉ 1 ngày T2–T6
const EMP = [
  ['Trần Ngọc Hân', 'SOL0105', 'Chuyên viên C&B', 0, 'hc', 0],
  ['Nguyễn Thu Trang', 'SOL0142', 'Chuyên viên Marketing', 0, 'hc', 1],
  ['Võ Minh Quân', 'SOL0214', 'Quản lý nhà hàng', 1, 'kho', 0, 3],
  ['Lý Minh Khang', 'SOL0566', 'Nhân viên phục vụ', 1, 'kho', 2, 1],
  ['Hồ Tấn Phát', 'SOL0352', 'Đầu bếp sushi', 1, 'kho', 1, 0],
  ['Mai Đức Thịnh', 'SOL0397', 'Phụ bếp', 1, 'kho', 2, 4],
  ['Phạm Quốc Thái', 'SOL0731', 'Phụ bếp', 2, 'tt', 0],
];
const ME = ['Trần Ngọc Hân', 8];          // người đăng nhập màn quản trị: Chuyên viên C&B, Phòng Hành chính Nhân sự
'''+s[b:]
s=s.replace("const LOGO = 'DATA_LOGO_KEEP';",logo,1)
R=[("""  if (w === 0 || HOL[`2026-${m}-${d}`]) return null;
  if (em[4] === 'hc')""","""  if (HOL[`2026-${m}-${d}`]) return null;
  if (em[4] === 'kho') { if (w === 1 + (isoWk(m, d) + em[6]) % 5) return null; return ['K1', 'K2', 'D'][(isoWk(m, d) + em[5]) % 3]; }
  if (w === 0) return null;
  if (em[4] === 'hc')"""),
("const LV = { e: 3, quota: 14, used: 6, days: [30, 31] };","const LV = { e: 3, quota: 12, used: 6, days: [30, 31] };"),
("const OTR = { e: 4, d: 27, from: '16:30', to: '19:00', punch: '18:45',","const OTR = { e: 4, d: 27, from: '17:00', to: '19:30', punch: '19:15',"),
("const SITE = 'Kho HCM';","const SITE = 'Miwaku Thảo Điền';"),
("'Tăng ca Kho HCM'","'Tăng ca Nhà hàng'"),("'Tăng ca Livestream'","'Tăng ca Bếp trung tâm'"),
("['Nghỉ bù tăng ca kiểm kê', 'Nghỉ bù', '06/09', 'Từ chối', 'Toàn bộ', 'Nghỉ bù kiểm kê…', '1 ngày']","['Nghỉ bù tăng ca tiệc', 'Nghỉ bù', '06/09', 'Từ chối', 'Toàn bộ', 'Nghỉ bù tiệc cuối tuần…', '1 ngày']"),
("'Đóng đơn sàn TMĐT…'","'Tiệc đặt trước 40 khách…'"),("'Kiểm kê cuối tuần…'","'Cuối tuần đông khách…'"),("'Nhận hàng nhà máy về trễ…'","'Hải sản tươi về trễ…'"),
("'Đóng đơn chương trình 15/10…'","'Tiệc công ty đặt bàn…'"),("'Đóng đơn sale 10/10…'","'Thiếu người ca tối…'"),("'Sắp xếp kệ hàng…'","'Dọn kho lạnh…'"),("'Xuất hàng cửa hàng mới…'","'Ra mắt món mới…'"),
("${SHIFT[s][0]} · Kho lẻ","${SHIFT[s][0]} · Phục vụ"),
("Đã báo tổ trưởng Lê Văn Hoà để xếp người thay ca chiều hai ngày này.","Đã báo quản lý Võ Minh Quân để xếp người thay ca hai ngày này."),
("Lê Văn Hoà · 27/10 10:05","Võ Minh Quân · 27/10 10:05"),("<b>Lê Văn Hoà</b> đã duyệt","<b>Võ Minh Quân</b> đã duyệt"),
("Dữ liệu máy chấm công Kho HCM: ra","Dữ liệu chấm công Miwaku Thảo Điền: ra"),
("Đóng đơn sàn TMĐT${I('chevron-down', 14)}","Phục vụ tiệc đặt trước${I('chevron-down', 14)}"),
("Ở lại sau ca sáng đóng đơn sàn TMĐT đợt sale cuối tháng: còn 320 đơn cần bàn giao đơn vị vận chuyển trong ngày.","Ở lại sau ca sáng hỗ trợ bếp tối: nhà hàng nhận tiệc đặt trước 40 khách lúc 18:00, cần chuẩn bị sushi platter."),
("Tăng ca sau ca sáng – đóng đơn sàn TMĐT","Tăng ca sau ca sáng – phục vụ tiệc đặt trước"),
("'Kho HCM · Ca kho sáng'","'Miwaku Thảo Điền · Ca sáng'"),("f('QUẢN LÝ TRỰC TIẾP', 'Lê Văn Hoà')","f('QUẢN LÝ TRỰC TIẾP', 'Võ Minh Quân')"),
("Lê Văn Hoà · 27/10 19:30","Võ Minh Quân · 27/10 19:30"),
]
s=rep(s,R,'ts')
s=s.replace('Quỹ 14 ngày/năm (12 + 2 thâm niên)','Quỹ 12 ngày/năm theo luật')
s=scrub(s)
s=re.sub(r'<title>[^<]*</title>','<title>SOL trên Timesheets</title>',s,count=1)
open('sol/ts.html','w').write(s)
import re as _r
left=[w for w in ['Kho','kho lẻ','Hoà','Trí','Đạt','TMĐT','Quảng Ngãi'] if w in _r.sub(r'data:[^"\']+','',s)]
print(left)
s=s.replace("'Võ Thành Đạt'","'Hồ Tấn Phát'").replace('Võ Thành Đạt','Hồ Tấn Phát').replace('Phạm Minh Trí','Lý Minh Khang')
s=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Base Timesheets cho SOL: xếp ca nhà hàng xoay theo tuần, bảng công tự đối chiếu, nghỉ phép và tăng ca.">',s,count=1)
open('sol/ts.html','w').write(s)
s=s.replace('<span class="ws" style="background:#B38A4E">C</span>','<span class="ws" style="background:#C8102E">S</span>').replace(' ngày/năm (12 + 2 ngày thâm niên)',' ngày/năm theo luật lao động')
open('sol/ts.html','w').write(s)
