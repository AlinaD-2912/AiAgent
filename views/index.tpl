<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewpoint" content="width=device-width, initial-scale=1.0">
    <title>AI Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        p {
            color: #666;
            margin-bottom: 30px;
        }
        .chat-container {
            background-color: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        #user-prompt {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        #send-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        #send-btn:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>AI Agent Assistant</h1>
    <p>Your intelligent companion for answers and assistance. Ask anything!</p>

    <div class="chat-container">
        <h2>How Can I Help You Today?</h2>
        <textarea id="user-prompt" rows="4" placeholder="Enter your prompt here..."></textarea>
        <button id="send-btn">Send Prompt</button>
    </div>

    <script>
        document.getElementById('send-btn').addEventListener('click', function() {
            const prompt = document.getElementById('user-prompt').value;
            console.log('Prompt sent:', prompt);
            // You would typically send this to your backend/AI service here
        });
    </script>
</body>
</html>