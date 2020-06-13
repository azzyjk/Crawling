const request = require("request");
const cheerio = require("cheerio");
const iconv = require("iconv-lite");

var url = "https://news.naver.com/";

request(
  {
    uri: url,
    method: "GET",
    encoding: "binary",
  },
  function (err, resp, body) {
    body = iconv.decode(body, "euc-kr");
    const $ = cheerio.load(body);
    console.log($("div").text());
  }
);
