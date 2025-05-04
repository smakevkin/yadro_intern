import requests as r

codes = [200,201, 202, 203, 305, 306] #перечисляемые коды для которых будем проверять сайт, но в скрипте будут проверяться только первые 5 кодов, строка 16

site_url = 'https://httpstat.us'

def req(code): 
    url = f"{site_url}/{code}"
    
    resp = r.get(url)
    status_code = resp.status_code
    
    #тут неуверен что правильно сделал, но в условиях задачи скачано что мы должны выводить статус_код
    #и тело ответа, а exception генерировать только для кодов >=400

    print(f"Статус код для сайта {url} : {status_code}")
    print(f"Тело ответа: {resp.text}")    
    
    if status_code >=400:
        raise Exception

for i in codes[:5]:
    req(i)
    print()#просто для удобство, отделять разные сайты