const request = require("request");
const cheerio = require("cheerio");
const iconv = require("iconv-lite");

var url =
  "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=";

request(
  {
    uri: url,
    method: "GET",
    encoding: "binary",
  },
  function (err, resp, body) {
    body = iconv.decode(body, "utf-8");
    const $ = cheerio.load(body);
    console.log($("div.box_line2 table.midsize.big tbody").text());
  }
);
