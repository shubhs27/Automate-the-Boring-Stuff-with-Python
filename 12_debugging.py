import traceback


try:
    raise Exception('This is the Error Message!!')
except:
    errorFile= open('error_log.txt','a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written in error_log.txt')



market= {'ns':'green', 'ew':'red'}
def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is Red! ' + str(intersection)
    # assert- this condition must hold true, for programmer errors not user errors

print(market)
switchLights(market)
print(market)



import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)
# log levels (debug - info - warning - error - critical)

logging.debug('Start of Program')
def factorial(n):
    logging.debug('Start of factorial(%s)' %(n))
    total=1
    for  i in range(1, n+1):
        total*=i
        logging.info('i is %s, total is %s' %(i,total))

    logging.debug('Return value is %s' %(total))
    return total

print(factorial(5))

logging.debug('End of Program')