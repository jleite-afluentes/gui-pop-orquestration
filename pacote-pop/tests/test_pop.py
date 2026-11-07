import json, subprocess, sys, tempfile, unittest
from pathlib import Path
CLI=Path(__file__).resolve().parents[1]/'skills/orquestrar-pop/scripts/pop.py'
class TestPop(unittest.TestCase):
 def run_cli(self,*args,code=0):
  p=subprocess.run([sys.executable,str(CLI),*map(str,args)],capture_output=True,text=True)
  self.assertEqual(p.returncode,code,p.stdout+p.stderr); return p
 def test_integrity_and_graph(self):
  with tempfile.TemporaryDirectory() as d:
   c=Path(d)/'empresa'; self.run_cli('init-company','--path',c,'--id','ACME','--name','Teste')
   self.run_cli('init-pop','--company',c,'--id','POP-1','--title','Teste','--owner','Ana')
   p=c/'pops/POP-1'; g={'nodes':[{'id':'POP-1','file':'pops/POP-1/pop.md'}],'edges':[]}; (c/'grafo.json').write_text(json.dumps(g))
   self.run_cli('check','--company',c)
   g['edges']=[{'from':'POP-1','type':'regido_por','to':'NAO-EXISTE'}]; (c/'grafo.json').write_text(json.dumps(g)); self.run_cli('check','--company',c,code=1)
   f=p/'entregas/pop.md'; f.write_text('original')
   self.run_cli('manifest','--pop',p,'--id','POP-1','--version','1','--actor','Ana'); self.run_cli('verify','--pop',p)
   self.run_cli('approve','--pop',p,'--owner','Ana','--confirm')
   f.write_text('alterado'); self.run_cli('verify','--pop',p,code=1)
   self.run_cli('approve','--pop',p,'--owner','Ana','--confirm','--output','outro.json',code=2)
 def test_reservation(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d); self.run_cli('reserve','--pop',p,'--actor','Ana'); self.run_cli('reserve','--pop',p,'--actor','Bia',code=2)
   self.run_cli('release','--pop',p,'--actor','Bia',code=2); self.run_cli('release','--pop',p,'--actor','Bia','--reason','retomada')
   self.assertTrue((p/'historico-reservas.jsonl').exists())
if __name__=='__main__': unittest.main()
