from django.db import models


class CaCursos(models.Model):
    idCaCursos = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=200, null=False)
    image = models.ImageField(upload_to='image/categorias',null=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    idFuncionario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=200, null=False)
    telefone = models.CharField(max_length=11, null=False)
    cargo = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nome + " - " + self.cargo

class Curso(models.Model):
    idCurso = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100, null=False)
    image = models.ImageField(upload_to='image/curso', null=True)
    descricao = models.CharField(max_length=300, null=False)
    dataInicio = models.DateField(null=False)
    dataFim = models.DateField(null=False)
    hora_inicio = models.TimeField(null=False)
    hora_final = models.TimeField(null=False)
    dias = models.CharField(max_length=100,null=False)
    valor_cur = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    fk_idCaCursos = models.ForeignKey(CaCursos, on_delete=models.CASCADE)
    fk_idFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " - " + self.descricao


class MetodoPagamento(models.Model):
    idMetodoPagamento = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100, null=False)

    def __str__(self):
      return self.tipo

    
class Pedido(models.Model):
    idPedido = models.BigAutoField(primary_key=True)
    fk_idCaCursos = models.ForeignKey(CaCursos, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    fk_idUsuario = models.ForeignKey('users.Usuario', on_delete=models.CASCADE)
    fk_idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fk_idMetodoPagamento = models.ForeignKey(MetodoPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.data.strftime("%Y/%m/##%d")