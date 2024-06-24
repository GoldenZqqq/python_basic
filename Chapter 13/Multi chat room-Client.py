import wx
from socket import *
import threading


class Client(wx.Frame):
    # 构造方法
    def __init__(self):
        # 实例属性
        self.name = "mia"  # 客户端名称
        self.isConnected = False  # 客户端是否连接服务器
        self.clent_socket = None

        # 界面布局
        wx.Frame.__init__(
            self,
            None,
            title=self.name + "聊天室客户端",
            size=(450, 650),
            pos=(100, 100),
        )
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建按钮
        # 加入聊天室
        self.conn_btn = wx.Button(
            self.pl, label="加入聊天室", pos=(10, 10), size=(200, 40)
        )
        # 离开聊天室
        self.dis_conn_btn = wx.Button(
            self.pl, label="离开聊天室", pos=(220, 10), size=(200, 40)
        )
        # 清空按钮
        self.clear_btn = wx.Button(self.pl, label="清空", pos=(10, 555), size=(200, 40))
        # 发送按钮
        self.send_btn = wx.Button(self.pl, label="发送", pos=(220, 555), size=(200, 40))
        # 创建聊天内容文本框
        self.text = wx.TextCtrl(
            self.pl,
            size=(410, 400),
            pos=(10, 60),
            style=wx.TE_READONLY | wx.TE_MULTILINE,
        )
        # 创建输入文本框
        self.input_text = wx.TextCtrl(
            self.pl, size=(410, 80), pos=(10, 470), style=wx.TE_MULTILINE
        )
        # 按钮的事件绑定
        self.Bind(wx.EVT_BUTTON, self.clear, self.clear_btn)
        self.Bind(wx.EVT_BUTTON, self.conn, self.conn_btn)
        self.Bind(wx.EVT_BUTTON, self.dis_conn, self.dis_conn_btn)
        self.Bind(wx.EVT_BUTTON, self.send, self.send_btn)

    # 点击 加入聊天室 按钮触发
    def conn(self, event):
        print("conn")

    # 点击 离开聊天室 按钮触发
    def dis_conn(self, event):
        print("dis_conn")

    # 点击 清空 按钮触发
    def clear(self, event):
        print("clear")

    # 点击 发送 按钮触发
    def send(self, event):
        print("send")


# 程序入口
if __name__ == "__main__":
    # 创建应用程序对象
    app = wx.App()
    # 创建客户端窗口
    client = Client()
    # 显示窗口
    client.Show()
    # 一直循环显示
    app.MainLoop()
