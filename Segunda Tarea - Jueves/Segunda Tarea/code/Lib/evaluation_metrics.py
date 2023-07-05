from math import sqrt
import os.path

def evaluation_metrics(TN, FN, TP, FP, cancer_interes, path):
    total = TN + FN + TP + FP

    prevalence = (TP + FN) / total

    precision = TP / (TP + FP)
    FDR = FP / (TP + FP)

    FOR = FN / (FN + TN)
    NPV = TN / (FN + TN)

    TPR = TP / (TP + FN)
    FNR = FN / (TP + FN)

    FPR = FP / (FP + TN)
    TNR = TN / (FP + TN)

    accuracy = (TP + TN) / total
    F1 = (2*precision*TPR) / (precision + TPR)

    PLR = TPR / FPR
    NLR = FNR / TNR

    DOR = PLR / NLR
    PT = (sqrt(TPR*(1 - TNR)) + TNR - 1) / (TPR + TNR - 1)

    MCC =  (TP*TN - FP*FN) / sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))


    file_name =  str(cancer_interes) + '_metrics.txt'
    file_path = os.path.join(path,file_name)

    f = open(file_path, 'w')
    
    with open(file_path, 'w') as f:
        f.write("Métricas para el " + str(cancer_interes) + "\n")
        f .write("\n")
        
        f.write("Prevalence: " + str( prevalence) + "\n")
        f.write("\n")

        f.write("Positive Predictive Value / Precision: " + str( precision) + "\n")
        f.write("False Discovery Rate: " + str(FDR) + "\n")
        f.write("\n")

        f.write("False Omission Rate: " + str(FOR) + "\n")
        f.write("Negative Predictive Value:" + str(NPV) + "\n")
        f.write("\n")

        f.write("True Positive Rate / Sensitivity / Recall / Prob of detection: "+ str( TPR)+ "\n")
        f.write("False Negative Rate / Miss rate: " + str(FNR) + "\n")
        f.write("\n")

        f.write("False Positive Rate / Prob of false alarm / Fall-out: " + str(FPR) + "\n")
        f.write("True Negative Rate / Specificity / Selectivity: " + str(TNR) + "\n")
        f.write("\n")

        f.write("Accuracy: " + str(accuracy) +"\n" )
        f.write("F1-Score: " + str(F1) +"\n" )
        f.write("\n")

        f.write("Positive Likelihood Ratio:" + str(PLR) + "\n")
        f.write("Negative Likelihood Ratio:" + str(NLR) + "\n")
        f.write("\n")

        f.write("Diagnostic Odds Ratio: "+ str(DOR) + "\n")
        f.write("Prevalence Threshold: "+ str(PT) + "\n")

        f.write("Matthews Correlation Coefficient: "+ str(MCC) + "\n")
