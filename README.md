# Machine-Learning
*****Project_1*****

This is a simulated dataset of single nucleotide polymorphism (SNP) genotype data containing 29623 SNPs (total features). Amongst all SNPs are 15 causal ones which means they and neighboring ones discriminate between case and controls while remainder are noise.

In the training are 4000 cases and 4000 controls. Your task is to predict the labels of 2000 test individuals whose true labels are known only to the instructor and TA.

Both datasets and labels are immediately following the link for this project file. The training dataset is called traindata.gz (in gzipped format), training labels are in trueclass, and test dataset is called testdata.gz (also in gzipped format).

You may use cross-validation to evaluate the accuracy of your method and for parameter estimation. 

It would take as input the training dataset, the trueclass label file for training points, and the test dataset. The output would be a prediction of the labels of the test dataset in the same format as in the class assignments. Also output the total number of features and the feature column numbers that were used for final prediciton. If all features were used just say "ALL" instead of listing all column numbers.

Achieved Accuracy of 78%
