import sys,re
sys.path.insert(0,'sol'); from common import *
s=open('mk/pay.html').read()
s=swap_ledger(s); s=hris_block(s)
R=[("'SỐ CA ĐÊM (TIMESHEETS)'","'SỐ CA ĐÓNG CỬA (TIMESHEETS)'"),("'PHỤ CẤP CA ĐÊM (30%)'","'PHỤ CẤP LÀM ĐÊM (30%)'"),
("n: 'Phụ cấp ca đêm (30%)'","n: 'Phụ cấp làm đêm (30%)'"),("['Số ca đêm (Timesheets)'","['Số ca đóng cửa (Timesheets)'"),
("công, ca đêm, tăng ca lấy từ Timesheets","công, ca đóng cửa, tăng ca lấy từ Timesheets"),
("'Một chính sách cho toàn công ty, công thức theo từng bộ phận;","'Áp dụng cho các nhà hàng, công thức theo từng chức danh;"),
("['Hoa hồng doanh số – đợt ngày 15', 6, 'Hoa hồng từ bảng kế toán bán hàng sau khi Giám đốc duyệt; điều chỉnh lương phát sinh. Chi ngày 15.']","['Bảng lương Văn phòng và Bếp trung tâm', 16, 'Lương thời gian theo công chuẩn từng bộ phận; tăng ca từ Timesheets; BHXH, TNCN, đoàn phí. Chi ngày 5.']"),
("PR-2610-KHO","PR-2610-MWTD")]
s=rep(s,R,'pay')
s=scrub(s)
s=re.sub(r'<title>[^<]*</title>','<title>SOL trên Payroll</title>',s,count=1)
s=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Base Payroll cho SOL: bảng lương nhà hàng Miwaku Thảo Điền lấy công, ca, tăng ca từ Timesheets; nhân viên xác nhận phiếu lương.">',s,count=1)
open('sol/pay.html','w').write(s)
print([w for w in ['Kho','kho','Đạt','Hoà','ca đêm'] if w in re.sub(r'data:[^"\']+','',s)])
