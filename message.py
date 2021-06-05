data = []
count = 0
with open('001.txt', 'r') as f: # 打開檔案，使用讀取模式
    for line in f: # 每筆資料，叫做line
        data.append(line) #把每筆資料line 加入空清單data
        count += 1 # 每讀取一筆資料count + 1
        if count % 3 == 0: # 每數到3的倍數
            print(len(data)) # 就print
print('檔案讀取完畢，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print('留言平均長度是', sum_len/len(data))    