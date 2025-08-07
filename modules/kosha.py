import requests
from bs4 import BeautifulSoup

def search_kosha(keyword: str):
    search_url = f"https://www.kosha.or.kr/kosha/data/boardList.do?searchCondition=TITLE&searchKeyword={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(search_url, headers=headers)

    if res.status_code != 200:
        return [f"검색 실패 (코드 {res.status_code})"]

    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.select(".bbs-title")
    results = [title.text.strip() for title in titles[:5]]
    return results if results else ["검색 결과 없음"]
