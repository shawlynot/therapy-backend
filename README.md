### Run
`uvicorn therapy_backend.main:app --reload`

### Install
`pip install -r requirements.txt`

### Updating dependencies
1. Add to pyproject.toml
1. `pip-compile --output-file=requirements.txt pyproject.toml`
1. Install
