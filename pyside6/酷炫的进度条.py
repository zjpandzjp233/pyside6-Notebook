from progress.bar  import PixelBar
"""
Bar
ChargingBar
FillingSquaresBar
FillingCirclesBar
IncrementalBar
PixelBar
ShadyBar
"""
import time

# 假设我们有一个任务需要完成100个步骤
total_steps = 10

# 创建一个进度条实例
bar = PixelBar('Processing', max=total_steps)

print(list( range(total_steps))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# 模拟任务的执行
for i in range(total_steps):
    # 模拟任务的每一步
    time.sleep(0.1)   # 这里可以替换为实际的任务代码
    
    # 更新进度条
    bar.next() 

# 任务完成后，完成进度条
bar.finish() 
"""
1.停止更新进度条：不再接受新的更新请求。
2.打印最终状态：通常会在进度条下方打印一条消息，表示任务已经完成。
3.恢复终端状态：如果进度条在运行过程中对终端进行了某些修改（如禁用了换行符），调用 finish() 方法会恢复这些设置，使得终端恢复正常工作状态。
"""