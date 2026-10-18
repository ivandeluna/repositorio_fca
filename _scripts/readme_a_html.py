#!/usr/bin/env python3
"""
Genera el index.html de un ejercicio a partir de su README.md y metadata.yml,
con el mismo estilo del sitio (encabezado UAdeC, migas de pan, insignias,
secciones, cajas de prompt, solución plegable, nota de transparencia).

Uso (desde la raíz del repositorio):
    python3 _scripts/readme_a_html.py carreras/<carrera>/<materia>/<ejercicio>/ [...]

Requiere: pip3 install markdown pyyaml beautifulsoup4 --break-system-packages
Convenciones que reconoce en el README.md:
  - "## Prompt..." : los bloques ``` de esa sección se vuelven cajas de prompt;
    el subtítulo o la línea en negritas inmediatamente anterior es su etiqueta.
  - <details markdown="1"> : solución plegable.
  - Citas con "El gancho" o "Nota de transparencia" : recuadros especiales.
  - Fórmulas $$...$$ (LaTeX sencillo) : se muestran como texto en un recuadro.
  - Línea final "---" + "**Autor:** ..." : pie del documento.
"""
import re, sys, html as H
from pathlib import Path
import markdown, yaml
from bs4 import BeautifulSoup, NavigableString

REPO = Path(__file__).resolve().parent.parent
TPL_HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} — Repositorio FCA</title>
<link rel="stylesheet" href="../../../../assets/style.css">
</head>
<body>

<header class="site-header">
  <div class="top">
    <div class="brand">
      <img src="../../../../assets/img/uadec-logo.png" alt="Universidad Autónoma de Coahuila" class="brand-logo">
      <div class="brand-text">
        <span class="kicker">Universidad Autónoma de Coahuila · Facultad de Contaduría y Administración, Unidad Torreón</span>
        <h1><a href="../../../../index.html">Repositorio de Métodos y Ejercicios</a></h1>
      </div>
    </div>
    <nav class="top-nav">
      <a href="../../../../index.html">Inicio</a>
      <a href="../../../../_docs/CONTRIBUIR.md">Cómo contribuir</a>
    </nav>
  </div>
</header>

<main>
  <div class="breadcrumb">
    <a href="../../../../index.html">Inicio</a><span class="sep">/</span>
    <a href="../../index.html">{carrera}</a><span class="sep">/</span>
    <a href="../index.html">{materia}</a><span class="sep">/</span>
    {titulo}
  </div>

  <article class="doc">
    <div class="doc-header">
      <h2>{titulo}</h2>
      <div class="badges">
{badges}
      </div>
    </div>

"""
TPL_FOOT = """
  </article>
</main>

<footer class="site-footer">
  Universidad Autónoma de Coahuila · Facultad de Contaduría y Administración, Unidad Torreón
</footer>

</body>
</html>
"""

def latex_to_text(s):
    s = s.strip()
    def frac(m): return f"( {m.group(1)} ) / ( {m.group(2)} )"
    for _ in range(3):
        s = re.sub(r'\\text\{([^{}]*)\}', r'\1', s)
        s = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', frac, s)
    rep = {r'\rightarrow':'→', r'\times':'×', r'\sum':'Σ', r'\cdot':'·', r'\%':'%', r'\ ':' ', r'\,':' ', r'\left':'', r'\right':''}
    for a,b in rep.items(): s = s.replace(a,b)
    return H.escape(re.sub(r'\s+',' ',s))

def convert(ej):
    meta = yaml.safe_load((ej/"metadata.yml").read_text(encoding='utf-8'))
    md = (ej/"README.md").read_text(encoding='utf-8')
    md = re.sub(r'^# .*\n', '', md, count=1)
    md = re.sub(r'^(\*\*(Carrera|Materia|Tema|Nivel|Duración estimada):\*\*.*\n)+', '', md.lstrip('\n'))
    # fórmulas $$...$$ -> marcador
    formulas = []
    def ff(m):
        formulas.append(latex_to_text(m.group(1))); return f"\n\nFORMULA{len(formulas)-1}X\n\n"
    md = re.sub(r'\$\$(.+?)\$\$', ff, md, flags=re.S)
    # pie de autor
    foot = ""
    mfoot = re.search(r'\n---\s*\n\s*(\*\*Autor[a]?:\*\*.*)\s*$', md, flags=re.S)
    if mfoot:
        foot = mfoot.group(1).strip(); md = md[:mfoot.start()]
    body = markdown.markdown(md, extensions=['tables','fenced_code','md_in_html','sane_lists'])
    soup = BeautifulSoup(body, 'html.parser')
    for p in soup.find_all('p'):
        m = re.fullmatch(r'FORMULA(\d+)X', p.get_text().strip())
        if m:
            d = soup.new_tag('div', attrs={'class':'formula'}); d.append(BeautifulSoup(formulas[int(m.group(1))],'html.parser')); p.replace_with(d)
    for h in soup.find_all('h2'): h.name='h3'; h['class']='section'
    for t in soup.find_all('table'): t['class']='data'
    for hr in soup.find_all('hr'): hr.decompose()
    for bq in soup.find_all('blockquote'):
        txt = bq.get_text()
        if 'El gancho' in txt:
            h3 = bq.find('h3')
            if h3: h3.name='p'; h3.string = h3.get_text(); h3['class']='hook-title'
            bq.name='div'; bq['class']='hook'
        elif 'Nota de transparencia' in txt or txt.strip().startswith('⚠'):
            bq.name='div'; bq['class']='ai-note'
        else:
            bq.name='div'; bq['class']='note'
    for p in soup.find_all('p'):
        if p.get_text().strip().startswith('📎'):
            p.name='div'; p['class']='doc-suggestion'
    for det in soup.find_all('details'):
        det['class']='solution'
        if det.has_attr('markdown'): del det['markdown']
        summ = det.find('summary')
        inner = soup.new_tag('div', attrs={'class':'inner'})
        for c in [c for c in det.contents if c is not summ]:
            inner.append(c.extract())
        det.append(inner)
    # prompts: bloques de código dentro de la sección de prompts
    in_prompts = False
    for el in list(soup.find_all(['h3','pre'])):
        if el.name=='h3' and 'section' in (el.get('class') or []):
            in_prompts = el.get_text().startswith('Prompt'); continue
        if el.name=='pre' and in_prompts:
            label = '🤖 Prompt sugerido'
            prev = el.find_previous_sibling()
            if prev is not None and (prev.name=='h3' and 'section' not in (prev.get('class') or []) or (prev.name=='p' and prev.find('strong') and len(prev.get_text())<80 and prev.get_text().strip().startswith(prev.find('strong').get_text().strip()[:5]))):
                label = ('🔎 ' if 'seguimiento' in prev.get_text().lower() or 'verific' in prev.get_text().lower() else '🤖 ') + prev.get_text().strip().rstrip(':')
                prev.decompose()
            box = soup.new_tag('div', attrs={'class':'prompt-box'})
            lab = soup.new_tag('span', attrs={'class':'label'}); lab.string = label
            box.append(lab); box.append(NavigableString(el.get_text().rstrip('\n')))
            el.replace_with(box)
    for h in soup.find_all('h3'):
        if 'section' not in (h.get('class') or []): h.name='h4'
    # enlaces .md relativos funcionan igual; imágenes con ancho completo
    for img in soup.find_all('img'): img['class']='figure'
    badges = "\n".join(f'        <span class="badge">{H.escape(str(b))}</span>' for b in [meta['carrera'],meta['materia'],meta['nivel'],meta['duracion_estimada'],meta['tipo']] if b)
    head = TPL_HEAD.format(titulo=H.escape(meta['titulo']), carrera=H.escape(meta['carrera']), materia=H.escape(meta['materia']), badges=badges)
    inner_html = soup.decode(formatter='html5')
    foot_html = ""
    if foot:
        foot_html = '\n    <div class="doc-footer">\n      ' + markdown.markdown(foot)[3:-4].replace('<strong>','').replace('</strong>','') + '\n    </div>'
    (ej/"index.html").write_text(head + inner_html + foot_html + TPL_FOOT, encoding='utf-8')
    print("html", ej.name)

for p in sys.argv[1:]:
    convert(REPO/p)
