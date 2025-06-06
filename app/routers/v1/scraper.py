from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.services.github_jobs_scraper import GitHubJobsScraper
from app.dependencies.auth import validate_api_key

router = APIRouter()

class GitHubJobsRequest(BaseModel):
    url: str

@router.post("/scrape/github-jobs")
def scrape_github_jobs(request: GitHubJobsRequest, _: str = Depends(validate_api_key)):
    scraper = GitHubJobsScraper()
    try:
        jobs = scraper.get_jobs(request.url)
        return {"success": True, "data": jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 