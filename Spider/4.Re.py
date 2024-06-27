import re

# 提取字符串相关函数
# re.match()  从字符串的起始位置开始匹配 noneType
# text = "姓名：张三 生日：1999年1月1日 毕业日期：2020年9月1日"
# t1 = re.match("姓名.*生日：(\d{4}).*毕业日期：(\d{4}).*", text)
# print(t1.group(1), t1.group(2), t1.groups())
# # re.search()  扫描整个字符串并返回第一个成功的匹配
# t2 = re.search("生日：(\d{4}).*日期：(\d{4})", text)
# print(t2.group(1), t2.group(2))

# # re.findall()
# t3 = re.findall("生日：(\d{4}).*日期：(\d{4})", text)[0][0]
# print(t3)


# text1 = """
# 姓名：张三 生日：1999年9月1日 毕业日期：2020年9月1日
# 姓名：李四 生日：2000年5月6日 毕业日期：2020年9月1日
# 姓名：王五 生日：1998年4月1日 毕业日期：2020年9月1日
# """
# t4 = re.findall("生日：(.*?) 毕业日期", text1)
# print(t4)


# 替换 re.sub()
# text2 = "0566-32323232"
# t7 = re.sub("^\d{4}", "0755", text2)
# text3 = "0666-32323232".replace("0566", "0755")
# print(text3)

# text4 = """
# <div class=" catalog-list_iR5a4">
#   <div>
#       <a style="color:" href="http://www.baidu.com/link?url=15tpX76v11VWAjfJBkWTLzZ9mHTRnhPKYCuJ2k4b4OJBEj4yfeV_LbdDlntgd82UoOIuoeadSF2piTtSBDycbsuwxozHJVJ8genR6LgtdZ9CkWlnz3BeNGSFixRcju5s" target="_blank" aria-label="程序简介" tabindex="0">
#           程序简介
#       </a><a style="color:" href="http://www.baidu.com/link?url=15tpX76v11VWAjfJBkWTLzZ9mHTRnhPKYCuJ2k4b4OJBEj4yfeV_LbdDlntgd82UoOIuoeadSF2piTtSBDycbsuwxozHJVJ8genR6LgtdZ7NYjRjzr6D5T8xkktkzasq" target="_blank" aria-label="应用说明" tabindex="0">
#           应用说明
#       </a><a style="color:" href="http://www.baidu.com/link?url=15tpX76v11VWAjfJBkWTLzZ9mHTRnhPKYCuJ2k4b4OJBEj4yfeV_LbdDlntgd82UoOIuoeadSF2piTtSBDycbsuwxozHJVJ8genR6LgtdZ7SqwFyzY69qiUe0wmZ0roZ" target="_blank" aria-label="基本程序" tabindex="0">
#           基本程序
#       </a><a style="color:" href="http://www.baidu.com/link?url=15tpX76v11VWAjfJBkWTLzZ9mHTRnhPKYCuJ2k4b4OJBEj4yfeV_LbdDlntgd82UoOIuoeadSF2piTtSBDycbsuwxozHJVJ8genR6LgtdZ8swLu3JbGpZjYdWAKRxrMV" target="_blank" aria-label="具体步骤" tabindex="0">
#           具体步骤
#       </a><a style="color:" href="http://www.baidu.com/link?url=15tpX76v11VWAjfJBkWTLzZ9mHTRnhPKYCuJ2k4b4OJBEj4yfeV_LbdDlntgd82UoOIuoeadSF2piTtSBDycbsuwxozHJVJ8genR6LgtdZ9ix5ARJ3gEZw1Rn4rBlZw9" target="_blank" aria-label="案例分析" tabindex="0">
#           案例分析
#       </a><a style="color:" href="http://www.baidu.com/link?url=B4I61jdJIde8T-2IyH2-LVpELHC__9bb4fCO478IfL7ZtcKIL0uasmm87RL0SM1zQRfGrrJAkduRYQrjbjLayLc44hf176UiMNqys61wLjfQypF6nvr2y0NaVwSe9xCN" target="_blank" aria-label="点击可查看更多内容" tabindex="0">
#           更多 >
#       </a>
#   </div>
# </div>
# """
# t8 = re.sub("<.*?>", "", text4)
# print(t8)

# # 字符串分割 re.split()
# text5 = "你好,Python.今天你学习了吗"
# t9 = re.split("[,.]", text5)
# print(t9)

# 换行加注释
# re.findall("生日：(\d{4}).*日期：(\d{4})", text)[0][0]
# text6 = "姓名：张三 生日：1999年1月1日 毕业日期：2020年9月1日"
# t10 = re.findall(
#     """生日  # 开始匹配
# .*?(\d{4}).*毕业日期  # 匹配生日
# .*?(\d{4})  # 匹配毕业日期
# """,
#     text6,
#     re.VERBOSE,
# )  # re.VERBOSE 忽略空白字符，并开启多行模式
# print(t10)

# 编译正则表达式 re.compile
text7 = "姓名：张三 生日：1999年1月1日 毕业日期：2020年9月1日"
tt = re.compile("生日.*?(\d{4}).*毕业日期.*?(\d{4})")
t11 = re.findall(tt, text7)
print(t11)
