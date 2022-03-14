from pymysql import *


def upload(self,username,FEV1,FVC,FEV1_FVE,PEF,RR):

    try:
        # 创建数据库的连接
        conn = connect(host='42.192.168.242', user='root', password='123456',
                       database='mytest', charset='utf8')
        cur=conn.cursor()
        sql = "insert into UserInfo(username,FEV1,FVC,FEV1_FVE,PEF,RR) values (%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(username,FEV1,FVC,FEV1_FVE,PEF,RR))
        conn.commit()
    except Exception as ex:
        print(ex)
        pass
    finally:
        cur.close()
        conn.close()

    return '0'
