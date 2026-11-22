import re
t=open('template.html',encoding='utf-8').read()
for k,f in [('AREF','aref.b64'),('ZAINR','zainr.b64'),('ZAINB','zainb.b64'),('LOGO','logo.b64')]:
    t=t.replace('{{%s}}'%k,open(f).read().strip())
open('/dev/null','w',encoding='utf-8').write(t)
i=t.index('</style>')+len('</style>'); head=t[:i].replace('<meta name="claude:viewport-fit-sides" content="cover">\n',''); body=t[i:]
open('index.html','w',encoding='utf-8').write('<!doctype html>\n<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'+head+'\n</head><body style="margin:0">'+body+'\n</body></html>')
m=re.search(r'<script>\n\(function\(\)\{.*?</script>',t,re.S); open('check.js','w',encoding='utf-8').write(m.group(0)[8:-9])
