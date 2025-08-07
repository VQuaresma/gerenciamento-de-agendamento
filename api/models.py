from django.db import models

class agenda(models.Model):
    status_agenda = [
        ('PEN', 'PENDENTE'),
        ('AGE','AGENDADO'),
        ('AND','EM ANDAMENTO'),
        ('CON','CONCLUIDO')
    ]

    data_hora = models.DateTimeField()
    status = models.CharField(max_length=10, choices=status_agenda, default='PENDENTE')  

    def __str__(self):
        return f'{self.data_hora} - {self.get_status_display()}'
    