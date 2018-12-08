#정규식으로 매칭된 객체를 입력으로 사용
def compare_corp_name(match):
    #정규식이 리스트로 반환 하기 때문에 String으로 변경
    match = match[0]
    corp_names = ['SIGMA-ALDRICH', 'DAEJUNG']
    for corp in corp_names:
        if match in corp:
            return corp

    cnt = []
    i = 0
    j = 0
    #회사이름 매치율 측정
    for corp in corp_names:
        i = 0
        j = 0
        cnt_num = 0
        if len(corp) > len(match):
            for _ in range(len(match)):
                if corp[i] == match[j]:
                    i += 1
                    j += 1
                    cnt_num += 1
                else:
                    i += 1
                    continue
            cnt.append(cnt_num)
            
        else:
            for _ in range(len(corp)):
                if corp[i] == match[j]:
                    i +=1
                    j +=1
                    cnt_num += 1
                else:
                    i += 1
                    continue
            cnt.append(cnt_num)
    
    if cnt[0] > cnt[1]:
        return corp_names[0]
    else:
        return corp_names[1]