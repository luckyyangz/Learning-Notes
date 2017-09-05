'''-----------learning note-----------'''
'''---------对行列进行操作---------'''
''' load .txt file '''
#读取为pandas的DataFrame格式，然后使用to_csv方法
lines=open('C:\Users\Jiao\Desktop\Document\Gait\ChenHongliDownstairs01.txt','r').readlines()
f=[i.strip() for i in lines]
partData=pd.DataFrame(f) 
partData.to_csv('partData.csv',index=False)

''' load csv file'''
trainLabel_all = pd.read_csv('trainLabel.csv',sep=' ')
trainData_all = np.load('data_first/train_unigram_11_6.npy')

'''转化为numpy格式，再切片'''
    trainLabel_all = np.array((trainLabel_all[label]))
    trainData_all=np.array(trainData_all)
    #remove the unknown data 
    known = [i for i in range(len(trainLabel_all)) if trainLabel_all[i]!=0]
    trainData_ = trainData_all[known]
    trainLabel = trainLabel_all[known]
    return trainData_,trainLabel

'''按行取数据'''
result.columns = ['id','age','gender','edu','value']
result_sort=result.sort_values(by=['age'],ascending=False)
m=result_sort
#m=m[m.age<'2']
m_test=m['value']

''' 切词分开处理 '''
for i in range(len(m)):
    a=[]
    seg_list=list(jieba.cut(m_test[i]))
    a+=seg_list
    print "/".join(seg_list)
df_data=pd.DataFrame(data=result[:,4],index=range(len(result)),columns=['dataValue'])
gender_label=df_label['gender']

#output.write('词语，词频，词权\n')

'''-------------生成txt文件----------'''
        row = ""
        row +=df_data['id'][i]#+'aga','gender','education'][i]+"/"+[+"/"+[][i]+"/" +[][i]+"/"
        for w in a:
            row  = row + unicode.encode(w, 'utf-8') + "/"
        f = open(segname, 'a')
        f.write(row)
         #   f.write('\n')
        f.close()

