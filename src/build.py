"""Build the bilingual website as static HTML and assets."""
from pathlib import Path
from html import escape as e
from hashlib import sha256
from shutil import copytree, copy2, rmtree
import os
from urllib.parse import urlsplit
import json
from employers import employers
from content import pages, DOJ
root=Path(__file__).resolve().parent.parent
src=root/'src'
stylesheet = (src / 'style.css').read_text()
style_version = sha256(stylesheet.encode()).hexdigest()[:12]
base = os.environ.get('SITE_URL') or json.loads((root/'site.json').read_text())['origin']
base = base.rstrip('/')
parsed = urlsplit(base)
if parsed.scheme not in ('http', 'https') or not parsed.netloc or parsed.query or parsed.fragment:
    raise ValueError('SITE_URL must be the public site URL, optionally including its project path.')
prefix = parsed.path
routes={}
def path(lang,slug=''):
    return ('/' if lang=='zh' else '/en/')+(slug+'/' if slug else '')
def asset(url,body,mime):
    if prefix and mime.startswith('text/html'):
        body = body.replace('href="/', f'href="{prefix}/').replace('src="/', f'src="{prefix}/')
    routes[url]=[mime,body]
def button(url,label,light=False):
    return f'<a class="button{" light" if light else ""}" href="{url}">{e(label)} <span class="arr" aria-hidden="true">↗</span></a>'
def link(url,label):
    return f'<a href="{e(url,quote=True)}">{e(label)}</a>'
def wechat_panel(lang):
    if lang == 'zh':
        title = '扫码加微信咨询'
        instructions = '在手机上可先保存二维码，再用微信「扫一扫」从相册识别。'
        download = '保存二维码'
        alt = '美国 Export License 咨询微信二维码'
    else:
        title = 'Scan to connect on WeChat'
        instructions = 'On your phone, save the code, then select it from your photos in WeChat Scan.'
        download = 'Save QR code'
        alt = 'WeChat QR code for U.S. export license questions'
    return f'''<section class="wechat-panel" id="wechat-consult" aria-labelledby="wechat-title">
        <h2 id="wechat-title">{e(title)}</h2>
        <img class="wechat-qr" src="/wechat-qr.png" width="516" height="516" fetchpriority="high" alt="{e(alt)}">
        <a class="textlink" href="/wechat-qr.png" download="wechat-qr.png">{e(download)} <span aria-hidden="true">↓</span></a>
        <p class="scan-help">{e(instructions)}</p>
        </section>'''

def make(lang,slug,title,desc,main):
    zh=lang=='zh'
    t=lambda a,b:a if zh else b
    home=path(lang); other='en' if zh else 'zh'; url=path(lang,slug)
    contact_link = '#wechat-consult' if not slug or slug == 'contact' else path(lang, 'contact')
    brand=f'<a class="brand" href="{home}" aria-label="Waferpath {t("首页","home")}"><i class="mark" aria-hidden="true"></i>Waferpath</a>'
    alt=''.join(f'<link rel="alternate" hreflang="{c}" href="{base}{path(l,slug)}">' for c,l in [('zh-Hans','zh'),('en','en'),('x-default','en')])
    ld={'@context':'https://schema.org','@type':'Article' if slug in [p[0] for p in pages[lang]] else 'WebPage','name':title,'description':desc,'url':base+url,'inLanguage':t('zh-Hans','en'),'publisher':{'@type':'Organization','name':'Waferpath','url':base+'/'},'isPartOf':{'@type':'WebSite','name':'Waferpath','url':base+'/'}}
    asset(url, f'''<!doctype html><html lang="{t('zh-CN','en')}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{e(title)} | Waferpath</title><meta name="description" content="{e(desc,quote=True)}"><link rel="canonical" href="{base}{url}">{alt}<meta property="og:type" content="website"><meta property="og:title" content="{e(title,quote=True)}"><meta property="og:description" content="{e(desc,quote=True)}"><meta property="og:url" content="{base}{url}"><meta property="og:image" content="{base}/wafer-macro.webp"><link rel="stylesheet" href="/style.css?v={style_version}"><link rel="icon" href="/icon.png"><script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script></head><body><a class="skip" href="#content">{t('跳到正文','Skip to content')}</a><header class="top"><div class="wrap">{brand}<nav class="nav"><a href="{path(lang,'companies')}">{t('公司资料','Companies')}</a><a href="{home}#guides">{t('求职指南','Guides')}</a><a href="{home}#questions">{t('常见问题','FAQ')}</a></nav><a class="lang" lang="{other}" href="{path(other,slug)}">{t('English','中文')}</a>{button(contact_link,t('微信咨询','WeChat'))}</div></header><main class="wrap" id="content">{main}</main><footer class="foot"><div class="wrap">{brand}<span>{t('半导体求职与出口许可','Semiconductor careers & export licensing')}</span><a href="{path(lang,'contact')}">{t('联系咨询','Contact')}</a></div></footer></body></html>''','text/html; charset=utf-8')
for lang,data in pages.items():
    zh=lang=='zh';t=lambda a,b:a if zh else b
    h=path(lang); contact=path(lang,'contact')
    cards=''
    for slug,title,desc,sections,refs in data:
        cards+=f'<a class="card" href="{path(lang,slug)}"><span class="arr" aria-hidden="true">↗</span><h3>{e(title)}</h3><p>{e(desc)}</p></a>'
        parts=''.join(f'<h2>{e(k)}</h2><p>{e(v)}</p>' for k,v in sections)
        sources=''.join('<li>'+link(u,n)+'</li>' for u,n in refs)
        art=f'<article class="inner"><a class="crumb" href="{h}#guides">← {t("求职指南","Guides")}</a><h1>{e(title)}</h1><p class="lead">{e(desc)}</p>{parts}<div class="source"><strong>{t("官方资料","Official sources")}</strong><ul>{sources}</ul></div>{button(contact,t("加微信咨询","Ask on WeChat"))}</article>'
        make(lang,slug,title+t(' · 半导体求职',' · Semiconductor careers'),desc,art)
    faqs=[
        (t('中国、俄罗斯或伊朗籍工程师还能在美国芯片公司工作吗？','Can engineers from China, Russia or Iran work for a U.S. chip company?'),t('国籍本身不能决定某个岗位能否入职。雇主要看候选人的身份、实际接触的技术以及适用的管制。美国司法部说明，EAR 和 ITAR 本身没有要求雇主只招聘美国公民。','Nationality alone cannot determine the outcome for a specific role. Employers assess the person’s status, access to technology and applicable controls. The Justice Department explains that the EAR and ITAR do not themselves require employers to hire only U.S. citizens.'),DOJ),
        (t('工作许可和出口许可是同一件事吗？','How does work authorization differ from export authorization?'),t('工作许可关系到你能否在美国受雇。出口许可关系到雇主能否向你开放特定受控技术。一个岗位可能需要分别核实这两项条件。','Work authorization concerns your eligibility to work in the U.S. Export authorization concerns the employer’s ability to release particular controlled technology to you. A role may require both assessments.'),DOJ),
    ]
    faq=''.join(f'<details><summary>{e(q)}</summary><p>{e(a)} {link(u,t("官方依据","Official source"))}</p></details>' for q,a,u in faqs)
    directory=path(lang,'companies')
    directory_title=t('芯片公司的 EL 条款','Semiconductor employers and export licensing')
    intro=t('芯片公司公开文件里，哪些岗位提到了出口许可？下列资料覆盖芯片设计、晶圆制造与设备。具体岗位是否需要 EL，取决于技术范围和候选人身份。','Explore hiring notices and disclosures from chip designers, foundries and equipment makers. License requirements depend on the role, the technology and the candidate’s status.')
    survey='https://www.csis.org/analysis/delays-and-uncertainty-export-licensing-process-findings-csis-survey-us-technology'
    tiles=[]; records=[]
    for key,name,cn,summary_zh,summary_en,source in employers:
        logo=f'<img src="/logos/{key}.webp" alt="" width="64" height="64" loading="lazy">'
        tiles.append(f'<a class="issuer" href="{directory}#{key}">{logo}<strong>{e(name)}</strong></a>')
        label=name+' · '+cn if zh and name!=cn else name
        records.append(f'<section class="record" id="{key}">{logo}<div><h2>{e(label)}</h2><p>{e(t(summary_zh,summary_en))}</p>{link(source,t("查看公开文件","Read source"))}</div></section>')
    grid=''.join(tiles)
    independent=t('公司名称和商标用于识别文件发布方。芯路独立整理。','Company names and marks identify the organizations discussed. This directory is independently compiled by Waferpath.')
    make(lang,'companies',directory_title,intro,f'<article class="inner"><a class="crumb" href="{h}">← {t("首页","Home")}</a><h1>{directory_title}</h1><p class="lead">{intro}</p>{"".join(records)}<p class="note">{independent}</p></article>')
    main=f'''<section class="hero">
        <img class="hero-image" src="/wafer-macro.webp" width="1728" height="576" fetchpriority="high" alt="">
        <div class="hero-heading"><div class="topic">{t('半导体求职与出口许可','U.S. semiconductor career support')}</div>
        <h1>{t('美国 Export License','U.S. export license')}<span>{t('申请卡住了？','application stalled?')}</span></h1></div>
        {wechat_panel(lang)}
        <div class="hero-copy"><p class="hero-answer">{t('我们帮你解决。','We can help you resolve it.')}</p>
        <p class="case-note">{t('成功案例涉及 AMD、Intel 和 Qualcomm 的岗位。','We have helped candidates resolve export license issues for roles at AMD, Intel and Qualcomm.')}</p>
        <a class="textlink" href="#guides">{t('阅读求职指南','Explore the guides')} ↓</a></div>
        </section>
    <section class="status-note" aria-labelledby="delays"><h2 id="delays">{t('2025 年后，在美国的工程师申请 Export License 基本批不下来了吗？','Have U.S. export licenses for engineers become nearly impossible to obtain since 2025?')}</h2><p>{t('高通在美国工程实习生招聘启事中明确提醒：如果岗位需要 EL，申请延误可能让你赶不上入职。2026 年 4 月，CSIS 调查中的受访企业也提到，视同出口申请等待时间尤其长。这些资料说明等待确实会影响工作机会，但没有给出美国芯片工程师的整体获批率。','Qualcomm warns engineering interns who need a license that delays may prevent them from starting on time. Respondents to an April 2026 CSIS survey also reported especially long waits for deemed exports. Neither source reports an overall approval rate for semiconductor engineers in the United States.')} {link(employers[0][-1],t('高通招聘启事','Qualcomm’s notice'))} · {link(survey,t('CSIS 调查','CSIS survey'))}</p></section>
    <section class="section" id="companies"><div class="head"><h2>{directory_title}</h2><a class="textlink" href="{directory}">{t('查看文件与岗位说明','Explore sources and roles')} →</a></div><p class="directory-intro">{intro}</p><div class="issuers">{grid}</div><p class="note issuer-note">{independent}</p></section>
    <section id="guides" class="section"><div class="head"><h2>{t('求职指南','Career guides')}</h2><p>{t('按你当前遇到的问题查阅','Start with the question in front of you.')}</p></div><div class="guides-layout"><img class="guide-image" src="/cleanroom.webp" width="1080" height="553" loading="lazy" alt="{t('晶圆厂洁净室内的工程师与检测设备','An engineer beside wafer inspection equipment in a cleanroom')}"><div class="cards">{cards}</div></div></section>
    <section id="questions" class="section faq"><h2>{t('常见问题','Common questions')}</h2><div>{faq}</div></section>
    '''
    make(lang,'',t('美国 Export License 申请卡住了？芯片工程师 EL 申请延期咨询','Stalled U.S. export license applications for semiconductor engineers'),t('为美国 Export License 申请卡住、入职延期的芯片工程师提供沟通支持。了解视同出口、offer 条件和入职安排。','Guidance for semiconductor candidates facing delays in U.S. deemed export licensing, conditional offers and start dates.'),main)
    contact_title = t('美国 Export License 微信咨询', 'U.S. export license questions')
    contact_desc = t('扫码加微信，咨询美国芯片岗位的 Export License 申请、补充材料和入职延期。',
                     'Get in touch on WeChat for questions about U.S. semiconductor job offers, export license applications and start dates.')
    contact_page = f'''<article class="inner contact-page">
        <a class="crumb" href="{h}">← {t('首页','Home')}</a>
        <h1>{contact_title}</h1>
        {wechat_panel(lang)}
        </article>'''
    make(lang, 'contact', contact_title, contact_desc, contact_page)
urls=[u for u,v in routes.items() if v[0].startswith('text/html')]
asset('/robots.txt','User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n','text/plain')
asset('/sitemap.xml','<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+e(base+p)+'</loc></url>' for p in urls)+'</urlset>','application/xml')
asset('/style.css',stylesheet,'text/css')
destination = root / 'dist' / 'client'
# Rebuild the generated directory so retired pages are removed from deployments.
if destination.exists():
    rmtree(destination)
destination.mkdir(parents=True)
for route, (mime, body) in routes.items():
    target = destination / route.lstrip('/')
    if mime.startswith('text/html'):
        target = target / 'index.html'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding='utf-8')
for image in ('wafer.webp', 'wafer-macro.webp', 'cleanroom.webp', 'icon.png', 'wechat-qr.png'):
    copy2(src / 'assets' / image, destination / image)
copytree(src / 'assets' / 'logos', destination / 'logos', dirs_exist_ok=True)
(destination / '.nojekyll').touch()
