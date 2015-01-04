import json
import pandas as pd
from glob import glob
 
def convert(x):    
    ob = json.loads(x)
    ob2 = ob.copy()
    for k, v in ob.items():
        if isinstance(v, list):
            ob2[k] = ','.join(str(v))
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob2['%s_%s' % (k, kk)] = vv
            del ob2[k]
    return ob2
 
for json_filename in glob('*.json'):
    csv_filename = '%s.csv' % json_filename[:-5]
    print ('Converting %s to %s' % (json_filename, csv_filename))
    df = pd.DataFrame([convert(line) for line in open(json_filename)])
    df.to_csv(csv_filename, encoding='utf-8', index=False)

