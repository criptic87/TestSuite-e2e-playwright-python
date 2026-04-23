# UI Test Automation Suite

A professional end-to-end UI automation suite built with `pytest` and `Playwright` against the [Sauce Demo](https://www.saucedemo.com/) application.

This project is designed to validate critical user journeys such as authentication, inventory interactions, and product data checks through a maintainable Page Object Model structure.

## Current Status

The suite is actively under development and should be considered a work in progress. New tests, better coverage, and additional automation best practices are being added continuously as the framework evolves.

At the moment, the latest local execution completed with:

- `19` passing tests
- Chromium browser coverage
- Execution time of approximately `19s`

## Tech Stack

- Python
- Pytest
- Playwright
- Page Object Model (POM)
- GitHub Actions workflow
- Jenkins pipeline placeholder
- Allure result/report folders for test artifacts

## Project Structure

```text
.
|-- conftest.py
|-- pytest.ini
|-- requirements.txt
|-- .github/
|   `-- workflows/
|       `-- test_push&pr.yml
|-- Jenkinsfile
|-- pages/
|   |-- login_page.py
|   `-- inventory_page.py
|-- test-data/
|   |-- users.json
|   `-- product_prices.json
`-- tests/
    |-- test_logins.py
    `-- test_inventory_products.py
```

## Coverage So Far

The current automated checks focus on:

- Successful login flows
- Invalid login validation and error handling
- Required field validation for username and password
- Locked user access restrictions
- Session persistence and logout behavior
- Inventory page access control
- Add-to-cart and remove-from-cart actions
- Product price presence and price verification against test data
- Parameterized product coverage for multiple inventory items

## Framework Highlights

- Reusable page objects for login and inventory screens
- Centralized fixtures in `conftest.py`
- Externalized test data through JSON files
- Failure-focused artifact retention configured in `pytest.ini`
  - Screenshots on failure
  - Videos on failure
  - Traces on failure

## Installation

Create and activate a virtual environment, then install the dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Running The Tests

Run the full suite with:

```powershell
.\.venv\Scripts\python.exe -m pytest
```

Run a specific test module with:

```powershell
.\.venv\Scripts\python.exe -m pytest tests\test_logins.py -v
```

## CI

The repository currently includes a GitHub Actions workflow as the main CI setup. The workflow in `.github/workflows/test_push&pr.yml` runs on:

- Push events to `main`
- Pull requests targeting `main`

It currently performs:

- Source checkout
- Python `3.13` setup
- Dependency installation
- Playwright browser installation
- Test execution

The repository also contains a `Jenkinsfile`, kept as an additional/backup CI option for future use if needed.

## Reporting

The project already contains `allure-results/` and `allure-report/` directories, which makes it ready to support richer test reporting as the framework continues to mature.

## Roadmap

Planned and ongoing improvements include:

- Expanding test coverage across additional user journeys
- Strengthening assertions and negative-path scenarios
- Adding more reusable utilities and best practices
- Improving CI/reporting quality
- Continuing to refine maintainability and readability standards

## Notes

This repository is not a finished framework yet. It is being improved incrementally, with new tests and better automation practices added on a regular basis.
