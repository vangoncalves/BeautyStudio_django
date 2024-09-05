from django.db import models

class Usuario(models.Model):
    idUsuario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=300, null=False)
    telefone = models.CharField(max_length=11, null=True)
    email = models.EmailField(max_length=300, null=False)
    username = models.CharField('username', max_length=11, null=True)

    def __str__(self):
        return self.email + " - " + self.nome

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
    valor_cur = models.FloatField(null=False)
    fk_idCaCursos = models.ForeignKey(CaCursos, on_delete=models.CASCADE)
    fk_idFuncionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome + " - " + self.descricao


class MetodoPagamento(models.Model):
    idMetodoPagamento = models.BigAutoField(primary_key=True)
    tipo = models.CharField(max_length=100, null=False)

    def __str__(self):
      return self.tipo

class Agendamento(models.Model):
    idAgendamento = models.BigAutoField(primary_key=True)
    fk_idCaCursos = models.ForeignKey(CaCursos, on_delete=models.CASCADE)
    fk_idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fk_idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fk_idMetodoPagamento = models.ForeignKey(MetodoPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.data.strftime("%Y/%m/##%d") + " - " + self.hora.srtftime("%H:%M:%S")

class NotaFiscal(models.Model):
    idNotaFiscal = models.BigAutoField(primary_key=True)
    valor = models.CharField(max_length=100, null=False)
    dataEmissao = models.DateTimeField(auto_now_add=True, null=False)
    fk_idMetodoPagamento = models.ForeignKey(MetodoPagamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.valor + " - " + self.dataEmissao

class Comprovante(models.Model):
    idComprovante = models.BigAutoField(primary_key=True)
    fk_idNotaFiscal = models.ForeignKey(NotaFiscal, on_delete=models.CASCADE)
    fk_Agendamento = models.ForeignKey(Agendamento, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.valor + " - " + self.dataEmissao