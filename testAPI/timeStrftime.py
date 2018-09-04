import time,sqlalchemy,hashlib


def shiJianChuoZhuanShiJian(shiJianChuo):
    time0 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(shiJianChuo))
    return f'对应时间为：{time0}'

def zhuanShiJianChu(dt):
    # 转换成时间数组
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    # print(timeArray)
    return f'对应时间戳为：{int(time.mktime(timeArray))}'

if __name__ == '__main__':
    timestamp = 1515385600
    print(shiJianChuoZhuanShiJian(timestamp))
    # print(int(time.time()))
    print(round(time.time()))


    # dt = '2018-08-09 15:54:12'
    # print(zhuanShiJianChu(dt))
    # # time1 = time.strftime('%Y-%m-%d %H:%M:%S')
    # # mssg = f"{time1}___载入URL..."
    # # print(mssg)
    # print(time.strftime("%Y-%m-%d %H:%M:%S"))

    # sii = "95fe560fe5aa5d7dc20f5507b1846460"[-6::]
    # print(hashlib.md5(sii.encode()).hexdigest())
    # print(str(int(time.time()))[-6::])
    # print(str(int(time.time()))[0:4])
    # d1 = {"a":"d","b":[{"d":"g","ar":1},{"d":"g","ar":2},{"d":"g","ar":3},{"d":"g","ar":4}]}
    # print([item["ar"] for item in d1["b"]])
    # print([item for item in d1["b"].keys("ar")])
    # # print(sii.count([*sii]))
    # print(hashlib.md5("dongjian1234".encode()).hexdigest())