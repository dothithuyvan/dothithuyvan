p='sol/build.py'; s=open(p).read()
s=s.replace("'cplan', 'townhall', 'esop']","'cplan', 'townhall', 'esop', 'goal', 'rules']")
s=s.replace("('Goal', None, 'Mục tiêu (mockup qua mục Mục tiêu trong Output)', 'mock')","('Goal', None, 'Mục tiêu công ty, nhà hàng, cá nhân', 'mock')")
s=s.replace("('Work rules', LG['Work rules'], 'Quy định và chính sách', '')","('Work rules', None, 'Quy định và chính sách, xác nhận đã đọc', 'mock')")
s=s.replace("[('Output', LG['Output']), ('Goal', None), ('Reviews', LG['Reviews'])]","[('Goal', None), ('Output', LG['Output']), ('Reviews', LG['Reviews'])]")
GOAL = """S.append(mks('goal', 'Goal', 'Chặng 07 · Goal', 'Goals', None, 'Mục tiêu <em>xuyên suốt</em>',
    ['Mọi mục tiêu đang thực hiện của chuỗi: khai trương nhà hàng mới, doanh thu quý, ATTP, đào tạo; mục tiêu trễ hạn hiện đỏ.',
     'Mỗi quản lý xem mục tiêu mình phụ trách: Quản lý nhà hàng thấy 4 mục tiêu của Miwaku Thảo Điền.'], '[0, 1]'))
"""
RULES = """S.append(mks('rules', 'Work rules', 'Chặng 09 · Work rules', 'Work rules', None, 'Quy định <em>một nơi, ai cũng đọc</em>',
    ['Thư viện quy định của SOL theo nhóm: công ca, nghỉ phép, ATTP, tiêu chuẩn phục vụ, đồng phục, phúc lợi; biết bao nhiêu người đã xác nhận.',
     'Mở một quy định: nội dung, phiên bản, phạm vi áp dụng và danh sách người chưa đọc để gửi nhắc.'], '[0, 1]'))
"""
if "mks('goal'" not in s:
    a=s.index("S.append(mks('output'"); s=s[:a]+GOAL+s[a:]
if "mks('rules'" not in s:
    a=s.index('slide cover end'); a=s.rindex('S.append(', 0, a); s=s[:a]+RULES+s[a:]
open(p,'w').write(s)
