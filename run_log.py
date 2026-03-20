import datetime
import os

def record_income():
    print("--- 每日跑车流水记录 ---")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 输入各项数据
    platform = input("输入平台（如：阳光、首汽、滴滴）: ")
    orders = input("完成单数: ")
    money = input("流水金额 (元): ")
    gas_cost = input("油费/电费 (元): ")
    note = input("备注 (如：投诉维权中、天气大雨): ")

    # 计算净利润
    try:
        profit = float(money) - float(gas_cost)
    except:
        profit = 0

    # 格式化数据
    log_entry = f"{date} | {platform} | 单数:{orders} | 流水:{money} | 能耗:{gas_cost} | 净利:{profit:.2f} | 备注:{note}\n"

    # 写入本地文件
    file_path = "daily_income.txt"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"\n✅ 已记录！今日净利: {profit:.2f} 元")
    
    # 自动备份到 GitHub
    confirm = input("\n是否立即同步到云端仓库？(y/n): ")
    if confirm.lower() == 'y':
        os.system("git add .")
        os.system(f'git commit -m "更新流水: {date}"')
        os.system("git push")
        print("☁️ 数据已安全同步到 GitHub！")

if __name__ == "__main__":
    record_income()
