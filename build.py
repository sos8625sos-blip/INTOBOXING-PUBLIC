"""app.html(앱 본문)을 GitHub Pages용 index.html로 감싸는 스크립트. 사용법: python3 build.py"""
import re, pathlib
src = pathlib.Path('app.html').read_text(encoding='utf-8')
cut = src.index('</style>') + len('</style>')
head_part, body_part = src[:cut], src[cut:]
head_part = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', '', head_part)
html = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#0c0c0f">
<meta name="description" content="인투복싱 라운드 타이머 · 콤비 콜아웃 · 운동 기록">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" href="icons/icon-192.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="INTO BOXING">
<style>
:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
body{{margin:0;font:14px/1.5 system-ui,-apple-system,sans-serif}}
img{{max-width:100%}}
[hidden]{{display:none!important}}
</style>
{head_part}
</head>
<body>
{body_part}
<script>
if('serviceWorker' in navigator){{window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{{}}))}}
</script>
</body>
</html>
'''
pathlib.Path('index.html').write_text(html, encoding='utf-8')
print('index.html 생성 완료')
