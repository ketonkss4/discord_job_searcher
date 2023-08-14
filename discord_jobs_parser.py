import os
from typing import List, Type

import streamlit as st
import requests
import asyncio
import json
import csv

from pydantic import BaseModel

from job_candidate import JobCandidate
from job_details import JobDetails
from llm_response import LLMResponse
from openai_processor import OpenAIProcessor
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def extract_job_details(response: LLMResponse) -> List[JobDetails]:
    print(response.text)
    parsed_data = json.loads(response.text)
    return [JobDetails(**detail) for detail in parsed_data["data"]]


def extract_job_candidates(response: LLMResponse) -> List[JobCandidate]:
    parsed_data = json.loads(response.text)
    return [JobCandidate(**detail) for detail in parsed_data["data"]]


async def main(data: List[dict], model: Type[BaseModel], prompt, extraction_function):
    llm_processor = OpenAIProcessor()
    tasks = [llm_processor.agenerate_details(data[i:i + 3], prompt, extraction_function) for i in
             range(0, len(data), 3)]
    llm_responses = await asyncio.gather(*tasks)

    # Default values (can be set to None or some default file name)
    csv_filename = None
    csv_headers = []
    csv_data = []

    if model == JobDetails:
        details_list = [detail for resp in llm_responses for detail in extract_job_details(resp)]
        csv_filename = 'langchain_jobs.csv'
        csv_headers = ['username', 'summary', 'date_posted', 'role', 'company', 'additional_info',
                       'skills', 'instructions', 'email', 'website']
        csv_data = [
            [
                item['author']['username'],
                details.summary,
                item['timestamp'],
                details.role,
                details.company,
                details.additional_info,
                details.skills,
                details.instructions,
                details.email,
                details.website
            ]
            for item, details in zip(data, details_list)
        ]
    elif model == JobCandidate:
        details_list = [detail for resp in llm_responses for detail in extract_job_candidates(resp)]
        csv_filename = 'langchain_candidates.csv'
        csv_headers = ['username', 'position_sought', 'summary', 'skills', 'experience_years',
                       'education', 'linkedin_url', 'github_url', 'contact_email', 'phone_number', 'resume_url',
                       'country']
        csv_data = [
            [
                details.username,
                details.position_sought,
                details.summary,
                details.skills,
                details.experience_years,
                details.education,
                details.linkedin_url,
                details.github_url,
                details.contact_email,
                details.phone_number,
                details.resume_url,
                details.country
            ]
            for details in details_list
        ]

    if csv_filename:
        # Write to the appropriate CSV
        with open(csv_filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(csv_headers)
            writer.writerows(csv_data)
    else:
        raise ValueError("Unexpected model type provided.")


# Streamlit UI
def run_app():
    st.title("Discord Channel Data Fetcher")

    channel_id = st.text_input("Enter the Channel ID:")
    selected_model = st.radio("Select Model", ["Job Details", "Job Candidates"])
    discord_token = os.getenv('DISCORD_TOKEN')
    if channel_id:
        if st.button(f"Fetch and Process {selected_model}"):
            token = discord_token  # Replace with your token
            url = f"https://discord.com/api/v8/channels/{channel_id}/messages?limit=100"
            headers = {"Authorization": f"{token}"}

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                model = JobDetails if selected_model == "Job Details" else JobCandidate
                asyncio.run(main(data, model, model.get_prompt(), model.get_extraction_function()))
                st.write(f"Data processed and saved to csv!")
            else:
                st.write(f"Error {response.status_code}: {response.text}")


if __name__ == "__main__":
    run_app()
