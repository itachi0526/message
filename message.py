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

# 留言長度小於100
new = []    
for d in data:
    if len(d) < 10:
        new.append(len(d))
print('一共有', len(new), '筆留言長度小於10')

# h這個字在那些留言裡面
s = []
for d in data:
    if 'h' in d:
        s.append(d)
print('一共有', len(s), '筆留言提到h')

# 24～28 進階 s = [d for d in data if 'h' in d] 再print

j = ['j' in d for d in data]
print(j)

# 'j' in d 會有True/ False的結果，所以應該會印出31個布林值     