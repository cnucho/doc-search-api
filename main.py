from fastapi import FastAPI, Query
from modules.kosha import search_kosha

app = FastAPI()

@app.get("/")
def home():
    return {"message": "정부문서 통합 검색 API"}

@app.get("/search")
def search_documents(keyword: str, source: str = Query("kosha")):
    if source == "kosha":
        results = search_kosha(keyword)
    else:
        results = ["지원하지 않는 기관입니다."]
    return {"keyword": keyword, "source": source, "results": results}
