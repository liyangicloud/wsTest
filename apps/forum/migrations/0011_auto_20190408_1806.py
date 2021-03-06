# Generated by Django 2.0.8 on 2019-04-08 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0010_auto_20190404_1132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentcommentreply',
            name='aomments_id',
        ),
        migrations.RemoveField(
            model_name='commentcommentreply',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='parent_comment',
            options={'ordering': ('-add_time',), 'verbose_name': '帖子回复表', 'verbose_name_plural': '帖子回复表'},
        ),
        migrations.AddField(
            model_name='parent_comment',
            name='to_uids',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='to_Parent_Comment', to=settings.AUTH_USER_MODEL, verbose_name='目标用户'),
        ),
        migrations.AlterField(
            model_name='parent_comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='form_Parent_Comment', to=settings.AUTH_USER_MODEL, verbose_name='当前用户'),
        ),
        migrations.DeleteModel(
            name='CommentCommentReply',
        ),
    ]
