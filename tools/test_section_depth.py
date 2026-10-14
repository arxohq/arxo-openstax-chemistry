"""Addressed regression tests for the captured common OpenStax convention."""
from pathlib import Path
import hashlib,json,sys,tempfile,unittest
sys.path.insert(0,str(Path(__file__).resolve().parent/'depth'))
import boundaries
from act_split import openstax_section_spans,locator_units
TEXT='6.4\n\nElectronic Structure of Atoms\n\nExample 6.4\n6.4\n\n12.3\n\nRate Laws\n\nA model statement.'
DECL={'unit':'openstax_section','sectionHeadings':{'6.4':'Electronic Structure of Atoms','12.3':'Rate Laws'}}
def fixture(root):
 p=root/'en.txt';p.write_text(TEXT);(root/'articles.json').write_text(json.dumps({'editions':[{'document':'en.txt',**DECL}]}))
 nodes=[{'kind':'source_edition','id':'ed','work':'work','lifecycle':[]},{'kind':'publication','id':'pub','edition':'ed','documentHash':'sha256:'+hashlib.sha256(p.read_bytes()).hexdigest()},{'kind':'fragment','id':'f','edition':'ed','locator':'section/6.4#definition'},{'kind':'rule','id':'rule','anchors':['f']}];ir=root/'own.json';ir.write_text(json.dumps({'nodes':nodes}));return p,ir,nodes
class SectionDepthTests(unittest.TestCase):
 def test_decimal_values_do_not_create_sections(self):
  self.assertEqual([h.number for _,h in openstax_section_spans(TEXT,DECL)],['6.4','12.3'])
 def test_missing_duplicate_and_undeclared_titles_fail(self):
  for text in [TEXT.replace('Rate Laws','Different title'),TEXT+'\n\n6.4\n\nElectronic Structure of Atoms']:
   with self.assertRaises(ValueError):openstax_section_spans(text,DECL)
  with self.assertRaises(ValueError):openstax_section_spans(TEXT,{})
 def test_table_excerpt_is_literal(self):
  self.assertEqual(len(openstax_section_spans('SOURCE-SECTION: 17.3 Table 17.1\nZn',{'sectionHeadings':{'17.3':'Table 17.1'}})),1)
 def test_section_locator_forms(self):
  for loc in ['6.4/history','section/6.4#definition','section/6.4']:
   self.assertEqual(locator_units(loc,'openstax_section'),('6.4',))
  self.assertEqual(locator_units('article/6.4','openstax_section'),())
 def test_exact_source_and_own_edition(self):
  with tempfile.TemporaryDirectory() as tmp:
   p,ir,nodes=fixture(Path(tmp));d=boundaries.depth(p,ir);self.assertEqual([r['level'] for r in d['rows']],['EXECUTABLE','—'])
   nodes.extend([{'kind':'source_edition','id':'foreign','work':'work','lifecycle':[]},{'kind':'fragment','id':'ff','edition':'foreign','locator':'12.3/rate'},{'kind':'rule','id':'rf','anchors':['ff']}]);ir.write_text(json.dumps({'nodes':nodes}));d=boundaries.depth(p,ir);self.assertEqual(d['rows'][1]['level'],'—');self.assertEqual(d['otherEdition'],1)
 def test_hash_and_stale_section_fail(self):
  with tempfile.TemporaryDirectory() as tmp:
   p,ir,nodes=fixture(Path(tmp));nodes[1]['documentHash']='sha256:wrong';ir.write_text(json.dumps({'nodes':nodes}))
   with self.assertRaisesRegex(ValueError,'source hash is not pinned'):boundaries.depth(p,ir)
   p,ir,nodes=fixture(Path(tmp));nodes[2]['locator']='section/6.5#stale';ir.write_text(json.dumps({'nodes':nodes}))
   with self.assertRaises(ValueError):boundaries.depth(p,ir)
if __name__=='__main__':unittest.main()
