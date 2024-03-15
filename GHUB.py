# 导入所需的模块
import json
import os.path
import time
import os
import threading
import pyttsx3
import pyautogui
import win32api, win32con

# 打印提示信息，说明按键功能和调试选项
print("1,2和e键会更新数据,debug可以从当前目录的设置.json中设置成1")
上 = -1
下 = 1
左 = -1
右 = 1
# 定义一个字典，存储各种参数的值，如次数，间隔，识别阈值等
config = {"次数": 2,
          "默认": 2,
          "R301": 2,
          "R99": 10,
          "fcns": 5,
          "dn": 7,
          "zz": 5,
          "hwk": 6,
          "car": 13,
          "bz": 2,
          "ak": 3,
          "ls": 60,
          "ph": 2,
          "zhz": 6,
          "zb": 0,
          "G7": 8,
          "debug": 0,
          "识别阈值": 0.9,
          "间隔": 0.0015}

# 定义一些常量，表示按键的虚拟键码
VK_1 = 0x31
VK_2 = 0x32

# 如果当前目录不存在设置.json文件，就创建一个，并写入默认的参数值
if os.path.exists("设置.json") == False:
    with open("设置.json", "w+", encoding="UTF-8") as f:
        json.dump(config, f, indent=4, sort_keys=True, ensure_ascii=False)


# 定义一个函数，用于刷新参数值和武器选择
def 刷新():
    # 声明全局变量，方便在函数内部修改
    global 次数, 次数2, 间隔, config_, choice_, 是否启动连点
    # 无限循环，每隔0.001秒检测一次按键状态和屏幕内容
    while True:
        time.sleep(0.001)
        # 获取1,2和e键的按键状态，如果有任何一个被按下，就更新参数值和武器选择
        press1 = win32api.GetAsyncKeyState(VK_1)
        press2 = win32api.GetAsyncKeyState(VK_2)
        press = win32api.GetAsyncKeyState(0x45)
        a = ""
        # 如果当前目录不存在设置.json文件，就创建一个，并写入默认的参数值
        if os.path.exists("设置.json") == False:
            with open("设置.json", "w+", encoding="UTF-8") as f:
                json.dump(config, f, indent=4, sort_keys=True, ensure_ascii=False)
        # 否则，读取设置.json文件中的参数值，并赋给相应的变量
        elif a == "":
            if press != 0 or press1 != 0 or press2 != 0:
                with open("设置.json", "r+", encoding="UTF-8") as f:
                    config_ = json.load(f)
                    次数 = config_["次数"]
                    间隔 = config_["间隔"]
                    识别阈值 = config_["识别阈值"]
                    # 尝试根据屏幕上的武器图标，判断用户使用的武器，并根据武器类型选择相应的后坐力补偿值
                    try:
                        #如果这里报错请查看locateOnScreen的__init__文件第174行改成return None
                        if pyautogui.locateOnScreen(r".\ts\R301.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["R301"]
                            是否启动连点 = False
                            # 如果开启了调试模式，就用语音播报武器名称
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("R301")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\R99.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["R99"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("R99")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\fcns.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["fcns"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("复仇女神")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\dn.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["dn"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("电能冲锋枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\zz.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["zz"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("专注轻机枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\hwk.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["hwk"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("哈沃克步枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\car.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["car"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("CAR冲锋枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\bz.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["bz"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("暴走")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\ak.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["ak"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("平行步枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\ls.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["ls"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("猎兽冲锋枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\ph.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["ph"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("喷火轻机枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\zhz.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["zhz"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("转换者冲锋枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\re45.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["re45"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("RE45自动手枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\zb.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["zb"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("滋崩")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\G7.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["G7"]
                            是否启动连点 = True
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("G7侦查枪")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\3030.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["3030"]
                            是否启动连点 = True
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("3 0 3 0")
                                engine.runAndWait()
                        elif pyautogui.locateOnScreen(r".\ts\Lstar.png", grayscale=True, confidence=识别阈值) != None:
                            choice_ = config_["Lstar"]
                            是否启动连点 = False
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("L star")
                                engine.runAndWait()
                        else:
                            choice_ = config_["默认"]
                            if config_["debug"] == 1:
                                engine = pyttsx3.init()
                                engine.say("默认")
                                engine.runAndWait()

                    # 如果出现异常，就用语音播报错误信息，并提示用户检查文件夹位置
                    except:
                        engine = pyttsx3.init()
                        engine.say("错误,请查看ts文件夹是否与exe在同一目录下")
                        engine.runAndWait()
                    # 打印当前的参数值，方便用户查看
                    # finally:
                    #     print(次数, choice_, 间隔)


# 如果这个脚本是作为主程序运行，就执行以下代码
if __name__ == "__main__":
    # 创建一个线程，用于执行刷新函数，并设置为守护线程，随主程序退出而退出
    t = threading.Thread(target=刷新, daemon=True)
    # 启动线程
    t.start()
    # 打开设置.json文件，读取参数值，并赋给相应的变量
    with open("设置.json", "r+", encoding="UTF-8") as f:
        config_ = json.load(f)
        choice_ = config_["默认"]
        次数 = config_["次数"]
        间隔 = config_["间隔"]
# 刷新函数
# 无限循环，每隔间隔时间检测一次鼠标和键盘的状态
while True:
    # 获取鼠标左键的状态
    time.sleep(间隔)
    # 获取鼠标左右键的状态
    start = win32api.GetAsyncKeyState(win32con.VK_LBUTTON)
    out = win32api.GetAsyncKeyState(win32con.VK_RBUTTON)
    # 获取Ctrl和空格键的状态
    ctrl = win32api.GetAsyncKeyState(win32con.VK_LCONTROL)
    space = win32api.GetAsyncKeyState(win32con.VK_SPACE)
    # 如果鼠标左右键都被按下，就执行以下代码
    if out != 0 and out != 1 and start != 0:
        # 向下压，根据武器类型选择不同的次数
        for i in range(choice_):
            win32api.mouse_event(win32con.MOUSE_MOVED, 0, 1)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 左, 0)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 右, 0)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 0, 下)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 0, 上)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 右, 0)
            time.sleep(间隔)
        for i in range(次数):
            win32api.mouse_event(win32con.MOUSE_MOVED, 左, 0)
            time.sleep(间隔)
        # for i in range(choice_):
        #     win32api.mouse_event(win32con.MOUSE_MOVED, 0, 1)
        #     time.sleep(间隔)
        # # 花圈，根据参数值选择不同的次数和方向
        # for i in range(次数):
        #     win32api.mouse_event(win32con.MOUSE_MOVED, -1, -1)
        #     time.sleep(间隔)
        # for i in range(次数):
        #     win32api.mouse_event(win32con.MOUSE_MOVED, 1, 1)
        #     time.sleep(间隔)
        # for i in range(次数):
        #     win32api.mouse_event(win32con.MOUSE_MOVED, 1, -1)
        #     time.sleep(间隔)
        # for i in range(次数):
        #     win32api.mouse_event(win32con.MOUSE_MOVED, -1, 1)
        #     time.sleep(间隔)
