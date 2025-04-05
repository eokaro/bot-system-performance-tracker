import logging
import requests
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.FileHandler("bot_performance.log"), logging.StreamHandler()])

# Simulated Bot Performance Data (No Database)
bot_performance_data = [
    {"bot_id": 1, "time_stamp": "2025-04-10 14:00:00", "speed": 20.5, "error_rate": 2.0, "status": "Active"},
    {"bot_id": 2, "time_stamp": "2025-04-10 14:01:00", "speed": 18.3, "error_rate": 5.2, "status": "Active"},
    {"bot_id": 3, "time_stamp": "2025-04-10 14:02:00", "speed": 22.1, "error_rate": 0.5, "status": "Active"}
]

# Function to analyze bot performance and detect defects
def analyze_bot_performance(bot_data: List[dict]) -> List[Tuple[int, float, float, str]]:
    """
    Analyzes the bot performance data and logs average speed and error rate.
    Detects bots with error rates above the threshold.
    
    Args:
        bot_data (List[dict]): List of dictionaries containing bot performance data.
    
    Returns:
        List[Tuple[int, float, float, str]]: A list containing bot analysis results.
    """
    defective_bots = []

    for bot in bot_data:
        bot_id = bot["bot_id"]
        avg_speed = bot["speed"]
        avg_error_rate = bot["error_rate"]
        status = bot["status"]

        logging.info(f"Bot {bot_id} - Avg Speed: {avg_speed:.2f}, Avg Error Rate: {avg_error_rate:.2f}, Status: {status}")

        # Detect defective bot based on error rate threshold (e.g., 4%)
        if avg_error_rate > 4.0:
            defective_bots.append((bot_id, avg_speed, avg_error_rate, status))

    return defective_bots

# Function to create Jira tickets for defective bots
def create_ticket(issue_summary: str, issue_description: str):
    """
    Creates a Jira ticket for tracking bot performance defects.
    
    Args:
        issue_summary (str): The summary of the issue.
        issue_description (str): The detailed description of the issue.
    """
    url = "https://yourcompany.atlassian.net/rest/api/2/issue"
    headers = {
        "Authorization": "Basic your_encoded_auth_token",
        "Content-Type": "application/json"
    }
    payload = {
        "fields": {
            "project": {"key": "SYMBOTIC"},
            "summary": issue_summary,
            "description": issue_description,
            "issuetype": {"name": "Bug"}
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        logging.info(f"Jira Ticket created successfully: {issue_summary}")
    else:
        logging.error(f"Failed to create Jira ticket: {response.text}")

# Main function to simulate bot system performance analysis
def main():
    """
    Main function to analyze bot performance and create Jira tickets for defects.
    """
    try:
        # Analyze bot performance data
        defective_bots = analyze_bot_performance(bot_performance_data)

        # Identify and create Jira tickets for defective bots
        for bot in defective_bots:
            bot_id, avg_speed, avg_error_rate, status = bot
            issue_summary = f"Bot {bot_id} Performance Issue"
            issue_description = f"Bot {bot_id} has a high error rate ({avg_error_rate*100:.2f}%) exceeding the acceptable threshold."
            create_ticket(issue_summary, issue_description)

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
