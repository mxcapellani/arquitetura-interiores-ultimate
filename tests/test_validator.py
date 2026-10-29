import unittest,tempfile,shutil,json
from pathlib import Path
from validate_skill import validate,B
ROOT=Path(__file__).resolve().parents[1]
class IntegrityTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.root=Path(self.tmp.name)/'package';shutil.copytree(ROOT,self.root)
 def change(self,path,old,new):
  p=self.root/path;p.write_text(p.read_text().replace(old,new,1))
 def test_valid_package(self):self.assertEqual(validate(self.root),[])
 def test_missing_skill(self):
  (self.root/B/'SKILL.md').unlink();self.assertTrue(validate(self.root))
 def test_missing_reference(self):
  (self.root/B/'references/lighting.md').unlink();self.assertTrue(validate(self.root))
 def test_duplicate_yaml(self):
  self.change(B/'SKILL.md','name: arquitetura-interiores-ultimate','name: arquitetura-interiores-ultimate\nname: duplicate');self.assertTrue(validate(self.root))
 def test_wrong_name(self):
  self.change(B/'SKILL.md','name: arquitetura-interiores-ultimate','name: other');self.assertTrue(validate(self.root))
 def test_missing_complete_prompt(self):
  self.change(B/'SKILL.md','Small countryside guesthouse with pitched roof, natural stone and wood materials, set in a meadow.','Abridged guesthouse.');self.assertTrue(validate(self.root))
 def test_corpus_disagrees_with_source(self):
  p=self.root/'tests/prompt-corpus.json';d=json.loads(p.read_text());d[0]['pt']='Invented original prompt';p.write_text(json.dumps(d));self.assertTrue(validate(self.root))
 def test_missing_catalogue_contract(self):
  self.change(B/'SKILL.md','**Catálogo:**','**Removed:**');self.assertTrue(validate(self.root))
 def test_missing_acceptance_case(self):
  self.change('tests/acceptance-tests.md','## T18 —','## Removed —');self.assertTrue(validate(self.root))
 def test_missing_notice(self):
  (self.root/'NOTICE.md').unlink();self.assertTrue(validate(self.root))
 def test_item27_cannot_be_inserted_into_original_corpus(self):
  p=self.root/'tests/prompt-corpus.json';d=json.loads(p.read_text());d.insert(26,{'id':'27','title':'Invented','pt':'new','en':'new'});p.write_text(json.dumps(d));self.assertTrue(validate(self.root))
if __name__=='__main__':unittest.main()
