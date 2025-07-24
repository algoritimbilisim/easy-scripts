# git-summary

## Description
This script generates a comprehensive CSV report of Git commit history, including statistics about lines added and removed for each commit. It creates a structured summary that can be easily analyzed in spreadsheet applications or data analysis tools.

## Requirements
- Bash
- Git repository (must be run inside a Git repository)
- awk command

## Usage
```bash
bash git_summary.sh
```

## Output
Creates a file named `git_commit_summary.csv` with the following columns:
- **tarih** (date): Commit date in YYYY-MM-DD format
- **commit**: Short commit hash
- **eklenen** (added): Number of lines added in the commit
- **cikartilan** (removed): Number of lines removed in the commit
- **mesaj** (message): Commit message (quoted for CSV compatibility)

## What it does
1. **Data Extraction**: Uses `git log` with `--numstat` to get detailed commit information
2. **Statistics Calculation**: Aggregates added and removed lines for each commit
3. **CSV Formatting**: Formats data as comma-separated values with proper quoting
4. **File Generation**: Creates a ready-to-use CSV file for analysis

## Sample Output
```csv
tarih,commit,eklenen,cikartilan,mesaj
2024-01-15,a1b2c3d,45,12,"Add user authentication feature"
2024-01-14,e4f5g6h,23,8,"Fix database connection issue"
2024-01-13,i7j8k9l,67,34,"Refactor payment processing module"
```

## Use Cases
- **Project Analysis**: Understanding development patterns and productivity
- **Code Review**: Identifying large commits that might need closer inspection
- **Team Metrics**: Analyzing contribution patterns across team members
- **Release Planning**: Understanding the scope of changes between versions
- **Documentation**: Creating development reports and summaries

## Features
- **Comprehensive Data**: Includes both quantitative (lines changed) and qualitative (commit message) information
- **CSV Format**: Easy to import into Excel, Google Sheets, or data analysis tools
- **Proper Escaping**: Handles commit messages with special characters correctly
- **Chronological Order**: Commits are listed from newest to oldest