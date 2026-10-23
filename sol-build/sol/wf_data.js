// ===== SOL (Công ty CP Sense Of Life) · Workforce · hôm nay 28/10/2026 =====
// Nguồn công khai: chuỗi nhà hàng Nhật, 7 thương hiệu, 37 cửa hàng, hơn 800 nhân sự. Phân bổ theo thương hiệu, tên người, định biên là giả định.
const GR = {
  pink: 'rgb(249,168,212),rgb(219,39,119)', orange: 'rgb(253,186,116),rgb(234,88,12)', teal: 'rgb(94,234,212),rgb(13,148,136)',
  indigo: 'rgb(165,180,252),rgb(79,70,229)', rose: 'rgb(251,113,133),rgb(225,29,72)', cyan: 'rgb(103,232,249),rgb(8,145,178)',
  green: 'rgb(134,239,172),rgb(22,163,74)', amber: 'rgb(252,211,77),rgb(202,138,4)', blue: 'rgb(147,197,253),rgb(37,99,235)',
  sky: 'rgb(125,211,252),rgb(2,132,199)', slate: 'rgb(203,213,225),rgb(71,85,105)',
};
const GRL = Object.values(GR);
const unacc = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
const mailOf = (name) => { const w = unacc(name).split(' '); return w[w.length - 1] + '.' + w.slice(0, -1).map(x => x[0]).join(''); };
const PER = (name, g, ten) => ({ name, g, mail: mailOf(name), ten });
const P = {
  truc: PER('Trần Ngọc Hân', GR.rose, '3 năm 2 tháng'),
  khanh: PER('Nguyễn Hoàng Phúc', GR.blue, '5 năm 4 tháng'),
  mai: PER('Lê Thị Thu Thảo', GR.pink, '4 năm 1 tháng'),
  hien: PER('Phạm Gia Huy', GR.amber, '4 năm 8 tháng'),
  hoa: PER('Võ Minh Quân', GR.orange, '3 năm 6 tháng'),
  nam: PER('Đặng Thanh Tú', GR.teal, '2 năm 9 tháng'),
  viet: PER('Huỳnh Bảo Ngọc', GR.indigo, '2 năm 2 tháng'),
  luc: PER('Lý Minh Khang', GR.cyan, '1 năm 4 tháng'),
  ha: PER('Lý Minh Khang', GR.cyan, '1 năm 4 tháng'),
};
const ME = P.truc;   // người đang đăng nhập: Chuyên viên C&B, Phòng Hành chính Nhân sự
const av = (p, s) => `<span class="mk-av" style="background:linear-gradient(135deg,${p.g});${s ? `width:${s}px;height:${s}px;font-size:${Math.round(s * .36)}px` : ''}">${ini2(p.name)}</span>`;

const T = (id, n, ty, o = {}) => ({ id, n, ty, ...o });
const ORG = T('root', 'SOL', 'co', { own: 3, ht: 'Ban Giám đốc', kids: [
  T('tl', 'Khối Vận hành nhà hàng', 'dv', { own: 5, ht: 'Giám đốc Vận hành', kids: [
    T('tl_dp', 'Kohaku Sushi', 'th', { who: P.hien, np: 256, xu: 12, ht: 'Quản lý thương hiệu' }),
    T('ksy', 'Kohaku Sashimi & Yakiniku', 'th', { np: 144, xu: 6, ht: 'Quản lý thương hiệu' }),
    T('kru', 'Kohaku Ramen & Udon', 'th', { np: 112, xu: 7, ht: 'Quản lý thương hiệu' }),
    T('ms', 'Machida Shoten', 'th', { np: 70, xu: 5, ht: 'Quản lý thương hiệu' }),
    T('s79', 'S79 Teppanyaki', 'th', { np: 66, xu: 3, ht: 'Quản lý thương hiệu' }),
    T('csmp', 'Miwaku', 'th', { who: P.khanh, ht: 'Quản lý thương hiệu', kids: [
      T('ta', 'Miwaku Thảo Điền', 'nh', { who: P.hoa, ht: 'Quản lý nhà hàng' }),
      T('tb', 'Miwaku Phú Mỹ Hưng', 'nh', { who: P.nam, ht: 'Quản lý nhà hàng' }),
      T('tc', 'Miwaku Lê Thánh Tôn', 'nh', { who: P.viet, ht: 'Quản lý nhà hàng' }),
    ] }),
    T('dn', 'Date Nariya', 'th', { np: 18, xu: 1, ht: 'Quản lý thương hiệu' }),
  ] }),
  T('bep', 'Bếp trung tâm', 'dv', { np: 36, ht: 'Bếp trưởng điều hành' }),
  T('mkt', 'Marketing', 'dp', { np: 14, ht: 'Trưởng phòng' }),
  T('kt', 'Tài chính Kế toán', 'dp', { np: 12, ht: 'Kế toán trưởng' }),
  T('hcns', 'Hành chính Nhân sự', 'dp', { np: 10, ht: 'Trưởng phòng' }),
  T('dt', 'Đào tạo', 'dp', { np: 6, ht: 'Trưởng phòng' }),
  T('mh', 'Mua hàng', 'dp', { np: 8, ht: 'Trưởng phòng' }),
] });
const UNIT = {}; (function walk(u, par) { u.par = par; UNIT[u.id] = u; (u.kids || []).forEach(k => walk(k, u)); })(ORG, null);
const desc = (u) => (u.kids || []).reduce((s, k) => s + 1 + desc(k), 0);
const xuAll = (u) => (u.xu || 0) + (u.kids || []).reduce((s, k) => s + xuAll(k), 0);
const N_UNITS = 1 + desc(ORG) + xuAll(ORG);
const CHIP = { co: 'Công ty', dv: 'Khối', dp: 'Phòng ban', tm: 'Tổ', th: 'Thương hiệu', nh: 'Nhà hàng' };

// ---------- Miwaku: 3 nhà hàng, 63 vị trí định biên (60 có người, 3 trống) ----------
const HO = ['Nguyễn', 'Trần', 'Lê', 'Phạm', 'Huỳnh', 'Võ', 'Đặng', 'Bùi', 'Ngô', 'Dương', 'Lý', 'Trương', 'Hồ', 'Châu', 'Lương', 'Mai', 'Đỗ', 'Tạ', 'Phan', 'Lâm'];
const DEM = ['Văn', 'Thị', 'Minh', 'Thanh', 'Hoàng', 'Ngọc', 'Quốc', 'Thu'];
const TEN = ['An', 'Bình', 'Cường', 'Dũng', 'Hạnh', 'Hiếu', 'Hùng', 'Khoa', 'Lan', 'Linh', 'Long', 'Nhân', 'Nhi', 'Phát', 'Phúc', 'Quân', 'Sơn', 'Tâm', 'Thảo', 'Thịnh', 'Toàn', 'Trang', 'Tuấn', 'Vy', 'Yến', 'Hậu', 'Kiệt', 'Lộc', 'Ngân', 'Như'];
const FIX = ['Trương Mỹ Linh', 'Hồ Tấn Phát', 'Ngô Bảo Trâm', 'Mai Đức Thịnh', 'Châu Ngọc Ánh', 'Phan Gia Bảo', 'Tạ Thu Uyên'];
const NAMES = ['Bùi Quang Vinh', ...FIX]; for (let k = 0; NAMES.length < 70; k++) NAMES.push(`${HO[(k * 7) % HO.length]} ${DEM[(k * 3) % DEM.length]} ${TEN[(k * 11) % TEN.length]}`);
const TENS = ['1 năm 3 tháng', '2 năm 8 tháng', '4 tháng', '7 tháng', '3 năm 2 tháng', '9 tháng', '1 năm 7 tháng', '2 năm 1 tháng', '11 tháng', '1 năm 10 tháng', '3 năm 9 tháng'];
let _ni = 0;
const nextP = () => { const name = NAMES[_ni]; const p = PER(name, GRL[_ni % GRL.length], TENS[_ni % TENS.length]); _ni++; return p; };
// mỗi nhà hàng: [id, quản lý, vị trí trống ở chức danh nào]
const ROLES = [['Trưởng ca', 'TRCA', 'G3', 1], ['Đầu bếp sushi', 'DBSU', 'G2', 2], ['Phụ bếp', 'PHBE', 'G1', 4], ['Nhân viên phục vụ', 'NVPV', 'G1', 8], ['Thu ngân', 'THNG', 'G1', 2], ['Lễ tân', 'LETA', 'G1', 1]];
const TEAMS = [['ta', P.hoa, { NVPV: 'P1' }], ['tb', P.nam, { PHBE: 'P1', NVPV: 'P2' }], ['tc', P.viet, {}]];
const NS = [];
let _code = 401;
const add = (t, pr, who, g, u, pri) => NS.push({ code: 'S-0' + (_code++), t, pr, who, g, u, pri });
add('Quản lý thương hiệu', 'QLTH', P.khanh, 'G5', 'csmp');
add('Bếp trưởng thương hiệu', 'BETR', P.mai, 'G4', 'csmp');
add('Điều phối ca', 'ĐPCA', nextP(), 'G2', 'csmp');
TEAMS.forEach(([id, lead, open]) => {
  add('Quản lý nhà hàng', 'QLNH', lead, 'G4', id);
  ROLES.forEach(([t, pr, g, n]) => {
    for (let i = 0; i < n; i++) add(t, pr, (id === 'ta' && pr === 'NVPV' && i === 0) ? P.luc : nextP(), g, id);
    if (open[pr]) add(t, pr, null, g, id, open[pr]);
  });
});
NS.forEach(r => { r.loc = 'hcm'; r.cc = 'Vận hành nhà hàng'; });

// ---------- trung tâm chi phí: [tên, mã, có người, trống, tạm dừng, bãi bỏ] ----------
const CCD = [
  ['Ban Giám đốc', 'BGD', 3, 0, 0, 0],
  ['Vận hành nhà hàng', 'VHNH', 731, NS.filter(r => !r.who).length + 9, 0, 0],
  ['Bếp trung tâm', 'BTT', 36, 2, 0, 0],
  ['Marketing', 'MKT', 14, 1, 0, 0],
  ['Tài chính Kế toán', 'TCKT', 12, 0, 0, 0],
  ['Hành chính Nhân sự', 'HCNS', 10, 1, 0, 0],
  ['Đào tạo', 'DT', 6, 0, 0, 0],
  ['Mua hàng', 'MH', 8, 0, 0, 0],
];
const CC = CCD.map(x => [x[0], x[2] + x[3] + x[4] + x[5], x[1]]);
const CCN = Object.fromEntries(CC.map(x => [x[0], x[1]]));
const CC_CODE = Object.fromEntries(CC.map(x => [x[0], x[2]]));
const P_ALL = CC.reduce((s, x) => s + x[1], 0);
const SUM = (k) => CCD.reduce((s, x) => s + x[k], 0);
const ST_FILLED = SUM(2), ST_OPEN = SUM(3), ST_HOLD = SUM(4), ST_ELIM = SUM(5);
const N_PPL = ST_FILLED;
const LOC = {
  hcm: ['TP. Hồ Chí Minh', '#DC2626', P_ALL],
};
const GRADE = { G1: ['Nhân viên', 8e6, 9.5e6, 12e6], G2: ['Chuyên viên', 10e6, 12.5e6, 15e6], G3: ['Trưởng ca', 12e6, 14e6, 16.5e6], G4: ['Quản lý', 15e6, 17.5e6, 21e6], G5: ['Quản lý cấp cao', 22e6, 28e6, 35e6] };
const FAM = 'Vận hành nhà hàng';
const UCOL = { csmp: '#DC2626', ta: '#EA580C', tb: '#DB2777', tc: '#7C3AED' };
const PC = (u) => {
  if (u.id === 'csmp') return NS.filter(r => r.who).length;
  if (['ta', 'tb', 'tc'].includes(u.id)) return NS.filter(r => r.who && r.u === u.id).length;
  if (u.np != null) return u.np;
  return (u.own || 0) + (u.kids || []).reduce((s, k) => s + PC(k), 0);
};
console.assert(PC(ORG) === 820 && N_PPL === 820 && PC(UNIT.csmp) === 60 && PC(UNIT.tl) === 731, 'nhân sự lệch: ' + PC(ORG) + '/' + N_PPL + '/' + PC(UNIT.csmp));
