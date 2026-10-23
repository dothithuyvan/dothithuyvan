# Bộ khung chung cho mock mới (ngôn ngữ thiết kế mới, cửa sổ 1440×880, bấm mới chuyển cảnh)
import json, base64, re, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
ICONS = json.load(open('icons.json'))
ICONS.update({
 'video': '<path d="m16 13 5.223 3.482a.5.5 0 0 0 .777-.416V7.87a.5.5 0 0 0-.752-.432L16 10.5"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
 'megaphone': '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
 'gift': '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5A4.8 8 0 0 1 12 8a4.8 8 0 0 1 4.5-5 2.5 2.5 0 0 1 0 5"/>',
 'message-circle': '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 'smile': '<circle cx="12" cy="12" r="10"/><path d="M8 14s1.5 2 4 2 4-2 4-2"/><line x1="9" x2="9.01" y1="9" y2="9"/><line x1="15" x2="15.01" y1="9" y2="9"/>',
 'image': '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
 'cake': '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/>',
 'bookmark': '<path d="m19 21-7-4-7 4V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2v16z"/>',
 'circle-dot': '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="1"/>',
 'send': '<path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/>',
 'pie-chart': '<path d="M21.21 15.89A10 10 0 1 1 8 2.83"/><path d="M22 12A10 10 0 0 0 12 2v10z"/>',
 'table': '<path d="M12 3v18"/><rect width="18" height="18" x="3" y="3" rx="2"/><path d="M3 9h18"/><path d="M3 15h18"/>',
 'folder': '<path d="M20 20a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.9a2 2 0 0 1-1.69-.9L9.6 3.9A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2Z"/>',
 'link': '<path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/>',
 'radar': '<path d="M19.07 4.93A10 10 0 0 0 6.99 3.34"/><path d="M4 6h.01"/><path d="M2.29 9.62A10 10 0 1 0 21.31 8.35"/><path d="M16.24 7.76A6 6 0 1 0 8.23 16.67"/><path d="M12 18h.01"/><path d="M17.99 11.66A6 6 0 0 1 15.77 16.67"/><circle cx="12" cy="12" r="2"/><path d="m13.41 10.59 5.66-5.66"/>',
})

def I(n, s=16, sw=2, c='currentColor'):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" style="flex:none;display:block">{ICONS.get(n, "")}</svg>'

def logo(k):
    return 'data:image/png;base64,' + base64.b64encode(open(f'img/logo-app/{k}.png', 'rb').read()).decode()

GR = ['#2563EB', '#0D9488', '#EA580C', '#DB2777', '#7C3AED', '#0891B2', '#CA8A04', '#16A34A', '#DC2626', '#4F46E5']
def ini(n):
    w = n.split(); return (w[0][0] + w[-1][0]).upper()
def av(n, s=28, k=None):
    c = GR[(k if k is not None else sum(map(ord, n))) % len(GR)]
    return f'<span class="av" style="width:{s}px;height:{s}px;font-size:{round(s*.36)}px;background:{c}">{ini(n)}</span>'

FONT = open('fonts.css').read()
FONT = '\n'.join(f for f in re.findall(r'@font-face\{[^}]*\}', FONT) if 'Inter' in f)

CSS = '''
*{box-sizing:border-box}html,body{margin:0;height:100%;background:#E9EDF2;font-family:"Inter",system-ui,sans-serif;color:#1F2937}
.wrap{display:grid;place-items:center;height:100%}.scaler{position:relative}
.cv{position:absolute;left:0;top:0;width:1440px;height:880px;transform-origin:0 0;background:#fff;border-radius:12px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 20px 60px rgba(15,23,42,.15)}
.chrome{display:flex;align-items:center;gap:8px;padding:9px 12px;background:#F3F4F6;border-bottom:1px solid #E5E7EB}.chrome i{width:11px;height:11px;border-radius:50%}
.chrome .url{margin-left:10px;flex:1;height:26px;display:flex;align-items:center;gap:6px;padding:0 10px;background:#fff;border:1px solid #E5E7EB;border-radius:7px;font-size:11.5px;color:#6B7280}.chrome .url b{color:#111827;font-weight:600}
.top{display:flex;align-items:center;gap:14px;height:48px;padding:0 16px;border-bottom:1px solid #E5E7EB;flex:none}
.top .br{display:flex;align-items:center;gap:8px;font-weight:700;font-size:15px;color:#111827;width:200px}.top .br img{width:24px;height:24px;border-radius:6px}
.top .se{margin:0 auto;display:flex;align-items:center;gap:8px;width:360px;height:30px;padding:0 10px;border:1px solid #E5E7EB;border-radius:7px;background:#F9FAFB;color:#6B7280;font-size:12.5px}
.top .se kbd{margin-left:auto;font:10px Inter;padding:1px 5px;border:1px solid #E5E7EB;border-radius:4px;color:#9CA3AF;background:#fff}
.top .ic{display:flex;align-items:center;gap:14px;color:#6B7280;width:200px;justify-content:flex-end}.top .bd{position:relative}.top .bd b{position:absolute;top:-7px;right:-11px;background:#EF4444;color:#fff;font-size:9px;padding:1px 4px;border-radius:8px}
.av{display:inline-grid;place-items:center;border-radius:50%;color:#fff;font-weight:600;flex:none;line-height:1}
.app{flex:1;display:flex;min-height:0}
.side{width:210px;flex:none;border-right:1px solid #E5E7EB;padding:12px 10px;display:flex;flex-direction:column;gap:2px}
.side .tt{display:flex;align-items:center;gap:8px;font-weight:700;font-size:14px;color:#111827;padding:4px 8px 12px}
.row{display:flex;align-items:center;gap:9px;height:31px;padding:0 9px;border-radius:7px;font-size:13px;color:#1F2937;white-space:nowrap;overflow:hidden}
.row span{overflow:hidden;text-overflow:ellipsis}.row em{margin-left:auto;font-style:normal;font-size:11.5px;color:#9CA3AF}
.row.on{background:#2563EB;color:#fff;font-weight:600}.row.on em{color:#DBEAFE}.row svg{color:inherit}
.sec{font-size:10.5px;font-weight:700;letter-spacing:.06em;color:#6B7280;padding:14px 9px 4px}
.sub .row{padding-left:22px;color:#374151}
.foot{margin-top:auto;display:flex;flex-direction:column;gap:2px;padding-top:10px;border-top:1px solid #F3F4F6}
.ws{display:flex;align-items:center;gap:8px;height:34px;padding:0 8px;font-size:13px;font-weight:600}.ws i{width:22px;height:22px;border-radius:6px;background:#C8102E;color:#fff;display:grid;place-items:center;font-style:normal;font-size:11px}
.main{flex:1;min-width:0;display:flex;flex-direction:column;background:#fff;position:relative}
.hd{display:flex;align-items:center;gap:12px;height:56px;padding:0 22px;border-bottom:1px solid #E5E7EB;flex:none}
.hd .t{font-size:16px;font-weight:700;color:#111827}.hd .n{font-size:12.5px;color:#6B7280}
.btn{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 12px;border-radius:7px;background:#2563EB;color:#fff;font-size:12.5px;font-weight:600;white-space:nowrap}
.btn.gh{background:#fff;color:#374151;border:1px solid #E5E7EB}
.q{display:flex;align-items:center;gap:7px;height:32px;width:220px;padding:0 10px;border:1px solid #E5E7EB;border-radius:7px;color:#9CA3AF;font-size:12.5px}
.ml{margin-left:auto}
.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl th{text-align:left;font-size:11px;font-weight:600;letter-spacing:.04em;color:#6B7280;background:#F9FAFB;padding:10px 12px;border-bottom:1px solid #E5E7EB;white-space:nowrap}
.tbl td{padding:0 12px;height:56px;border-bottom:1px solid #F3F4F6;vertical-align:middle}
.tbl b{font-weight:600;color:#111827}.tbl small{display:block;color:#6B7280;font-size:11.5px;margin-top:2px}
.nm{display:flex;align-items:center;gap:10px}
.chip{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 8px;border-radius:6px;font-size:11.5px;font-weight:600;white-space:nowrap}
.c-g{background:#DCFCE7;color:#15803D}.c-b{background:#DBEAFE;color:#1D4ED8}.c-o{background:#FFEDD5;color:#C2410C}.c-r{background:#FEE2E2;color:#B91C1C}.c-x{background:#F3F4F6;color:#4B5563}.c-v{background:#EDE9FE;color:#6D28D9}.c-t{background:#CCFBF1;color:#0F766E}.c-y{background:#FEF3C7;color:#A16207}
.card{border:1px solid #E5E7EB;border-radius:10px;background:#fff}
.kpi{padding:14px 16px}.kpi span{display:block;font-size:11px;font-weight:600;letter-spacing:.05em;color:#6B7280;text-transform:uppercase}.kpi b{display:block;font-size:26px;font-weight:700;color:#111827;margin-top:6px}.kpi small{display:block;font-size:11.5px;color:#6B7280;margin-top:4px}
.dot{width:8px;height:8px;border-radius:50%;display:inline-block;flex:none}
.scr{flex:1;overflow:hidden}
[data-sc].off{display:none!important}
.hi{outline:2px solid #2563EB;outline-offset:2px;border-radius:10px;box-shadow:0 0 0 6px rgba(37,99,235,.12)}
.anim [data-ad]{animation:rin .5s cubic-bezier(.2,.7,.2,1) both}
@keyframes rin{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
@media (prefers-reduced-motion: reduce){.anim [data-ad]{animation:none}}
.stepi{position:fixed;right:14px;bottom:10px;font:12px Inter;color:#6B7280}
'''

JS = '''
var cv=document.querySelector('.cv'),sc=document.querySelector('.scaler'),EMB=/[?&]embed/.test(location.search)||window.parent!==window;
function fit(){var s=Math.min(innerWidth/1440,(innerHeight-(EMB?0:24))/880);cv.style.transform='scale('+s+')';sc.style.width=1440*s+'px';sc.style.height=880*s+'px'}
addEventListener('resize',fit);fit();
if(EMB){document.documentElement.style.background='transparent';document.body.style.background='transparent';cv.style.boxShadow='none';cv.style.borderRadius='0';document.querySelector('.stepi').style.display='none'}
var N=+document.body.dataset.n,cur=-1;
function has(l,i){return (' '+l+' ').indexOf(' '+i+' ')>=0}
function show(i,anim){i=Math.max(0,Math.min(N-1,+i||0));if(i===cur)return;cur=i;
 cv.classList.remove('anim');void cv.offsetWidth;if(anim!==false)cv.classList.add('anim');
 document.querySelectorAll('[data-sc]').forEach(function(e){e.classList.toggle('off',!has(e.dataset.sc,i))});
 document.querySelectorAll('[data-hi]').forEach(function(e){e.classList.toggle('hi',has(e.dataset.hi,i))});
 document.querySelectorAll('[data-ad]').forEach(function(e){e.style.animationDelay=e.dataset.ad+'ms'});
 document.querySelector('.stepi').textContent=(i+1)+' / '+N}
addEventListener('message',function(e){var m=e.data||{};if(m.mockGo!=null)show(m.mockGo,m.anim)});
if(!EMB){sc.addEventListener('click',function(){show(cur+1)});addEventListener('keydown',function(e){if(e.key==='ArrowRight'||e.key===' ')show(cur+1);if(e.key==='ArrowLeft')show(cur-1,false)})}
var h=(location.hash.match(/^#s(\\d+)/)||[])[1];show(h?h-1:0,!h);
'''

def page(title, url, app_name, app_logo, body, n):
    me = av('Trần Ngọc Hân', 26, 8)
    return f'''<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>{title}</title><style>{FONT}{CSS}</style></head>
<body data-n="{n}"><div class="wrap"><div class="scaler"><div class="cv">
<div class="chrome"><i style="background:#FE5F58"></i><i style="background:#FCBC3F"></i><i style="background:#34C648"></i><div class="url"><b>sol.base.vn</b>{url}</div></div>
<div class="top"><div class="br">{('<span style="width:24px;height:24px;border-radius:6px;background:#2563EB;color:#fff;display:grid;place-items:center;font-size:12px;font-weight:700">' + app_logo[7:] + '</span>') if app_logo.startswith('letter:') else f'<img src="{app_logo}" alt="">'}{app_name}</div><div class="se">{I('search',14)}Tìm kiếm tất cả…<kbd>Ctrl+K</kbd></div>
<div class="ic">{I('circle-question-mark',17)}<span class="bd">{I('bell',17)}<b>3</b></span>{I('moon',17)}{me}{I('chevron-down',15)}</div></div>
<div class="app">{body}</div></div></div></div><div class="stepi"></div><script>{JS}</script></body></html>'''

def ad(i, base=80, step=50):
    return f' data-ad="{base + i * step}"'
