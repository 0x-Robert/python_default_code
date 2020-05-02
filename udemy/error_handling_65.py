l = [1,2,3]
i = 5



try:
   l[0]

except IndexError as ex:
    print("Don't worry: {}".format(ex))  #인덱스에러
except NameError as ex:  
    print(ex)                            #네임에러
except Exception as ex:                  #익셉션에러
    print('other:{}'.format(ex))
else:                                    #문제가 없을 때 done 출력 
    print('done')
finally:
    print('clean up')                    #가장 마지막에 실행됨 에러가 있던 없던 마지막에 실행됨

# print("last")

