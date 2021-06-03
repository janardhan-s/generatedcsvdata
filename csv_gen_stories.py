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
    
def gen_stories_of_csv_file(data_list1, data_list2):
    n1 = len(data_list1)
    n2 = len(data_list2)
    #print(n1, n2)

    for i in range(1, n1):
        #print(i)
        for j in range(1, n2):
            #print(j)
            if data_list1[i][1] == data_list2[j][3]:
                data_list2[j][5] = data_list1[i][3]
                data_list2[j][6] = data_list1[i][4]
                data_list2[j][7] = data_list1[i][5]
                data_list2[j][8] = data_list1[i][6]
            
            
    return data_list2        
def main():
    filename = "01-epics.csv"
    fname = "02-stories.csv"
    
    
    data_list1 = read_csv_file(filename)
    #print(data_list0)
    data_list2 = read_csv_file2(fname)
    #print(data_list1)
    jlist = gen_stories_of_csv_file(data_list1, data_list2)
    gen_list = []
    for r in jlist:
        #print(r)
        nlist = ('{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}'.format(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13],r[14],r[15],r[16],r[17]))
        gen_list.append(nlist)
    print(gen_list)

    with open("gen_data_csv.csv", "w") as csv_file:
        dd = csv.writer(csv_file, delimiter = '\t')
        for line in gen_list:
            dd.writerow(line)

if (__name__=="__main__"):
	main()