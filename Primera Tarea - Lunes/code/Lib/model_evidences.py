import os.path
import pyAgrum as gum

def model_evidences(model, evidence_dict, cancer_interes, path):

    ie = ''

    file_name = str(cancer_interes) + '_evidences.txt'
    file_path = os.path.join(path,file_name)

    f = open(file_path, 'w')
    
    with open(file_path, 'w') as f:

        for (target, evidence_list) in evidence_dict["evidences"]:
            
            evidence_impact = ''
            f.write(str(evidence_impact))
