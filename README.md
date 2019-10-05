# 랩매니저

> 영상인식기술을 통해 시약들의 정보를 관리의 효율을 높여주는 소프트웨어입니다.



[![NPM Version][npm-image]][npm-url]

[![Build Status][travis-image]][travis-url]

[![Downloads Stats][npm-downloads]][npm-url]



‘Lab Manager' 서비스는 현재 모든 화학 약품을 다루는 연구실에서 필요로한 서비스로, 지금까지는 시약제품을 관리할 때 수기로 직접 작성하여 문서화 해오던 것을 모바일 어플리케이션을 통해 효율적으로 관리하도록 도와주는 서비스이다. 시약관련 빅데이터 수집을 통해 수기로 작성했을 때 발생할 수 있는 번거로움과 오류상황을 사전에 차단한다. 



![](../header.png)



## 설치 및 방법


윈도우:



```sh

1. 아나콘다3 64bit 설치 (2018년 12월 기준 4.2.0 버전) 다만 반드시 파이썬 3.7 버전 권장
https://www.anaconda.com/distribution/
![image](https://user-images.githubusercontent.com/25981278/66249865-1883ee00-e775-11e9-97f0-fdcfd283590f.png)
원활한 실행을 위해 아나콘다 설치 시 Advanced Option에 모두 체크
```



```sh

2. 설치 완료 후 Anaconda Navigator를 실행 후 메인 화면에서 Notebook 실행
![image](https://user-images.githubusercontent.com/25981278/66249896-a52eac00-e775-11e9-9edd-152485234f81.png)

```



```sh

3. Text-Recognition 리포지토리를 원하는 경로에 내려받습니다. 그 후, 노트북에서 Test-Recognition-master 디렉터리로 이동합니다.

```



```sh

4. 아나콘다 설치경로나 윈도우 검색기능을 통하여 Anaconda Prompt를 실행시킵니다. 다음 명령어 들을 차례로 입력해주세요.

```

```sh

conda install -c menpo opencv // 이미지 처리를 위한 OpenCV라이브러리 설치

pip install stringdist // 문자열 유사도 측정 알고리즘 사용을 위한 라이브러리 설치

```




```sh

5. 다음은 대망의 광학문자인식을 위한 딥러닝 LSTM기반의 OCR 라이브러리 설치 입니다.

```
[Tesseract 설치링크](https://github.com/UB-Mannheim/tesseract/wiki)

```sh
6. 위 링크에서 Tesseract-ocr-w64-setup-v4.0.0.20181030.exe(2018년 12월 기준) 파일 다운후 설치 옵션에서 additional language 모두 선택하여 설치합니다.
```

```sh
7. 관리자 권한으로 실행된 Anaconda Prompt에서 pip install pytesseract 명령을 입력합니다

```

```sh
8. 이제 실행을 위한 모든 준비를 마쳤습니다. 

```




## 사용 예제



스크린 샷과 코드 예제를 통해 사용 방법을 자세히 설명합니다.



_더 많은 예제와 사용법은 [Wiki][wiki]를 참고하세요._



## 개발 환경 설정



모든 개발 의존성 설치 방법과 자동 테스트 슈트 실행 방법을 운영체제 별로 작성합니다.



```sh

make install

npm test

```



## 정보



이름 – [@트위터 주소](https://twitter.com/dbader_org) – 이메일주소@example.com



XYZ 라이센스를 준수하며 ``LICENSE``에서 자세한 정보를 확인할 수 있습니다.



[https://github.com/yourname/github-link](https://github.com/dbader/)





<!-- Markdown link & img dfn's -->

[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square

[npm-url]: https://npmjs.org/package/datadog-metrics

[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square

[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square

[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics

[wiki]: https://github.com/yourname/yourproject/wiki
