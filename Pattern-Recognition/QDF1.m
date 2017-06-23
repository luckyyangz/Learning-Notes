
clear
clc
%读数据图像
train_mages=255*loadMNISTImages('train-images.idx3-ubyte');
test_mages=255*loadMNISTImages('t10k-images.idx3-ubyte');
%读数据标签
train_label=loadMNISTLabels('train-labels.idx1-ubyte');
test_label=loadMNISTLabels('t10k-labels.idx1-ubyte');
%求出样本协方差
%e=cov(c); 
%计算判别函数，默认先验概率
%ei=pinv(e);

for n=1:1:10
    b=train_mages(:,train_label==(n-1));
    u(:,n)=mean(b,2);
    c=b'; %60000*784
    e(:,:,n)=cov(c);
    ei(:,:,n)=pinv(e(:,:,n));
%    u(:,n)=mean(b,2);
    w(:,n)=ei(:,:,n)*u(:,n);
    wi=-0.5*ei;
    wi0(:,n)=-0.5*u(:,n)'*ei(:,:,n)*u(:,n)+log(0.1);
end
for i=1:1:10
    for j=1:1:10000
        g(i,j)=test_mages(:,j)'*wi(:,:,n)*test_mages(:,j)+w(:,i)'*test_mages(:,j)+wi0(:,i);
    end
end
[a,t]=max(g,[],1);
t=t-1;
p=sum(test_label==t')/length(test_label);
