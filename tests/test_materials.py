"""检查合成资料的关键业务关系，避免错误输入被误作有效资料。"""
import unittest
import numpy as np
from inspect_data import load_materials

class MaterialIntegrity(unittest.TestCase):
    def test_domain_relationships(self):
        v,a=load_materials()
        c=len(v['objects']['types'])
        self.assertEqual(a['scores'].shape[1],c)
        self.assertEqual(a['duration_scores'].shape[0],c)
        self.assertEqual(a['transition_scores'].shape,(c+1,c))
        for ep in v['objects']['episodes']:
            blocks=ep['blocks']
            self.assertEqual(blocks[0][0],0)
            self.assertEqual(blocks[-1][1],len(a[ep['frame_scores']]))
            self.assertTrue(all(x[1]==y[0] for x,y in zip(blocks,blocks[1:])))
        self.assertEqual({x['kind'] for x in v['objects']['annotations']},{'contains_complete','overlap_forbid'})

if __name__ == '__main__':
    unittest.main()
