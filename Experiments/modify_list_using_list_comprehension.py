filenames = ["1.doc","2.report","3.presentation"]

filenames_target = ["1-doc.txt","2-report.txt","3-presentation.txt"]

#opzione_1
filenames_testing_1 = ["{}.txt".format(item.replace(".","-")) for item in filenames]

#opzione_2
filenames_testing_2 = [item.replace(".","-")+".txt" for item in filenames]

print(filenames_testing_1==filenames_testing_2==filenames_target)