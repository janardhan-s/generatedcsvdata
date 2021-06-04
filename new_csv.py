from mycsvmod import get_org_est_pos
from mycsvmod import get_spented_time_pos
from mycsvmod import get_original_hours
from mycsvmod import get_rem_hours_pos
from mycsvmod import get_spent_hours
import csv

def read_csv_file(filename):
    data_list1 = []
    
    fd1 = open(filename, 'r')
    fdata = csv.reader(fd1)
    
    for row in fdata:
        #print(row)
        data_list1.append(row)
    #print(len(data_list0))
    
    n1 = len(data_list1)
    fd1.close()
    return(data_list1)
    
def read_csv_file2(fname):

    data_list2 = []
    
    fd2 = open(fname, 'r')
    gdata = csv.reader(fd2)
    
    for row in gdata:
       # print(row)
        data_list2.append(row)
    #print(len(data_list1))
    
    n2 = len(data_list2)
    fd2.close()
    return(data_list2)
def new_csv_column(data_list2):
    
    data_list2[0].insert(6,"progress")
    data_list2[0].insert(11,"spenthours")
    data_list2[0].insert(10,"original hours")
    data_list2[0].insert(12,"remaining hours")
    for j in range(1, len(data_list2)):
        data_list2[j].insert(6,"0")
        data_list2[j].insert(11,"0")
        data_list2[j].insert(10,"0")
        data_list2[j].insert(12,"0")
    return data_list2
    
def gen_stories_of_csv_file(data_list1, data_list2):
    n1 = len(data_list1)
    n2 = len(data_list2)

    i = 1
    j = 1
    data_list2[0].insert(5,"ESdate")
    data_list2[0].insert(6,"ETdate")
    data_list2[0].insert(7,"EASdate")
    data_list2[0].insert(8,"EAEdate")
    for i in range (1, n1):
        for j in range (1, n2):
            a = get_org_est_pos()
            b = get_spented_time_pos()
            c = get_original_hours()
            d = get_rem_hours_pos()
            e = get_spent_hours()
            if (data_list1[i][1] == data_list2[j][3]):
                data_list2[j].insert(5,data_list1[i][3])
                data_list2[j].insert(6,data_list1[i][4])
                data_list2[j].insert(7,data_list1[i][5])
                data_list2[j].insert(8,data_list1[i][6])
                data_list2[j][15] = int(data_list2[j][a]) - int(data_list2[j][b]) #rem time
                data_list2[j][c] = int(data_list2[j][a])/3600 # original hours
                data_list2[j][e] = int(data_list2[j][b])/3600 # spent hours
                data_list2[j][d] = int(data_list2[j][c])-(data_list2[j][e]) #rem hours
                data_list2[j][10] = ((data_list2[j][d])/(data_list2[j][c]))*100
                
    return data_list2			
def main():
    filename = "01-epics.csv"
    fname = "02-stories.csv"
    
    
    data_list1 = read_csv_file(filename)
    #print(data_list0)
    data_list2 = read_csv_file2(fname)
    #print(data_list1)
    ncolumn = new_csv_column(data_list2)
    #print(ncolumn)
    
    jlist = gen_stories_of_csv_file(data_list1, ncolumn)
    print(jlist)
    
    gen_list = []
    for r in jlist:
        #print(r)
        nlist = ('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19],r[20],r[21]))
        gen_list.append(nlist)
    #print(gen_list)

    with open("gen_data_file.csv", "w") as csv_file:
        dd = csv.writer(csv_file, delimiter = '\t')
        for line in gen_list:
            dd.writerow(line)

if (__name__=="__main__"):
	main()