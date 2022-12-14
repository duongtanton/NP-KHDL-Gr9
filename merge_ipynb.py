import copy
import json

def read_ipynb(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_ipynb(notebook, notebook_path):
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f)

# Reading the notebooks
ipynb1 = read_ipynb('Data-Collection.ipynb')
ipynb2 = read_ipynb('Data-Exploration.ipynb')
ipynb3 = read_ipynb('Problem-Framing.ipynb')
ipynb4 = read_ipynb('Data-Modeling.ipynb')

# Copying the notebook
ipynb_final = copy.deepcopy(ipynb1)

# Concatenating the notebooks
ipynb_final['cells'] = ipynb1['cells'] + ipynb2['cells'] + ipynb3['cells'] + ipynb4['cells']

# Saving the new notebook 
write_ipynb(ipynb_final, 'Final-Version.ipynb')