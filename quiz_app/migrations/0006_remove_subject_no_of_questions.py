# Generated by Django 4.1.4 on 2023-02-15 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0005_question_answer_question_op1_question_op2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='no_of_questions',
        ),
    ]