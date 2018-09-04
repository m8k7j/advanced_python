def bank_avaliable():
    number = 100
    while True:
        if number < 0:
            break
        else:
            catch = yield number
            number -= catch


        
re = bank_avaliable()
print(next(re))
print(re.send(10))
print(re.send(30))


