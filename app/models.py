from django.db import models

# Modelo predefinido para auxiliar no desenvolvimento

# class Livro(models.Model):
#     nome = models.CharField(max_length=100, verbose_name="Nome do livro")
#     autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name="Autor do livro")
#     editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name="Editora do livro")
#     genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Gênero do livro")
#     preco = models.IntegerField(verbose_name="Preço do livro")
#     data_plub = models.DateField(verbose_name="Data de publicação do livro")
#     status = models.BooleanField(verbose_name="Status do livro")
#     cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF do leitor")
    
#     def __str__(self):
#         return f'{self.nome}, {self.autor}'
    
#     class Meta:
#         verbose_name = "Livro"
#         verbose_name_plural = "Livros"

# Create your models here.


class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")
    
    def __str__(self):
        return f"{self.nome}, {self.uf}"
    
    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da ocupação")

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da pessoa")
    nome_pai = models.CharField(max_length=100, verbose_name="Nome do pai da pessoa")
    nome_mae = models.CharField(max_length=100, verbose_name="Nome da mãe da pessoa")
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF da pessoa")
    data_nasc = models.DateField(verbose_name = "Data de nascimento da pessoa")
    email = models.DateField(max_length=100, verbose_name="E-mail da pessoa")
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, verbose_name="Cidade da pessoa")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE, verbose_name="Ocupação da pessoa")
    
    def __str__(self):
        return f"{self.nome}, {self.cpf}"
    
    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

class InstituicaoEnsino(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do autor")
    site = models.CharField(max_length=100, verbose_name="Site da instituição")
    telefone = models.CharField(max_length=100, verbose_name="Telefone da instituição")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        
class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da área do saber")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Área do saber"
        verbose_name_plural = "Áreas do saber"

class Curso(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do curso")
    carga_horaria_total = models.FloatField(verbose_name="Carga horária total")
    duracao_meses = models.IntegerField(verbose_name="Duração do curso em meses")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber do curso")
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino do curso")

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

class Turma(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da turma")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do livro")
    area_saber = models.ForeignKey(AreaSaber, on_delete=models.CASCADE, verbose_name="Área do saber da disciplina")
    
    def __str__(self):
        return f'{self.nome}, {self.autor}'
    
    class Meta:
        verbose_name = "Disciplina"
        verbose_name_plural = "Disciplinas"

class Matricula(models.Model):
    instituicao_ensino = models.ForeignKey(InstituicaoEnsino, on_delete=models.CASCADE, verbose_name="Instituição de ensino da matrícula")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da matrícula")
    data_inicio = models.DateField(verbose_name="Data de início da matrícula")
    data_previsao_termino = models.DateField(verbose_name="Data de previsão de término da matrícula")

class AvaliacaoTipo(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do tipo da avaliação")

    def __str__(self):
        return f"{self.nome}"
    
    class Meta:
        verbose_name = "Avaliação tipo"
        verbose_name_plural = "Avaliações tipo"

class Avaliacao(models.Model):
    descricao = models.CharField(max_length=100, verbose_name="Deascrição da avaliação")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name="Curso da avaliação")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, verbose_name="Disciplina da avaliação")
    avaliacao_tipo = models.ForeignKey(AvaliacaoTipo, on_delete=models.CASCADE, verbose_name="Tipo da avaliação")

    def __str__(self):
        return f"{self.descricao}"
    
    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

