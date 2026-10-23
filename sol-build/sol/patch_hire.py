import sys,re
sys.path.insert(0,'sol'); from common import *
s=open('qm/r_p11.html').read()
R=[('<b>quess.base.vn</b>','<b>sol.base.vn</b>'),('<span class="ltr" style="background:#0F766E">Q</span>Quess','<span class="ltr" style="background:#C8102E">S</span>SOL'),
('<span class="nm">Chuyên viên tuyển dụng</span><span class="n ">29</span>','<span class="nm">Nhân viên phục vụ</span><span class="n ">29</span>'),
('<span class="nm">Account Manager</span><span class="n ">14</span>','<span class="nm">Phụ bếp</span><span class="n ">14</span>'),
('<span class="nm">Chuyên viên KD B2B</span><span class="n ">9</span>','<span class="nm">Quản lý nhà hàng</span><span class="n ">9</span>'),
('Tin tuyển: Chuyên viên tuyển dụng, Account Manager','Tin tuyển: Nhân viên phục vụ, Quản lý nhà hàng'),
('6 năm tuyển dụng khối bán lẻ, từng tuyển 300 nhân sự mỗi năm','5 năm vận hành nhà hàng Nhật, từng quản lý ca 25 nhân sự, có chứng nhận ATTP'),
('Không phù hợp JD','Không khớp lịch ca'),
]
s=rep(s,R,'hire')
ROWS=[('Trần Quốc Bảo','6 năm · Bán lẻ','5 năm · Nhà hàng Nhật','Quản lý nhà hàng','Trợ lý quản lý nhà hàng'),
('Ngô Thị Minh Châu','4 năm · Siêu thị','3 năm · Chuỗi cà phê','Nhân viên phục vụ','Trưởng ca phục vụ'),
('Vũ Hải Đăng','3 năm · Điện tử','2 năm · Khách sạn','Nhân viên phục vụ','Nhân viên F&amp;B'),
('Lâm Thanh Tùng','5 năm · TMĐT','4 năm · Nhà hàng BBQ','Quản lý nhà hàng','Trưởng ca'),
('Phạm Đức Long','2 năm · May mặc','2 năm · Quán ăn','Nhân viên phục vụ','Nhân viên phục vụ'),
('Kiều Minh Khôi','1 năm · Sản xuất','1 năm · Trà sữa','Nhân viên phục vụ','Nhân viên pha chế'),
('Lưu Hoàng Yến','3 năm · Tài chính','3 năm · Khách sạn','Nhân viên phục vụ','Lễ tân khách sạn'),
('Hồ Văn Thắng','7 năm · Logistics','6 năm · Nhà hàng Nhật','Quản lý nhà hàng','Quản lý ca'),
('Cao Thị Bích Ngọc','2 năm · F&amp;B','2 năm · Bếp Việt','Phụ bếp','Phụ bếp'),
('Đinh Công Sơn','4 năm · Năng lượng','4 năm · Nhà hàng Hàn','Quản lý nhà hàng','Trưởng ca'),
('Triệu Văn Hòa','3 năm · Cảng biển','3 năm · Nhà hàng','Nhân viên phục vụ','Nhân viên phục vụ'),
('Tạ Hữu Nghĩa','Mới tốt nghiệp','Sinh viên','Phụ bếp','Bán thời gian')]
tb_a=s.index('<tbody>'); tb_b=s.index('</tbody>')
body=s[tb_a:tb_b]; trs=body.split('<tr ')
out=[trs[0]]
for tr,(nm,ox,nx,job,last) in zip(trs[1:],ROWS):
    assert nm in tr, nm
    tr=tr.replace(f'<small>{ox}</small>',f'<small>{nx}</small>',1)
    cells=re.findall(r'</span></td><td>([^<]*)</td><td>([^<]*)</td>',tr)
    o=cells[0]; tr=tr.replace(f'</span></td><td>{o[0]}</td><td>{o[1]}</td>',f'</span></td><td>{job}</td><td>{last}</td>',1)
    out.append(tr)
s=s[:tb_a]+'<tr '.join(out)+s[tb_b:]
s=s.replace('<small>6 năm · Bán lẻ</small>','<small>5 năm · Nhà hàng Nhật</small>')
s=re.sub(r'<title>[^<]*</title>','<title>SOL trên E-Hiring</title>',s,count=1)
s=s.replace('Quess','SOL').replace('quess','sol')
open('sol/hire.html','w').write(s)
