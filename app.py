# 中医问诊智能体
# 遵循传统中医：望闻问切 + 体质辨识 + 养生建议

def tcm_agent():
    print("🏥 欢迎使用中医智能问诊助手\n")

    # 1. 基础信息
    name = input("请告诉我你的名字：")
    age = input("年龄：")
    gender = input("性别（男/女）：")
    print(f"\n你好 {name}，我将根据中医方式为你辨证问诊～\n")

    # 2. 核心问诊（中医四诊简化版）
    print("📝 请回答以下身体情况（是/否）\n")

    cold = input("容易怕冷吗？")
    hot = input("容易上火、口干口苦吗？")
    sleep = input("睡眠质量差、多梦或易醒吗？")
    appetite = input("胃口不好、腹胀吗？")
    stool = input("大便稀溏或粘马桶吗？")
    tired = input("经常疲劳、没精神吗？")
    mood = input("容易烦躁、郁闷或压力大吗？")

    # 3. 体质判断逻辑
    print("\n✅ 正在为你辨证...\n")

    if cold == "是" and tired == "是" and stool == "是":
        tizhi = "【阳虚体质】→ 阳气不足，畏寒怕冷"
        food = "建议：生姜、红枣、羊肉、桂圆、小米粥"
        life = "建议：早睡不熬夜，少喝冷饮，注意腰腹保暖"

    elif hot == "是" and mood == "是":
        tizhi = "【阴虚/肝郁体质】→ 内热、压力大、易上火"
        food = "建议：百合、莲子、银耳、绿豆、冬瓜"
        life = "建议：少熬夜，少辛辣，多散步放松心情"

    elif sleep == "是" and tired == "是":
        tizhi = "【气血不足】→ 心神失养、疲劳乏力"
        food = "建议：红枣、枸杞、山药、小米、乌鸡"
        life = "建议：午休10-20分钟，避免过度劳累"

    elif appetite == "是" and stool == "是":
        tizhi = "【脾胃虚弱 + 湿气重】"
        food = "建议：薏米、赤小豆、山药、白扁豆、生姜"
        life = "建议：少吃甜、冷、油腻，饭后散步"

    else:
        tizhi = "【平和体质/轻微亚健康】"
        food = "建议：饮食均衡，作息规律"
        life = "建议：保持运动，心情舒畅"

    # 4. 输出结果
    print("="*40)
    print("📋 中医辨证结果")
    print("="*40)
    print(tizhi)
    print(food)
    print(life)
    print("="*40)
    print("\n⚠️ 本结果仅供养生参考，不替代医院诊疗")

# 启动智能体
tcm_agent()
