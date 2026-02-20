# 🕷️ Job Scraper

A beginner-friendly Python web scraper that extracts job listings from [Fake Python Jobs](https://realpython.github.io/fake-jobs/) and presents them through a clean, interactive HTML interface. Built with `requests`, `BeautifulSoup`, and vanilla HTML/CSS/JS.

---

## 📸 Preview

```
┌─────────────────────────────────────────────────────────┐
│  Job Scraper                          ● Ready to scrape  │
├──────────────┬──────────────────────────────────────────┤
│  Target URL  │  [ Senior Python Developer ]              │
│  ──────────  │  Payne, Roberts and Davis                 │
│  Filter      │  📍 Stewartbury, AA          [ View → ]   │
│  ──────────  │                                           │
│  Stats       │  [ Energy Engineer          ]             │
│  ──────────  │  Vasquez-Davidson                         │
│  Export CSV  │  📍 Christopherville, AA     [ View → ]   │
└──────────────┴──────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
job-scraper/
├── job_scraper.py   # Python scraper — fetches, parses, and exports jobs
├── index.html       # Interactive HTML interface to visualize results
└── README.md        # You are here
```

---

## ⚙️ Requirements

- Python 3.8+
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:

```bash
pip install requests beautifulsoup4
```

---

## 🚀 Usage

### Run the scraper

```bash
python job_scraper.py
```

This will:
1. Fetch the job listings page
2. Parse each job card for title, company, location, and URL
3. Save all results to **`jobs.csv`** in the current directory
4. Print a preview of the first 3 results in the terminal

**Sample terminal output:**

```
Fetching jobs from https://realpython.github.io/fake-jobs/ ...
Found 100 job listing(s).
Saved 100 job(s) to 'jobs.csv'.

--- Preview (first 3 results) ---
  Senior Python Developer @ Payne, Roberts and Davis | Stewartbury, AA
  https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html

  Energy Engineer @ Vasquez-Davidson | Christopherville, AA
  https://realpython.github.io/fake-jobs/jobs/energy-engineer-1.html

  Legal Executive @ Jackson, Chambers and Levy | Port Ericaburgh, AA
  https://realpython.github.io/fake-jobs/jobs/legal-executive-2.html
```

### Open the HTML interface

Simply open `index.html` in your browser:

```bash
open index.html        # macOS
start index.html       # Windows
xdg-open index.html    # Linux
```

Then enter the target URL in the sidebar and click **Scrape**.

---

## 📄 CSV Output

The scraper writes a `jobs.csv` file with the following columns:

| Column   | Description                          | Example                                  |
|----------|--------------------------------------|------------------------------------------|
| Title    | Job title                            | Senior Python Developer                  |
| Company  | Hiring company name                  | Payne, Roberts and Davis                 |
| Location | City and region                      | Stewartbury, AA                          |
| Job URL  | Link to the full job detail page     | https://realpython.github.io/fake-jobs/… |

---

## 🧠 How It Works

```
  URL
   │
   ▼
requests.get()          ← Fetches raw HTML from the target URL
   │
   ▼
BeautifulSoup()         ← Parses the HTML into a navigable tree
   │
   ▼
soup.select("div.card-content")   ← Finds all job cards on the page
   │
   ▼
Extract fields          ← title · company · location · url
   │
   ▼
csv.DictWriter()        ← Writes structured rows to jobs.csv
```

Each job card on the page follows a predictable HTML pattern:

```html
<div class="card-content">
  <h2 class="title">Senior Python Developer</h2>
  <h3 class="company">Payne, Roberts and Davis</h3>
  <p class="location">Stewartbury, AA</p>
  <a href="https://…">Apply</a>
</div>
```

The scraper targets these CSS classes to reliably extract data from every card.

---

## 🌐 HTML Interface Features

| Feature | Description |
|---|---|
| **Scrape button** | Fetches and renders job cards instantly |
| **Live filter** | Search by title, company, or location in real time |
| **Grid / List view** | Toggle between card grid and compact list layout |
| **Stats panel** | Shows total jobs found, currently shown, and source domain |
| **Export CSV** | Download results as a `.csv` file directly from the browser |

---

## 🔧 Edge Cases Handled

- **Missing fields** — any field not found in the HTML defaults to `"N/A"` instead of crashing
- **Network errors** — HTTP failures and timeouts are caught and reported cleanly
- **Empty results** — the interface displays a friendly empty state if no jobs are found
- **CSV quoting** — commas inside company names or locations are safely quoted by `csv.DictWriter`

---

## 🔄 Alternative Practice URLs

You can point this scraper at other beginner-friendly sites:

| Site | URL | Fields |
|---|---|---|
| Books to Scrape | `http://books.toscrape.com` | title, price, rating |
| Quotes to Scrape | `http://quotes.toscrape.com` | text, author, tags |
| Scrape This Site | `https://www.scrapethissite.com/pages/simple/` | country, population, area |

---

## 📚 What You'll Learn

- Inspecting HTML structure with browser DevTools
- Fetching web pages with the `requests` library
- Navigating and selecting HTML elements with `BeautifulSoup`
- Exporting structured data to CSV with the `csv` module
- Handling missing data and network errors gracefully
- Building a frontend interface with HTML, CSS, and JavaScript

---

## 📜 License

This project is intended for educational purposes. The target site [realpython.github.io/fake-jobs](https://realpython.github.io/fake-jobs/) is provided by Real Python specifically for scraping practice.

---

> Made for learning. Built with Python 🐍
