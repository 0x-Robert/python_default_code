# count=0
# while count < 5:
#     print(count)
#     count += 1

count = 0
while True:
     if count >=5:
          break

     if count == 2:           #2일때 1을 추가하고 continue를 만나서 count찍고 반복해서 위로 올라감
          count += 1
          continue

     print(count)
     count += 1
