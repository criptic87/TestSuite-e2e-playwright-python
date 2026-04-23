# UI Test Automation Suite

[![Playwright Tests](https://github.com/criptic87/TestSuite-e2e-playwright-python/actions/workflows/test_push&pr.yml/badge.svg)](https://github.com/criptic87/TestSuite-e2e-playwright-python/actions/workflows/test_push&pr.yml)

A professional end-to-end UI automation suite built with `pytest` and `Playwright` against the [Sauce Demo](https://www.saucedemo.com/) application.

This project validates critical user journeys — authentication, inventory interactions, product data integrity, and sorting behaviour — through a maintainable Page Object Model structure with externalized test data and CI integration.

---

## Current Status

The suite is actively under development. New tests, broader coverage, and additional automation best practices are being added continuously.

Latest local execution:

- **22** passing tests
- Chromium browser coverage
- Execution time approximately **22s**

---

## Tech Stack

- Python 3.13
- pytest
- Playwright
- Page Object Model (POM)
- GitHub Actions (primary CI)
- Jenkins (pipeline placeholder)
- Allure (reporting-ready)

---

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

---

## Coverage

**Authentication**
- Successful login with valid credentials
- Invalid credentials error handling and message validation
- Required field validation (missing username, missing password)
- Locked-out user access restriction
- Session persistence after page refresh
- Logout and post-logout access control
- Redirect to login when accessing protected routes unauthenticated
- Close error message and retry login flow

**Inventory**
- Inventory page load verification
- Add to cart — single and multiple items
- Parametrized add-to-cart across all six products
- Remove from cart and badge count reset
- Product price presence validation for all items
- Product price accuracy verified against external test data
- Product sorting by name A-Z and Z-A (parametrized)
- Product sorting by price low-to-high and high-to-low (parametrized)

---

## Key Design Decisions

**Page Object Model** — selectors and actions live in page classes, not in tests. When a selector changes, one line updates in the page object and all tests that use it stay green.

**Fixture hierarchy** — `login_page` → `logged_in_inventory` → `inventory_with_item` build on each other. Tests request only the state they need, with no repeated setup code.

**Externalized test data** — credentials and product data live in JSON files, not hardcoded in tests. Data can change without touching test logic.

**Auto-waiting over hard waits** — `expect()` assertions and Playwright actions wait automatically. No `time.sleep()` anywhere in the suite.

**Parametrized tests for variation** — sorting direction and product selection use `@pytest.mark.parametrize` to cover multiple scenarios from a single test definition, keeping the suite DRY and output readable.

**Failure artifacts** — screenshots, videos, and Playwright traces are captured automatically on failure, making CI failures diagnosable without reproducing locally.

---

## Installation

**Linux / macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

---

## Running The Tests

```bash
# Run the full suite
pytest

# Run with visible browser
pytest --headed

# Run a specific file
pytest tests/test_logins.py -v

# Run a specific test
pytest tests/test_logins.py::test_session_persists_on_refresh -v
```

---

## Framework Highlights

- Reusable page objects for login and inventory screens
- Centralized fixtures in `conftest.py` with clear state hierarchy
- Externalized test data through JSON files for users and products
- Failure-focused artifact retention configured in `pytest.ini`
  - Screenshots on failure
  - Videos on failure
  - Playwright traces on failure

---

## CI

The GitHub Actions workflow at `.github/workflows/test_push&pr.yml` triggers on:

- Push events to `main`
- Pull requests targeting `main`

Each run performs:

- Source checkout
- Python 3.13 setup
- Dependency installation via `requirements.txt`
- Playwright Chromium browser installation
- Full test suite execution

The repository also includes a `Jenkinsfile` as an alternative CI option for Jenkins-based pipelines.

---

## Reporting

The project is Allure-ready. The `allure-results/` and `allure-report/` directories are in place to support richer HTML reporting as the framework matures.

To generate and open an Allure report locally (requires Allure CLI):

```bash
allure serve allure-results
```

---

## Roadmap

- Cart page and checkout flow coverage
- End-to-end test: login → add items → checkout → confirm
- Problem user behaviour validation (broken images, non-functional buttons)
- Performance glitch user timeout handling
- Cross-browser execution (Firefox, WebKit)
- Allure report integration in CI pipeline
- Expanded negative-path and edge case scenarios

---

## Notes

This repository is being built incrementally as a portfolio project and learning exercise. It is not a finished framework — new tests and improvements are added on a regular basis.
