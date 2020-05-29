with open('report.txt',encoding='gbk')as f:
    lines=f.readlines()
print(lines)
stu_list=[]
for line in lines:
    line = line.split()
    stu_list.append(line)
stu_list[0].insert(0,'名次')
stu_list[0].append("总分"，'平均分')
print(stu_list)
for i in stu_list[1:len(stu_list)]:
    sum=0
    av=0
    for j in i[1:len(i)]:
        sum+=int(j)
    av=round(sum/(len(i)-1))
    i.append(sum)
    i.append(av)
print(stu_list)
stu_list[1:len(stu_list)]=sorted(stu_list[1:],key=lambda student:student[-2],reverse=True)
for i  in range (1,len(stu_list)):
    stu_list[i].insert(0,i)
print(stu_list)
ave_list=['0','平均']
for i in range(2,13):
    sum=0
    for j in range(1,len(stu_list)):
        sum+=int(stu_list[j][i])
        if int(stu_list[j][i])<60:
            stu_list[j][i]='不及格'
        ave=round(sum/(len(stu_list)-1))
        ave_list.append(ave)
    stu_list.insert(1,ave_list)
    print(stu_list)

    stu_list_str=''
    for i in stu_list:
        for x in range(len(stu_list)):
            for y in range(len(stu_list[0])):
                stu_list[x][y]=str(stu_list[x][y])
        stu_list_str +=''.join(i)
        stu_list_str +='\n'
    print(stu_list_str)

    with open('result.txt','w',encoding='gbk') as result:
        result.write(stu_list_str)


