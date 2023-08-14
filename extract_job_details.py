extract_job_details = [
    {
        "name": "extract_job_details",
        "description": "Extract job details from a discord message text.",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "summary": {
                                "type": "string",
                                "description": "Summary of the job description"
                            },
                            "role": {
                                "type": "string",
                                "description": "Role of the job"
                            },
                            "company": {
                                "type": "string",
                                "description": "Company associated with the job"
                            },
                            "additional_info": {
                                "type": "string",
                                "description": "Additional information about the job"
                            },
                            "skills": {
                                "type": "string",
                                "description": "Skills required for the job"
                            },
                        },
                        "required": ["summary"]
                    }
                }
            }
        }
    },
]
