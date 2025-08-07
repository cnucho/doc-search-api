from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "정부문서 검색 API가 작동 중입니다."}

@app.get("/search")
def search_documents(keyword: str):
    # TODO: Replace this placeholder with actual document crawling or API search
    return {
        "keyword": keyword,
        "results": [
            f"검색 결과 예시 1 for {keyword}",
            f"검색 결과 예시 2 for {keyword}"
        ]
    }
