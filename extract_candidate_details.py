extract_candidate_details = [{
    "name": "extract_candidate_details",
    "description": "Extract candidate details from a message text.",
    "parameters": {
        "type": "object",
        "properties": {
            "data": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "username": {
                            "type": "string",
                            "description": "Username of the candidate"
                        },
                        "position_sought": {
                            "type": "string",
                            "description": "Position the candidate is seeking"
                        },
                        "summary": {
                            "type": "string",
                            "description": "Brief summary or objective from the candidate"
                        },
                        "skills": {
                            "type": "string",
                            "description": "Skills the candidate possesses"
                        },
                        "experience_years": {
                            "type": "integer",
                            "description": "Number of years of experience the candidate has"
                        },
                        "education": {
                            "type": "string",
                            "description": "Education background of the candidate"
                        },
                        "linkedin_url": {
                            "type": "string",
                            "description": "URL to the candidate's LinkedIn profile"
                        },
                        "github_url": {
                            "type": "string",
                            "description": "URL to the candidate's GitHub profile"
                        },
                        "contact_email": {
                            "type": "string",
                            "description": "Contact email address of the candidate"
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "Contact phone number for the candidate"
                        },
                        "resume_url": {
                            "type": "string",
                            "description": "URL to the candidate's online resume or LinkedIn profile"
                        },
                        "country": {
                            "type": "string",
                            "description": "Country where the candidate resides"
                        }
                    }
                }
            }
        }
    }
}]
