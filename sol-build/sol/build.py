import base64, re, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

def uri(p):
    return 'data:image/png;base64,' + base64.b64encode(open(p, 'rb').read()).decode()

def mock_logo(f):
    s = open(f).read()
    m = re.search(r"const LOGO = '([^']+)'", s)
    return m.group(1) if m else None

LG = {k: uri(f'logos/c_{k}.png') for k in ['HRIS', 'Payroll', 'Timesheets', 'Workforce', 'Requests', 'Project']}
LG['Careers'] = mock_logo('sol/car.html')
LG['Base'] = uri('logos/q_a41.png')
for _k, _f in [('Academy', 'academy'), ('E-Hiring', 'hiring'), ('Interview', 'interview'), ('Output', 'output'), ('Reviews', 'review'), ('Townhall', 'townhall'), ('ESOPs', 'esop')]:
    LG[_k] = uri(f'img/logo-app/{_f}.png')
SOL_RED, SOL_WHITE = uri('logos/sol_red.png'), uri('logos/sol_white.png')
BASE_BLUE, BASE_WHITE = uri('logos/q_a20.png'), uri('logos/base_white.png')
FONTS = open('fonts.css').read()

MOCKS = {k: f'sol/{k}.html' for k in ['hire', 'interview', 'wf', 'hris', 'car', 'ts', 'pay', 'output', 'reviews', 'cplan', 'townhall', 'esop', 'goal', 'academy']}

def logos(white=False):
    a, b = (SOL_WHITE, BASE_WHITE) if white else (SOL_RED, BASE_BLUE)
    return f'<div class="logos"><img class="sl" src="{a}" alt="SOL"><span class="x"></span><img class="bl" src="{b}" alt="Base.vn"></div>'

def vbar(ch):
    return f'<div class="vbar">{logos()}<div class="ch">{ch}</div></div>'

def appchip(name, logo=None):
    ic = f'<img src="{logo}" alt="">' if logo else f'<i>{name[0]}</i>'
    return f'<span class="ac">{ic}{name}</span>'

# ---------------- hành trình ----------------
J = [
    ('01', 'Thu hút &amp; tuyển dụng', 'Tin tuyển, ứng viên từ mọi kênh, phỏng vấn', [('E-Hiring', LG['E-Hiring']), ('Interview', LG['Interview'])], 0),
    ('02', 'Tổ chức &amp; định biên', 'Sơ đồ thương hiệu, nhà hàng, vị trí, khung lương', [('Workforce', LG['Workforce'])], 0),
    ('03', 'Hồ sơ &amp; hợp đồng', 'Một hồ sơ cho mỗi người, hợp đồng theo loại', [('HRIS', LG['HRIS'])], 0),
    ('04', 'Đào tạo &amp; hội nhập', 'Khoá học, giấy tờ, checklist ngày đầu', [('Academy', LG['Academy']), ('Careers', LG['Careers'])], 1),
    ('05', 'Công, ca, phép, tăng ca', 'Xếp ca xoay, chấm công, đơn từ', [('Timesheets', LG['Timesheets'])], 1),
    ('06', 'Lương &amp; phiếu lương', 'Lấy công từ Timesheets, nhân viên xác nhận', [('Payroll', LG['Payroll'])], 1),
    ('07', 'Mục tiêu &amp; hiệu suất', 'Mục tiêu, đầu ra công việc, đánh giá', [('Goal', None), ('Output', LG['Output']), ('Reviews', LG['Reviews'])], 2),
    ('08', 'Phát triển &amp; thăng tiến', 'Kế hoạch thăng cấp, quyết định nhân sự', [('Careers', LG['Careers'])], 2),
    ('09', 'Gắn kết &amp; giữ chân', 'Truyền thông nội bộ, cổ phiếu thưởng', [('Townhall', LG['Townhall']), ('ESOPs', LG['ESOPs'])], 2),
]
def journey():
    cols = ''.join(f'''<div class="jc" data-s="{g}" style="--d:{(i % 3) * .12:.2f}s"><div class="jn"><b>{n}</b><i></i></div>
      <h4>{t}</h4><p>{d}</p><div class="jap">{''.join(appchip(a, l) for a, l in apps)}</div></div>''' for i, (n, t, d, apps, g) in enumerate(J))
    return f'''<section class="slide" data-steps="3" data-label="Lưu đồ · Hành trình nhân sự">
 {vbar('Hành trình nhân sự')}
 <div class="head"><div class="ey" data-s="0">Toàn cảnh</div><div class="h1" data-s="0" style="--d:.1s">Hành trình nhân sự <em>trọn vẹn</em> trên Base</div></div>
 <div class="jr"><div class="jline"></div>{cols}</div>
 <div class="jph" data-s="0" style="--d:.3s"><span>Vào làm</span></div><div class="jph p2" data-s="1"><span>Vận hành hằng tháng</span></div><div class="jph p3" data-s="2"><span>Phát triển và giữ chân</span></div>
 <div class="jloop" data-s="3"><svg viewBox="0 0 1728 70" preserveAspectRatio="none"><path d="M1700 4 C1700 52, 1660 60, 1600 60 L128 60 C68 60, 28 52, 28 4"/><path class="ah" d="M18 18 L28 2 L38 18"/></svg>
   <div class="jlt"><b>Một dòng dữ liệu, một vòng đời.</b> Vị trí trong Workforce là gốc: tuyển đúng vị trí, hồ sơ gắn vị trí, công chảy sang lương, quản lý giỏi được đào tạo lên mở nhà hàng mới.</div></div>
</section>'''

# ---------------- toàn cảnh app ----------------
APPS = [
    ('E-Hiring', LG['E-Hiring'], 'Tuyển dụng: tin tuyển, ứng viên, pipeline', 'mock'),
    ('Academy', LG['Academy'], 'Chương trình đào tạo, khoá học, bài kiểm tra', 'mock'),
    ('Interview', LG['Interview'], 'Lịch phỏng vấn, hội đồng, điểm đánh giá', 'mock'),
    ('Workforce', LG['Workforce'], 'Cơ cấu tổ chức, vị trí, định biên', 'mock'),
    ('HRIS', LG['HRIS'], 'Hồ sơ nhân sự, hợp đồng, thuế, bảo hiểm', 'mock'),
    ('Careers', LG['Careers'], 'Hội nhập, lộ trình, quyết định nhân sự', 'mock'),
    ('Timesheets', LG['Timesheets'], 'Công, ca, nghỉ phép, tăng ca', 'mock'),
    ('Payroll', LG['Payroll'], 'Tính lương, phiếu lương, xác nhận', 'mock'),
    ('Goal', None, 'Mục tiêu công ty, nhà hàng, cá nhân', 'mock'),
    ('Output', LG['Output'], 'Đầu ra, mục tiêu, phản hồi, ghi nhận', 'mock'),
    ('Reviews', LG['Reviews'], 'Kỳ đánh giá hiệu suất', 'mock'),
    ('ESOPs', LG['ESOPs'], 'Quyền chọn cổ phần cho quản lý chủ chốt', 'mock'),
    ('Townhall', LG['Townhall'], 'Bản tin, thông báo, kỷ niệm', 'mock'),
]
def apps_slide():
    cards = ''.join(f'''<div class="apc {'has' if m else ''}" data-s="0" style="--d:{.2 + i * .04:.2f}s"><div class="t">{f'<img src="{l}" alt="">' if l else f'<i>{a[0]}</i>'}<b>{a}</b></div><p>{d}</p></div>''' for i, (a, l, d, m) in enumerate(APPS))
    return f'''<section class="slide" data-steps="0" data-label="Toàn cảnh bộ HRM">
 {vbar('Bộ HRM')}
 <div class="head"><div class="ey" data-s="0">HRM Operation Services</div><div class="h1" data-s="0" style="--d:.1s">{len(APPS)} ứng dụng, <em>một nền tảng</em> nhân sự</div>
  <div class="lead" data-s="0" style="--d:.15s">Hồ sơ, chấm công, tính lương, tuyển dụng, đánh giá và phát triển đội ngũ dùng chung một nguồn dữ liệu nhân sự.</div></div>
 <div class="apg">{cards}</div>
</section>'''

# ---------------- trang mockup ----------------
def mks(mk, label, ch, app, logo, t, caps, mp):
    lis = ''.join(f'<li data-i="{i}">{c}</li>' for i, c in enumerate(caps))
    ic = f'<img src="{logo}" alt="">' if logo else f'<i class="lt">{app[0]}</i>'
    return f'''<section class="slide mks" data-steps="{len(caps) - 1}" data-mk="{mk}" data-map="{mp}" data-label="{label}">
 {vbar(ch)}
 <div class="kcol"><div class="app">{ic}{app}</div><div class="t">{t}</div><ol class="kcaps">{lis}</ol></div>
 <div class="kframe"><iframe title="mock" tabindex="-1" scrolling="no"></iframe></div>
</section>'''

def chap(n, name, ds, on):
    tabs = ''.join(f'<span class="{"on" if i == on else ""}">{x}</span>' for i, x in enumerate(['A · Hành trình nhân sự', 'B · Từng chặng trên Base']))
    return f'''<section class="slide chc" data-steps="0" data-label="Phần {n} · {name}">{vbar('')}
<div class="chx"><div class="ey" data-s="0" style="--d:.15s">Phần {n}</div><div class="nm" data-s="0" style="--d:.25s">{name}</div><div class="ds" data-s="0" style="--d:.4s">{ds}</div></div>
<div class="chs" data-s="0" style="--d:.55s">{tabs}</div></section>'''

def text_stage(label, ch, num, title, sub, groups):
    cols = ''.join(f'''<div class="tsc" data-s="0" style="--d:{.25 + i * .12:.2f}s"><div class="t"><i>{a[0]}</i><b>{a}</b></div><p class="dd">{d}</p><ul>{''.join(f'<li>{x}</li>' for x in pts)}</ul></div>''' for i, (a, d, pts) in enumerate(groups))
    return f'''<section class="slide" data-steps="0" data-label="{label}">
 {vbar(ch)}
 <div class="head"><div class="ey" data-s="0">Chặng {num}</div><div class="h1" data-s="0" style="--d:.1s">{title}</div><div class="lead" data-s="0" style="--d:.15s">{sub}</div></div>
 <div class="tsg">{cols}</div>
 <div class="tsn" data-s="0" style="--d:.7s">Các ứng dụng này sẽ được trình bày trực tiếp trên hệ thống tại buổi gặp.</div>
</section>'''

S = []
S.append(f'''<section class="slide cover" data-steps="0" data-label="Bìa">
 <div class="cv-l">
  <div data-s="0" style="--d:.1s">{logos(True)}</div>
  <div class="eb" data-s="0" style="--d:.3s">SOL × Base.vn</div>
  <div class="ttl" data-s="0" style="--d:.45s">Hành trình nhân sự<br>số hoá tại SOL</div>
  <div class="sub" data-s="0" style="--d:.65s">Từ tuyển dụng đến giữ chân đội ngũ hơn 800 người trên chuỗi nhà hàng</div>
  <div class="dt" data-s="0" style="--d:.85s">Tài liệu giới thiệu tính năng · 10 · 2026</div>
 </div>
 <div class="cv-r" data-s="0" style="--d:.2s"><div class="cv-sun"></div><img src="{SOL_WHITE}" alt=""></div>
</section>''')
S.append(f'''<section class="slide" data-steps="0" data-label="Nội dung">
 {vbar('')}
 <div class="ag-h"><div class="ey" data-s="0">SOL × Base.vn · 10/2026</div><div class="h1" data-s="0" style="--d:.1s">Nội dung <em>tài liệu</em></div></div>
 <div class="ag-l"><div class="ag-r" data-s="0" style="--d:.3s"><b>A</b><span class="t">Hành trình nhân sự</span><span class="c">Lưu đồ trọn vẹn và toàn cảnh 13 ứng dụng HRM</span></div>
 <div class="ag-r" data-s="0" style="--d:.42s"><b>B</b><span class="t">Từng chặng trên Base</span><span class="c">Mockup trên dữ liệu minh hoạ của SOL: tuyển dụng, tổ chức, hồ sơ, hội nhập, công ca, lương, phát triển</span></div></div>
</section>''')
S.append(chap('A', 'Hành trình nhân sự', 'Một vòng đời nhân sự khép kín, từ ngày ứng tuyển đến ngày được đào tạo lên quản lý nhà hàng mới', 0))
S.append(journey())
S.append(apps_slide())
S.append(chap('B', 'Từng chặng trên Base', 'Dữ liệu minh hoạ theo chuỗi nhà hàng của SOL: thương hiệu Miwaku, nhà hàng Miwaku Thảo Điền', 1))
S.append(mks('hire', 'E-Hiring', 'Chặng 01 · E-Hiring', 'E-Hiring', LG['E-Hiring'], 'Mọi ứng viên <em>về một pipeline</em>',
    ['52 ứng viên trong tuần từ 7 nguồn: career site, form ứng tuyển, site tích hợp, email, giới thiệu nội bộ.',
     'Lọc theo tin tuyển và stage: nhân viên phục vụ, quản lý nhà hàng; bỏ ứng viên đã loại.',
     'Scorecard từ Interview trả về: 3 ứng viên đạt, sẵn sàng sang bước Offer.'], '[0, 1, 2]'))
S.append(mks('interview', 'Interview', 'Chặng 01 · Interview', 'Interviews', LG['Interview'], 'Phỏng vấn <em>và chấm điểm</em>',
    ['Mọi buổi phỏng vấn của khối Nhà hàng và Bếp trên một danh sách: vòng sàng lọc, thử ca tại nhà hàng, thử tay nghề bếp.',
     'Lọc buổi đã hoàn thành: điểm của hội đồng làm căn cứ chuyển ứng viên sang bước Offer trên E-Hiring.'], '[0, 1]'))
S.append(mks('wf', 'Workforce', 'Chặng 02 · Workforce', 'Workforce', LG['Workforce'], 'Sơ đồ tổ chức <em>theo thương hiệu</em>',
    ['Sơ đồ SOL: Khối Vận hành nhà hàng, Bếp trung tâm và các phòng; số người cập nhật theo hồ sơ.',
     'Mở Khối Vận hành nhà hàng: 7 thương hiệu, số người của từng thương hiệu.',
     'Vào Miwaku: 3 nhà hàng, quản lý từng nhà hàng, danh sách nhân sự và thâm niên.',
     'Vị trí và định biên: vị trí trống cần tuyển, cấp bậc, khung lương của vị trí.'], '[0, 1, 2, 3]'))
S.append(mks('hris', 'HRIS', 'Chặng 03 · HRIS', 'HRIS', LG['HRIS'], 'Hồ sơ, hợp đồng, <em>chính sách</em>',
    ['820 nhân viên đang làm việc trên một danh sách: chính thức, thử việc, bán thời gian, thời vụ.',
     'Hồ sơ Quản lý nhà hàng: thông tin điều hành, hợp đồng hiện tại, hồ sơ nghề nghiệp.',
     'Hợp đồng theo loại: chính thức, thử việc, bán thời gian trả theo giờ, thời vụ; báo sắp hết hạn.',
     'Văn phòng: văn phòng Điện Biên Phủ, Bếp trung tâm và từng nhà hàng là một địa điểm làm việc.',
     'Thuế TNCN: lũy tiến cho chính thức, khấu trừ 10% cho thử việc, bán thời gian, thời vụ.',
     'Bảo hiểm: BHXH, BHYT, BHTN trên lương cơ bản; danh sách chờ đăng ký.'], '[0, 1, 2, 3, 4, 5]'))
S.append(mks('academy', 'Academy', 'Chặng 04 · Academy', 'Academy', LG['Academy'], 'Đào tạo <em>gắn với lộ trình</em>',
    ['Trưởng ca vào học: khoá đang học, lịch học, hạn nộp bài trong tuần.',
     'Chương trình "Chuẩn bị lên Quản lý nhà hàng": 5 khoá theo lộ trình, tiến độ của 72 học viên.',
     'Khoá Quản lý ca và lập lịch ca nằm trong kế hoạch thăng cấp PL-2026-0014 trên Careers.',
     'Học bài: bảng định biên ca theo lượt khách, hoàn thành bài là cập nhật tiến độ.',
     'Báo cáo đào tạo toàn chuỗi: ghi danh, hoàn thành, tỷ lệ đạt bài kiểm tra.',
     'Câu hỏi tình huống chấm bằng AI theo hướng dẫn chấm của phòng Đào tạo.',
     'Sổ điểm: lọc ngay học viên cần chấm ở các nhà hàng.'], '[0, 1, 2, 3, 4, 5, 6]'))
S.append(mks('car', 'Careers · Hội nhập', 'Chặng 04 · Careers', 'Careers', LG['Careers'], 'Hội nhập <em>nhân viên mới</em>',
    ['Hồ sơ hội nhập theo chương trình: Nhà hàng, Bếp, Bếp trung tâm, Văn phòng.',
     'Nhân viên mới tự nộp giấy tờ theo checklist (kể cả giấy chứng nhận ATTP); đủ thì tạo hồ sơ HRIS.'], '[0, 1]'))
S.append(mks('ts', 'Timesheets', 'Chặng 05 · Timesheets', 'Timesheets', LG['Timesheets'], 'Công, ca, <em>phép, tăng ca</em>',
    ['Xếp ca nhà hàng xoay theo tuần: sáng, tối, đóng cửa; nghỉ 1 ngày trong tuần, làm cuối tuần.',
     'Bảng công tự đối chiếu chấm công với ca: đủ điểm, đi muộn, thiếu dữ liệu, tăng ca.',
     'Nhân viên tạo đơn nghỉ phép trên app, thấy ngay quỹ phép còn lại.',
     'Quản lý nhà hàng duyệt; đơn đã duyệt đi thẳng vào bảng công.',
     'Báo cáo tăng ca sau giờ làm: giờ được tính theo phần trùng với dữ liệu chấm công.',
     'Tăng ca được duyệt, kiểm tra trần giờ trong ngày và trong kỳ công.'], '[0, 1, 2, 3, 4, 5]'))
S.append(mks('pay', 'Payroll', 'Chặng 06 · Payroll', 'Payroll', LG['Payroll'], 'Bảng lương <em>từ dữ liệu công</em>',
    ['Bảng lương Miwaku Thảo Điền: lương cơ bản từ HRIS, công từ Timesheets, ra lương thời gian.',
     'Bấm vào ô để xem công thức và nguồn: phụ cấp làm đêm theo số ca đóng cửa.',
     'Nhân viên xác nhận phiếu lương trên app; theo dõi người chưa xác nhận.',
     'Chính sách lương riêng cho khối nhà hàng và khối văn phòng, bếp trung tâm.'], '[0, 1, 2, 3]'))
S.append(mks('goal', 'Goal', 'Chặng 07 · Goal', 'Goals', None, 'Mục tiêu <em>từ chuỗi tới từng ca</em>',
    ['Quản lý nhà hàng mở app thấy ngay: điểm quý so với mức kỳ vọng hôm nay, key result nào đúng tiến độ, cái nào chậm.',
     'Mọi mục tiêu, target và key result của mình trên một bảng; mỗi mục tiêu căn chỉnh lên target của thương hiệu.',
     'Key result giao tới trưởng ca: ai phụ trách, điểm bao nhiêu, cập nhật lúc nào.'], '[0, 1, 2]'))
S.append(mks('output', 'Output', 'Chặng 07 · Output', 'Output', LG['Output'], 'Mục tiêu, phản hồi, <em>ghi nhận</em>',
    ['Mục tiêu đổ về từ dự án: khai trương Miwaku Landmark 81, việc nào xong, việc nào trễ.',
     'Quản lý gửi phản hồi 1:1 và sau sự kiện cho từng nhân viên, có mức đánh giá.',
     'The Wall: đồng đội tặng kudos, bảng xếp hạng người được ghi nhận nhiều nhất tháng.'], '[0, 1, 2]'))
S.append(mks('reviews', 'Reviews', 'Chặng 07 · Reviews', 'Reviews', LG['Reviews'], 'Kỳ đánh giá <em>hiệu suất</em>',
    ['Quản lý nhà hàng thấy ngay các phiếu cần đánh giá, hạn và thời gian ước tính.',
     'Bắt đầu phiếu tiếp theo bằng một cú bấm; kết quả làm căn cứ thăng tiến, tăng lương.'], '[0, 1]'))
S.append(mks('cplan', 'Careers · Kế hoạch thăng cấp', 'Chặng 08 · Careers', 'Careers', LG['Careers'], 'Đào tạo quản lý <em>từ nội bộ</em>',
    ['Kế hoạch thăng cấp Trưởng ca lên Quản lý nhà hàng: bối cảnh, chỉ số, lý do, kết quả mong đợi.',
     'Cột mốc có hạn và bằng chứng: khoá học, điều hành độc lập, chỉ tiêu tháng 12.',
     'Giai đoạn 4/7: đánh giá cuối kỳ, hội đồng xét duyệt, ra quyết định thăng cấp.',
     'Theo chính sách Planning Thăng cấp; quyết định tự tạo hồ sơ Promotion.'], '[0, 1, 2, 3]'))
S.append(mks('car', 'Careers · Quyết định nhân sự', 'Chặng 08 · Careers', 'Careers', LG['Careers'], 'Quyết định <em>nhân sự</em>',
    ['Thăng chức, tăng lương, điều chuyển giữa các nhà hàng trên một danh sách.',
     'Thăng chức Quản lý nhà hàng lên Quản lý khu vực: từ, đến, lương, vòng duyệt; hiệu lực thì cập nhật HRIS.'], '[2, 3]'))
S.append(mks('townhall', 'Townhall', 'Chặng 09 · Townhall', 'Townhall', LG['Townhall'], 'Truyền thông <em>toàn chuỗi</em>',
    ['Bản tin chung cho văn phòng, bếp trung tâm và từng nhà hàng: kỷ niệm, thư ban điều hành, người mới.',
     'Thông báo theo kênh, biết ai chưa đọc: lịch Tết, khoá đào tạo quản lý.'], '[0, 1]'))
S.append(mks('esop', 'ESOPs', 'Chặng 09 · ESOPs', 'ESOPs', LG['ESOPs'], 'Giữ chân <em>quản lý chủ chốt</em>',
    ['Chương trình quyền chọn cho quản lý chủ chốt: đã cấp, còn lại, đề xuất và mốc điều kiện đang chờ.',
     'Từng đợt cấp: người nhận, số quyền chọn, tiến độ vesting.'], '[0, 1]'))
S.append(f'''<section class="slide cover end" data-steps="0" data-label="Cảm ơn">
 <div class="cv-l"><div data-s="0">{logos(True)}</div><div class="ttl" data-s="0" style="--d:.2s">Cảm ơn</div><div class="sub" data-s="0" style="--d:.4s">Base.vn đồng hành cùng SOL trên hành trình nhân sự số</div></div>
 <div class="cv-r" data-s="0" style="--d:.2s"><div class="cv-sun"></div><img src="{SOL_WHITE}" alt=""></div>
</section>''')

mocks = ''.join(f'<script type="text/mock" data-id="{k}">{base64.b64encode(open(f, "rb").read()).decode()}</script>\n' for k, f in MOCKS.items())
tpl = open('sol/deck_tpl.html').read()
html = tpl.replace('/*FONTS*/', FONTS).replace('<!--SLIDES-->', '\n'.join(S)).replace('<!--MOCKS-->', mocks)
open('sol/SOL_Base_Hanh_trinh_nhan_su.html', 'w').write(html)
print(len(html) / 1e6, 'MB', len(S), 'slides')
