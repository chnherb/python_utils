# coding=utf8
import MySQLdb
import sys
import time
import pandas as pd
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

host = 'localhost'
port = 3306
user = 'root'
passwd = 'root'
db = 'newsdb'
charset = 'utf8'


class MySQLDBUtil:
    @staticmethod
    def Insert(tableName, newsdict):
        conn = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        try:
            cursor = conn.cursor()
            # curtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            sql = "insert into %s(website,title,title_fen,content,content_fen,date,source,url,remarks) \
                values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                (tableName, newsdict['website'], newsdict['title'], u'', newsdict['content'], u'',
                 newsdict['date'], newsdict['source'], newsdict['url'], newsdict['remarks'])
            # print(sql)
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("error:", e)
            # writefile(newsdict['url'],'mysqlError.txt','a')
        finally:
            conn.close()

    @staticmethod
    def Insertbydict(tableName, newsdict):
        conn = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        try:
            cursor = conn.cursor()
            keys = ''
            values = ''
            for k, v in newsdict.items():
                keys = keys + k + ','
                if type(v) != str:
                    values = values + str(v) + ','
                else:
                    values = values + '\'' + v + '\'' + ','
            keys = keys[:-1]
            values = values[:-1]
            print(keys)
            print(values)
            sql = "insert into %s(%s) values (%s)" % (tableName, keys, values)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print("error:", e)
            # writefile(newsdict['url'],'mysqlError.txt','a')
        finally:
            conn.close()

    @staticmethod
    def Insertbydataframe(tableName, df):
        from sqlalchemy import create_engine
        engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s:%s/%s?charset=%s") %
                               (user, passwd, host, port, db, charset))
        try:
            df.to_sql(tableName, con=engine, if_exists='append', index=False)
        except Exception as e:
            print("error:", e)

    @staticmethod
    def Select(tableName, stuinfo):
        stuinfo.replace("'", "")
        stuinfo.replace(" ", "")
        if len(stuinfo) == 0:
            return u'非法操作'
        conn = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        # conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='herb', db='universityinfo', charset='utf8')
        try:
            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            sql = "select * from %s where stuno = '%s' or stuname like '%%%s%%'" % (
                tableName, stuinfo, stuinfo)
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            count = 1
            if len(results) < count:
                count = len(results)
            infolist = []
            for index, row in enumerate(results):
                no = row['stuno']
                name = row['stuname']
                dept = row['studept']
                grade = row['gradeinfo']
                infolist.append("第%d条记录：" % (index+1))
                infolist.append("%s,%s,%s" % (no, name, dept))
                infolist.append(grade)
                if index >= count - 1:
                    break
            info = '\n'.join(infolist)
            info = u'查询到%d条记录，显示%d条记录：\n%s' % (len(results), count, info)
            # print info
            return info
        except Exception as e:
            conn.rollback()
            print e
        finally:
            conn.close()

    @staticmethod
    def Select(tableName):
        conn = MySQLdb.connect(
            host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)
        try:
            sql = "select * from %s " % (tableName)
            df = pd.io.sql.read_sql(sql, conn)
            # print(df.shape)
            # print(type(df))
            return df
        except Exception as e:
            conn.rollback()
            print e
            return null
        finally:
            conn.close()


if __name__ == '__main__':
    # MySQLDBUtil.Insert('tbmusicrecord',u'Huangbo',u'张宇')
    # # MySQLDBUtil.Select('grade', u'想')
    # MySQLDBUtil.Select('tbnews')
    # date = time.localtime(time.time())
    # print(type(date))
    # print(date)

    # df = MySQLDBUtil.Select(u'tbnews')
    # print(len(df))

    newsdict = dict()
    newsdict['nid'] = "1"
    newsdict['website'] = '165'
    newsdict['title_fen'] = '163'
    newsdict['content_fen'] = '163'
    newsdict['date'] = '2017-09-07 07:51:00'
    newsdict['source'] = 'xxxx'
    newsdict['url'] = 'https:///'
    newsdict['remarks'] = '2'
    MySQLDBUtil.Insertbydict('tbnewsfen', newsdict)
