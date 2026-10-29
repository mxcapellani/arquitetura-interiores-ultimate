"""Integrity checks; not a behavioural or visual evaluation."""
from pathlib import Path
import json,re,sys,yaml
class UniqueLoader(yaml.SafeLoader): pass
def unique(loader,node,deep=False):
 out={}
 for k,v in node.value:
  key=loader.construct_object(k,deep=deep)
  if key in out: raise ValueError('duplicate YAML key')
  out[key]=loader.construct_object(v,deep=deep)
 return out
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique)
B=Path('.agents/skills/arquitetura-interiores-ultimate')
def norm(t): return re.sub(r'\s+',' ',t).replace('wall- mounted','wall-mounted').strip()
def validate(root):
 root=Path(root);errors=[]
 required=['README.md','LICENSE','NOTICE.md','CHANGELOG.md','docs/FUNCTIONAL_AUDIT.md','docs/FUNCTIONAL_SPECIFICATION.md','docs/SOURCE_AND_ATTRIBUTION.md','docs/INSTALLATION.md','docs/LIMITATIONS.md','docs/source-extracted.txt','tests/prompt-corpus.json','tests/acceptance-tests.md','tests/comparison-matrix.md','.github/workflows/validate.yml',str(B/'SKILL.md')]
 for p in required:
  if not (root/p).is_file() or not (root/p).read_text().strip(): errors.append('missing/empty '+p)
 if errors:return errors
 skill=(root/B/'SKILL.md').read_text()
 try:
  assert skill.startswith('---\n')
  metadata=yaml.load(skill.split('---',2)[1],Loader=UniqueLoader)
  assert set(metadata)=={'name','description'}
  assert metadata['name']=='arquitetura-interiores-ultimate'
  assert isinstance(metadata['description'],str) and len(metadata['description'].strip())>40
 except Exception: errors.append('invalid YAML metadata')
 try:
  corpus=json.loads((root/'tests/prompt-corpus.json').read_text())
  assert [x['id'] for x in corpus]==[f'{i:02d}' for i in range(1,31) if i!=27]
  extracted=norm((root/'docs/source-extracted.txt').read_text())
  for item in corpus:
   assert f"#### {item['id']} — {item['title']}" in skill
   for lang in ('en','pt'):
    assert norm(item[lang]) in extracted, 'source differs'
    assert item[lang] in skill, 'missing complete original prompt'
 except Exception as exc:errors.append('corpus mismatch: '+str(exc))
 for token in ('**Catálogo:**','**Complementação:**','**Variação controlada:**','**Seleção original:**','27 não aparece','## Precisão e controle final'):
  if token not in skill:errors.append('missing behaviour contract '+token)
 for path in root.rglob('*.md'):
  for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
   if '://' in link or link.startswith('#'):continue
   target=(path.parent/link.split('#')[0]).resolve()
   if not target.is_relative_to(root.resolve()) or not target.exists():errors.append('invalid link '+str(path)+' '+link)
 cases=(root/'tests/acceptance-tests.md').read_text()
 for i in range(1,19):
  if f'## T{i:02d} —' not in cases:errors.append('missing acceptance case')
 return errors
if __name__=='__main__':
 errors=validate(Path(__file__).resolve().parents[1]);print('\n'.join(errors) if errors else 'PASS: structure, YAML, links, 29 full bilingual prompts and source correspondence');sys.exit(bool(errors))
