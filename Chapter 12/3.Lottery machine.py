import wx
import random


class MyFrame(wx.Frame):
    # 抽奖列表
    NameList = ["mia", "tom", "jack"]

    # 构造方法
    def __init__(self):
        super().__init__(None, title="抽奖器")
        # 创建面板
        self.pl = wx.Panel(self)
        # 创建静态文本
        self.staticText = wx.StaticText(self.pl, label=random.choice(self.NameList))
        # 创建按钮
        self.btn1 = wx.Button(self.pl, label="开始抽奖", pos=(100, 150))
        self.btn2 = wx.Button(self.pl, label="结束抽奖", pos=(200, 150))
        # 绑定事件
        self.Bind(wx.EVT_BUTTON, self.onClick, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.stop, self.btn2)

    def onClick(self, event):  # 抽奖
        self.timer = wx.Timer(self)  # 创建了一个定时器
        self.Bind(wx.EVT_TIMER, self.update_name, self.timer)
        self.timer.Start(100)  # 每隔100毫秒更新名字

    def update_name(self, event):
        self.staticText.SetLabelText(random.choice(self.NameList))

    def stop(self, event):
        self.timer.Stop()  # 停止计时器


if __name__ == "__main__":  # Python程序主入口
    # 创建应用程序对象
    app = wx.App()
    # 创建窗口
    frm = MyFrame()
    # 显示窗口
    frm.Show()
    # 让窗口一直显示
    app.MainLoop()
