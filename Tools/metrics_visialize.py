import pandas as pd
import matplotlib.pyplot as plt
import json

# JSONL文件路径
file_path = "/home/zhangzishuai/RAG-Rerank/Experiments/fintune_output/TopiOCOA/rewrited/e10_acc-step4/loss.jsonl"
save_file_path = '/home/zhangzishuai/RAG-Rerank/Experiments/fintune_output/TopiOCOA/rewrited/e10_acc-step4/loss.png'

# 创建一个空列表来存储数据
data_list = []

# 逐行读取文件
with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        # 去除行尾的空格,换行符
        trimmed_line = line.rstrip()
        # 解析 JSON
        obj = json.loads(trimmed_line)
        # 添加到列表
        data_list.append(obj)

#  data_list
# 000 = {'loss': 2.9927, 'grad_norm': 9.52935791015625, 'learning_rate': 9.945205479452056e-05, 'epoch': 0.07}
# 001 = {'loss': 2.6412, 'grad_norm': 11.861735343933105, 'learning_rate': 9.876712328767123e-05, 'epoch': 0.14}
# 002 = {'loss': 2.6373, 'grad_norm': 9.721269607543945, 'learning_rate': 9.808219178082192e-05, 'epoch': 0.21}

# 创建 DataFrame
data = pd.DataFrame(data_list)
'''
可视化data
print(data[:3])

     loss  grad_norm  learning_rate  epoch
0  2.9927   9.529358       0.000099   0.07
1  2.6412  11.861735       0.000099   0.14
2  2.6373   9.721270       0.000098   0.21
'''



# 提取 epoch 和 loss 列
epochs = data['epoch']
losses = data['loss']

# 绘制损失随epoch的变化
plt.figure(figsize=(10, 5))
plt.plot(epochs, losses, marker='o', linestyle='-', color='b')
plt.title('Training Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.savefig(save_file_path)