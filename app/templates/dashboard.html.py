<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8" />
    <title>Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" />
</head>
<body>
<nav class="navbar navbar-expand-lg navbar-light bg-light px-4">
    <a class="navbar-brand" href="{% url 'dashboard' %}">Meu Sistema</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
            <li class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Produtos</a>
                <ul class="dropdown-menu">
                    <li><a class="dropdown-item" href="{% url 'produtos_cards' %}">Produtos (Cards)</a></li>
                    <li><a class="dropdown-item" href="{% url 'cadastrar_produto' %}">Cadastrar Produto</a></li>
                    <li><a class="dropdown-item" href="{% url 'listar_produtos' %}">Listar Produtos</a></li>
                </ul>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="{% url 'usuarios' %}">Usuários</a>
            </li>
        </ul>
    </div>
</nav>

<div class="container mt-5">
    <h1 class="mb-4">Dashboard</h1>

    <div class="row">
        <div class="col-md-4">
            <div class="card text-white bg-primary mb-3 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">Usuários</h5>
                    <p class="card-text fs-3">{{ total_usuarios }}</p>
                    <a href="{% url 'usuarios' %}" class="btn btn-light btn-sm">Gerenciar Usuários</a>
                </div>
            </div>
        </div>

        <div class="col-md-4">
            <div class="card text-white bg-success mb-3 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title">Produtos</h5>
                    <p class="card-text fs-3">{{ total_produtos }}</p>
                    <a href="{% url 'listar_produtos' %}" class="btn btn-light btn-sm">Ver Produtos</a>
                </div>
            </div>
        </div>

        <div class="col-md-4 d-flex align-items-center justify-content-center">
            <a href="{% url 'cadastrar_produto' %}" class="btn btn-outline-primary btn-lg w-100">
                Cadastrar Novo Produto
            </a>
        </div>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>

