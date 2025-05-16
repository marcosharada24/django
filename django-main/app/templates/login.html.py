<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <div class="card shadow rounded-4">
                <div class="card-body p-4">
                    <h3 class="card-title mb-4 text-center">Entrar no Sistema</h3>
                    
                    {% if mensagem %}
                        <div class="alert alert-danger">
                            {{ mensagem }}
                        </div>
                    {% endif %}

                    <form method="post">
                        {% csrf_token %}

                        <div class="mb-3">
                            <label for="email" class="form-label">E-mail</label>
                            <input type="email" name="email" class="form-control" id="email" required>
                        </div>

                        <div class="mb-3">
                            <label for="senha" class="form-label">Senha</label>
                            <input type="password" name="senha" class="form-control" id="senha" required>
                        </div>

                        <button type="submit" class="btn btn-primary w-100">Entrar</button>
                    </form>

                    <p class="mt-3 text-center">
                        Não tem cadastro?
                        <a href="{% url 'cadastro' %}">Cadastre-se</a>
                    </p>
                </div>
            </div>
        </div>
    </div>
</div>
</body>
</html>

