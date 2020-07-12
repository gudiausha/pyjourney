import requests
import math

def slam(statusQuery,parentId):
    params={"status":statusQuery}
    resp = requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?',params=params).json()
    total = resp["total_pages"]
    total_rotor = 0
    rotor_list=0
    for i in range(1,total+1):
        params={"status":statusQuery,"page":i}
        resp=requests.get('https://jsonmock.hackerrank.com/api/iot_devices/search?',params=params).json()
        # print('page:',i)
        # print(resp["data"]["parent"])
        for j in resp["data"]:
            if 'parent' in j and j['parent']!= None and j['parent']['id']==parentId:
                # rotor_list.append(j['operatingParams']['rotorSpeed'])
                rotor_list+=j['operatingParams']['rotorSpeed']
                total_rotor+=1

    print('rotor count:',total_rotor)
    print('rotor speed list:',rotor_list)
    print('Avg rotor speed:',math.floor(rotor_list/total_rotor))

                # print('yes',j['parent']['id'])
            # else:
            #     print('none')
        # print(resp["data"]["asset"])
        # print(type(resp["data"]))


slam("RUNNING",7)

#print(total)
