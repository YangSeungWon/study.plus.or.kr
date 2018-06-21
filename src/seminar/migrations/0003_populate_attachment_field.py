# Generated by Django 2.0.6 on 2018-06-21 07:00

from django.db import migrations


def populate_attachment_field(apps, schema_editor):
    Seminar = apps.get_model('seminar', 'Seminar')
    SeminarAttachment = apps.get_model('seminar', 'SeminarAttachment')

    delete_list = []

    for seminar_attachment in SeminarAttachment.objects.all():
        reverse_relation = seminar_attachment.old_seminars
        if not reverse_relation.exists():
            delete_list.append(seminar_attachment)
            continue

        seminar_attachment.seminar = reverse_relation.first()
        seminar_attachment.save()

    for item in delete_list:
        item.delete()


def reverse_populate_attachment_field(apps, schema_editor):
    Seminar = apps.get_model('Seminar')
    SeminarAttachment = apps.get_model('SeminarAttachment')

    delete_list = []

    for seminar_attachment in SeminarAttachment.objects.all():
        seminar_attachment.seminar.attachments.add(seminar_attachment)


class Migration(migrations.Migration):

    dependencies = [
        ('seminar', '0002_auto_20180621_1559'),
    ]

    operations = [
        migrations.RunPython(populate_attachment_field, reverse_code=reverse_populate_attachment_field)
    ]
