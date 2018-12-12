import csv
import stringdist
#>pip install stringdist


MIN_DiscordNumber=4
MAX_DiscordRate=0.5
MIN_DiscordRate=0.3

def compareProductCode(MedicineInfoList,name,list , discordRate):
    string_len = len(name)
    if name in list:
        print('제품코드 정확히 일치!')
        print('인덱스 ',list.index(name))
        MedicineInfoList.append(list.index(name))
        return 1, MedicineInfoList
    else:
        for list_item in list:
            value = stringdist.levenshtein(name,list_item)
            #절대값으로 했을경우
            # if MIN_DiscordNumber>value :
            #     MedicineInfoList.append(list_item)
            # 유사도 비율로 했을 경우
            if discordRate > value/string_len:
                MedicineInfoList.append(list.index(list_item))

        if len(MedicineInfoList) ==0 :
            return 0,MedicineInfoList
        else:
            return 2,MedicineInfoList
def compareSimilarity(name, list_name,dicordRate):
    print("내 데이터 ",name)
    print("DB의 데이터 ",list_name)
    string_length = len(name)
    value = stringdist.levenshtein(name, list_name)
    print('오차율 : ',value)
    if dicordRate>= value/string_length:
        return 1
    else:
        return 2

def searchFromDB(productCode,productName,CasNo):
    f = open('medicine_list3.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    productName_list = []
    productCode_list = []
    # companyName_list = []
    casNum_list = []
    for line in rdr:
        productName_list.append(line[0])
        casNum_list.append(line[1])
        # companyName_list.append(line[2])
        productCode_list.append(line[3])
    f.close()
    MedicineInfoList = []
    #print(productCode_list)
    #print(productName_list)

    # 순서 : 제품코드 -> 제품 이름 -> cas NO
    isExist_pCode, indexOfTarget_list = compareProductCode(MedicineInfoList, productCode, productCode_list,
                                                           MIN_DiscordRate)
    if isExist_pCode == 0:
        print('존재 X')
    elif isExist_pCode == 1:
        print("완전 일치")
        correctIdx = None
        isSame = compareSimilarity(productName, productName_list[indexOfTarget_list[0]], MAX_DiscordRate)
        if (isSame == 1):
            print('데이터 확정=============')
        else:
            print('cas 검사 필요')
            isSame_CAS = compareSimilarity(CasNo, casNum_list[indexOfTarget_list[0]], MIN_DiscordRate)
            if isSame_CAS == 1:
                print('데이터 확정(cas에서 확정)=============')

            else:
                print('후보 리스트 보여주기')
                print('후보 1 ) ================')
        print('제품이름  : ', productName_list[indexOfTarget_list[0]])
        print('제품코드  : ', productCode_list[indexOfTarget_list[0]])
        print('CAS NO  : ', casNum_list[indexOfTarget_list[0]])

    else:
        print('부분일치')
        correctIdx = None
        for idx in indexOfTarget_list:
            isSame = compareSimilarity(productName, productName_list[idx], MIN_DiscordRate)
            if (isSame == 1):
                print('데이터 확정=============')
                correctIdx = idx
                break
            else:
                print('cas 검사 필요')
                isSame_CAS = compareSimilarity(CasNo, casNum_list[idx], MIN_DiscordRate)
                if isSame_CAS == 1:
                    print('데이터 확정(cas에서 확정)==========')
                    correctIdx = idx
                    break
                else:
                    print('후보 리스트 보여주기(부분일치에서끝까지)')
        if correctIdx == None:
            no = 1;
            for idx in indexOfTarget_list:
                print('후보 %d ) ================' % no)
                print('제품이름  : ', productName_list[idx])
                print('제품코드  : ', productCode_list[idx])
                print('CAS NO  : ', casNum_list[idx])
                no += 1
        else:
            print('제품이름  : ', productName_list[correctIdx])
            print('제품코드  : ', productCode_list[correctIdx])
            print('CAS NO  : ', casNum_list[correctIdx])


if __name__=='__main__':
    # 전달 할 값
    # companyName = 'Sigma Aldridh'
    productName = 'La Acid'
    CasNo = '21-51-5'
    productCode = 'PHR1215'
    searchFromDB(productCode,productName,CasNo)
