import matplotlib.pyplot as plt

    # 重点：plot的color函数接受的rgb需要是float类型，所以需要归一化
def rgb_normalized(triple):
    normalized_color = tuple([i/255 for i in triple])
    return normalized_color

color_dict_1 = {
    "深红": (142, 0, 40),
    "橘红": (189, 60, 51),
    "橙": (228, 148, 90),
    "浅橙": (249, 198, 118),
    "浅黄": (251, 236, 171),
    "浅蓝": (209, 226, 239),
    "天蓝": (127, 169, 205),
    "宝蓝": (82, 124, 180),
    "深蓝": (63, 96, 163),
    "靛蓝": (48, 50, 125)
}

color_dict_2 = {
    "品红": (239,118,122),
    "灰蓝": (69,105,144),
    "淡黄": (240,230,140),
}


def main(color_dict):
    #RGB转化为浮点数
    color_dict = {key: rgb_normalized(value) for key, value in color_dict.items()}
    x = range(4,14)
    zhishu = [float(f"1.{j}") for j in range(0,len(color_dict))] # 每个颜色一个指数

    curve_data={}
    for j in range(0,len(color_dict)): # 每个颜色生成一条线
        curve_data[f"y_{j}"] = [i**(zhishu[j]) for i in x]

    for j in range(0,len(curve_data)):
        y = curve_data[f"y_{j}"]
        color_name = list(color_dict.keys())[j]
        plt.plot(x, y,color=color_dict[color_name])

    plt.savefig('./fig.png')


if __name__ == '__main__':
#选用颜色套件
    color_dict = color_dict_1
    main(color_dict)