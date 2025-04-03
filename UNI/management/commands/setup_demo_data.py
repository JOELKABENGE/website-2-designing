import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from UNI.models import Department, Category, Issue, Activity

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates initial demo data for the application'

    def handle(self, *args, **options):
        # Create admin user if it doesn't exist
        admin_username = os.getenv('ADMIN_USERNAME', 'admin')
        admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
        admin_password = os.getenv('ADMIN_PASSWORD', 'admin123')

        try:
            if not User.objects.filter(username=admin_username).exists():
                admin_user = User.objects.create_superuser(
                    username=admin_username,
                    email=admin_email,
                    password=admin_password,
                    first_name='Admin',
                    last_name='User'
                )
                self.stdout.write(self.style.SUCCESS('Admin user created successfully'))
            else:
                admin_user = User.objects.get(username=admin_username)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating admin user: {e}'))
            return

        # Create departments
        departments = [
            {'name': 'Computer Science', 'description': 'Department of Computer Science and Software Engineering'},
            {'name': 'Mathematics', 'description': 'Department of Mathematics and Statistics'},
            {'name': 'Physics', 'description': 'Department of Physics and Astronomy'},
            {'name': 'Humanities', 'description': 'Department of Humanities and Social Sciences'},
            {'name': 'Administration', 'description': 'Administrative Department'},
            {'name': 'Finance', 'description': 'Department of Finance and Accounting'},
            {'name': 'Marketing', 'description': 'Department of Marketing and Sales'},
            {'name': 'Human Resources', 'description': 'Department of Human Resources'},
            {'name': 'law', 'description': 'Department of Law and Legal Studies'},
            {'name': 'Engineering', 'description': 'Department of Engineering and Technology'},
            {'name': 'Medicine', 'description': 'Department of Medicine and Health Sciences'},
            {'name': 'Dentistry', 'description': 'Department of Dentistry and Oral Health'},
            {'name': 'Pharmacy', 'description': 'Department of Pharmacy and Pharmaceutical Sciences'},
            {'name': 'Nursing', 'description': 'Department of Nursing and Midwifery'},
            {'name': 'Psychology', 'description': 'Department of Psychology and Mental Health'},
            {'name': 'Education', 'description': 'Department of Education and Teaching'},
            {'name': 'Agriculture', 'description': 'Department of Agriculture and Environmental Sciences'},
            {'name': 'Architecture', 'description': 'Department of Architecture and Urban Planning'},
            {'name': 'Design', 'description': 'Department of Design and Creative Arts'},
            {'name': 'Music', 'description': 'Department of Music and Performing Arts'},
            {'name': 'Film', 'description': 'Department of Film and Media Studies'},
            {'name': 'Journalism', 'description': 'Department of Journalism and Mass Communication'},
            {'name': 'History', 'description': 'Department of History and Archaeology'},
            {'name': 'Philosophy', 'description': 'Department of Philosophy and Ethics'},
            {'name': 'Religion', 'description': 'Department of Religion and Theology'},
            {'name': 'Languages', 'description': 'Department of Languages and Linguistics'},
            {'name': 'Literature', 'description': 'Department of Literature and Writing'},
            {'name': 'Geography', 'description': 'Department of Geography and Geology'},
            {'name': 'Economics', 'description': 'Department of Economics and Development Studies'},
            {'name': 'Political Science', 'description': 'Department of Political Science and International Relations'},
            {'name': 'Sociology', 'description': 'Department of Sociology and Anthropology'},
        ]

        try:
            for dept_data in departments:
                dept, created = Department.objects.get_or_create(
                    name=dept_data['name'],
                    defaults={'description': dept_data['description']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Department "{dept.name}" created'))
                else:
                    self.stdout.write(self.style.WARNING(f'Department "{dept.name}" already exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating departments: {e}'))

        # Create categories
        categories = [
            {'name': 'Grading', 'color': 'blue'},
            {'name': 'Registration', 'color': 'green'},
            {'name': 'Scheduling', 'color': 'purple'},
            {'name': 'Technical', 'color': 'yellow'},
            {'name': 'Materials', 'color': 'red'},
        ]

        try:
            for cat_data in categories:
                cat, created = Category.objects.get_or_create(
                    name=cat_data['name'],
                    defaults={'color': cat_data['color']}
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Category "{cat.name}" created'))
                else:
                    self.stdout.write(self.style.WARNING(f'Category "{cat.name}" already exists'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error creating categories: {e}'))

        self.stdout.write(self.style.SUCCESS('Demo data setup completed successfully'))