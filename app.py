from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# {"data":["a","b","1"]}
@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>21BCE9261</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@100..900&display=swap');

        body {
            background: linear-gradient(135deg, #f3ec78, #af4261);
            font-family: "Lexend", sans-serif;
            font-weight: 700;
            color: #ffffff;
        }

        h1 {
            font-size: 3rem;
            color: #f3ec78;
            text-align: center;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }

        form {
            background: rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            margin: 2rem auto;
        }

        textarea {
            width: 100%;
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
            border: 1px solid #ffffff;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.8);
            font-size: 1rem;
            color: #333333;
            margin-bottom: 15px;
        }

        button {
            width: 100%;
            border-radius: 10px;
            padding: 10px;
            border: none;
            background-color: #ff6f61;
            color: white;
            font-size: 1.2rem;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }

        button:hover {
            background-color: #d9534f;
        }

        #response {
            background: rgba(255, 255, 255, 0.1);
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.3);
            max-width: 600px;
            margin: 2rem auto;
        }

        h2 {
            color: #ffde59;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }

        pre {
            background: rgba(0, 0, 0, 0.8);
            color: #ffde59;
            padding: 10px;
            border-radius: 10px;
            white-space: pre-wrap;
            font-size: 1rem;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }

        label {
            display: block;
            font-size: 1.2rem;
            margin-bottom: 10px;
            color: #ffde59;
        }

        input[type="checkbox"] {
            margin-right: 10px;
        }

        .hidden {
            display: none;
        }

        #numbersSection, #alphabetsSection, #highestAlphabetSection, #highestNumberSection {
            margin-top: 10px;
            padding: 10px;
            background-color: rgba(255, 255, 255, 0.2);
            border-radius: 10px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>

<body>
    <div>
        <h1>Assignment</h1>
        <form id="jsonForm">
            <textarea id="jsonInput" rows="6" cols="50"></textarea><br>
            <button type="button" onclick="submitJson()">Submit</button>
        </form>
        <div id="response">
            <h2>Response</h2>
            <pre id="responseData"></pre>
            <div>
                <label><input type="checkbox" id="showNumbers" onclick="toggleSection()"> Numbers</label>
                <label><input type="checkbox" id="showAlphabets" onclick="toggleSection()"> Alphabets</label>
                <label><input type="checkbox" id="showHighestAlphabet" onclick="toggleSection()"> Highest Alphabet</label>
                <label><input type="checkbox" id="showHighestNumber" onclick="toggleSection()"> Highest Number</label>
            </div>
            <div id="numbersSection" class="hidden"></div>
            <div id="alphabetsSection" class="hidden"></div>
            <div id="highestAlphabetSection" class="hidden"></div>
            <div id="highestNumberSection" class="hidden"></div>
        </div>
    </div>
    <script>
        function submitJson() {
            const jsonInput = document.getElementById('jsonInput').value;
            const url = '/bfhl';

            fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: jsonInput
            })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('responseData').textContent = JSON.stringify(data, null, 2);
                    document.getElementById('numbersSection').textContent = `Numbers: ${data.numbers.join(', ')}`;
                    document.getElementById('alphabetsSection').textContent = `Alphabets: ${data.alphabets.join(', ')}`;
                    document.getElementById('highestAlphabetSection').textContent = `Highest Alphabet: ${data.highest_alphabet.join(', ')}`;
                    document.getElementById('highestNumberSection').textContent = `Highest Number: ${data.highest_number.join(', ')}`;
                })
                .catch(error => console.error('Error:', error));
        }

        function toggleSection() {
            document.getElementById('numbersSection').classList.toggle('hidden', !document.getElementById('showNumbers').checked);
            document.getElementById('alphabetsSection').classList.toggle('hidden', !document.getElementById('showAlphabets').checked);
            document.getElementById('highestAlphabetSection').classList.toggle('hidden', !document.getElementById('showHighestAlphabet').checked);
            document.getElementById('highestNumberSection').classList.toggle('hidden', !document.getElementById('showHighestNumber').checked);
        }
    </script>
</body>

</html>
'''

@app.route('/bfhl', methods=['POST'])
def post_bfhl():
    data = request.json.get('data', [])
    numbers = [int(x) for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    # Filter only lowercase alphabets
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    
    # Find the highest lowercase alphabet
    highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []

    response = {
        "is_success": True,
        "user_id": "abhiram_rayidi",
        "email": "abhiram.21bce9261@vitapstudent.ac.in",
        "roll_number": "21BCE9261",
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase_alphabet
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_bfhl():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run()
