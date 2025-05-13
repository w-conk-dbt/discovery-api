import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API token from environment variable
headers = {'Authorization': f'Bearer {os.getenv("DBT_API_TOKEN")}'}

graphql_query = """
query ($jobId: BigInt!, $runId: BigInt!) {
  job(id: $jobId, runId: $runId) {
    models {
      name
      status
      tests {
        name
        status
      }
    }
  }
}
"""

json_data = {
    'query': graphql_query,
    'variables': {
        'jobId': int(os.getenv("DBT_JOB_ID")),
        'runId': int(os.getenv("DBT_RUN_ID"))
    }
}

response = requests.post('https://metadata.cloud.getdbt.com/graphql', 
                        headers=headers, 
                        json=json_data)
print(response.json())
