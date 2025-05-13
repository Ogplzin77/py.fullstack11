from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    html = """
   <!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>

  <title>Academia FitLife</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background: #f2f2f2;
      color: #333;
    }

    header {
      background: #111;
      color: #fff;
      padding: 40px;
      text-align: center;
    }

    nav {
      background: #333;
      display: flex;
      justify-content: center;
      gap: 20px;
      padding: 10px 0;
    }

    nav a {
      color: #fff;
      text-decoration: none;
      font-weight: bold;
    }

    nav a:hover {
      text-decoration: underline;
    }

    .hero {
      background: url('https://images.unsplash.com/photo-1599058917212-df084cc1f708') no-repeat center center/cover;
      color: white;
      padding: 100px 20px;
      text-align: center;
    }

    .hero h1 {
      font-size: 48px;
      margin-bottom: 10px;
    }

    .hero p {
      font-size: 20px;
    }

    .services {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
      padding: 40px 20px;
    }

    .service-card {
      background: white;
      padding: 20px;
      border-radius: 8px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      text-align: center;
    }

    .service-card h3 {
      margin-top: 10px;
    }

    footer {
      background: #111;
      color: white;
      text-align: center;
      padding: 20px;
    }
  </style>
</head>
<body>
  <header>
    <h1>Academia FitLife</h1>
    <p>Transforme seu corpo, transforme sua vida</p>
  </header>

  <nav>
    <a href="#">Início</a>
    <a href="#">Sobre</a>
    <a href="def">Serviços</a>
    <a href="#">Contato</a>
  </nav>

  <section class="hero">
    <h1>Bem-vindo à FitLife</h1>
    <p>Treinos personalizados e estrutura completa para todos os objetivos</p>
  </section>

  <section class="services">
    <div class="service-card">
      <h3>Musculação</h3>
      <p>Equipamentos modernos e acompanhamento profissional.</p>
    </div>
    <div class="service-card">
      <h3>Treino Funcional</h3>
      <p>Melhore sua resistência, força e agilidade com exercícios variados.</p>
    </div>
    <div class="service-card">
      <h3>Aulas Coletivas</h3>
      <p>Zumba, spinning, yoga e muito mais para todos os gostos.</p>
    </div>
    <div class="service-card">
      <h3>Personal Trainer</h3>
      <p>Acompanhamento individualizado para alcançar seus objetivos.</p>
    </div>
  </section>

  <footer>
    <p>&copy; 2025 Academia FitLife. Todos os direitos reservados.</p>
  </footer>
</body>
</html>
    """
    return HttpResponse(html)

# def end
# def home(request):
#     <!DOCTYPE html>
# <html lang="pt-br">
# <head>
#   <meta charset="UTF-8" />
#   <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
#   <title>Academia FitLife</title>
#   <style>
#     body {
#       font-family: Arial, sans-serif;
#       margin: 0;
#       padding: 0;
#       background: #f2f2f2;
#       color: #333;
#     }

#     header {
#       background: #111;
#       color: #fff;
#       padding: 20px;
#       text-align: center;
#     }

#     nav {
#       background: #222;
#       display: flex;
#       justify-content: center;
#       gap: 20px;
#       padding: 10px 0;
#     }

#     nav a {
#       color: #fff;
#       text-decoration: none;
#       font-weight: bold;
#     }

#     nav a:hover {
#       text-decoration: underline;
#     }

#     .hero {
#       background: url('https://images.unsplash.com/photo-1599058917212-df084cc1f708') no-repeat center center/cover;
#       color: white;
#       padding: 100px 20px;
#       text-align: center;
#     }

#     .hero h1 {
#       font-size: 48px;
#       margin-bottom: 10px;
#     }

#     .hero p {
#       font-size: 20px;
#     }

#     .services {
#       display: grid;
#       grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
#       gap: 20px;
#       padding: 40px 20px;
#     }

#     .service-card {
#       background: white;
#       padding: 20px;
#       border-radius: 8px;
#       box-shadow: 0 0 10px rgba(0,0,0,0.1);
#       text-align: center;
#     }

#     .service-card h3 {
#       margin-top: 10px;
#     }

#     footer {
#       background: #111;
#       color: white;
#       text-align: center;
#       padding: 20px;
#     }
#   </style>
# </head>
# <body>
#   <header>
#     <h1>Academia FitLife</h1>
#     <p>Transforme seu corpo, transforme sua vida</p>
#   </header>

#   <nav>
#     <a href="#">Início</a>
#     <a href="#">Sobre</a>
#     <a href="#">Serviços</a>
#     <a href="#">Contato</a>
#   </nav>

#   <section class="hero">
#     <h1>Bem-vindo à FitLife</h1>
#     <p>Treinos personalizados e estrutura completa para todos os objetivos</p>
#   </section>

#   <section class="services">
#     <div class="service-card">
#       <h3>Musculação</h3>
#       <p>Equipamentos modernos e acompanhamento profissional.</p>
#     </div>
#     <div class="service-card">
#       <h3>Treino Funcional</h3>
#       <p>Melhore sua resistência, força e agilidade com exercícios variados.</p>
#     </div>
#     <div class="service-card">
#       <h3>Aulas Coletivas</h3>
#       <p>Zumba, spinning, yoga e muito mais para todos os gostos.</p>
#     </div>
#     <div class="service-card">
#       <h3>Personal Trainer</h3>
#       <p>Acompanhamento individualizado para alcançar seus objetivos.</p>
#     </div>
#   </section>

#   <footer>
#     <p>&copy; 2025 Academia FitLife. Todos os direitos reservados.</p>
#   </footer>
# </body>
# </html>

#     return HttpResponse(html)
