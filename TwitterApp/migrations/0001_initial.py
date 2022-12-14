# Generated by Django 4.1 on 2022-10-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tweets",
            fields=[
                ("TweetId", models.IntegerField(primary_key=True, serialize=False)),
                ("Tweet", models.CharField(max_length=1000)),
                ("PostedBy", models.CharField(max_length=255)),
                ("PostedOn", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("UserId", models.IntegerField(primary_key=True, serialize=False)),
                ("UserName", models.CharField(max_length=255)),
                ("Follwers", models.CharField(max_length=255)),
                ("CreatedOn", models.DateField()),
            ],
        ),
    ]
