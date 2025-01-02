**Live Link : https://bankdetailsapiserver.pythonanywhere.com/**


## This API Server was built using the following steps:

-> **Created a database:** Django's ORM (Object-Relational Mapper) was used to create the database schema.

-> **Seeded the database:** Data from a CSV file was imported into the database using django-extensions.

-> **Developed a REST API:** Django REST Framework (DRF) was used to build the API endpoints.

-> **Deployed the API to a cloud platform**

## How to Use Our API:

### Access the bank list endpoint with a GET parameter branch_name:
**eg :** https://bankdetailsapiserver.pythonanywhere.com/banks/?branch_name=RTGS-HO


### Access the branch details endpoint with the IFSC code:
**eg :** https://bankdetailsapiserver.pythonanywhere.com/branches/ABHY0065002/


