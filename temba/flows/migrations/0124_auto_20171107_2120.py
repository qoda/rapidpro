# Generated by Django 1.11.6 on 2017-11-07 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0123_backfill_flowrun_results")]

    operations = [
        migrations.AddIndex(
            model_name="flowpathrecentmessage",
            index=models.Index(fields=["from_uuid", "to_uuid", "-created_on"], name="flows_flowp_from_uu_0f7a72_idx"),
        )
    ]
