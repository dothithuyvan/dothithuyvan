import sys,re
sys.path.insert(0,'sol'); from common import *
s=open('qm/r_p9.html').read()
R=[('<b>quess.base.vn</b>','<b>sol.base.vn</b>'),
('Kế hoạch thăng cấp lên Trưởng nhóm Kinh doanh B2B','Kế hoạch thăng cấp lên Quản lý nhà hàng'),
('Lý Hoàng Phúc','Trương Mỹ Linh'),('Chuyên viên KD B2B · Bậc 4','Trưởng ca · G3'),('Trưởng nhóm KD B2B','Quản lý nhà hàng'),('Bậc 1 · KD B2B miền Nam','G4 · Miwaku'),
('còn 41 ngày','còn 64 ngày'),('Trương Ngọc Lan','Võ Minh Quân'),('Giám đốc khối Kinh doanh','Quản lý nhà hàng Miwaku Thảo Điền'),
('Nhóm kinh doanh B2B miền Nam có 6 chuyên viên, phụ trách khách hàng doanh nghiệp thuê dịch vụ tuyển dụng và nhân sự. Giám đốc khối cần một trưởng nhóm quản lý trực tiếp để tập trung vào khách hàng chiến lược.','Theo kế hoạch mở rộng chuỗi, Miwaku cần thêm quản lý nhà hàng đào tạo từ nội bộ, nắm chuẩn vận hành và cách phục vụ kiểu Nhật để nhận nhà hàng mới.'),
('Giá trị HĐ ký mới 9 tháng','Doanh thu ca phụ trách 9 tháng'),('12,4 tỷ','6,8 tỷ'),('124%','112%'),('Tỷ lệ chốt deal','Điểm hài lòng khách'),('>41%<','>4,8/5<'),('nhóm 29%','chuỗi 4,5'),
('Chuyên viên được kèm','Nhân viên được kèm'),('2 người','5 người'),('đạt chỉ tiêu','qua thử việc'),('Công nợ quá hạn','Phàn nàn nghiêm trọng'),('>0 đ<','>0 vụ<'),
('Đã dẫn dắt hai hợp đồng cung ứng nhân sự quy mô lớn, chuẩn hoá bộ báo giá theo loại dịch vụ và kèm cặp người mới. Cần chính thức hoá vai trò quản lý để mở rộng nhóm trong năm 2027.','Điều hành ca tối đông khách nhất nhà hàng, chuẩn hoá checklist mở và đóng ca, kèm 5 nhân viên mới qua thử việc. Cần chính thức hoá vai trò quản lý để sẵn sàng nhận nhà hàng mới.'),
('Nhóm 6 người đạt 45 tỷ giá trị hợp đồng năm 2027','Nhà hàng đạt 100% doanh thu kế hoạch năm 2027'),('Ít nhất 80% thành viên đạt chỉ tiêu quý','Tỷ lệ nghỉ việc nhân viên dưới 5% mỗi quý'),
('Rút thời gian lập đề xuất dịch vụ từ 5 xuống 3 ngày','Điểm kiểm tra ATTP nội bộ từ 95/100'),('Họp 1-1 hằng tuần với từng thành viên','Họp đầu ca hằng ngày, 1-1 hằng tháng với trưởng ca'),
('Hoàn thành khoá Quản lý nhóm kinh doanh và lập kế hoạch kèm cặp hằng tuần','Hoàn thành khoá Quản lý nhà hàng và lập kế hoạch kèm cặp'),('Hạn 15/10/2026 · xong 12/10','Hạn 30/09/2026 · xong 26/09'),
('Dẫn dắt nhóm 3 người chốt hợp đồng cung ứng 120 nhân sự cho một khách hàng bán lẻ','Điều hành độc lập nhà hàng 2 tuần khi quản lý nghỉ phép'),('Hạn 15/11/2026 · xong 10/11','Hạn 20/10/2026 · xong 18/10'),('HĐ-1126/QS-KD','BC-1018/MW-TD'),
('Nhóm đạt từ 90% chỉ tiêu tháng 12, họp 1-1 định kỳ với từng thành viên','Nhà hàng đạt 95% doanh thu kế hoạch tháng 12, tự lập lịch ca cả tháng'),('đang thực hiện, đạt 62% sau 3 tuần','đang thực hiện, đã lập lịch ca tháng 11'),
('Nguyễn Thị Hồng Nhung','Nguyễn Hoàng Phúc'),('Ban Tổng giám đốc','Ban Vận hành'),('22/09/2026 · 09:05','05/09/2026 · 09:05'),('18/11/2026 · 16:40','27/10/2026 · 16:40'),('>01/10/2026<','>15/09/2026<'),
('>22/09<','>05/09<'),('>24/09<','>08/09<'),('>10/11<','>18/10<'),('chủ sở hữu Phòng Nhân sự','chủ sở hữu Phòng Hành chính Nhân sự'),
('<span class="ltr" style="background:#0F766E">Q</span>Quess','<span class="ltr" style="background:#C8102E">S</span>SOL')]
for o,n in R:
    if o not in s: print('MISS',o[:60])
    s=s.replace(o,n)
s=re.sub(r'>LP<','>TL<',s); s=re.sub(r'>TL</span>(\s*<div[^>]*>\s*<span[^>]*>Người đề xuất)',r'>VQ</span>\1',s)
s=s.replace('>HN<','>NP<')
s=re.sub(r'<title>[^<]*</title>','<title>SOL trên Careers</title>',s,count=1)
s=s.replace('Quess','SOL').replace('quess','sol')
open('sol/cplan.html','w').write(s)
s=re.sub(r'Ít nhất 80% thành viên đạt chỉ tiêu quý','Tỷ lệ nghỉ việc nhân viên dưới 5% mỗi quý',s)
s=s.replace('<i>Q</i>Quess','<i style="background:#C8102E">S</i>SOL').replace('<i>Q</i>SOL','<i style="background:#C8102E">S</i>SOL')
out=[];i=0
for m in re.finditer(r'>TL<',s):
    out.append(s[i:m.start()]); look=s[m.end():m.end()+700]
    a=look.find('Võ Minh Quân'); b=look.find('Trương Mỹ Linh')
    out.append('>VQ<' if a>=0 and (b<0 or a<b) else '>TL<'); i=m.end()
out.append(s[i:]); s=''.join(out)
open('sol/cplan.html','w').write(s)
s=re.sub(r'Ít nhất 80% thành viên qua thử việc quý','Tỷ lệ nghỉ việc nhân viên dưới 5% mỗi quý',s)
s=s.replace('5 người đánh giá · 360 độ','2 người đánh giá · 360 độ').replace('Quản lý nhà hàng Miwaku Thảo Điền','Quản lý nhà hàng')
open('sol/cplan.html','w').write(s)
