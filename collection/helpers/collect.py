from main.models import Company, JobPosting

# Use model manager big_companies for the model Company
def get_big_companies():  
    return(", ".join(c[1]['name'] for c in enumerate(Company.big_companies.all().values())))

def working_with_models():
    values = {}
    # values["n"]
    # 1. Access the choice field option name
    # 2. hasattr to check an object has an attribute
    values["1"] = ('Access the choice field option name',)
    values["2"] = ('hasattr can be used with an object to check if it has a specified attribute',)
    

    values["1"] += (
        JobPosting.objects.first().level,
        JobPosting.objects.first().get_level_display()
    )  

    jp = JobPosting.objects.first()
    values["2"] += (
        f"hasattr(jp, \'something\')': {hasattr(jp, 'something')}",
        f"hasattr(jp, \'level\')': {hasattr(jp, 'level')}",
        )
   
    return values