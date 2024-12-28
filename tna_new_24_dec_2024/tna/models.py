from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator

class Role(models.Model):
    role_name = models.CharField()

    def __str__(self):
        return self.role_name

class User(models.Model):
    username = models.CharField()
    password = models.CharField()  # Ensure this field is used to store hashed passwords
    email = models.EmailField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)  # e.g., Active, Inactive

    def __str__(self):
        return self.username

class OrderDetail(models.Model):
    order_id = models.AutoField(primary_key=True) # Auto-incrementing primary key
    style_name = models.CharField()
    merchant = models.ForeignKey(User, related_name='merchant_orders', on_delete=models.CASCADE)
    qa = models.ForeignKey(User, related_name='qa_orders', on_delete=models.CASCADE)
    vendor = models.ForeignKey(User, related_name='vendor_orders', on_delete=models.CASCADE)
    order_place_date = models.DateField()
    remarks = models.TextField()

    def __str__(self):
        return self.order_id

class Task(models.Model):
    task_id = models.AutoField(primary_key=True) # Auto-incrementing primary key
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    name = models.CharField()
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField() # This is the planned end date, so in begining it will take reference from just end date and then extension + end date. 
    remarks = models.TextField()

    def __str__(self):
        return self.name

class SubTask(models.Model):
    subtask_id = models.AutoField(primary_key=True) # Auto-incrementing primary key
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    sub_task_name = models.CharField()
    type_of_work = models.CharField()
    original_start_date = models.DateField()
    min_days_required = models.IntegerField()
    original_end_date = models.DateField()

    def __str__(self):
        return self.sub_task_name

class Extension(models.Model):
    extension_id = models.AutoField(primary_key=True) # Auto-incrementing primary key
    sub_task = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    admin_approval = models.BooleanField( default=False)
    extension_days = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.()  # e.g., Pending, Approved, Rejected

class SubTaskCompleteDetail(models.Model):
    id = models.CharField( primary_key=True)
    sub_task = models.ForeignKey(SubTask, on_delete=models.CASCADE)
    date_when_completed = models.DateField()
    remarks = models.TextField()

class FabricDetail(models.Model):
    id = models.CharField( primary_key=True)
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    fabric_name = models.CharField()

class EmployeeDetail(models.Model):
    id = models.CharField( primary_key=True)
    name = models.CharField()
    department = models.CharField()
    designation = models.CharField()
    role = models.CharField()

class PoDetail(models.Model):
    id = models.CharField( primary_key=True)
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    po_number = models.IntegerField()

class Notification(models.Model):
    id = models.CharField( primary_key=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserNotification(models.Model):
    id = models.CharField( primary_key=True)
    user = models.ForeignKey(EmployeeDetail, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    notification_delivered_at = models.DateTimeField()

class NotificationHistory(models.Model):
    id = models.CharField( primary_key=True)
    user_notification = models.ForeignKey(UserNotification, on_delete=models.CASCADE)
    status = models.BooleanField()  # e.g., Delivered, Failed
    timestamp = models.DateTimeField(auto_now_add=True)
