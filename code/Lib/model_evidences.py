import os.path
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb

def model_evidences(model, evidence_dict, cancer_interes, path):
    

    ie = gum.LazyPropagation(model)
    ie.makeInference()

    file_name = str(cancer_interes) + '_evidences.txt'
    file_path = os.path.join(path,file_name)

    f = open(file_path, 'w')
    
    with open(file_path, 'w') as f:

        for (target, evidence_list) in evidence_dict["evidences"]:
            ie.evidenceImpact(target, evidence_list)

            f.write(str(ie.evidenceImpact(target, evidence_list)))
