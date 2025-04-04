# Bot System Performance Tracker

## Project Overview

This Python-based project tracks and analyzes the performance of robotic systems used in automation environments like Symbotic’s warehouse systems. The tool collects bot performance data, processes it to calculate key performance indicators (KPIs), logs the results, and tracks defects or performance issues. It also integrates with Jira for defect tracking and resolution.

## Features

- **Bot Performance Tracking**: Tracks bot performance data (speed, error rate, status) over time.
- **Automated Defect Tracking**: If bots have performance issues (e.g., high error rates), automated Jira tickets are created.
- **Database Integration**: Stores bot performance data using SQLite for easy analysis and tracking.
- **Logging**: Logs all actions and errors for traceability and debugging.

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bot-system-performance-tracker.git
