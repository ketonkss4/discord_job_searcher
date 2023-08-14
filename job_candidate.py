from pydantic import BaseModel, Field
from typing import Optional

from extract_candidate_details import extract_candidate_details


class JobCandidate(BaseModel):
    username: Optional[str] = Field(None, description="Username of the candidate")
    position_sought: Optional[str] = Field(None, description="Position the candidate is seeking")
    summary: Optional[str] = Field(None, description="Brief summary or objective from the candidate")
    skills: Optional[str] = Field(None, description="Skills the candidate possesses")
    experience_years: Optional[int] = Field(None, description="Number of years of experience the candidate has")
    education: Optional[str] = Field(None, description="Education background of the candidate")
    linkedin_url: Optional[str] = Field(None, description="URL to the candidate's LinkedIn profile")
    github_url: Optional[str] = Field(None, description="URL to the candidate's GitHub profile")
    contact_email: Optional[str] = Field(None, description="Contact email address of the candidate")
    phone_number: Optional[str] = Field(None, description="Contact phone number for the candidate")
    resume_url: Optional[str] = Field(None, description="URL to the candidate's online resume or LinkedIn profile")
    country: Optional[str] = Field(None, description="Country where the candidate resides")

    @staticmethod
    def get_prompt():
        return '''You are a discord job candidate extraction bot. Given the discord channel messages, you need to 
        identify and extract job candidate details into the list of data items in the JSON schema provided of the 
        extract_candidate_details function. Ensure only job candidate details are extracted. If the text is not about
        a job candidate or is a job posting return an empty JSON like this: {{}}'''

    @staticmethod
    def get_extraction_function():
        return extract_candidate_details
