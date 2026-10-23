import re
LEDGER=open('sol/ledger_pay.js').read()
def swap_ledger(s, me="const ME = ['Trần Ngọc Hân', 8];"):
    a=s.find('// ===== Sổ cái — The Cocoon')
    if a<0: return s
    b=s.index('const POS = ',a)
    s=s[:a]+LEDGER+s[b:]
    s=re.sub(r"const ME = \['Ngô Thanh Trúc', \d+\];",me,s)
    return s
def rep(s,R,name):
    for o,n in R:
        if o not in s: raise SystemExit(f'{name}: missing {o[:80]}')
        s=s.replace(o,n)
    return s
GENERIC=[('<b>cocoon.base.vn</b>','<b>sol.base.vn</b>')]

import re
def rep_soft(s,R):
    for o,n in R:
        s=s.replace(o,n)
    return s
def hris_block(s):
    if 'const TOTAL = 274' not in s: return s
    a=s.index('const TOTAL = 274'); b=s.index('const AVC =')
    s=s[:a]+'''const TOTAL = 826, ACTIVE = 820, LONG = 6, TYPES = { ct: 468, tv: 42, btg: 286, tvu: 24 };   // 468+42+286+24 = 820
    const TAXP = { prog: 468, flat: 342 }; TAXP.applied = TAXP.prog + TAXP.flat; TAXP.wait = ACTIVE - TAXP.applied;      // 810 · 10 chờ
    const INSP = { on: 460 }; INSP.wait = TYPES.ct - INSP.on;                                                        // 8 chờ
    const pc = (a, b) => Math.round(a / b * 100);
    // [tên, mã, tài khoản, chức danh, loại, trạng thái, văn phòng, màu]
    const STAFF = [
      ['Châu Ngọc Ánh', 'SOL0391', 'anh.chau', 'Phụ bếp', 'Thử việc', 'tv', 'Miwaku Thảo Điền', 1],
      ['Đinh Gia Hưng', 'SOL0702', 'hung.dinh', 'Nhân viên phục vụ', 'Bán thời gian', 'on', 'Kohaku Sushi Phan Xích Long', 3],
      ['Hồ Tấn Phát', 'SOL0352', 'phat.ho', 'Đầu bếp sushi', 'Chính thức', 'on', 'Miwaku Thảo Điền', 7],
      ['Lê Thị Thu Thảo', 'SOL0118', 'thao.le', 'Bếp trưởng thương hiệu', 'Chính thức', 'on', 'Miwaku Thảo Điền', 3],
      ['Lý Minh Khang', 'SOL0566', 'khang.ly', 'Nhân viên phục vụ', 'Chính thức', 'on', 'Miwaku Thảo Điền', 5],
      ['Nguyễn Khánh Vy', 'SOL0688', 'vy.nguyen', 'Lễ tân', 'Bán thời gian', 'on', 'Kohaku Sashimi & Yakiniku Q1', 0],
      ['Phạm Quốc Thái', 'SOL0731', 'thai.pham', 'Phụ bếp', 'Thời vụ', 'on', 'Bếp trung tâm', 6],
      ['Trần Ngọc Hân', 'SOL0105', 'han.tran', 'Chuyên viên C&B', 'Chính thức', 'on', 'Văn phòng Điện Biên Phủ', 8],
      ['Trương Mỹ Linh', 'SOL0318', 'linh.truong', 'Trưởng ca', 'Chính thức', 'on', 'Miwaku Thảo Điền', 4],
      ['Võ Minh Quân', 'SOL0214', 'quan.vo', 'Quản lý nhà hàng', 'Chính thức', 'on', 'Miwaku Thảo Điền', 2],
    ].sort((a, b) => a[0].localeCompare(b[0], 'vi'));
    '''+s[b:]
    a=s.index('const HOA = {'); b=s.index('\n',a)
    s=s[:a]+"const HOA = { name: 'Võ Minh Quân', code: 'SOL0214', acc: 'quan.vo', title: 'Quản lý nhà hàng', start: '1 thg 4, 2023', off: '1 thg 6, 2023', tenure: '3 năm 6 tháng 27 ngày công việc', con: 'SOL-HDLD-2025-0214', mail: 'quan.vo@sol.com.vn', phone: '0909 318 472', dob: '22/08/1992', ws: 'SOL', office: 'Miwaku Thảo Điền', jp: 'Quản lý nhà hàng', jpCode: 'S-0404', type: 'Chính thức' };"+s[b:]
    a=s.index('const CON = ['); b=s.index('const SVC')
    s=s[:a]+'''const CON = [
      ['Đinh Gia Hưng', 3, 'SOL-BTG-2026-0702', 'HĐ bán thời gian', '1 thg 10, 2026', '31 thg 3, 2027', '35.000 ₫/giờ'],
      ['Phạm Quốc Thái', 6, 'SOL-TVU-2026-0731', 'HĐ thời vụ', '15 thg 10, 2026', '15 thg 2, 2027', 8000000],
      ['Châu Ngọc Ánh', 1, 'SOL-TV-2026-0391', 'HĐ thử việc', '1 thg 9, 2026', '31 thg 10, 2026', 8000000, 1],
      ['Nguyễn Khánh Vy', 0, 'SOL-BTG-2026-0688', 'HĐ bán thời gian', '1 thg 9, 2026', '28 thg 2, 2027', '35.000 ₫/giờ'],
      ['Lý Minh Khang', 5, 'SOL-HDLD-2025-0566', 'HĐ chính thức', '1 thg 7, 2025', '30 thg 6, 2027', 9000000],
      ['Hồ Tấn Phát', 7, 'SOL-HDLD-2025-0352', 'HĐ chính thức', '1 thg 3, 2025', '28 thg 2, 2027', 12500000],
      ['Trương Mỹ Linh', 4, 'SOL-HDLD-2024-0318', 'HĐ chính thức', '1 thg 5, 2024', '30 thg 4, 2027', 14000000],
      ['Võ Minh Quân', 2, 'SOL-HDLD-2025-0214', 'HĐ chính thức', '1 thg 6, 2025', '', 17500000],
    ];
    '''+s[b:]
    R=GENERIC+[
    ("const SVC = [['HĐ chính thức', '#0D9488'], ['HĐ thử việc', '#2563EB'], ['HĐ thời vụ', '#D97706'], ['HĐ KOL', '#DB2777'], ['HĐ cộng tác viên', '#7C3AED']];","const SVC = [['HĐ chính thức', '#0D9488'], ['HĐ thử việc', '#2563EB'], ['HĐ bán thời gian', '#DB2777'], ['HĐ thời vụ', '#D97706']];"),
    ("${c[6] ? vndH(c[6]) : '—'}","${c[6] ? (typeof c[6] === 'string' ? c[6] : vndH(c[6])) : '—'}"),
    ("st('#EA580C', 'Sắp hết hạn', 9, 1) + st('#9CA3AF', 'Đã hết hạn', 2, 1)","st('#EA580C', 'Sắp hết hạn', 14, 1) + st('#9CA3AF', 'Đã hết hạn', 5, 1)"),
    ('286 hợp đồng','839 hợp đồng'),
    ("${HOA.jpCode} — Kho HCM","${HOA.jpCode} — ${HOA.office}"),
    ('<i style="background:#B38A4E">C</i>The Cocoon','<i style="background:#C8102E">S</i>SOL'),
    ("+ g('KHÔNG GIAN LÀM VIỆC') + n('database', 'Y&amp;B', 'w1') + n('database', 'Nature Story', 'w2')","+ g('KHÔNG GIAN LÀM VIỆC') + n('database', 'SOL', 'w1')"),
    ('Thử việc, thời vụ, KOL, cộng tác viên','Thử việc, bán thời gian, thời vụ'),
    ("{ path: '/employees/CC0127/profile'","{ path: '/employees/SOL0214/profile'"),
    ]
    s=rep(s,[r for r in R if r[0] in s or r[0].startswith('{ path')],'hris') if False else rep_soft(s,R)
    a=s.index('const OFF = ['); b=s.index('\n',a)
    s=s[:a]+"const OFF = [['Văn phòng Điện Biên Phủ', 'VP-DBP', 'Hồ Chí Minh · Vietnam'], ['Bếp trung tâm', 'BTT', 'Hồ Chí Minh · Vietnam'], ['Kohaku Sushi Phan Xích Long', 'KS-PXL', 'Hồ Chí Minh · Vietnam'], ['Kohaku Sashimi & Yakiniku Q1', 'KSY-Q1', 'Hồ Chí Minh · Vietnam'], ['Miwaku Thảo Điền', 'MW-TD', 'Hồ Chí Minh · Vietnam'], ['Miwaku Phú Mỹ Hưng', 'MW-PMH', 'Hồ Chí Minh · Vietnam'], ['Miwaku Lê Thánh Tôn', 'MW-LTT', 'Hồ Chí Minh · Vietnam']];"+s[b:]
    s=re.sub(r'<title>[^<]*</title>','<title>SOL trên HRIS</title>',s,1)
    s=re.sub(r'<meta name="description" content="[^"]*">','<meta name="description" content="Base HRIS cho SOL: hồ sơ nhân viên, hợp đồng, văn phòng, chính sách thuế và bảo hiểm.">',s,1)
    return s

def scrub(s):
    s=s.replace('style="background:#B38A4E">C<','style="background:#C8102E">S<')
    for o,n in [('The Cocoon','SOL'),('Công ty CP Y&B','Công ty CP Sense Of Life'),('Cocoon','SOL'),('cocoon','sol')]:
        s=s.replace(o,n)
    return s
