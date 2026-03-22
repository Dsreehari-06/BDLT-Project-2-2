from home.models import Voters
import datetime

print("Deleting all existing voters...")
Voters.objects.all().delete()

voters_data = [
    ("Sreehari Dakara", "sreeharidakara06@gmail.com"),
    ("Merugu Manitej", "2411cs070024@mallareddyuniversity.ac.in"),
    ("Kotha Manish", "2411cs070061@mallareddyuniversity.ac.in"),
    ("Begari Sairam", "2411cs070007@mallareddyuniversity.ac.in"),
    ("Priya Reddy", "2411cs070014@mallareddyuniversity.ac.in"),
    ("Ravi Kiran Kumar", "2411cs070013@mallareddyuniversity.ac.in"),
    ("Tharun Bhaskar Yadav", "sreeharidakara2@gmail.com")
]

dob = datetime.date(2000, 1, 1)
pincode = "500001"
region = "Telangana"

print("Creating new voters...")
for i, (name, email) in enumerate(voters_data, 1):
    Voters.objects.create(
        uuid=str(i),
        name=name,
        email=email,
        dob=dob,
        pincode=pincode,
        region=region
    )

print("Successfully created all 7 voters!")
for v in Voters.objects.all():
    print(f"UUID: {v.uuid} | Name: {v.name} | Email: {v.email}")
