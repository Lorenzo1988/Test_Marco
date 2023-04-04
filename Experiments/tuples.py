filenames=["1.Raw Data.txt","2.Reports.txt","3.Presentation.txt"]

filenames_new=[]
for filename in filenames:
#replace(arg1= "vecchia stringa", arg2=nuova stringa, arg3= quante occorrenze)
    filename_new = filename.replace(".","-",1)
    filenames_new.append(filename_new)
#    filenames_new = filenames_new.append(filename_new)

print(filenames_new)
print(filenames)
