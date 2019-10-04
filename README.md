# 대학 연구소 시약 관리 효율화 프로그램
</hr>

OpenCV와 OCR 라이브러리, 문자열 유사도 측정 알고리즘을 활용하여 시약 관리를 효율적으로 하게 해주는 프로그램입니다.
<br><br><br>

## OpenCV를 이용한 이미지 처리
</hr>
gray함수는 윤곽선을 찾기 전에 8bits의 회색조 이미지로 변경합니다
gradient함수는 opencv의 Morphological Transformation를 이용하여 dilation 과 erosion의 차이를 계산합니다. 문자의 외곽선을 추출 할 수 있습니다.
binarization함수는 adaptiveThreshold를 적용하여 8bits 이미지는 2bits이미지로 변경합니다. 주로 block_size와 minus값을 변경할 필요가 있습니다.
closing함수는 dilation적용후 closing을 적용합니다. 문자의 테두리를 강조합니다.
find_contours함수는 강조된 문자의 외곽을 검출합니다.
segmentaion함수는   검출된 문자의 외곽을 바탕으로 OCR처리를 위해 문자를 자릅니다.
그 외 기타 테스트를 위한 함수들이 있습니다.

![그림1](https://user-images.githubusercontent.com/25981278/66192373-457bc680-e6cb-11e9-9221-46c128679a82.png)

<br><br><br>
## Pytesseract로 광학문자인식
</hr>
분리된 이미지를 OCR로 처리하는 모듈입니다.
Read_file() 또는   read_image_list() -> ocr() 순서로 실행됩니다.
이미지를 읽는 부분을 두 함수로 나눈이유는 분석하기 위해 이미지를 따로 저장했기 때문에 파일로 된 이미지를 읽는 함수가 있습니다.
OCR로 추출해낸   문자열들 중에서 시약명, 시약회사, 제품코드, CAS number를 정규식을 통해 추출합니다.
시약회사별로 제품코드, 제품명, CAS   number가 다르게 위치해있기에 회사별로 정규식이 있습니다.
정규식 처리를 보정하는 모듈입니다. 현재는 회사 이름 보정 기능만 구현되어 있습니다.
<br><br><br>
## 문자열 유사도 측정 알고리즘을 통한 오류 보정

## 동작예시 

