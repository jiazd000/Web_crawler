# -*- coding: utf-8 -*-
import MySQLdb
print('xx')


def get_database():
    DATABASE = {
        'host': 'localhost',
        'database': 'test',
        'user': 'root',
        'password': '12291107'
    }
    database = MySQLdb.connect(host='localhost', user='root', passwd='12291107',
                         db='test', port=3306,charset="utf8")
    # db = MySQLdb.connect(**DATABASE)
    return database


def get_tables(database):
    cursor = database.cursor()
    # cursor.execute("SET NAMES utf8")
    # sql = cursor.execute(sql)
    # cursor.execute('SELECT VERSION()')
    # data = cursor.fetchone()
    # print 'database version is %s' % data
    sql = '''
        create table house(
            housenum varchar(50) primary key not null,
            price varchar(50) ,
            unit varchar(50),
            area varchar(50),
            layout varchar(50),
            floor varchar(50),
            direction varchar(50),
            time varchar(50),
            subway varchar(50),
            village varchar(50),
            place varchar(50)
        ) DEFAULT CHARSET=utf8;
    '''
    cursor.execute(sql)

    # return database


def insert_data(database,house_data):
    cursor = database.cursor()

    sql = '''INSERT INTO house(housenum,price,
             unit,area,layout,floor,direction,time,
              subway,village,place)
             VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % (
                            house_data['链家编号'],
                            house_data['价格'],
                            house_data['单位'],
                            house_data['面积'],
                            house_data['户型'],
                            house_data['楼层'],
                            house_data['朝向'],
                            house_data['发布时间'],
                            house_data['地铁'],
                            house_data['小区'],
                            house_data['位置']

    )
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       database.commit()
    except:
       # Rollback in case there is any error
       database.rollback()
       print('error')
    # database.close()

