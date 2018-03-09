# -*- coding: utf-8 -*-
import json
import redis  # pip install redis
import pymysql

def main():
    # 指定redis数据库信息
    rediscli = redis.StrictRedis(host='10.11.203.144', port = 6379, db = 0)
    # 指定mysql数据库
    mysqlcli = pymysql.connect(host='127.0.0.1', user='root', passwd='asd19960321', db='my_spider', charset='utf8')

    # 无限循环
    while True:
        #  更改 hmr_liepin 来抓取不同items 存入数据库
        source, data = rediscli.blpop(["hmr_liepin:items"]) # 从redis里提取数据

        item = json.loads(data.decode('utf-8')) # 把 json转字典

        try:
            # 使用cursor()方法获取操作游标
            cur = mysqlcli.cursor()
            # 使用execute方法执行SQL INSERT语句
            sql = "insert into jobs( jid, title, salaryMin, salaryMax, exp, tags, date_pub, advantage, addr , company , spider , crawled ,link) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = [item['jid'], item['title'], item['salaryMin'], item['salaryMax'], item['exp'], item['tags'],
                    item['date_pub'], item['advantage'], item['addr'], item['company'], item['spider'], item['crawled'],
                    item['link']]
            cur.execute(sql,data)


            # 提交sql事务
            mysqlcli.commit()
            #关闭本次操作
            cur.close()
            print("插入 %s" % item['title'])
        except pymysql.Error as e:
            mysqlcli.rollback()
            print("插入错误" ,str(e),item['link'])


if __name__ == '__main__':
    main()