# 랩매니저

> 영상인식기술을 통해 시약들의 정보를 관리의 효율을 높여주는 소프트웨어입니다.

‘Lab Manager' 서비스는 현재 모든 화학 약품을 다루는 연구실에서 필요로한 서비스로, 지금까지는 시약제품을 관리할 때 수기로 직접 작성하여 문서화 해오던 것을 모바일 어플리케이션을 통해 효율적으로 관리하도록 도와주는 서비스이다. 시약관련 빅데이터 수집을 통해 수기로 작성했을 때 발생할 수 있는 번거로움과 오류상황을 사전에 차단한다. 


![](https://user-images.githubusercontent.com/25981278/66251852-8fc67b80-e78f-11e9-83ff-b51df0828cc7.PNG)



## 설치 및 방법


윈도우:



1. 아나콘다3 64bit를 설치합니다. (2018년 12월 기준 4.2.0 버전) 다만 반드시 파이썬 3.7 버전 권장드립니다.

[아나콘다 설치 링크](https://www.anaconda.com/distribution/)

원활한 실행을 위해 아나콘다 설치 시 Advanced Option에 모두 체크합니다.
<img src="https://user-images.githubusercontent.com/25981278/66249865-1883ee00-e775-11e9-97f0-fdcfd283590f.png" width="50%"></img>


2. 설치 완료 후, 아나콘다 설치경로나 윈도우 검색기능을 통하여 Anaconda Prompt를 **관리자권한**으로 실행시킵니다. <br>다음 명령어 들을 차례로 입력해주세요.

<img src="https://user-images.githubusercontent.com/25981278/66249950-87ae1200-e776-11e9-909d-aef3aef050eb.png" width="50%"></img>

```sh

conda install -c menpo opencv // 이미지 처리를 위한 OpenCV라이브러리 설치

pip install stringdist // 문자열 유사도 측정 알고리즘 사용을 위한 라이브러리 설치

```

3. 다음은 대망의 광학문자인식을 위한 딥러닝 LSTM기반의 OCR 라이브러리 설치 입니다.

<img src="https://user-images.githubusercontent.com/25981278/66250770-d2815700-e781-11e9-8417-c69358c6ee77.png" width="50%"></img>

[Tesseract 설치링크](https://github.com/UB-Mannheim/tesseract/wiki)

4. 위 링크에서 Tesseract-ocr-w64-setup-v4.0.0.20181030.exe(2018년 12월 기준) 파일 다운후<br>설치 옵션에서 additional language 모두 선택하여 설치합니다.

5. 설치후, 파이썬과 Tesseract 연동을 위해 Pytesseract를 설치합니다.<br>***관리자권한***으로 실행된 Anaconda Prompt에서 다음 명령어를 입력해주세요
```sh

pip install pytesseract

```

6. 이제 실행을 위한 모든 준비를 마쳤습니다. 다음 사용 예제를 참고해주세요.


## 사용 예제


Anaconda Navigator를 실행 후 메인 화면에서 Notebook 실행합니다

<img src="https://user-images.githubusercontent.com/25981278/66249896-a52eac00-e775-11e9-9edd-152485234f81.png" width="50%"></img>

Text-Recognition 리포지토리를 원하는 경로에 내려받습니다. 그 후, 노트북에서 Test-Recognition-master 디렉터리로 이동합니다.

<img src="https://user-images.githubusercontent.com/25981278/66251642-61e03780-e78d-11e9-9eb1-4d8bc9aef595.png" width="50%"></img>
<br>
test.ipynb 파일을 실행합니다.
<br>
<img src="https://user-images.githubusercontent.com/25981278/66251782-c223a900-e78e-11e9-8e2c-79659e5df29a.png" width="50%"></img>
<br>
이미지 전처리 과정과 함께 위와 같이 뜬다면 성공입니다.

## 이미지 처리 과정 참고

<img src="https://user-images.githubusercontent.com/25981278/66192373-457bc680-e6cb-11e9-9221-46c128679a82.png" width="50%"></img>

## 프로그램 구조 참고

<img src="https://user-images.githubusercontent.com/25981278/66192375-457bc680-e6cb-11e9-98b6-f2c47c78010a.png" width="50%"></img>

## 정보



이준의  – wnsspdl@naver.com



<!-- Markdown link & img dfn's -->

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square

[npm-url]: https://npmjs.org/package/datadog-metrics

[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square

[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square

[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics

[wiki]: https://github.com/yourname/yourproject/wiki
