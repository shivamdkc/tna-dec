# Generated by Django 5.1.4 on 2025-01-02 05:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDetail',
            fields=[
                ('employee_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('style_name', models.CharField(max_length=200)),
                ('order_place_date', models.DateField()),
                ('remarks', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubTask',
            fields=[
                ('subtask_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_task_name', models.CharField(max_length=200)),
                ('type_of_work', models.CharField(max_length=200)),
                ('original_start_date', models.DateField()),
                ('min_days_required', models.IntegerField()),
                ('original_end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FabricDetail',
            fields=[
                ('fabric_id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('fabric_name', models.CharField(max_length=200)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.orderdetail')),
            ],
        ),
        migrations.CreateModel(
            name='PoDetail',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('po_number', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.orderdetail')),
            ],
        ),
        migrations.CreateModel(
            name='SubTaskCompleteDetail',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('date_when_completed', models.DateField()),
                ('remarks', models.TextField(null=True)),
                ('sub_task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.subtask')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('remarks', models.TextField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.orderdetail')),
            ],
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.task'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('status', models.CharField(max_length=200)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.role')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='merchant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchant_orders', to='tna.user'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='qa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qa_orders', to='tna.user'),
        ),
        migrations.AddField(
            model_name='orderdetail',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_orders', to='tna.user'),
        ),
        migrations.CreateModel(
            name='Extension',
            fields=[
                ('extension_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_approval', models.BooleanField(default=False)),
                ('extension_days', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('A', 'Approved'), ('R', 'Rejected')], max_length=200)),
                ('sub_task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.subtask')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.user')),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('is_read', models.BooleanField(default=False)),
                ('notification_delivered_at', models.DateTimeField()),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.employeedetail')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationHistory',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('status', models.BooleanField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user_notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tna.usernotification')),
            ],
        ),
    ]
