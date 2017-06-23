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

n=size(X,1)  %������
c=5     %�����
t=randint(1,c,[1,n]); %���ȡ��n������c���������±�
Means=X(t,:);   %�����c����������ֵ
Label_index=zeros(n,1); %1000�������ı�ǩ��ʼ��Ϊ0
old_Label=Label_index;
c=zeros(1000,5)
while true
    for j=1:5    %�ֱ�1000�������������ʼ��ȡ��ֵ���õ�cΪ1000*5�ľ���
        for i=1:1000
            c(i,j)=norm(X(i,:)-Means(j,:));
        end 
    end  
    [min_c,Label_index]=min(c,[],2) %�õ�1000����������ĵ㣬�������ǩ
    %while True
    for j=1:5   %���¾�ֵ���õ��µ�������ĵ�
        index=find(Label_index==j); %�ҵ�ͬ���͵������ֵ
        Means(j,:)=mean(X(index,:));
    end
    if (old_Label==Label_index) %ֱ����ǩ���ڸı䣬�˳�������
        break;
    end
    old_Label=Label_index;
end
%����������ͼ
index = find(Label_index==1); %ȡ�����ͬΪ1���������ú�ɫ��ǣ�����ͼ
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
%���������
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

 
    
    





