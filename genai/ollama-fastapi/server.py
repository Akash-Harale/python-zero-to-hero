from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def read_root():
    return {"message":"Welcome to the Chatbot API"}

@app.get("/contact-us")
def contact_us():
    return {"email":"akash.v.harale@gmail.com"}