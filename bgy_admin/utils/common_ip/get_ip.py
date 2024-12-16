from utils.common_ip.xdbSearcher import XdbSearcher


def search_ip(ip_str):
    # 1. 缓存
    dbPath = "./utils/common_ip/data/ip2region.xdb"
    cb = XdbSearcher.loadContentFromFile(dbfile=dbPath)
    # 2. 创建查询对象
    searcher = XdbSearcher(contentBuff=cb)
    # 3. 执行查询
    region_str = searcher.searchByIPStr(ip_str).split("|")
    # 4. 解析查询结果
    contury = region_str[0]
    province = region_str[2]
    city = region_str[3]
    if province != str(0) and city != str(0):
        addr = contury + "-" + province + "-" + city
    elif city == str(0) and province == str(0):
        addr = contury
    elif city == str("内网IP"):
        addr = "内网IP"
    else:
        addr = "未知"
    # 5. 关闭查询对象
    searcher.close()
    return {"common_ip": ip_str, "addr": addr}
