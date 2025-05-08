from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(prompt: Prompt):
    text = prompt.prompt.lower()

    if "attendance" in text:
        return {"intent": "get_attendance"}

    elif "assignment" in text and ("pending" in text or "not submitted" in text or "incomplete" in text):
        return {"intent": "get_pending_assignments"}

    elif "fee" in text or "payment" in text or "dues" in text:
        return {"intent": "check_fee_status"}

    elif "student detail" in text or "profile" in text or "my info" in text:
        return {"intent": "get_student_details"}

    elif "timetable" in text and ("today" in text or "classes" in text):
        return {"intent": "get_todays_timetable"}

    elif "message" in text and ("reply" in text or "response" in text):
        return {"intent": "check_teacher_reply"}

    elif "exam" in text:
        if "schedule" in text or "datesheet" in text or "start" in text or "when" in text:
            return {"intent": "get_exam_schedule"}
        elif "result" in text or "marks" in text or "score" in text:
            return {"intent": "get_exam_results"}

    elif "school" in text and ("name" in text or "information" in text):
        return {"intent": "get_school_info"}

    elif "who am i" in text or "logged in" in text or "my account" in text:
        return {"intent": "who_am_i"}
    elif text in ["hello", "hi", "hey"]:
        return {"intent": "greeting"}

    elif text in ["salam", "salaam", "assalamualaikum", "السلام عليكم"]:
        return {"intent": "salam"}

    elif "thank" in text:
        return {"intent": "thanks"}

    elif text in ["ok", "okay"]:
        return {"intent": "acknowledge"}

    elif "bye" in text:
        return {"intent": "goodbye"}
    elif "help" in text or "support" in text:
        return {"intent": "help"}
    elif "nice to meet you" in text:
        return {"intent": "nice_to_meet_you"}
    elif "goodbye" in text or "see you later" in text:
        return {"intent": "goodbye"}

    return {"intent": "unknown"}

