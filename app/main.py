from fastapi import FastAPI

app = FastAPI(title="Hey i want to build a python file with fibonnaci code in it")


@app.get("/health")
def health():
    return {"status": "ok", "service": "hey-i-want-to-build-a-python-file-with-fibonnaci"}


@app.get("/")
def root():
    return {
        "title": "Hey i want to build a python file with fibonnaci code in it",
        "summary": "Approved-build plan for test: hey i want to build a python file with fibonnaci code in it.",
        "requirements": ["Deliver requested scope: hey i want to build a python file with fibonnaci code in it","Write the approved build into the bound local folder","Generate .brain graph and distribute workspace intelligence"],
    }
