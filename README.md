# EZYMETRICS
campigns:![image](https://github.com/user-attachments/assets/59e7d341-3445-4dc1-ba54-d3a05a2fdc26)
leads : ![image](https://github.com/user-attachments/assets/9f24e092-ab98-4853-9a21-70b41dba22b7)
leads data: ![image](https://github.com/user-attachments/assets/61c5e9ec-0310-4a18-954a-22c5dcbbea79)
report pdf image:![image](https://github.com/user-attachments/assets/890f6587-8814-4219-912b-209cdfe1b47a)
email -alert(if the phone number less than specified digit):![image](https://github.com/user-attachments/assets/92e882bf-6c41-4014-a95b-7e0149b1eace)

This project is a Django-based API for managing campaigns and leads in a CRM system. It supports creating, retrieving, updating, and deleting (CRUD) operations for campaigns and leads, as well as generating reports.
Features:
Campaigns: Manage campaigns, including budget, dates, and performance metrics.
Leads: Manage leads, including contact details and campaign association.
Reports: Generate PDF and CSV reports for campaigns and leads.
Email Alerts: Automatically send email alerts based on certain conditions.
Usage
Start the Django development server:python manage.py runserver
API Endpoints:
Leads:
GET /api/leads/: List all leads.
POST /api/leads/: Create a new lead.
GET /api/leads/<id>/: Retrieve details of a specific lead.
PUT /api/leads/<id>/: Update a specific lead.
DELETE /api/leads/<id>/: Delete a specific lead.
Campaigns:
GET /api/campaigns/: List all campaigns.
POST /api/campaigns/: Create a new campaign.
GET /api/campaigns/<id>/: Retrieve details of a specific campaign.
PUT /api/campaigns/<id>/: Update a specific campaign.
DELETE /api/campaigns/<id>/: Delete a specific campaign.
Reports:
Generate a PDF report:
plaintext
Copy code
GET /api/generate-report/
Generate a CSV report:
plaintext
Copy code
GET /api/generate-csv/


