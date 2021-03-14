import db

query_sql="select * from user"
data=db.query_data(query_sql)

for i in data:
    print(i)

insert_sql="""
    insert user (name,sex,age,email)
    values ('mayi','man',20,'mayi@qq.com')
"""
db.insert_or_update_data(insert_sql)

query_sql="select * from user"
data=db.query_data(query_sql)

for i in data:
    print(i)

update_sql="update user set name='damayi' where id=3"
db.insert_or_update_data(update_sql)

query_sql="select * from user"
data=db.query_data(query_sql)

for i in data:
    print(i)