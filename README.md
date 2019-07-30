# Word Frequency Extractor

### What is This?
------------------------
 - csv to csv extract word frequency
 - 베트남어 키보드 개발용
 - 베트남 단어 추천을 위한 빅데이터 구축용
 - 베트남 소설 사이트인 [truyenful](http://truyenfull.vn/)에서 크롤링 후 데이터 처리를 위해 제작 (크롤러 미포함 아래 Install List 참고)
# Prerequisites
------------------------

### Install List

 - Python `3.7.1`

 - Scrapy `1.5.2`
 ```
pip install scrapy
```
 - 🔥IMPORTANT🔥 Crawled data must be colleted using [truyenfull_crawler](https://github.com/hatttruong/crawler-webpage/tree/master/truyenfull_crawler) in order to use this program 

## USAGE (사용방법)
 1. Copy crawled .csv files to 'chapter'
 2. run!
 3. result will be saved into WordFrequency Folder

------------------------
# Result
자동 내림차순 정렬

| 단어 | 빈도수 | 
| ------ | ------ | 
| Sở | 86 
| không | 56
| Phiên | 55
| ... | ...
