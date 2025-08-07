# modules/kosha.py
import requests
from bs4 import BeautifulSoup

def search_kosha(keyword: str):
    search_url = f"https://www.kosha.or.kr/kosha/data/boardList.do?searchCondition=TITLE&searchKeyword={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(search_url, headers=headers)

    if res.status_code != 200:
        return [f"검색 실패 (코드 {res.status_code})"]

    soup = BeautifulSoup(res.text, "html.parser")
    titles = soup.select(".bbs-title")  # 실제 구조에 맞게 수정 필요
    results = [title.text.strip() for title in titles[:5]]  # 상위 5개 문서 제목

    return results if results else ["검색 결과 없음"]
