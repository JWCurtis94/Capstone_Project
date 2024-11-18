from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0004_delete_verdict'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE accounts_profile ALTER COLUMN bio DROP NOT NULL;"
        ),
    ]