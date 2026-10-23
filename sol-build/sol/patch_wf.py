import re,sys
s=open('mk/wf.html').read()
a=s.index('// ===== The Cocoon'); b=s.index('const HC = [];')
s=s[:a]+open('sol/wf_data.js').read()+'\n'+s[b:]
R=[('<title>The Cocoon trên Workforce</title>','<title>SOL trên Workforce</title>'),
('Base Workforce cho The Cocoon: sơ đồ tổ chức 274 nhân sự, Khối Vận hành kho, đơn vị Kho HCM và định biên.','Base Workforce cho SOL: sơ đồ tổ chức 820 nhân sự, Khối Vận hành nhà hàng, thương hiệu Miwaku và định biên.'),
('background:#B38A4E">C</span>The Cocoon','background:#C8102E">S</span>SOL'),
('<b>cocoon.base.vn</b>','<b>sol.base.vn</b>'),('@cocoonvietnam.com','@sol.com.vn'),
("posPage({ rows: NS, cc: 'Kho vận' })","posPage({ rows: NS, cc: 'Vận hành nhà hàng' })"),
('/units/kho-hcm','/units/miwaku'),('const pay = 8500000','const pay = 9800000'),('.t-tm{--tc:#8B5CF6}','.t-tm{--tc:#8B5CF6}.t-th{--tc:#DC2626}.t-nh{--tc:#F59E0B}')]
for o,n in R:
    assert o in s,o; s=s.replace(o,n)
open('sol/wf.html','w').write(s)
