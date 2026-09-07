
from house_operation import *

def main():
    # 调用main_menu函数显示主菜单
    # 循环显示菜单
    while True:
        main_menu()
        key = input("请输入你的选择(1-6) ")
        if key in ["1","2","3","4","5","6"]:
            if key == "1":
                print("请输入1-后面我们会处理逻辑...")
            elif key == "2":
                print("请输入2-后面我们会处理逻辑...")
            elif key == "3":
                print("请输入3-后面我们会处理逻辑...")
            elif key == "4":
                print("请输入4-后面我们会处理逻辑...")
            elif key == "5":
                print("请输入5-后面我们会处理逻辑...")
            elif key == "6":
                break


if __name__ == "__main__":
    main()
    print("你退出了程序欢迎下次使用")