# Generated by Django 1.10.5 on 2017-02-23 14:50

from django.db import migrations


class Migration(migrations.Migration):

    def recalculate_channellog_counts(apps, schema_editor):
        ChannelLog = apps.get_model("channels", "ChannelLog")
        Channel = apps.get_model("channels", "Channel")
        ChannelCount = apps.get_model("channels", "ChannelCount")

        # for each channel that has a channel count
        for channel in Channel.objects.filter(channelcount__count_type__in=["LE", "LS"]).order_by("pk").distinct("pk"):
            # recalculate the log count for successes
            success_count = ChannelLog.objects.filter(channel=channel, is_error=False).count()
            ChannelCount.objects.filter(channel=channel, count_type="LS").delete()
            ChannelCount.objects.create(channel=channel, count_type="LS", count=success_count, is_squashed=True)

            # and for errors
            error_count = ChannelLog.objects.filter(channel=channel, is_error=True).count()
            ChannelCount.objects.filter(channel=channel, count_type="LE").delete()
            ChannelCount.objects.create(channel=channel, count_type="LE", count=error_count, is_squashed=True)

    dependencies = [("channels", "0063_auto_20170222_2332")]

    operations = [migrations.RunPython(recalculate_channellog_counts)]
