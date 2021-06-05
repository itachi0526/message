data = []
count = 0
with open('001.txt', 'r') as f: # 打開檔案，使用讀取模式
    for line in f: # 每筆資料，叫做line
        data.append(line) #把每筆資料line 加入空清單data
        count += 1 # 每讀取一筆資料count + 1
        if count % 3 == 0: # 每數到3的倍數
            print(len(data)) # 就print