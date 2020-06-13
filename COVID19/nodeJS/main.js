const axios = require("axios");
const cheerio = require("cheerio");
const iconv = require("iconv-lite");

var url = {
  url:
    "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=",
  method: "GET",
  responseType: "arraybuffer",
  responseEncoding: "binary",
};

const getHtml = async () => {
  try {
    const response = await axios(url);
    const html = iconv.decode(response.data, "utf-8").toString();
    return html;
  } catch (error) {
    console.error(error);
  }
};

getHtml().then((html) => {
  const $ = cheerio.load(html);
  const $text = $("div.box_line2 table.midsize.big tbody").text();
  console.log($text);
});
