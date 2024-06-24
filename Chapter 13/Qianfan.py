# coding=utf-8
import os
import qianfan


def gpt(question):
    with open("Chapter 13/QIANFAN_ACCESS_KEY", "r", encoding="utf-8") as f:
        ACCESS_KEY = f.read()

    with open("Chapter 13/QIANFAN_SECRET_KEY", "r", encoding="utf-8") as f:
        SECRET_KEY = f.read()

    os.environ["QIANFAN_ACCESS_KEY"] = ACCESS_KEY
    os.environ["QIANFAN_SECRET_KEY"] = SECRET_KEY

    chat_robot = qianfan.ChatCompletion()

    resp = chat_robot.do(messages=[{"role": "user", "content": question}])
    return resp.body["result"]
