# Pytest-BDD_Final
Pytest-bdd

pytest-bdd is a plugin for pytest that lets users write tests as Gherkin feature files rather than test functions. Because it integrates with pytest, it can work with any other pytest plugins, such as pytest-html for pretty reports and pytest-xdist for parallel testing. It also uses pytest fixtures for dependency injection.

Pytest markers:
pytest-bdd uses pytest markers as a storage of the tags for the given scenario test, so we can use standard test selection.
Pytest allows to group tests using markers. pytest.mark decorator is used to mark a test function with custom metadata like @pytest.mark.smoke. This is very handy when we want to run only a subset of tests like "smoke tests" to quickly verify if the changes made by the developer not breaking any major functionalities.


References:
https://pypi.org/project/pytest-bdd/

Installations:
pip install pytest_base_url
pip install pytest-bdd
pip install pytest

Command to run all the tests:
pytest --base-url "https://citiwealthbuilderqa.jemstep.com"  --browsertype chrome

If you want to run specific tests with tags "login", then below is command
pytest --base-url "https://citiwealthbuilderqa.jemstep.com" -k "login" --browsertype chrome
