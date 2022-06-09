

# 备份命令格式
# mysqldump -u用户名 -p 源库名 >~/**.sql
# 举例
# mysqldump -uroot -p class_1 >C:\Users\Administrator\Desktop\新建文件夹/stu.sql
# --all-databases 备份所有库
# -b 库1 库2 库3 备份多个库
# 库名 表1 表2 表3 备份指定库的多张表


# 恢复命令格式
# mysql  -u root -p 目标库名 <***.sql
# 举例
# mysql -uroot -p student <C:\Users\Administrator\Desktop\新建文件夹/stu.sql
# 从所有库备份中恢复某一个库（--one-database）
# mysql -uroot -p --one-database 目标库名 < all.sql