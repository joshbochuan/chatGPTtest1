import json

# 讀取 JSON 檔案
with open('emotional_intelligence.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 顯示問題並獲取回答
total_score = 0

for question in data:
    print(question['question'])
    print('請選擇適合你的選項：')

    for option in question['options']:
        print(option['option'] + ': ' + option['text'])

    user_choice = input('請輸入你的選項（A/B/C/D）：')

    # 檢查用戶選擇的選項並增加相應的得分
    for option in question['options']:
        if option['option'] == user_choice:
            total_score += option['score']
            break

    print()

# 顯示最終得分
print('你的情商測驗總得分為：', total_score)

# 根據得分範圍分區
if total_score >= 30:
    print('恭喜！你的情商非常高。')
elif total_score >= 20:
    print('你有一定的情商，但還有提升的空間。')
elif total_score >= 10:
    print('你的情商較低，可以開始學習提升它。')
else:
    print('你的情商非常低，建議你積極學習和培養情商。')