# Generated by Django 4.1.4 on 2023-01-10 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CURSO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('carga_horaria', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EIXO',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=20)),
                ('icons', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='TipoCurso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TURMA',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('nome_turma', models.CharField(max_length=255, verbose_name='Nome da turma')),
                ('numero_turma', models.IntegerField(verbose_name='Numero da turma')),
                ('data_inicio', models.DateField(verbose_name='Data de Inicio')),
                ('data_termino', models.DateField(verbose_name='Data de termino')),
                ('nome_professor', models.CharField(max_length=255, verbose_name='Nome do Professor')),
                ('registro_alunos', models.CharField(max_length=500, verbose_name='Alunos')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrifolio.curso')),
            ],
        ),
        migrations.CreateModel(
            name='PROJETO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=50, unique=True, verbose_name='Nome do projeto')),
                ('data_inicio', models.DateField(verbose_name='Data de inicio')),
                ('data_entrega', models.DateField(verbose_name='Data de entrega')),
                ('observacao', models.TextField(max_length=500, verbose_name='Observação')),
                ('texto', models.FileField(upload_to='', verbose_name='Texto')),
                ('slide', models.FileField(upload_to='', verbose_name='Slide')),
                ('video', models.FileField(upload_to='', verbose_name='Video')),
                ('foto', models.ImageField(upload_to='', verbose_name='Foto')),
                ('foto_capa', models.ImageField(upload_to='', verbose_name='Foto de capa')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('destaque', models.CharField(choices=[('F', 'Falso'), ('v', 'Verdeiro')], max_length=2)),
                ('eixo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Projeto', to='integrifolio.eixo')),
                ('id_turma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrifolio.turma')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='tipo_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrifolio.tipocurso'),
        ),
    ]
