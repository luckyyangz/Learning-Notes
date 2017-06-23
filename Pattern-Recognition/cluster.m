clc,clear
Sigma=[1,0;0,1];
mu1=[1,-1];
x1=mvnrnd(mu1,Sigma,200);
mu2=[5.5,-4.5];
x2=mvnrnd(mu2,Sigma,200);
mu3=[1,4];
x3=mvnrnd(mu3,Sigma,200);
mu4=[6,4.5];
x4=mvnrnd(mu4,Sigma,200);
mu5=[9,0.0];
x5=mvnrnd(mu5,Sigma,200)
X=[x1;x2;x3;x4;x5];
plot(x1(:,1),x1(:,2),'r.'); hold on;
plot(x2(:,1),x2(:,2),'b.');
plot(x3(:,1),x3(:,2),'k.');
plot(x4(:,1),x4(:,2),'g.');
plot(x5(:,1),x5(:,2),'m.');

n=size(X,1)  %样本数
c=5     %类别数
t=randint(1,c,[1,n]); %随机取出n样本中c个样本的下标
Means=X(t,:);   %随机的c个样本做均值
Label_index=zeros(n,1); %1000个样本的标签初始化为0
old_Label=Label_index;
c=zeros(1000,5)
while true
    for j=1:5    %分别将1000个样本和五个初始点取均值，得到c为1000*5的矩阵
        for i=1:1000
            c(i,j)=norm(X(i,:)-Means(j,:));
        end 
    end  
    [min_c,Label_index]=min(c,[],2) %得到1000个样本最近的点，赋予其标签
    %while True
    for j=1:5   %更新均值，得到新的五个中心点
        index=find(Label_index==j); %找到同类型的求其均值
        Means(j,:)=mean(X(index,:));
    end
    if (old_Label==Label_index) %直到便签不在改变，退出分类器
        break;
    end
    old_Label=Label_index;
end
%画出分类后的图
index = find(Label_index==1); %取出类别同为1的样本，用红色标记，并画图
figure;
plot(X(index,1),X(index,2),'r.'); hold on;
index = find(Label_index==2);
plot(X(index,1),X(index,2),'b.');
index = find(Label_index==3);
plot(X(index,1),X(index,2),'k.');
index = find(Label_index==4);
plot(X(index,1),X(index,2),'g.');
index = find(Label_index==5);
plot(X(index,1),X(index,2),'m.');
%计算错误率
b=0
for j=1:5   
    a=tabulate(Label_index(200*(j-1)+1:200*j));
    [my_max] = max(a(:,2));
    b=200-my_max+b;
end
c_error=b/1000;
%print error count and error_rate
sprintf('cluster error=%d',b)
sprintf('error_rate=%.3f',c_error)

 
    
    





