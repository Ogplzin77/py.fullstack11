from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    html = """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Meu Site Django</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #6e8efb, #a777e3);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                color: white;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.7);
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 1rem;
            }
            p {
                font-size: 1.2rem;
                margin-bottom: 2rem;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #ff6b6b;
                color: white;
                text-decoration: none;
                border-radius: 5px;
                transition: all 0.3s ease;
            }
            .btn:hover {
                background: #ff5252;
                transform: translateY(-3px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌟 Bem-vindo ao Meu Site Django! 🌟</h1>
            <p>Esta é uma página inicial personalizada com HTML + CSS integrado.</p>
            <a href="#" class="btn">Explorar</a>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

