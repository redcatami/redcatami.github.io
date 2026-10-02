from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import sys

root=Path(sys.argv[1] if len(sys.argv)>1 else '_site').resolve()
base=sys.argv[2] if len(sys.argv)>2 else ''
errors=[]
class Links(HTMLParser):
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        for key in ('href','src'):
            target=attrs.get(key,'')
            if not target or target.startswith(('#','data:','mailto:')) or urlsplit(target).netloc:
                continue
            target=unquote(urlsplit(target).path)
            if base and target.startswith(base+'/'):
                target=target[len(base):]
            dest=root/target.lstrip('/') if target.startswith('/') else self.page.parent/target
            if dest.is_dir():dest=dest/'index.html'
            if not dest.exists():errors.append(f'{self.page.relative_to(root)}: missing {target}')

pages=list(root.rglob('*.html'))
for page in pages:
    text=page.read_text(encoding='utf-8')
    if '{{' in text or '{%' in text:errors.append(f'{page}: unresolved Liquid')
    parser=Links();parser.page=page;parser.feed(text)
for forbidden in ('.tools','vendor','examples','scripts','.github','Gemfile','README.md'):
    if (root/forbidden).exists():errors.append(f'Build exposed {forbidden}')
if errors:
    print('\n'.join(errors));sys.exit(1)
print(f'Verified {len(pages)} rendered HTML pages; all internal links and assets resolve; no tooling or sample source exposed.')
