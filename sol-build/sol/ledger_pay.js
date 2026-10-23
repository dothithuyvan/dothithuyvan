// ===== Sổ cái — SOL (Công ty CP Sense Of Life), nhà hàng Miwaku Thảo Điền · bảng lương tháng 10/2026 ở bước Xem lại =====
// Cấu trúc khoản lương: lương thời gian theo công thực tế / công chuẩn 26, phụ cấp làm đêm 30% cho ca đóng cửa sau 22:00,
// tăng ca 150%, BHXH trên lương cơ bản + trách nhiệm, đoàn phí 0,5%. Tên người, mức lương, số công, số ca, giờ tăng ca là giả định.
const POLICY = 'Bảng lương Khối Nhà hàng';
const RUN = 'Bảng lương tháng 10/2026 – Miwaku Thảo Điền';
const POL_EMP = 731, CC = 26, NIGHT = 0.3;
// [tên, chức danh, lương cơ bản (HRIS), trách nhiệm, xăng xe + điện thoại, người phụ thuộc, xác nhận, công tính lương, số ca đóng cửa, giờ tăng ca, KPI, tạm ứng, ca đóng cửa T9, tăng ca T9, công T9]
const EMP = [
  ['Võ Minh Quân', 'Quản lý nhà hàng', 17500000, 2000000, 800000, 1, 'ok', 26, 8, 6, 1500000, 0, 9, 5, 26],
  ['Trương Mỹ Linh', 'Trưởng ca', 14000000, 1000000, 500000, 0, 'ok', 26, 10, 8, 1000000, 0, 10, 7, 26],
  ['Hồ Tấn Phát', 'Đầu bếp sushi', 12500000, 0, 500000, 1, 'ok', 26, 12, 10, 800000, 0, 11, 9, 26],
  ['Ngô Bảo Trâm', 'Đầu bếp sushi', 12000000, 0, 500000, 0, 'wait', 25, 11, 8, 800000, 2000000, 12, 8, 26],
  ['Mai Đức Thịnh', 'Phụ bếp', 9000000, 0, 300000, 0, 'ok', 26, 12, 9.5, 500000, 0, 10, 8, 26],
  ['Châu Ngọc Ánh', 'Phụ bếp', 8000000, 0, 300000, 0, 'ok', 24.5, 8, 4, 400000, 0, 6, 3, 25],
  ['Phan Gia Bảo', 'Phụ bếp', 8500000, 0, 300000, 0, 'ok', 26, 13, 12.25, 500000, 1500000, 12, 10, 26],
  ['Tạ Thu Uyên', 'Phụ bếp', 8500000, 0, 300000, 1, 'wait', 25.5, 9, 6, 500000, 0, 9, 5, 26],
  ['Lý Minh Khang', 'Nhân viên phục vụ', 9000000, 0, 300000, 0, 'ok', 26, 10, 7.75, 500000, 0, 9, 6, 26],
  ['Nguyễn Văn An', 'Nhân viên phục vụ', 8500000, 0, 300000, 0, 'ok', 26, 9, 5, 400000, 0, 8, 4, 26],
];
