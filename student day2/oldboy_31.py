#   31、av_catalog = {
#       "欧美": {
#           "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
#           "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
#           "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
#           "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
#       },
#       "日韩": {
#           "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
#        },
#       "大陆": {
#           "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
#       }
#   }
#
#       a, 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
#       b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
#       c, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收  费,屌丝请绕过"删除。
#       d, 将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
#       e, 给'大陆'对应的字典添加一个键值对'1048': ['一天就封了']
#       f, 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]键值对。
#       g, 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'

dic ={
    "欧美": {
            "www.youporn.com": ["很多免费的,世界最大的", "质量一般"],
            "www.pornhub.com": ["很多免费的,也很大", "质量比yourporn高点"],
            "letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"],
            "x-art.com": ["质量很高,真的很高", "全部收费,屌丝请绕过"]
            },
    "日韩": {
            "tokyo-hot": ["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]
            },
    "大陆": {
            "1024": ["全部免费,真好,好人一生平安", "服务器在国外,慢"]
            }
    }
# a 给此["很多免费的,世界最大的", "质量一般"]列表第二个位置插入一个元素：'量很大'。
dic["欧美"]["www.youporn.com"].append('量很大')

# b, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收费,屌丝请绕过"删除。
# dic["欧美"]["x-art.com"].pop()
print(dic)
# c, 将此["质量很高,真的很高", "全部收费,屌丝请绕过"]列表的"全部收  费,屌丝请绕过"删除。
# print(("全部收  费,屌丝请绕过".replace(' ', '')))
dic["欧美"]["x-art.com"].remove(("全部收  费,屌丝请绕过".replace(' ', '')))
print(dic)
# d, 将此["质量怎样不清楚,个人已经不喜欢日韩范了", "verygood"]列表的"verygood"全部变成大写。
# print("verygood".upper())
dic["日韩"]["tokyo-hot"][-1] = dic["日韩"]["tokyo-hot"][-1].upper()
print(dic)
# e, 给'大陆'对应的字典添加一个键值对'1048': ['一天就封了']
dic["大陆"]["1048"] = '一天就封了'
print(dic)
# f, 删除此"letmedothistoyou.com": ["多是自拍,高质量图片很多", "资源不多,更新慢"]键值对。
dic["欧美"].pop("letmedothistoyou.com")
print(dic)
# g, 给此["全部免费,真好,好人一生平安", "服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
dic['大陆']["1024"][0] += '可以爬下来'
print(dic)