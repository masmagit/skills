from .models import Company

# Use model manager big_companies for the model Company
def get_big_companies():  
    return(", ".join(c[1]['name'] for c in enumerate(Company.big_companies.all().values())))