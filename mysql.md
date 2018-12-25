

1. 安装mysql客户端：  
```yum install mysql``` 
1. 安装mysql 服务器端：  
```yum install mysql-server yum  ```
1. 安装mysql 服务器端：   
```
yum install mysql-server yum
install mysql-devel
```
1. 安装mysql 服务器端：  
```yum install -y mariadb-server  ```
1. 启动服务  
```systemctl start mariadb.service```  
windows启动 ```net start mysql```
1. 添加到开机启动
```~]# systemctl enable mariadb.service```
1. 登入数据库
```mysql -uroot -p```
1. 查看库
show databases;
1. 使用库
use 库名

1. 查看当前库
select database()

1. 增加用户到mysql
INSERT INTO mysql.user(Host,User) VALUES("%","root")

1. 更新表
update user set host = '%' where user = 'root';

1. 查看表内容
select host, user from user;
flush privileges ;
1. 登录 创建root管理员： 
mysqladmin -u root password 123456 

1. 忘记密码  
```service mysqld stop;
mysqld_safe --user=root --skip-grant-tables;```

1. 这一步骤执行的时候不会出现新的命令行，你需要重新打开一个窗口执行下面的命令  
```mysql -u root;
use mysql ;
update user set password=password("123456") where user="root";
flush privileges; 
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'JM#5vtEhFdAJXx@D' WITH GRANT OPTION;
```
1. 报错问题
![](20151120212649940.png)
```my.ini是否配置正确  
 [mysqld]
 #basedir代表自己MySQL的安装根目录
 basedir = D:\\MySoftWare\\mysql-5.7.9-winx64
 #datadir代表自己MySQL的数据库保存的目录，如果没有在MySQL安装的根目录下新建一个data文件夹 
 datadir = D:\\MySoftWare\\mysql-5.7.9-winx64\\data
 #port代表端口号
 port = 3306
 sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES 
```