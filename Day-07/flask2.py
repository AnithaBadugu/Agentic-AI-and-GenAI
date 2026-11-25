# FLASK - Example 2

from flask import Flask, request, render_template

from google import genai

app=Flask(__name__)
client=genai.Client(api_key="")

@app.route("/", methods=["GET","POST"])
def hi():
    answer=""
    if request.method=="POST":
        question=request.form["questions"]
        
        response=client.models.generate_content(
            model="gemini-3.8-flash",
            contents=question,
        )
        answer=response.text 
    return render_template("f1.html", answer=answer)
if __name__=="__main__":
    app.run(debug=True)

f1.html :
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>GEMINI AI CHATBOT</h1>
    <form method="POST">
        <input name="questions" placeholder="Ask any question" required>
        <button type="submit">Ask Gemini</button>
    </form>
    <h3> Gemini Response</h3>
    <p>{{ answer }}</p>
</body>
</html>
