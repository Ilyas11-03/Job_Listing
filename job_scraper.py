"""
Fake Python Jobs Web Scraper
Scrapes job listings from https://realpython.github.io/fake-jobs/
and saves them to a CSV file.
"""

import csv
import sys

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://realpython.github.io/fake-jobs/"
OUTPUT_FILE = "jobs.csv"
CSV_HEADERS = ["Title", "Company", "Location", "Job URL"]


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetch the page at the given URL and return a BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_jobs(soup: BeautifulSoup) -> list[dict]:
    """Extract job listings from the parsed HTML."""
    jobs = []

    job_cards = soup.select("div.card-content")

    for card in job_cards:
        # --- Job title ---
        title_tag = card.select_one("h2.title")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"

        # --- Company name ---
        company_tag = card.select_one("h3.company")
        company = company_tag.get_text(strip=True) if company_tag else "N/A"

        # --- Location ---
        location_tag = card.select_one("p.location")
        location = location_tag.get_text(strip=True) if location_tag else "N/A"

        # --- Job detail URL ---
        link_tag = card.select_one("a[href]")
        job_url = link_tag["href"] if link_tag else "N/A"

        jobs.append(
            {
                "Title": title,
                "Company": company,
                "Location": location,
                "Job URL": job_url,
            }
        )

    return jobs


def save_to_csv(jobs: list[dict], filename: str) -> None:
    """Write the list of job dicts to a CSV file."""
    if not jobs:
        print("No jobs to save.")
        return

    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_HEADERS)
        writer.writeheader()
        writer.writerows(jobs)

    print(f"Saved {len(jobs)} job(s) to '{filename}'.")


def main() -> None:
    print(f"Fetching jobs from {BASE_URL} ...")
    soup = fetch_page(BASE_URL)

    if soup is None:
        print("Failed to retrieve the page. Exiting.")
        sys.exit(1)

    jobs = parse_jobs(soup)
    print(f"Found {len(jobs)} job listing(s).")

    save_to_csv(jobs, OUTPUT_FILE)

    # Preview first 3 results in the terminal
    print("\n--- Preview (first 3 results) ---")
    for job in jobs[:3]:
        print(
            f"  {job['Title']} @ {job['Company']} | {job['Location']}\n"
            f"  {job['Job URL']}\n"
        )


if __name__ == "__main__":
    main()
