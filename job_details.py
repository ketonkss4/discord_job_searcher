from pydantic import BaseModel, Field
from typing import Optional

from extract_job_details import extract_job_details


class JobDetails(BaseModel):
    summary: Optional[str] = Field(None, description="Summary of the job description")
    role: Optional[str] = Field(None, description="Role of the job")
    company: Optional[str] = Field(None, description="Company associated with the job")
    additional_info: Optional[str] = Field(None, description="Additional information about the job")
    skills: Optional[str] = Field(None, description="Skills required for the job")
    instructions: Optional[str] = Field(None, description="Instructions for applying to the job")
    email: Optional[str] = Field(None, description="Contact email address for the job")
    website: Optional[str] = Field(None, description="Contact website for the job")

    @staticmethod
    def get_prompt():
        return '''You are a discord job extraction bot. Given the discord channel messages, you need to 
             identify and extract job details into the list of data items in the JSON schema provided of the 
             extract_job_details function. If the text is not about a job or is a person looking for a job return an
             empty JSON like this: {{}}'''

    @staticmethod
    def get_extraction_function():
        return extract_job_details
