# SOL × Base · Hành trình nhân sự — mã dựng deck

Chạy từ thư mục `sol-build/`:

```
python3 sol/m_interview.py   # (tương tự m_output, m_reviews, m_townhall, m_esop, m_goal_rules)
python3 sol/build.py         # ghép deck -> sol/SOL_Base_Hanh_trinh_nhan_su.html
```

- `sol/*.html`: 14 mockup đã chạy dữ liệu SOL (nhúng vào deck qua `build.py`).
- `sol/kit.py`: khung chung cho mockup mới (Interview, Output, Reviews, Townhall, ESOPs, Goal, Work rules).
- `sol/patch_*.py`: script đã dùng một lần để đổi dữ liệu Cocoon/Quess sang SOL (cần file gốc, không kèm ở đây); sửa tiếp thì sửa thẳng `sol/*.html`.
- `logos/`, `img/logo-app/`: logo SOL, Base và logo app từ thư viện giao diện.

## Trạng thái (22 trang)
- Academy: `sol/patch_academy.py` đổi mock gốc `src/academy_goc.html` sang SOL (7 cảnh).
- Goal: `sol/m_goal.py` dựng theo hồ sơ Goal (Trang chủ, Mục tiêu, Key result).
- Work rules: đã bỏ khỏi deck theo yêu cầu.
