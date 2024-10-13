from flask import request, render_template, flash, Blueprint, jsonify
from libs.postgres.db import db
from libs.postgres.models import QA
from openai import OpenAI
import os

# Set the OpenAI API key
api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI(api_key = api_key)

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# @bp.route('/ask', methods=['GET', 'POST'])
# def ask_question():
#     """Route for the main page where users can ask questions."""
#     if request.method == 'POST':
#         # Retrieve the question from the form
#         question = request.form.get('question')

#         # Validate the input
#         if not question:
#             flash('Please enter a question.', 'danger')
#             #return redirect(url_for('index'))
#             return render_template('ask.html')

#         try:
#             # Send the question to the OpenAI API
#             stream = client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful assistant."},
#                     {"role": "user", "content": question}
#                 ],
#                 max_tokens=100
#             )


#             # Extract the answer from the response
#             answer = ''
#             for chunk in stream:
#                 if chunk.choices[0].delta.content is not None:
#                     answer += chunk.choices[0].delta.content
                

#             # Save the question and answer to the database
#             qa = QA(question=question, answer=answer)
#             db.session.add(qa)
#             db.session.commit()

#             # Render the template with the question and answer
#             return render_template('ask.html', question=question, answer=answer)

#         except Exception as e:
#             flash(f'Error: {str(e)}', 'danger')
#             #return redirect(url_for('index'))
#             return render_template('ask.html')

#     # Handle GET requests
#     return render_template('ask.html')

@bp.route('/ask', methods=['GET', 'POST'])
def ask_question():
    """Route for the main page where users can ask questions."""
    if request.method == 'POST':
        # Check if the request is JSON
        if request.is_json:
            question = request.json.get('question')
        else:
            question = request.form.get('question')

        # Validate the input
        if not question:
            flash('Please enter a question.', 'danger')
            return render_template('ask.html')

        try:
            # Mocking OpenAI for now
            # Send the question to the OpenAI API (this is mocked in tests)
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                max_tokens=100
            )

            # Extract the answer from the response
            answer = ''
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    answer += chunk.choices[0].delta.content

            # Save the question and answer to the database
            qa = QA(question=question, answer=answer)
            db.session.add(qa)
            db.session.commit()

            # Return JSON if the request was JSON
            if request.is_json:
                print('Request is JSON')
                return jsonify({'question': question, 'answer': answer})
            

            # Render the template with the question and answer
            return render_template('ask.html', question=question, answer=answer)

        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return render_template('ask.html')

    # Handle GET requests
    return render_template('ask.html')