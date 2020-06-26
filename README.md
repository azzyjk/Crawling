# 크롤링

다음부터는 안에있는 코드이다.
아래는 NodeJS로 크롤링을 해주었다.
```javascript
var express = require("express"); 
const axios = require("axios"); //Url로 GET 요청한 후 데이터를 받아오기 위한 모듈
const cheerio = require("cheerio"); //받아온 데이터를 parsing하기 위한 모듈
const iconv = require("iconv-lite"); //받아온 데이터를 utf-8로 변경해주기 위한 모듈
var router = express.Router();
```
내가 사용할 모듈들을 추가해 주었다.


```javascript
var url = {
  url:
    "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=",
  method: "GET",
  responseType: "arraybuffer",
  responseEncoding: "binary",
};
```
질병 관리본부에서 GET Method를 통해 데이터를 받아올 것이라 저장해 놓았다.
responseType과 responseEncoding은 해당 데이터를 binary로 받아오게 한 담에 iconv-lite로 utf-8로 변경 해줄 것이다.
